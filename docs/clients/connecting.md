# Connecting

## Utilities

There are a few different utilities for connecting to a target, `connect` being the simplest:

!!! note

    All connection utilities use `http://localhost:5000` as the target by default.

```py
import hoist

@hoist.main  # using the main utility
async def main():
    async with hoist.connect("...") as conn:
        ...
```

If you don't want to use the `async with` block, you may use `connect_directly` instead:

```py
import hoist

@hoist.main
async def main():
    conn = await hoist.connect_directly("...")
    ...
```

`connect_directly` lets Hoist use a [weakref finalizer](https://docs.python.org/3/library/weakref.html#weakref.finalize) instead of the context manager.

Finally, you may use the `connect_with` decorator, to omit `hoist.main` completely:

```py
import hoist

@hoist.connect_with("test")
async def main(conn: hoist.Connection):
    ...
```

## Manually

If theres some special case where you can't use a utility, you may directly instantiate `hoist.Connection`:

```py
import hoist

async def main():
    conn = hoist.Connection("http://localhost:5000", "test")
    await conn.connect()
    ...
    await conn.close()
```
