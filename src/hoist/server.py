import logging
from contextlib import suppress
from secrets import choice, compare_digest
from string import ascii_letters
from typing import (
    Any, List, NoReturn, Optional, Sequence, Tuple, TypeVar, Union,
    get_type_hints
)

import uvicorn
from rich.console import Console
from starlette.responses import Response
from starlette.types import Receive, Scope, Send
from starlette.websockets import WebSocket, WebSocketDisconnect
from versions import Version, parse_version

from ._errors import *
from ._logging import log
from ._operations import BASE_OPERATIONS, call_operation, verify_schema
from ._socket import ClientError, Socket, make_client, make_client_msg
from ._typing import (
    DataclassLike, Listener, ListenerData, LoginFunc, MessageListeners,
    Operations, Payload, Schema
)
from .exceptions import CloseSocket, SchemaValidationError

logging.getLogger("uvicorn.error").disabled = True
logging.getLogger("uvicorn.access").disabled = True

print_exc = Console().print_exception


__all__ = ("Server",)

T = TypeVar("T", bound=DataclassLike)


async def _base_login(server: "Server", sent_token: str) -> bool:
    return compare_digest(server.token, sent_token)


async def _process_listeners(
    listeners: Optional[List[ListenerData]],
    payload: Payload,
) -> None:
    for i in listeners or ():
        func = i[0]
        param = i[1]
        is_schema: bool = isinstance(param, dict)

        schema: Any = param if is_schema else get_type_hints(param)
        verify_schema(schema, payload)

        await func(
            payload if is_schema else param(**payload),  # type: ignore
        )


