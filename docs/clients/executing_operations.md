# Executing Operations

## Builtins

For convenience, all builtin utilities are defined as a method on `Connection`:

```py
import hoist

@hoist.connect_with(...)
async def main(c: hoist.Connection):
    await c.print("hello world")
```

These do nothing special internally whatsoever.

## Executing

Use the `operation` method to run an operation on the server:

```py
import hoist

@hoist.connect_with(...)
async def main(c: hoist.Connection):
    await c.operation("...")
```

You may pass parameters via keyword arguments or simply passing a `dict`:

```py
import hoist

@hoist.connect_with(...)
async def main(c: hoist.Connection):
    await c.operation("...", {"a": "b"})
    await c.operation("...", a="b")
    # these two are equivalent!
    await c.operation("...", {"a": "b"}, c="d")  # you can even do this!
```
