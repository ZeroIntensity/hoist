import logging
from typing import Any, Dict

from rich.logging import RichHandler
from typing_extensions import Final

__all__ = (
    "log",
    "hlog",
)

_FORMAT: Final[str] = "%(message)s"
_COLORS: Final[Dict[int, str]] = {
    logging.DEBUG: "bold blue",
    logging.INFO: "bold green",
    logging.WARNING: "bold dim yellow",
    logging.ERROR: "bold red",
    logging.CRITICAL: "bold dim red",
}


def setup_logging() -> None:
    """Set up logging."""
    logging.basicConfig(
        level="INFO",
        format=_FORMAT,
        datefmt="[%X]",
        handlers=[
            RichHandler(
                show_level=False,
                show_path=False,
                show_time=False,
            )
        ],
    )


setup_logging()
logger = logging.getLogger("hoist")


def log(
    key: str,
    value: Any,
    *,
    level: int = logging.INFO,
    highlight: bool = False,
) -> None:
    """Log a rich message."""
    logger.log(
        level,
        f"[{_COLORS[level]}]{key}:[/] {value}",
        extra={
            "markup": True,
            **(
                {
                    "highlighter": None,
                }
                if not highlight
                else {}
            ),
        },
    )


def hlog(
    key: str,
    value: Any,
    *,
    level: int = logging.INFO,
) -> None:
    """Log a highligted rich message."""
    log(
        key,
        value,
        level=level,
        highlight=True,
    )
