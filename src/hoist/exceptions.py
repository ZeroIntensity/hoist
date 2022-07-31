from typing import Optional, Dict, Any


class _ResponseError(Exception):
    def __init__(
        self,
        *args,
        code: int,
        error: str,
        message: str,
        payload: Optional[Dict[str, Any]] = None,
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
    """Client version is not high enough for the server."""
