from aiohttp import ClientWebSocketResponse
from .exceptions import (
    ServerLoginError,
    ServerResponseError,
    InvalidVersionError,
)
from typing import NamedTuple, Dict, Optional, Any, overload, Literal
from .version import __version__
from ._typing import Payload
import asyncio

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
        self._closed: bool = False

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
                payload=res.data,
            )

        return res

    async def login(self) -> None:
        try:
            await self.send(
                {
                    "token": self._token,
                    "version": __version__,
                },
                reply=True,
            )
        except ServerResponseError as e:
            if e.code == 4:
                assert e.payload
                raise InvalidVersionError(
                    f"server needs version {e.payload['needed']}, but you have {__version__}",  # noqa
                )
            if e.code == 3:
                raise ServerLoginError("login token is not valid") from e

            raise e  # we shouldnt ever get here

        self._logged = True

    @property
    def logged(self) -> bool:
        """Whether the socket has authenticated with the server."""
        return self._logged

    async def close(self) -> None:
        """Close the socket."""
        await self.send({"end": True})
        self._closed = True

    @overload
    async def send(
        self,
        payload: Payload,
        *,
        reply: Literal[False] = False,
    ) -> Literal[None]:
        ...

    @overload
    async def send(
        self,
        payload: Payload,
        *,
        reply: Literal[True] = True,
    ) -> _Response:
        ...

    async def send(
        self,
        payload: Payload,
        *,
        reply: bool = False,
    ) -> Optional[_Response]:
        await self._ws.send_json(payload)

        if reply:
            await self._recv()
