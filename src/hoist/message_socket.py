from typing import Optional

from ._typing import Messagable, Payload


class MessageSocket:
    """Object handling a messagable target."""

    def __init__(
        self,
        conn: Messagable,
    ) -> None:
        self._conn = conn

    async def message(
        self,
        msg: str,
        data: Optional[Payload] = None,
    ) -> None:
        """Send a message to the target."""
        await self._conn.message(msg, data or {})
