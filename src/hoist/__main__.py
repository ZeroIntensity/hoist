import asyncio
import json
import string
import sys
from typing import List, NoReturn, Optional

import click

from .__about__ import __version__
from .exceptions import ServerConnectError, ServerLoginError
from .server import Server
from .utils import connect
from .utils import debug as enable_debug

__all__ = ("main",)


async def _connect(
    token: str,
    url: str,
    op: str,
    payload: dict,
) -> None:
    async with connect(token, url) as c:
        await c.operation(op, payload)


def _error(msg: str) -> NoReturn:
    click.echo(f"error: {msg}", err=True)
    sys.exit(1)


def _process_payload(ctx: click.Context, _, value: str):
    if value is not None:
        try:
            obj = ctx.params["payload"] = json.loads(value)
        except json.JSONDecodeError:
            _error(
                "invalid JSON object passed for payload",
            )
        return obj


@click.command()
@click.argument(
    "action",
    type=click.Choice(["serve", "connect"]),
    required=False,
)
@click.option(
    "--token",
    "-t",
    type=str,
    help="Server login token.",
    default=None,
)
@click.option(
    "--host",
    "-h",
    type=str,
    help="Where to host the server.",
    default="0.0.0.0",
    show_default=True,
)
@click.option(
    "--port",
    "-p",
    type=int,
    help="Port to put the server on.",
    default=5000,
    show_default=True,
)
@click.option(
    "--log-level",
    "-l",
    type=int,
    help="Log level to use.",
    default=20,
)
@click.option(
    "--minimum-version",
    "-m",
    type=str,
    help="Minimum version to connect to the server with.",
    default=None,
)
@click.option(
    "--default-len",
    "-d",
    type=int,
    help="Default length of randomly generated key.",
    default=25,
    show_default=True,
)
@click.option(
    "--version",
    "-v",
    help="Display version and exit.",
    is_flag=True,
)
@click.option(
    "--fancy",
    "-f",
    help="Run the server in fancy mode.",
    is_flag=True,
)
@click.option(
    "--support",
    "-s",
    help="Operation to support.",
    multiple=True,
    default=None,
)
@click.option(
    "--unsupport",
    help="Operation to not support.",
    multiple=True,
    default=None,
)
@click.option(
    "--token-string",
    help="String to use for the autogenerated token.",
    default=string.ascii_letters,
    type=str,
)
@click.option(
    "--url",
    "-u",
    help="URL to connect to.",
    default="http://localhost:5000",
    type=str,
    show_default=True,
)
@click.option(
    "--debug",
    help="Enable debug logging.",
    is_flag=True,
)
@click.option(
    "--execute",
    "-e",
    help="Operation to execute.",
    type=str,
)
@click.option(
    "--payload",
    "-p",
    help="Payload to pass to operation.",
    type=str,
    callback=_process_payload,
)
def main(
    action: str,
    token: Optional[str],
    host: str,
    port: int,
    log_level: int,
    minimum_version: Optional[str],
    default_len: int,
    version: bool,
    fancy: bool,
    support: Optional[List[str]],
    unsupport: Optional[List[str]],
    token_string: str,
    url: str,
    debug: bool,
    execute: str,
    payload: dict,
) -> None:
    """Start a new Hoist server."""
    if version:
        return click.echo(f"Hoist {__version__}")

    if debug:
        enable_debug()

    if action == "serve":
        server = Server(
            token=token,
            log_level=log_level,
            minimum_version=minimum_version,
            default_token_len=default_len,
            fancy=fancy,
            supported_operations=support,
            unsupported_operations=unsupport,
            default_token_choices=token_string,
        )
        server.start(host=host, port=port)
    elif action == "connect":
        if not token:
            _error("missing required option: url")

        loop = asyncio.get_event_loop()

        try:
            loop.run_until_complete(_connect(token, url, execute, payload))
        except ServerConnectError:
            _error(f"could not connect to {url}")
        except ServerLoginError:
            _error(
                f"could not connect to {url}: login token is invalid",
            )
    else:
        _error("missing required argument: action")


if __name__ == "__main__":
    main()
