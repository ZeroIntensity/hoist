from typing import (
    TYPE_CHECKING, Any, Awaitable, Callable, Dict, List, Optional, Tuple, Type,
    TypeVar, Union
)

from typing_extensions import Protocol

if TYPE_CHECKING:
    from versions import Version
    from yarl import URL

    from ._messages import BaseMessagable, ListenerData
    from ._operations import OperatorParam
    from .message import Message
    from .server import Server


_T = TypeVar("_T")


class DataclassLike(Protocol):
    """Dataclass-like object protocl."""

    __annotations__: Dict[str, Any]

    def __init__(self, *args, **kwargs) -> None:
        ...


class HasDict(Protocol):
    """Object with `__dict__` attribute."""

    @property
    def __dict__(self):
        ...


_PyBuiltins = Union[str, float, int, bool, dict, None]
JSONLike = Union[_PyBuiltins, HasDict]
Payload = Dict[str, Any]
Operator = Union[
    Callable[[_T], Awaitable[JSONLike]],
    Callable[[], Awaitable[JSONLike]],
    Callable[["Server", _T], Awaitable[JSONLike]],
    Callable[["Server"], Awaitable[JSONLike]],
]
SchemaNeededType = Union[Type[Any], Tuple[Optional[Type[Any]], ...]]
Schema = Dict[str, SchemaNeededType]
OperationData = Tuple[Operator[_T], "OperatorParam", bool]
Operations = Dict[str, OperationData[_T]]
UrlLike = Union[str, "URL"]
LoginFunc = Callable[["Server", str], Awaitable[bool]]
ResponseErrors = Dict[int, Tuple[str, str]]
Listener = Union[
    Callable[["Message", _T], Awaitable[None]],
    Callable[["Message"], Awaitable[None]],
    Callable[[], Awaitable[None]],
]
MessageListeners = Dict[
    Optional[Union[Tuple[str, ...], str]],
    List["ListenerData"],
]
VersionLike = Union[str, "Version"]


TransportMessageListener = Callable[
    ["BaseMessagable", str, Payload, Optional[dict], int],
    Awaitable[None],
]
