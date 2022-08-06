from ward import test

import hoist


@test("connect and message a server")
async def _():
    with hoist.serve("test"):
        async with hoist.connect("test") as c:
            await c.message("hello")


@test("message listeners")
async def _():
    with hoist.serve("test") as server:

        @server.receive("hello")
        async def hello(msg: hoist.Message, payload: dict) -> None:
            assert isinstance(msg, hoist.Message)
            assert isinstance(payload, dict)

            assert msg.content == "hello"
            assert isinstance(msg.to_dict(), dict)
            await msg.reply("hi")

        async with hoist.connect("test") as c:

            @c.receive("hi")
            async def hi(msg: hoist.Message, _) -> None:
                assert msg.replying
                assert msg.replying.content == "hello"

            await c.message("hello")
