import logging
from typing import Any

from ._logging import log
from ._typing import Payload, Schema
from .exceptions import SchemaValidationError

__all__ = (
    "invalid_payload",
    "verify_schema",
)


def verify_schema(schema: Schema, data: Payload) -> None:
    """Verify that a payload matches the schema."""
    for key, typ in schema.items():
        value = data.get(key)
        if key is Any:
            continue

        vtype = type(value) if value is not None else None

        if isinstance(typ, tuple):
            if vtype not in typ:
                log(
                    "schema validation",
                    f"expected {', '.join([i.__name__ if i else 'None' for i in typ])}, got {vtype}",  # noqa
                    level=logging.DEBUG,
                )
                raise SchemaValidationError(current=vtype, needed=typ)
            continue

        if vtype is not typ:
            log(
                "schema validation",
                f"expected {typ.__name__}, got {vtype}",
                level=logging.DEBUG,
            )
            raise SchemaValidationError(current=vtype, needed=typ)


def invalid_payload(exc: SchemaValidationError) -> Payload:
    """Raise an invalid payload error."""
    needed = exc.needed

    return {
        "current": exc.current,
        "needed": exc.needed.__name__  # type: ignore
        if not isinstance(needed, tuple)
        else [i.__name__ if i else str(i) for i in needed],
    }
