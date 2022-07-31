from starlette.websockets import WebSocket, WebSocketDisconnect
from starlette.responses import Response
from starlette.types import Scope, Receive, Send
from ._logging import log
import uvicorn
from typing import (
    NoReturn,
    Optional,
    Sequence,
    Union,
    Callable,
    Awaitable,
)
from secrets import choice
from string import ascii_letters
import logging
from ._socket import Socket, make_client_msg, ClientError, make_client
from rich.console import Console
from versions import Version, parse_version

logging.getLogger("uvicorn.error").disabled = True
logging.getLogger("uvicorn.access").disabled = True

LoginFunc = Callable[["Server", str], Awaitable[bool]]
print_exc = Console().print_exception


__all__ = ("Server",)


async def _base_login(server: "Server", sent_token: str) -> bool:
    return server.token == sent_token


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
    ) -> None:
        self._token = token or "".join(
            [choice(default_token_choices) for _ in range(default_token_len)],
        )
        self._hide_token = hide_token
        self._login_func = login_func
        logging.getLogger("hoist").setLevel(log_level)
        self._minimum_version = minimum_version

    @property
    def token(self) -> str:
        """Authentication token used to connect."""
        return self._token

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
                minver if isinstance(minver, Version) else parse_version(minver)
            )

            if not (parse_version(version) >= minver_actual):
                await ws.error(4)

        if not (await self._login_func(self, token)):
            await ws.error(3)

        log(
            "login",
            f"{make_client(ws.address)} has successfully authenticated",  # noqa
        )

        while True:
            operation, data = await ws.recv(
                {
                    "operation": str,
                    "data": dict,
                }
            )

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
            else:
                log(
                    "exception",
                    f"exception occured while receiving{make_client_msg(addr)}",  # noqa
                    level=logging.CRITICAL,
                )
                print_exc(show_locals=True)

    def start(
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
                    response = Response("Hello, world!", media_type="text/plain")
                    await response(scope, receive, send)

                if typ == "websocket":
                    if path == "/hoist":
                        socket = WebSocket(scope, receive, send)
                        obj = Socket(socket)
                        await obj.connect()

                        return await self._ws(obj)

                    response = Response("Not found.", media_type="text/plain")
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
        uvicorn.run(_app, host=host, port=port, lifespan="on")
