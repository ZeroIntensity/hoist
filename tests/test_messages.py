from typing import Any

from ward import fixture, test

import hoist


@fixture
def server():
    with hoist.serve("test") as s:

        @s.receive("hello")
        async def hello(msg: hoist.Message):
            await msg.reply("hi")

        @s.receive("test")
        async def test(msg: hoist.Message):
            await msg.reply("123")

        yield s


@test("basic messaging")
async def _():
    with hoist.serve("test"):
        async with hoist.connect("test") as c:
            assert (await c.message("")).id == 1
            assert (await c.message("")).id == 2
            msg = await c.message("123")
            assert msg.content == "123"


@test("messages from server")
async def _(s: hoist.Server = server):  # type: ignore
    async with hoist.connect(s.token) as c:
        called: bool = False

        @c.receive("hi")
        async def hi():
            await c.message("test")

        @c.receive("123")
        async def x():
            nonlocal called
            called = True

        await c.message("hello")
        assert called


@test("replies")
async def _(s: hoist.Server = server):  # type: ignore
    async with hoist.connect(s.token) as c:
        called: bool = False

        @c.receive("123")
        async def x():
            nonlocal called
            called = True

        async with c.message_later("hello") as msg:

            @msg.receive("hi")
            async def hi(msg: hoist.Message):
                await msg.reply("test")

        assert called
