import aiohttp
from ward import test

import hoist


@test("startup and shutdown")
async def _():
    async with aiohttp.ClientSession() as s:
        with hoist.serve():
            async with s.get("http://localhost:5000/hoist") as res:
                assert res.status == 200

        with hoist.serve(port=5005):
            async with s.get("http://localhost:5005/hoist") as res:
                assert res.status == 200
