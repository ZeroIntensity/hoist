from ._typing import Operations, Schema, Payload, Operator
from typing import NamedTuple, get_type_hints, TypeVar, Type
from .exceptions import SchemaValidationError

T = TypeVar("T")


class _Print(NamedTuple):
    text: str


async def _print(payload: _Print):
    print(payload.text)


BASE_OPERATIONS: Operations = {"print": _print}


def verify_schema(schema: Schema, data: Payload) -> None:
    """Verify that a payload matches the schema."""
    for key, typ in schema.items():
        value = data.get(key)
        vtype = type(value) if value is not None else None

        if type(typ) is tuple:
            if vtype not in typ:
                raise SchemaValidationError

        if vtype is not typ:
            raise SchemaValidationError


async def call_operation(op: Operator[T], payload: Payload) -> None:
    hints = get_type_hints(op)
    cl: Type[T] = hints[list(hints.keys())[0]]

    verify_schema(get_type_hints(cl), payload)
    await op(cl(**payload))
