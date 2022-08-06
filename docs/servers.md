# Servers

## Starting Servers

The Hoist CLI can get limited quickly, so how do we create servers without the CLI?

Hoist has two utilities for this, `start` and `serve`.

### Start

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

### Serve

Calling something like `close()` is generally considered bad practice though, and you should use a context manager instead. That's where `serve` comes in.

This is the same as the above:

```py
with hoist.serve("test") as server:
    ...
# server is stopped once the context is over
```

## Authentication

In order for a client to connect, it must authenticate itself. By default, this is done by securely comparing the key sent by the client to the token on the server, and returning a response accordingly. However, Hoist allows you to change this behavior.

A custom login function should have a signature like this:

```py
async def login(
    server: hoist.Server, # this is the server object
    sent_token: str, # this is the token sent by the client
) -> bool: # must return a bool, true being successful authentication
    ...
```

Now, you may pass it to `start` or `serve`, like so:

```py
async def login(
    server: hoist.Server,
    sent_token: str,
) -> bool:
    token: str = server.token
    # this is the servers token, which in this case is "test"
    return sent_token == token

server = hoist.start("test", login_func=login)
```

!!! danger

    Using `==` when comparing the servers token to the sent token is vulnerable to [timing attacks](https://en.wikipedia.org/wiki/Timing_attack). It's only used for simplicity in this example. You should something like [`secrets.compare_digest`](https://docs.python.org/3/library/secrets.html#secrets.compare_digest) to handle this in a secure way.

## Version Management

Maybe you are using a version that has a brand new feature or a breaking change. This means that a Hoist client won't work on older versions, so how is this handled? By default, Hoist doesn't do any version checking when a client connects.

To opt-in to this feature, pass `minimum_version` when creating your server:

```py
import hoist

server = hoist.start("test", minimum_version=hoist.__version__)
```

This will require all clients that connect to be the same version as you, or higher.

## Auto-Generated Tokens

So far we've only manually set the token when creating the server. When you don't specify the token, Hoist automatically generates a secure 25 character random string to use instead.

You can see this in action by simply using the CLI:

=== "Linux/Mac"

    ```
    python3 -m hoist
    ```

=== "Windows"

    ```
    py -m hoist
    ```

### Customization

Lets say we want 50 characters instead of 25:

```py
hoist.start(default_token_len=50)
```

Or maybe we want the key to only use punctuation characters:

```py
import string

hoist.start(default_token_choices=string.punctuation)
```

If you want the token to be hidden on startup (meaning you can only view it via the `token` property), you can pass `#!python hide_token=True`:

```py
import hoist

hoist.start(hide_token=True)
```

Then in your terminal, it should show the following:

```
startup: starting server on 0.0.0.0:5000
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

## Logging

If you want Hoist to change the level of server messages, you can pass `log_level`:

```py
import hoist
import logging

hoist.start(log_level=logging.ERROR) # only log errors
```

### Debug Logging

If you would like debug logging, you can use the `debug` utility:

```py
import hoist

hoist.debug() # equivalent to passing log_level=logging.DEBUG
hoist.start()
```

### Tracing

`debug` comes with two parameters, `trace` and `enable_uvicorn`.

You can use `trace` to include where the log was called:

```py
hoist.debug(trace=True)
hoist.start()
```

The log message now looks like:

```
(start) startup: starting server on...
```

### Uvicorn

There are some cases where an internal error might only show up on the `uvicorn` logger.

To enable uvicorn logging, pass `enable_uvicorn=True` to `debug`:

```py
hoist.debug(enable_uvicorn=True)
hoist.start()
```

Now, when running the terminal should now look like:

```
startup: starting server on 0.0.0.0:5000 with token ...
INFO:     Started server process [...]
Started server process [...]
INFO:     Waiting for application startup.
Waiting for application startup.
INFO:     Application startup complete.
Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:5000 (Press CTRL+C to quit)
Uvicorn running on http://0.0.0.0:5000 (Press CTRL+C to quit)
```
