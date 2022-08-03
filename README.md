# Hoist

## Easy client-server communication

### Quick Example

```py
import hoist

@hoist.main
async def main():
    server = await hoist.connect("http://localhost:5000", "test")
    await server.message("hello", {"a": "world"})
```

```py
import hoist

server = hoist.start("test")  # set "test" as the authentication key

@server.receive("hello")
async def hello(payload: dict) -> None:
    print("hello", payload.get("a"))
```
