import aiohttp
from typing import Optional
import asyncio
from ._client_ws import ServerSocket

__all__ = ("Connection",)


class Connection:
    """Class handling a connection to a server."""

    def __init__(
        self,
        url: str,
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
    def url(self) -> str:
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

    async def close(self) -> None:
        """Close the connection."""
        self._connected = False
        await self._session.close()

    async def connect(self, token: Optional[str] = None) -> None:
        """Open the connection."""
        auth: Optional[str] = token or self.token

        if not auth:
            raise ValueError(
                "no authentication token (did you forget to pass it?)",
            )

        self._connected = True
        self._ws = ServerSocket(
            await self._session._ws_connect(self.url),
            auth,
        )
        await self._ws.login()

    def __del__(self) -> None:
        loop = asyncio.new_event_loop()

        if self._ws:
            loop.run_until_complete(self._ws.close())

        loop.run_until_complete(self.close())
