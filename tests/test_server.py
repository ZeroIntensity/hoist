import string

import aiohttp
from ward import raises, test

import hoist


@test("startup and shutdown")
async def _():
    async with aiohttp.ClientSession() as s:
        with hoist.serve():
            async with s.get("http://localhost:5000/hoist") as res:
                assert res.status == 200

        with hoist.serve(port=5005):
            async with s.get("http://localhost:5005/hoist/ack") as res:
                assert await res.json() == {"version": hoist.__version__}


@test("authentication")
async def _():
    with hoist.serve("test"):
        async with hoist.connect("test"):
            ...

        with raises(hoist.ServerLoginError):
            async with hoist.connect("x"):
                ...


@test("auto token generation")
async def _():
    with hoist.serve() as s:
        assert len(s.token) == 25

    with hoist.serve(default_token_len=50) as s:
        assert len(s.token) == 50

    with hoist.serve(default_token_choices=string.digits) as s:
        assert s.token.isdigit()


@test("server error handling")
async def _():
    server = hoist.Server()

    with raises(hoist.ServerNotStartedError):
        await server.broadcast("")

    with raises(hoist.ServerNotStartedError):
        server.close()

    server.start()

    with raises(hoist.AlreadyInUseError):
        server.start()

    server.close()
