import asyncio
import inspect
from threading import Thread
from typing import Any, Callable, Coroutine, Optional

from rich.console import Console

from ._typing import UrlLike
from .client import Connection
from .server import Server

print_exc = Console().print_exception

__all__ = (
    "main",
    "connect",
    "start",
)


def main(func: Callable[[], Coroutine[Any, Any, Any]]) -> None:
    """Run a main async function."""
    frame = inspect.currentframe()
    assert frame
    assert frame.f_back

    if frame.f_back.f_globals["__name__"] == "__main__":
        try:
            asyncio.run(func())
        except BaseException as e:
            if isinstance(e, KeyboardInterrupt):
                return

            print_exc()


async def connect(
    url: UrlLike,
    token: str,
    **kwargs: Any,
) -> Connection:
    """Connect to a Hoist server."""
    conn = Connection(url, token, **kwargs)
    await conn.connect()
    return conn


def start(
    token: Optional[str] = None,
    server: Optional[Server] = None,
    *,
    host: str = "0.0.0.0",
    port: int = 5000,
    **kwargs,
) -> Server:
    """Start a Hoist server in a new thread."""
    srvr = server or Server(token, *kwargs)
    t = Thread(
        target=srvr.start,
        kwargs={
            "host": host,
            "port": port,
        },
    )
    t.start()
    return srvr
