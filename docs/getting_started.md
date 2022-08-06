# Getting Started

## Installation

=== "Linux/Mac"

    ```
    python3 -m pip install -U hoist-new
    ```

=== "Windows"

    ```
    py -m pip install -U hoist-new
    ```

## Basic Server

Once Hoist has ben installed, we can run a basic server to make sure everything is working properly.

In your terminal, run the following:

=== "Linux/Mac"

    ```
    python3 -m hoist -t test
    ```

=== "Windows"

    ```
    py -m hoist -t test
    ```

!!! note

    The `-t` flag just specifies the authentication key used by the server. This can be any string that you want, and when left blank, Hoist will automatically create a secure random string for you.

Running this command will start the server on port 5000 by default.

You should see the following in your terminal:

```
startup: starting server on 0.0.0.0:5000 with token test
```

Now, open a new Python file and use the following to test that the server is working properly.

```py
import hoist

@hoist.connect_to("http://localhost:5000", "test")
async def main(server: hoist.Connection) -> None:
    await server.message("hi")
```

Now, running this file shouldn't have any output, but if we look at the server, it should now look something like this:

```
connect: connecting to 127.0.0.1:41788
login: 127.0.0.1:41788 has successfully authenticated
disconnect: no longer receiving from 127.0.0.1:41788
```

Congratulations! You have successfully written your first program with Hoist!

## Utilities

In the above code, you may have noticed something different about Hoist. Traditionally, you would instantiate some class and then use that in a context manager. Instead, we used the `connect_to` decorator. This is one of Hoist's utilities.

Hoist has several utilities to make things nicer for the developer and to minimize boilerplate code. The above is identical to the following code:

```py
import hoist
import asyncio

async def main():
    async with hoist.connect("test") as server:
        await server.message("hi")

if __name__ == '__main__':
    asyncio.run(main())
```

Sure, you could use this and it would work just fine, but writing it might waste time or get repetitive over time.

However, high-level utilities like that can have downsides. Something like `connect_to` only works for that single use case, and isn't very flexible.

There are alternatives for when you need it though. Hoist has a utility called `main`, which removes `asyncio` boilerplate:

```py
# also identical to the above
import hoist

@hoist.main
async def main():
    async with hoist.connect("test") as server:
        await server.message("hi")

# no need for asyncio.run!
```

Hoist even does some magic internally to replicate the `#!python if __name__ == '__main__'`!