class Server:
    """Class for handling a server."""

    def __init__(
        self,
        token: Optional[str] = None,
        *,
        default_token_len: int = 25,
        default_token_choices: Union[str, Sequence[str]] = ascii_letters,
        hide_token: bool = False,
        login_func: LoginFunc = _base_login,
        log_level: int = logging.INFO,
        minimum_version: Optional[Union[str, Version]] = None,
        extra_operations: Optional[Operations] = None,
        unsupported_operations: Optional[List[str]] = None,
        supported_operations: Optional[List[str]] = None,
        extra_listeners: Optional[MessageListeners] = None,
    ) -> None:
        self._token = token or "".join(
            [choice(default_token_choices) for _ in range(default_token_len)],
        )
        self._hide_token = hide_token
        self._login_func = login_func
        logging.getLogger("hoist").setLevel(log_level)
        self._minimum_version = minimum_version
        self._operations = {**BASE_OPERATIONS, **(extra_operations or {})}
        self._supported_operations: List[str] = supported_operations or ["*"]
        self._unsupported_operations: List[str] = unsupported_operations or []

        self._verify_operations()
        self._message_listeners: MessageListeners = {**(extra_listeners or {})}

    @property
    def message_listeners(self) -> MessageListeners:
        """Listener function for messages."""
        return self._message_listeners

    @property
    def supported_operations(self) -> List[str]:
        """Operations supported by the server."""
        return self._supported_operations

    @property
    def unsupported_operations(self) -> List[str]:
        """Operations blacklisted by the server."""
        return self._unsupported_operations

    def _verify_operations(self) -> None:
        so = self.supported_operations
        uo = self.unsupported_operations

        if "*" in so:
            if len(so) > 1:
                raise ValueError(
                    '"*" should be the only operation',
                )
            return

        for i in so:
            if i in uo:
                raise ValueError(
                    f'operation "{i}" is both supported and unsupported',
                )

    async def _verify_operation(  # not sure if i need async here
        self, operation: str
    ) -> bool:
        so = self.supported_operations
        uo = self.unsupported_operations

        if operation in uo:
            return False

        if "*" in so:
            return not (operation in uo)

        return not (operation not in self.supported_operations)

    @property
    def token(self) -> str:
        """Authentication token used to connect."""
        return self._token

    async def _call_listeners(
        self,
        message: str,
        payload: Payload,
    ) -> None:
        ml = self.message_listeners
        listeners = ml.get(message)
        await _process_listeners(listeners, payload)

        glbl = ml.get(None)
        await _process_listeners(glbl, payload)

    @staticmethod
    async def _handle_schema(
        ws: Socket,
        payload: Payload,
        schema: Schema,
    ) -> List[Any]:
        try:
            verify_schema(
                schema,
                payload,
            )
        except SchemaValidationError:
            await ws.error(INVALID_CONTENT)

        return [payload[i] for i in schema]

    async def _process_operation(self, ws: Socket, payload: Payload) -> None:
        operation, data = await self._handle_schema(
            ws,
            payload,
            {
                "operation": str,
                "data": dict,
            },
        )

        op = self._operations.get(operation)

        if not op:
            await ws.error(UNKNOWN_OPERATION)

        if not (await self._verify_operation(operation)):
            await ws.error(UNSUPPORTED_OPERATION)

        try:
            await call_operation(op, data)
        except SchemaValidationError:
            await ws.error(INVALID_CONTENT)

        await ws.success()

    async def _process_message(self, ws: Socket, payload: Payload) -> None:
        message, data = await self._handle_schema(
            ws,
            payload,
            {
                "message": str,
                "data": dict,
            },
        )

        try:
            await self._call_listeners(message, data)
        except Exception as e:
            if isinstance(e, SchemaValidationError):
                await ws.error(INVALID_CONTENT)

            await ws.error(SERVER_ERROR)

        await ws.success()

    async def _ws_wrapper(self, ws: Socket) -> None:
        version, token = await ws.recv(
            {
                "version": str,
                "token": str,
            }
        )

        minver = self._minimum_version

        if minver:
            minver_actual = (
                minver
                if isinstance(minver, Version)
                else parse_version(minver)  # fmt: off
            )

            if not (parse_version(version) >= minver_actual):
                await ws.error(
                    BAD_VERSION,
                    payload={"needed": minver_actual.to_string()},
                )

        if not (await self._login_func(self, token)):
            await ws.error(LOGIN_FAILED)

        await ws.success()

        log(
            "login",
            f"{make_client(ws.address)} has successfully authenticated",  # noqa
        )

        while True:
            data: Payload
            action, data = await ws.recv(
                {
                    "action": str,
                    "data": dict,
                }
            )

            if action == "operation":
                await self._process_operation(ws, data)
            elif action == "message":
                await self._process_message(ws, data)
            else:
                await ws.error(INVALID_ACTION)

    async def _ws(self, ws: Socket) -> None:
        try:
            await self._ws_wrapper(ws)
        except Exception as e:
            addr = ws.address
            if isinstance(e, WebSocketDisconnect):
                log(
                    "disconnect",
                    f"unexpected disconnect{make_client_msg(addr)}",
                    level=logging.WARNING,
                )
            elif isinstance(e, ClientError):
                log(
                    "error",
                    f"connection from {make_client(addr)} encountered error {e.code} ([bold red]{e.error}[/]): [bold white]{e.message}",  # noqa
                    level=logging.ERROR,
                )
                await ws.close(1003)
            elif isinstance(e, CloseSocket):
                await ws.close(1000)
            else:
                log(
                    "exception",
                    f"exception occured while receiving{make_client_msg(addr)}",  # noqa
                    level=logging.CRITICAL,
                )
                print_exc(show_locals=True)

                with suppress(ClientError):
                    await ws.error(SERVER_ERROR)

    def start(  # type: ignore
        self,
        *,
        host: str = "0.0.0.0",
        port: int = 5000,
    ) -> NoReturn:  # type: ignore
        """Start the server."""

        async def _app(
            scope: Scope,
            receive: Receive,
            send: Send,
        ) -> None:
            typ: str = scope["type"]

            if typ != "lifespan":
                path: str = scope["path"]

                if typ == "http":
                    response = Response(
                        "Hello, world!",
                        media_type="text/plain",
                    )
                    await response(scope, receive, send)

                if typ == "websocket":
                    if path == "/hoist":
                        socket = WebSocket(scope, receive, send)
                        obj = Socket(socket)
                        await obj.connect()

                        return await self._ws(obj)

                    response = Response(
                        "Not found.",
                        media_type="text/plain",
                        status_code=404,
                    )
                    await response(scope, receive, send)

        tokmsg: str = (
            f" with token [bold blue]{self.token}[/]"
            if not self._hide_token
            else ""  # fmt: off
        )
        log(
            "start",
            f"server running on [bold cyan]{host}:{port}[/]{tokmsg}",
        )

        try:
            uvicorn.run(_app, host=host, port=port, lifespan="on")
        except RuntimeError as e:
            raise RuntimeError(
                "server cannot start from a running event loop",
            ) from e

    def receive(
        self,
        message: Optional[Union[str, Tuple[str, ...]]] = None,
        parameter: Optional[Union[Schema, T]] = None,
    ):
        """Add a listener for message receiving."""

        def decorator(func: Listener):
            listeners = self.message_listeners

            param = parameter

            if not param:
                hints = get_type_hints(func)
                if hints:
                    param = hints[tuple(hints.keys())[0]]

            value = (func, (param or {}))

            if message in listeners:
                listeners[message].append(value)
            else:
                listeners[message] = [value]

        return decorator
