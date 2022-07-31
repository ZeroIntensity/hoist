from starlette.websockets import WebSocket
from starlette.datastructures import Address
from ._logging import log
from typing import Dict, Any, Tuple, Type, Union, Optional, NoReturn, List
import json

Schema = Dict[str, Union[Type[Any], Tuple[Type[Any], ...]]]

ERRORS: Dict[int, Tuple[str, str]] = {
    0: (
        "INVALID_JSON",
        "Invalid JSON structure was received.",
    ),
    1: (
        "INVALID_CONTENT",
        "JSON content is invalid.",
    ),
    2: (
        "LOGIN_FAILED",
        "Login token is invalid.",
    ),
}


class ClientError(Exception):
    """The client caused an error on the server."""

    def __init__(
        self,
        *args,
        code: int,
        error: str,
        message: str,
        **kwargs,
    ) -> None:
        self._code: int = code
        self._error: str = error
        self._message: str = message
        super().__init__(*args, **kwargs)

    @property
    def code(self) -> int:
        """Error code."""
        return self._code

    @property
    def error(self) -> str:
        """Error name."""
        return self._error

    @property
    def message(self) -> str:
        """Error message."""
        return self._message


def make_client_msg(addr: Optional[Address], to: bool = False) -> str:
    target: str = "from" if not to else "to"
    return f" {target} [bold blue]{addr.host}:{addr.port}[/]" if addr else ""


class Socket:
    """Class for handling a WebSocket."""

    def __init__(
        self,
        ws: WebSocket,
        *,
        disconnect_error: bool = True,
    ):
        self._ws = ws
        self._disconnect_error = disconnect_error
        self._logged: bool = False

    async def connect(self) -> None:
        ws = self._ws
        await ws.accept()

        log(
            "connect",
            f"now receiving{make_client_msg(ws.client)}",
        )

    @property
    def ws(self) -> WebSocket:
        """Raw WebSocket object."""
        return self._ws

    @property
    def disconnect_error(self) -> bool:
        """Whether the socket should end if an error is encountered."""
        return self._disconnect_error

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

        if self.disconnect_error:
            await self.ws.close(1003)

        raise ClientError(code=code, error=error, message=message)

    async def recv(self, schema: Schema) -> List[Any]:
        try:
            load: dict = json.loads(await self.ws.receive_text())
        except json.JSONDecodeError:
            await self.error(0)

        for key, typ in schema.items():
            value = load.get(key)
            vtype = type(value) if value is not None else None

            if type(typ) is tuple:
                if vtype not in typ:
                    await self.error(1)

            if vtype is not typ:
                await self.error(1)

        return [load[i] for i in schema]

    async def recv_only(self, schema: Schema) -> Any:
        return (await self.recv(schema))[0]
