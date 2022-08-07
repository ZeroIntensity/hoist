# Messages

## Connecting

Before we start sending messages, we need to connect to a server. We can use the `connect_to` utility like we did earlier:

```py
import hoist

@hoist.connect_to("http://localhost:5000", "mytoken")
async def main(server: hoist.Connection) -> None:
    ...
```
