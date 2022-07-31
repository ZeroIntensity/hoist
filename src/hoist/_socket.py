from starlette.websockets import WebSocket
from starlette.datastructures import Address
from ._logging import log
from typing import Dict, Any, Tuple, Type, Union, Optional, NoReturn, List
import json
from .exceptions import ClientError

__all__ = (
    "make_client_msg",
    "make_client",
    "Socket",
)

Schema = Dict[str, Union[Type[Any], Tuple[Type[Any], ...]]]

ERRORS: Dict[int, Tuple[str, str]] = {
    1: (
        "INVALID_JSON",
        "Invalid JSON structure was received.",
    ),
    2: (
        "INVALID_CONTENT",
        "JSON content is invalid.",
    ),
    3: (
        "LOGIN_FAILED",
        "Login token is invalid.",
    ),
    4: (
        "BAD_VERSION",
        "Version of client is not high enough.",
    ),
}


def make_client_msg(addr: Optional[Address], to: bool = False) -> str:
    target: str = "from" if not to else "to"
    return f" {target} [bold cyan]{addr.host}:{addr.port}[/]" if addr else ""


def make_client(addr: Optional[Address]) -> str:
    return f"[bold cyan]{addr.host}:{addr.port}[/]" if addr else "client"


class Socket:
    """Class for handling a WebSocket."""

    def __init__(
        self,
        ws: WebSocket,
    ):
        self._ws = ws
        self._logged: bool = False

    async def connect(self) -> None:
        ws = self._ws
        await ws.accept()

        log(
            "connect",
            f"connecting{make_client_msg(ws.client, to=True)}",
        )

    @property
    def ws(self) -> WebSocket:
        """Raw WebSocket object."""
        return self._ws

    @property
    def logged(self) -> bool:
        """The authentication status of the current connection."""
        return self._logged

    @logged.setter
    def logger(self, value: bool) -> None:
        self._logged = value

    async def _send(
        self,
        obj: Dict[str, Any],
        *,
        success: bool = True,
        payload: Optional[Dict[str, Any]] = None,
    ) -> None:
        await self.ws.send_json(
            {
                "success": success,
                "data": payload,
                **obj,
            }
        )

    async def error(
        self,
        code: int,
        description: Optional[str] = None,
    ) -> NoReturn:
        err = ERRORS[code]
        error = err[0]
        message = err[1]

        await self._send(
            {
                "code": code,
                "error": error,
                "message": message,
                "desc": description,
            },
            success=False,
        )

        raise ClientError(code=code, error=error, message=message)

    async def recv(self, schema: Schema) -> List[Any]:
        try:
            load: dict = json.loads(await self.ws.receive_text())
        except json.JSONDecodeError:
            await self.error(1)

        for key, typ in schema.items():
            value = load.get(key)
            vtype = type(value) if value is not None else None

            if type(typ) is tuple:
                if vtype not in typ:
                    await self.error(2)

            if vtype is not typ:
                await self.error(2)

        return [load[i] for i in schema]

    async def recv_only(self, schema: Schema) -> Any:
        return (await self.recv(schema))[0]

    async def close(self, code: int) -> None:
        await self.ws.close(code)
        log(
            "disconnect",
            f"no longer receiving{make_client_msg(self.ws.client)}",
        )

    @property
    def address(self) -> Optional[Address]:
        """Address object of the connection."""
        return self.ws.client
