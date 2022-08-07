from ward import raises, test

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


"""

"""


@test("client error handling")
async def _():
    with raises(hoist.ServerConnectError):
        async with hoist.connect("test", "http://example.com"):
            ...

    with raises(hoist.ServerConnectError):
        async with hoist.connect(""):
            ...

    with raises(ValueError):
        with hoist.serve():
            await hoist.Connection("http://localhost:5000").connect()

    with raises(hoist.NotConnectedError):
        c = hoist.Connection("")
        await c.close()
        await c.close()

    with hoist.serve("test"):
        c = hoist.Connection("http://localhost:5000")
        await c.connect("test")

        with raises(hoist.AlreadyConnectedError):
            await c.connect("test")

        await c.close()
