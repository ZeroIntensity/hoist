# Messages

## Connecting

Before we start sending messages, we need to connect to a server. We can use the `connect_to` utility like we did earlier:

```py
import hoist

@hoist.connect_to("http://localhost:5000", "mytoken")
async def main(server: hoist.Connection) -> None:
    ...
```

Once again, we can check if it's working by sending a message to the server:

```py
await server.message("hello world!")
```

This won't produce any output since we haven't set up any listeners yet, but you should be able to see that everything went well in the server console.

## Listeners

Hoist handles messages in a callback based way, meaning we have to create message listeners. We can do this by using the `receive` decorator on the client or server.

We'll start by setting up a listener on the client:

```py
import hoist

@hoist.connect_to("http://localhost:5000", "mytoken")
async def main(server: hoist.Connection) -> None:
    @server.receive('hello world')
    async def hello(message: hoist.Message, payload: dict):
        # this gets called when the client receives "hello world"
        print(payload.get("name"))
```

Now, we can set it up on the server the same way:

```py
import hoist

server = hoist.start("test")

@server.receive("hi")
async def hi(message: hoist.Message, payload: dict):
    await message.reply("hello world", {"name": "test"})
```
