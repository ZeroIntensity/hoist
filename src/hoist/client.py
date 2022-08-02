import asyncio
from typing import Optional

import aiohttp
from yarl import URL

from ._client_ws import ServerSocket
from ._typing import Payload, UrlLike
from .exceptions import (
    InvalidOperationError, NotConnectedError, ServerResponseError
)

__all__ = ("Connection",)


class Connection:
    """Class handling a connection to a server."""

    def __init__(
        self,
        url: UrlLike,
        token: Optional[str] = None,
        *,
        loop: Optional[asyncio.AbstractEventLoop] = None,
        session: Optional[aiohttp.ClientSession] = None,
    ) -> None:
        self._url = url
        self._token: Optional[str] = token
        self._connected: bool = False
        self._loop = loop or asyncio.get_event_loop()
        self._session = session or aiohttp.ClientSession(loop=self._loop)
        self._ws: Optional[ServerSocket] = None

    @property
    def url(self) -> UrlLike:
        """URL of the server."""
        return self._url

    @property
    def token(self) -> Optional[str]:
        """Authentication token of the server."""
        return self._token

    @property
    def connected(self) -> bool:
        """Whether the server is currently connected."""
        return self._connected

    async def _close(self) -> None:
        """Close the connection."""
        self._connected = False

        if self._ws:
            await self._ws.close()

        await self._session.close()

    async def connect(self, token: Optional[str] = None) -> None:
        """Open the connection."""
        auth: Optional[str] = token or self.token

        if not auth:
            raise ValueError(
                "no authentication token (did you forget to pass it?)",
            )

        raw_url = self.url
        url_obj = raw_url if isinstance(raw_url, URL) else URL(raw_url)

        url = url_obj.with_scheme(
            "wss" if url_obj.scheme == "https" else "ws",
        ).with_path("/hoist")

        self._connected = True
        self._ws = ServerSocket(
            await self._session._ws_connect(url),
            auth,
        )
        await self._ws.login()

    def __del__(self) -> None:
        loop = self._loop
        coro = self._close()

        if loop.is_closed():
            loop = asyncio.new_event_loop()
            loop.run_until_complete(coro)
        else:
            loop.create_task(coro)

    async def _execute_operation(
        self,
        operation: str,
        payload: Payload,
    ) -> None:
        if not self._ws:
            raise NotConnectedError(
                "not connected to websocket (did you forget to call connect?)"
            )

        try:
            await self._ws.send(
                {
                    "operation": operation,
                    "data": payload,
                },
                reply=True,
            )
        except ServerResponseError as e:
            if e.code == 5:
                raise InvalidOperationError(
                    f'"{operation}" is not a valid operation'
                ) from e
            raise e
