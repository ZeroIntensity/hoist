import logging
from contextlib import suppress
from secrets import choice, compare_digest
from string import ascii_letters
from typing import Any, List, NoReturn, Optional, Sequence, Union

import uvicorn
from rich.console import Console
from starlette.responses import HTMLResponse, JSONResponse, Response
from starlette.types import Receive, Scope, Send
from starlette.websockets import WebSocket, WebSocketDisconnect
from versions import Version, parse_version

from ._errors import *
from ._html import HTML
from ._logging import hlog, log
from ._messages import (
    LISTENER_CLOSE, LISTENER_OPEN, NEW_MESSAGE, SINGLE_NEW_MESSAGE,
    MessageListener, create_message
)
from ._operations import BASE_OPERATIONS, call_operation, verify_schema
from ._socket import ClientError, Socket, make_client, make_client_msg
from ._typing import (
    LoginFunc, MessageListeners, Operations, Payload, Schema, VersionLike
)
from .exceptions import CloseSocket, SchemaValidationError
from .message import Message
from .version import __version__

logging.getLogger("uvicorn.error").disabled = True
logging.getLogger("uvicorn.access").disabled = True

print_exc = Console().print_exception


__all__ = ("Server",)


async def _base_login(server: "Server", sent_token: str) -> bool:
    return compare_digest(server.token, sent_token)


def _invalid_payload(exc: SchemaValidationError) -> Payload:
    needed = exc.needed

    return {
        "current": exc.current,
        "needed": exc.needed.__name__  # type: ignore
        if not isinstance(needed, tuple)
        else [i.__name__ if i else str(i) for i in needed],
    }


class _SocketMessageTransport:
    def __init__(
        self,
        ws: Socket,
        server: "Server",
        event_message: str = NEW_MESSAGE,
    ) -> None:
        self._ws = ws
        self._server = server
        self._message = event_message

    async def message(
        self,
        msg: str,
        data: Optional[Payload] = None,
        replying: Optional[Message] = None,
    ) -> Message:
        """Send a message to the client."""
        d = data or {}

        await self._ws.success(
            message=self._message,
            payload={
                "message": msg,
                "data": d,
                "replying": replying.to_dict() if replying else None,
            },
        )

        return Message(
            self,
            msg,
            self._server._current_id,
            data=data,
            replying=replying,
        )


class Server(MessageListener):
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
        minimum_version: Optional[VersionLike] = None,
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
        self._supported_operations = supported_operations or ["*"]
        self._unsupported_operations = unsupported_operations or []
        self._clients: List[Socket] = []
        super().__init__(extra_listeners)

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
        except SchemaValidationError as e:
            await ws.error(
                INVALID_CONTENT,
                payload=_invalid_payload(e),
            )

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
        except SchemaValidationError as e:
            await ws.error(INVALID_CONTENT, payload=_invalid_payload(e))

        await ws.success()

    async def _process_message(self, ws: Socket, payload: Payload) -> None:
        message, data, replying = await self._handle_schema(
            ws,
            payload,
            {
                "message": str,
                "data": dict,
                "replying": (dict, None),
            },
        )

        transport = _SocketMessageTransport(ws, self)
        await ws.success(
            payload={"id": self._current_id + 1},
            message=LISTENER_OPEN,
        )

        try:
            await self._call_listeners(
                transport,
                message,
                data,
                await create_message(transport, replying)
                if replying
                else None,  # fmt: off
            )
        except Exception as e:
            if isinstance(e, SchemaValidationError):
                await ws.error(INVALID_CONTENT, payload=_invalid_payload(e))

            raise e

        await ws.success(message=LISTENER_CLOSE)

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
        self._clients.append(ws)

        try:
            await self._ws_wrapper(ws)
        except Exception as e:
            log(
                "exc",
                f"{e.__class__.__name__}: {str(e) or '<no message>'}",
                level=logging.DEBUG,
            )
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

        self._clients.remove(ws)

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
                    if path == "/hoist/ack":
                        msg = {"version": __version__}
                        hlog("ack", msg, level=logging.DEBUG)
                        response = JSONResponse(msg)
                    else:
                        response = HTMLResponse(
                            HTML,
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
            "startup",
            f"starting server on [bold cyan]{host}:{port}[/]{tokmsg}",
        )

        try:
            uvicorn.run(_app, host=host, port=port, lifespan="on")
        except RuntimeError as e:
            raise RuntimeError(
                "server cannot start from a running event loop",
            ) from e

    async def broadcast(
        self,
        message: str,
        payload: Optional[Payload] = None,
    ) -> None:
        """Send a message to all connections."""
        for i in self._clients:
            transport = _SocketMessageTransport(
                i,
                self,
                SINGLE_NEW_MESSAGE,
            )
            await transport.message(message, payload)
