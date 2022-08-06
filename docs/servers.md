# Servers

## Starting Servers

The Hoist CLI can get limited quickly, so how do we create servers without the CLI?

Hoist has two utilities for this, `start` and `serve`.

Lets begin with `start`:

```py
import hoist

server = hoist.start("test")  # uses "test" as the authentication key
```

This is equivalent to running `hoist -t test`, like we did earlier.

Unlike other frameworks, starting a Hoist server is non-blocking, meaning you can run any other code and the server will just run in the background.

Then, to stop the server we can call `server.close()`, like so:

```py
server = hoist.start("test")  # uses "test" as the authentication key
... # do some other stuff here
server.close()
# server is now stopped
```

Calling something like `close()` is generally considered bad practice though, and you should use a context manager instead. That's where `serve` comes in.

This is the same as the above:

```py
with hoist.serve("test") as server:
    ...
# server is stopped once the context is over
```

## Broadcasting

At any point while the server is alive, it may broadcast a message to all connected clients.

However, `broadcast` is an async function, so you should use something like the `main` utility to call it:

```py
import hoist

@hoist.main
async def main():
    server = hoist.start("test")
    await server.broadcast("this is my message")
```

This code won't work very well though, since there won't be any clients connected right after the server starts.

We'll talk more about messages in the next section.
