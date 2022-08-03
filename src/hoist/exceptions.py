from typing import Any, Dict, Optional

from ._typing import Payload


class _ResponseError(Exception):
    def __init__(
        self,
        *args,
        code: int,
        error: str,
        message: str,
        payload: Optional[Payload] = None,
        **kwargs,
    ) -> None:
        self._code: int = code
        self._error: str = error
        self._message: str = message
        self._payload = payload
        super().__init__(*args, **kwargs)

    @property
    def code(self) -> int:
        """Error code."""
        return self._code

    @property
    def error(self) -> str:
        """Error name."""
        return self._error

    @property
    def message(self) -> str:
        """Error message."""
        return self._message

    @property
    def payload(self) -> Optional[Dict[str, Any]]:
        """Error payload."""
        return self._payload


class ServerResponseError(_ResponseError):
    """Generic bad server response."""


class ServerLoginError(Exception):
    """Failed to log in to the target server."""


class ClientError(_ResponseError):
    """The client caused an error on the server."""


class InvalidVersionError(Exception):
    """Version is not high enough."""


class SchemaValidationError(Exception):
    """Schema validation failed."""


class CloseSocket(Exception):
    """Close the socket."""


class NotConnectedError(Exception):
    """Socket is not connected to the server."""


class InvalidOperationError(Exception):
    """Operation was not found."""


class AlreadyConnectedError(Exception):
    """Attempted to connect to the WebSocket twice."""


class InvalidActionError(Exception):
    """Invalid action was sent to the server."""
