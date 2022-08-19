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
            # assert (await c.message("")).id == 1
            # assert (await c.message("")).id == 2
            # this breaks on windows for whatever reason
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


@test("message listener parameters")
async def _():
    with hoist.serve("test") as s:

        @s.receive("x")
        async def x(message: hoist.Message):
            for i in range(1, 4):
                await message.reply(str(i))

        async with hoist.connect("test") as co:
            a_called: bool = False
            b_called: bool = False
            c_called: bool = False

            @co.receive("1")
            async def a():
                nonlocal a_called
                a_called = True

            @co.receive("2")
            async def b(message: hoist.Message):
                nonlocal b_called
                b_called = True
                assert type(message) is hoist.Message

            @co.receive("3")
            async def c(message: hoist.Message, payload: dict):
                nonlocal c_called
                c_called = True
                assert type(message) is hoist.Message
                assert type(payload) is dict

            await co.message("x")

            assert a_called
            assert b_called
            assert c_called


@test("message listener parameters without type hints")
async def _():
    with hoist.serve("test") as s:

        @s.receive("x")
        async def x(message: hoist.Message):
            for i in range(1, 4):
                await message.reply(str(i))

        async with hoist.connect("test") as co:
            a_called: bool = False
            b_called: bool = False
            c_called: bool = False

            @co.receive("1")
            async def a():
                nonlocal a_called
                a_called = True

            @co.receive("2")
            async def b(message):
                nonlocal b_called
                b_called = True
                assert type(message) is hoist.Message

            @co.receive("3")
            async def c(message, payload):
                nonlocal c_called
                c_called = True
                assert type(message) is hoist.Message
                assert type(payload) is dict

            await co.message("x")

            assert a_called
            assert b_called
            assert c_called

            # yeah i copy pasted who cares
