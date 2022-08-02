from typing import (
    TYPE_CHECKING, Any, Awaitable, Callable, Dict, Tuple, Type, TypeVar, Union
)

if TYPE_CHECKING:
    from yarl import URL

    from .server import Server

_T = TypeVar("_T")

Payload = Dict[str, Any]
Operator = Callable[[_T], Awaitable[Any]]
Schema = Dict[str, Union[Type[Any], Tuple[Type[Any], ...]]]
Operations = Dict[str, Operator]
UrlLike = Union[str, "URL"]
LoginFunc = Callable[["Server", str], Awaitable[bool]]
ResponseErrors = Dict[int, Tuple[str, str]]