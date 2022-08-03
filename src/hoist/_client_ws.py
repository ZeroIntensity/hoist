import asyncio
from typing import TYPE_CHECKING, Literal, NamedTuple, Optional, overload

from aiohttp import ClientWebSocketResponse

from ._messages import NEW_MESSAGE
from ._typing import Payload, TransportMessageListener
from .exceptions import (
    InvalidVersionError, ServerLoginError, ServerResponseError
)
from .message_socket import MessageSocket
from .version import __version__

if TYPE_CHECKING:
    from .client import Connection

__all__ = ("ServerSocket",)


class _Response(NamedTuple):
    success: bool
    data: Optional[Payload]
    error: Optional[str]
    message: Optional[str]
    desc: Optional[str]
    code: int


class ServerSocket:
    """Class for handling a WebSocket connection to a server."""

    def __init__(
        self,
        client: "Connection",
        ws: ClientWebSocketResponse,
        token: str,
    ) -> None:
        self._ws = ws
        self._token = token
        self._logged: bool = False
        self._closed: bool = False
        self._message_listener: Optional[TransportMessageListener] = None
        self._queue = asyncio.Queue[_Response]()
        self._client = client

    async def _recv(self) -> _Response:
        res = await self._queue.get()

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

    async def _listener(self):
        while True:
            res = _Response(**await self._ws.receive_json())
            listener = self._message_listener
            data = res.data

            if res.message == NEW_MESSAGE:
                assert listener
                assert data

                await listener(
                    MessageSocket(self._client),
                    data["message"],
                    data["data"],
                )
                continue

            await self._queue.put(res)

    async def login(self, listener: TransportMessageListener) -> None:
        """Send login message to the server."""
        self._message_listener = listener
        asyncio.create_task(self._listener())

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
        if not self._ws.closed:
            await self.send({"end": True})
        self._closed = True

    @overload
    async def send(  # type: ignore
        self,
        payload: Payload,
        *,
        reply: Literal[False] = False,
    ) -> Literal[None]:
        """Send a message to the server."""
        ...

    @overload
    async def send(
        self,
        payload: Payload,
        *,
        reply: Literal[True] = True,
    ) -> _Response:
        """Send a message to the server."""
        ...

    async def send(
        self,
        payload: Payload,
        *,
        reply: bool = False,
    ) -> Optional[_Response]:
        """Send a message to the server."""
        await self._ws.send_json(payload)

        if reply:
            return await self._recv()

        return None
