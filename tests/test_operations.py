from ward import test

import hoist


@test("custom operations")
async def _():

    with hoist.serve("test") as s:

        @s.operation("hello")
        async def hello():
            return 1

        @s.operation("test")
        async def test(text: str):
            return text

        @s.operation("x")
        async def x(server: hoist.Server, payload: dict):
            assert type(server) is hoist.Server
            assert type(payload) is dict
            return 1

        @s.operation("server only")
        async def server_only(server: hoist.Server):
            assert type(server) is hoist.Server
            return 1

        @s.operation("payload only")
        async def payload_only(payload: dict):
            assert type(payload) is dict
            return 1

        async with hoist.connect("test") as c:
            assert await c.operation("hello") == 1
            assert await c.operation("test", text="hi") == "hi"
            assert await c.operation("x") == 1
            assert await c.operation("server only") == 1
            assert await c.operation("payload only") == 1


@test("custom operations without type hints")
async def _():
    with hoist.serve("test") as s:

        @s.operation("1")
        async def first(payload):
            assert type(payload) is dict
            return 1

        @s.operation("2")
        async def second(server, payload):
            assert type(server) is hoist.Server
            assert type(payload) is dict
            assert "x" in payload
            return 1

        async with hoist.connect("test") as c:
            assert await c.operation("1") == 1
            assert await c.operation("2", x="") == 1
