from rich.console import Console
from typing import Any, Callable, Coroutine
import asyncio
import inspect

print_exc = Console().print_exception


def main(func: Callable[..., Coroutine[Any, Any, Any]]) -> None:
    """Run a main async function."""
    frame = inspect.currentframe()
    assert frame
    assert frame.f_back

    if frame.f_back.f_globals["__name__"] == "__main__":
        try:
            asyncio.run(func())
        except BaseException:
            print_exc()
