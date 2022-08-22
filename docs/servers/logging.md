# Logging

## Changing Level

You can change the log level by passing `log_level`:

```py
import hoist
import logging

server = hoist.start("authkey", log_level=logging.ERROR)
```

## Debug Logging

If you would like to enable debug logging, instead of manually passing `log_level`, you should call `hoist.debug`:

```py
import hoist

hoist.debug()
# debug logging has been enabled!
hoist.start(...)
```

!!! note

    `hoist.debug()` works for all of Hoist, not just servers.

### Tracing

There are some cases where you might want to trace where some debug logs are actually called from. You can enable this by passing `trace=True` to `debug`:

```py
import hoist

hoist.debug(trace=True)
...
```

### Uvicorn Logging

In rare cases, some important logs may only show up on the [uvicorn](https://www.uvicorn.org/) logger instead of Hoist's. To enable `uvicorn`'s logging, pass `enable_uvicorn=True`:

```py
import hoist

hoist.debug(enable_uvicorn=True)
server = hoist.start(...)
```

## Getting The Logger

All Hoist logging is done under the `hoist` logger:

```py
import logging
import hoist

hoist_logger = logging.getLogger("hoist")
```
