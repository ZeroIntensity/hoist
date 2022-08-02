from typing import (
    TYPE_CHECKING, Any, Awaitable, Callable, Dict, List, Optional, Tuple, Type,
    TypeVar, Union
)

from typing_extensions import Protocol

if TYPE_CHECKING:
    from yarl import URL

    from .server import Server

_T = TypeVar("_T")


class DataclassLike(Protocol):
    """Dataclass-like protocol."""

    __annotations__: Dict[str, Any]

    def __init__(self, *args, **kwargs) -> None:
        ...


_A = TypeVar("_A", bound=Type[DataclassLike])

Payload = Dict[str, Any]
Operator = Callable[[_T], Awaitable[Any]]
Schema = Dict[str, Union[Type[Any], Tuple[Type[Any], ...]]]
Operations = Dict[str, Operator]
UrlLike = Union[str, "URL"]
LoginFunc = Callable[["Server", str], Awaitable[bool]]
ResponseErrors = Dict[int, Tuple[str, str]]
Listener = Callable[[_T], Awaitable[None]]
MessageListeners = Dict[
    Optional[Union[Tuple[str, ...], str]],
    List[Tuple[Listener[_A], Union[_A, Schema]]],
]
