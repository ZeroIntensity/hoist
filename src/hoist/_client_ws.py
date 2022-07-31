from aiohttp import ClientWebSocketResponse
from .exceptions import ServerLoginFailed, ServerResponseError
from typing import NamedTuple, Dict, Optional, Any
from .version import __version__

__all__ = ("ServerSocket",)


class _Response(NamedTuple):
    success: bool
    data: Optional[Dict[str, Any]]
    error: Optional[str]
    message: Optional[str]
    desc: Optional[str]
    code: int


class ServerSocket:
    def __init__(
        self,
        ws: ClientWebSocketResponse,
        token: str,
    ) -> None:
        self._ws = ws
        self._token = token
        self._logged: bool = False

    async def _recv(self) -> _Response:
        res = _Response(**await self._ws.receive_json())

        code = res.code
        error = res.error
        message = res.message

        if res.code != 0:
            assert error
            assert message

            raise ServerResponseError(
                f"code {code} [{error}]: {message}",
                code=res.code,
                error=error,
                message=message,
            )

        return res

    async def login(self) -> None:
        await self._ws.send_json(
            {
                "token": self._token,
                "version": __version__,
            }
        )
        try:
            await self._recv()
        except ServerResponseError as e:
            raise ServerLoginFailed("login token is not valid") from e

        self._logged = True

    @property
    def logged(self) -> bool:
        """Whether the socket has authenticated with the server."""
        return self._logged

    async def close(self) -> None:
        """Close the socket."""
        await self._ws.close()
