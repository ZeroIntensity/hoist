import logging

import aiohttp
from ward import fixture, test

import hoist


@fixture()
def server():
    with hoist.serve("test", log_level=logging.DEBUG) as server:
        yield server


@fixture()
async def client():
    async with aiohttp.ClientSession() as s:
        yield s


@test("startup and shutdown")
async def _(s=server):
    async with aiohttp.ClientSession() as s:
        async with s.get("http://localhost:5000/hoist") as res:
            assert res.status == 200

        async with s.get("http://localhost:5000/hoist/ack") as res:
            assert await res.json() == {"version": hoist.__version__}


@test("authentication")
async def _(s=server, c=client):
    async with c.ws_connect("ws://localhost:5000/hoist") as w:
        ...
