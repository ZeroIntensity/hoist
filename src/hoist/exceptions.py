class _ResponseError(Exception):
    def __init__(
        self,
        *args,
        code: int,
        error: str,
        message: str,
        **kwargs,
    ) -> None:
        self._code: int = code
        self._error: str = error
        self._message: str = message
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


class ServerResponseError(_ResponseError):
    """Generic bad server response."""


class ServerLoginFailed(Exception):
    """Failed to log in to the target server."""


class ClientError(_ResponseError):
    """The client caused an error on the server."""
