# Welcome to Hoist's documentation!

-   [Repository](https://github.com/ZeroIntensity/hoist)
-   [PyPI](https://pypi.org/project/hoist-http/)

### Quick Example

```py
import hoist

server = hoist.start("test") # set "test" as the authentication key

@server.receive("hello")
async def hello(message: hoist.Message) -> None:
    print("server got hello")
    await message.reply("hi")
```

```py
import hoist

@hoist.connect_with("test") # log with "test"
async def main(server: hoist.Connection):
    @server.receive("hi")
    async def hello():
        print("client got hi")

    await server.message("hello")
```

## What is Hoist

Hoist is a library created to make client-server communication very simple.

At its core, it's just a WebSocket/HTTP library, but built in a way to make the developers life easy while keeping communication flexible and predictable.

## Why should I use Hoist?

Hoist is high level and focuses on developer experience and simplicity. It does all the heavy lifting, so you don't have to.

In Hoist, you don't have to worry about your server crashing or giving some arbitrary response.

## Why shouldn't I use Hoist?

For the reasons above, Hoist has to make some design choices that others might not agree with, the biggest issue being external flexibility.

As of now, you pretty much can't get Hoist to work with other frameworks and errors can be introduced when not using some of the utilities.

If you need a nice way to communicate between a client and server, Hoist is a great option, but if you need a fullstack web application, then not so much.
