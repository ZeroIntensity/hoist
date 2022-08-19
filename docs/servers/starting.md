# Starting

## Command Line

You can use the Hoist CLI to start a basic server:

=== "Linux/Mac"

    ```
    python3 -m hoist -t authkey
    ```

=== "Windows"

    ```
    py -m hoist -t authkey
    ```

## Programatically

For most cases, you are going to want more than just the CLI with your server. You can easily start a server via the `start` utility:

```py
import hoist

server = hoist.start("your authentication key")
```

You can also open the server in a temporary context with `serve`:

```py
import hoist

with hoist.serve("auth") as server:
    ...
# server is now closed!
```

Finally, you may directly create a server by instatiating `hoist.Server`:

```py
import hoist

server = hoist.Server("authkey")
server.start()
```

!!! note

    All keyword arguments passed to `start` or `serve` are passed directly to `hoist.Server`.

You may close the server at any time by calling `close`:

```py
import hoist

server = hoist.start(...)
server.close()
```

## Changing the URL

By default, all Hoist servers are put on `0.0.0.0:5000`. If you would like to change the host or port, you can pass them as keyword arguments to `start` or `serve`:

```py
import hoist

server = hoist.start("auth", port=5001)  # starts the server on
```

If you are directly creating a `Server` object, you pass the arguments to `start` instead of the constructor:

```py
import hoist

server = hoist.Server(...)
server.start(port=5001)
```
