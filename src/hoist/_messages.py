from typing import Any, List, Optional, Tuple, TypeVar, Union, get_type_hints

from typing_extensions import Final

from ._operations import verify_schema
from ._typing import (
    DataclassLike, Listener, ListenerData, Messagable, MessageListeners,
    Payload, Schema
)
from .message_socket import MessageSocket

__all__ = ("MessageListener",)

T = TypeVar("T", bound=DataclassLike)

NEW_MESSAGE: Final[str] = "newmsg"


async def _process_listeners(
    listeners: Optional[List[ListenerData]],
    payload: Payload,
    conn: Messagable,
) -> None:

    for i in listeners or ():
        func = i[0]
        param = i[1]
        is_schema: bool = isinstance(param, dict)

        schema: Any = param if is_schema else get_type_hints(param)
        verify_schema(schema, payload)

        await func(
            MessageSocket(conn),
            payload if is_schema else param(**payload),  # type: ignore
        )


class MessageListener:
    """Base class for handling message listening."""

    def __init__(
        self,
        extra_listeners: Optional[MessageListeners] = None,
    ):
        self._message_listeners: MessageListeners = {
            **(extra_listeners or {}),
        }

    @property
    def message_listeners(self) -> MessageListeners:
        """Listener function for messages."""
        return self._message_listeners

    async def _call_listeners(
        self,
        ws: Messagable,
        message: str,
        payload: Payload,
    ) -> None:
        ml = self.message_listeners
        listeners = ml.get(message)
        data = (payload, ws)
        await _process_listeners(listeners, *data)

        glbl = ml.get(None)
        await _process_listeners(glbl, *data)

    def receive(
        self,
        message: Optional[Union[str, Tuple[str, ...]]] = None,
        parameter: Optional[Union[Schema, T]] = None,
    ):
        """Add a listener for message receiving."""

        def decorator(func: Listener):
            listeners = self.message_listeners

            param = parameter

            if not param:
                hints = get_type_hints(func)
                if hints:
                    param = hints[tuple(hints.keys())[1]]

            value = (func, (param or {}))

            if message in listeners:
                listeners[message].append(value)
            else:
                listeners[message] = [value]

        return decorator
