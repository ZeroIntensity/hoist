import logging
from rich.logging import RichHandler
from typing import Dict
from typing_extensions import Final

_FORMAT: Final[str] = "%(message)s"
_COLORS: Final[Dict[int, str]] = {
    logging.DEBUG: "bold blue",
    logging.INFO: "bold green",
    logging.WARNING: "bold dim yellow",
    logging.ERROR: "bold red",
    logging.CRITICAL: "bold dim red",
}


def setup_logging() -> None:
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


def log(key: str, value: str, *, level: int = logging.INFO) -> None:
    logger.log(
        level,
        f"[{_COLORS[level]}]{key}:[/] {value}",
        extra={"markup": True, "highlighter": None},
    )