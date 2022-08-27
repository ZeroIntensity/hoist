# Broadcasting

Broadcasting a message to all connected clients is super simple. Just call `broadcast` from the server:

```py
import hoist

server = hoist.start()

@hoist.main
async def main():
    await server.broadcast("this is my broadcast!") # see below as to why this is problematic
```

## Dangers

The downside of broadcasting lies in one of Hoist's design choices.

Earlier we talked about how Hoist handles messages in a synchronous way, where there is an expected frame of time where a client will be listening for a message.

But with broadcasts, it's handled in an asynchronous way, meaning there's no way to garuntee that the client will actually receive the message.

Only use broadcasts if you really need to.
