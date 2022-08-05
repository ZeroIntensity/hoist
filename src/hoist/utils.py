import asyncio
import inspect
import logging
import os
from contextlib import asynccontextmanager
from threading import Thread
from typing import Any, Awaitable, Callable, Coroutine, Optional, Union

from rich.console import Console

from ._typing import UrlLike
from .client import Connection
from .server import Server

print_exc = Console().print_exception

__all__ = (
    "main",
    "connect",
    "start",
    "connect_to",
    "debug",
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


@asynccontextmanager
async def connect(
    url: UrlLike,
    token: str,
    **kwargs: Any,
):
    """Connect to a Hoist server."""
    try:
        conn = Connection(url, token, **kwargs)
        await conn.connect()
        yield conn
    finally:
        await conn.close()


def connect_to(
    url: UrlLike,
    token: str,
    **kwargs: Any,
):
    """Connect to a server with a decorator."""

    def inner(func: Callable[[Connection], Awaitable[Any]]):
        async def _wrapper():
            conn = Connection(url, token, **kwargs)

            try:
                await conn.connect()
                await func(conn)
            except BaseException as e:
                if isinstance(e, KeyboardInterrupt):
                    return

                print_exc()
            finally:
                if not conn.closed:
                    await conn.close()

        asyncio.run(_wrapper())

    return inner


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


def debug(*, trace: Union[bool, str] = False) -> None:
    """Enable debug logging."""
    logging.getLogger("hoist").setLevel(logging.DEBUG)
    os.environ["HOIST_TRACE"] = (
        trace if not isinstance(trace, bool) else "all" if trace else ""
    )
