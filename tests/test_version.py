from versions import parse_version
from ward import raises, test

import hoist

CURRENT_VERSION = parse_version(hoist.__version__)


@test("test minimum server version")
async def _():
    with hoist.serve(minimum_version=CURRENT_VERSION.next_patch()):
        with raises(hoist.InvalidVersionError):
            async with hoist.connect("a"):
                ...


@test("test minimum client version")
async def _():
    with hoist.serve():
        with raises(hoist.InvalidVersionError):
            async with hoist.connect(
                "a",
                minimum_version=CURRENT_VERSION.next_patch(),
            ):
                ...
