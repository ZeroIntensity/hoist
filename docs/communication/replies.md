# Replies

## Sending A Reply

You can send a reply by calling `reply` on a `Message` object:

```py
import hoist

server = hoist.start(...)

@server.receive("...")
async def msg(message: hoist.Message):
    new_message = await message.reply("this is my reply!")
    print(f'new message id is {new_message.id}')
```

## Listening For Replies

Since most message responses are called by the time we might call the `receive` decorator, things might not work as intended.

So, we need to ensure that the receivers are setup _before_ we send the message. We can do this via `message_later`:

```py
@server.receive("...")
async def msg():
    async with server.message_later("hello") as msg:
        @msg.receive("hi")
        async def hi(msg: hoist.Message):
            ...
    # message gets sent at the end of the context, message listener is ready!
```
