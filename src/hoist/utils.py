import asyncio
import inspect
from typing import Any, Callable, Coroutine

from rich.console import Console

from ._typing import UrlLike
from .client import Connection

print_exc = Console().print_exception


def main(func: Callable[[], Coroutine[Any, Any, Any]]) -> None:
    """Run a main async function."""
    frame = inspect.currentframe()
    assert frame
    assert frame.f_back

    if frame.f_back.f_globals["__name__"] == "__main__":
        try:
            asyncio.run(func())
        except BaseException:
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
