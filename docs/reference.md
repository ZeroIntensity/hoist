# Reference

## `hoist.exceptions`

!!! note

    Everything in this module derives from `BaseException`, and may be raised.


### `AlreadyConnectedError`



**Attempted to connect to the WebSocket twice.**

---


### `AlreadyInUseError`



**Port is already in use.**

---


### `BadContentError`



**Invalid JSON content was sent to the server.**

---


### `ClientError`

*Derives from `hoist.exceptions._ResponseError`*

**The client caused an error on the server.**

---


### `ConnectionFailedError`



**Failed to connect to the target server..**

---


### `InvalidActionError`



**Invalid action was sent to the server.**

---


### `InvalidOperationError`



**Operation was not found.**

---


### `NotConnectedError`



**Socket is not connected to the server.**

---


### `SchemaValidationError`



**Schema validation failed.**

---

#### `current`

```py
@property
def current() -> Optional[Type[Any]]
```

*Current type.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/exceptions.py#L94)

---
#### `needed`

```py
@property
def needed() -> Union[Type[Any], Tuple[Optional[Type[Any]], ...]]
```

*Type(s) needed to be valid.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/exceptions.py#L89)

---
### `ServerConnectError`



**Failed to connect to a server.**

---


### `ServerLoginError`



**Failed to log in to the target server.**

---


### `ServerNotStartedError`



**Server is not started.**

---


### `ServerResponseError`

*Derives from `hoist.exceptions._ResponseError`*

**Generic bad server response.**

---


### `InvalidVersionError`



**Version is not high enough.**

---


### `CloseSocket`



**Close the socket.**

---


### `_ResponseError`



#### `__init__`
```py

def __init__(
    code: int,
    error: str,
    message: str,
    payload: Optional[Dict[str, Any]]
) -> None
```



---


#### `code`

```py
@property
def code() -> int
```

*Error code.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/exceptions.py#L38)

---
#### `error`

```py
@property
def error() -> str
```

*Error name.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/exceptions.py#L43)

---
#### `message`

```py
@property
def message() -> str
```

*Error message.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/exceptions.py#L48)

---
#### `payload`

```py
@property
def payload() -> Optional[Dict[str, Any]]
```

*Error payload.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/exceptions.py#L53)

---

## `hoist.client`

### `Connection`

*Derives from `hoist._messages.MessageListener`*

**Class handling a connection to a server.**

#### `__init__`
```py

def __init__(
    url: Union[str, yarl.URL],
    token: Optional[str],
    loop: Optional[asyncio.events.AbstractEventLoop],
    session: Optional[aiohttp.client.ClientSession],
    extra_listeners: Optional[Dict[Union[Tuple[str, ...], str, None], List[Tuple[Callable[[hoist.message.Message, ~_A], Awaitable[None]], Union[~_A, Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]]]]]]],
    minimum_version: Union[str, versions.version.Version, None]
) -> None
```



---


#### `close`
```py

def close() -> None
```

*Close the connection.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L67)

---

#### `connect`
```py

def connect(
    token: Optional[str]
) -> None
```

*Open the connection.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L101)

---

#### `message`
```py

def message(
    msg: str,
    data: Optional[Dict[str, Any]],
    replying: Optional[hoist.message.Message]
) -> Message
```

*Send a message to the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L174)

---
#### `closed`

```py
@property
def closed() -> bool
```

*Whether the client is closed.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L47)

---
#### `connected`

```py
@property
def connected() -> bool
```

*Whether the server is currently connected.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L62)

---
#### `token`

```py
@property
def token() -> Optional[str]
```

*Authentication token of the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L57)

---
#### `url`

```py
@property
def url() -> Union[str, yarl.URL]
```

*URL of the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L52)

---

## `hoist.message`

### `Message`

*Derives from `hoist._messages.MessageListener`*

**Object handling a messagable target.**

#### `__init__`
```py

def __init__(
    conn: Messagable,
    msg: str,
    id: int,
    data: Optional[Dict[str, Any]],
    replying: Optional[hoist.message.Message]
) -> None
```



---


#### `reply`
```py

def reply(
    msg: str,
    data: Optional[Dict[str, Any]]
) -> Message
```

*Send a message to the target.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L46)

---

#### `to_dict`
```py

def to_dict() -> dict
```

*Convert the message to a dictionary.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L54)

---
#### `content`

```py
@property
def content() -> str
```

*Message content.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L26)

---
#### `data`

```py
@property
def data() -> Dict[str, Any]
```

*Raw message payload.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L31)

---
#### `id`

```py
@property
def id() -> int
```

*Message ID.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L41)

---
#### `replying`

```py
@property
def replying() -> Optional[hoist.message.Message]
```

*Message that the current message is replying to.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L36)

---

## `hoist.server`

### `Server`

*Derives from `hoist._messages.MessageListener`*

**Class for handling a server.**

#### `__init__`
```py

def __init__(
    token: Optional[str],
    default_token_len: int,
    default_token_choices: Union[str, Sequence[str]],
    hide_token: bool,
    login_func: Callable[[hoist.server.Server, str], Awaitable[bool]],
    log_level: Optional[int],
    minimum_version: Union[str, versions.version.Version, None],
    extra_operations: Optional[Dict[str, Callable[[~_T], Awaitable[Any]]]],
    unsupported_operations: Optional[Sequence[str]],
    supported_operations: Optional[Sequence[str]],
    extra_listeners: Optional[Dict[Union[Tuple[str, ...], str, None], List[Tuple[Callable[[hoist.message.Message, ~_A], Awaitable[None]], Union[~_A, Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]]]]]]]
) -> None
```



---


#### `broadcast`
```py

def broadcast(
    message: str,
    payload: Optional[Dict[str, Any]]
) -> None
```

*Send a message to all connections.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L461)

---

#### `close`
```py

def close() -> None
```

*Close the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L480)

---

#### `start`
```py

def start(
    host: str,
    port: int
) -> None
```

*Start the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L412)

---
#### `supported_operations`

```py
@property
def supported_operations() -> Sequence[str]
```

*Operations supported by the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L139)

---
#### `token`

```py
@property
def token() -> str
```

*Authentication token used to connect.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L182)

---
#### `unsupported_operations`

```py
@property
def unsupported_operations() -> Sequence[str]
```

*Operations blacklisted by the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L144)

---
### `_SocketMessageTransport`



**Connection class for wrapping message objects.**

#### `__init__`
```py

def __init__(
    ws: Socket,
    server: Server,
    event_message: str
) -> None
```



---


#### `message`
```py

def message(
    msg: str,
    data: Optional[Dict[str, Any]],
    replying: Optional[hoist.message.Message]
) -> Message
```

*Send a message to the client.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L76)

---

### `_base_login`

```py

def _base_login(
    server: Server,
    sent_token: str
) -> bool
```

*Default login function used by servers.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L46)

---

### `_invalid_payload`

```py

def _invalid_payload(
    exc: SchemaValidationError
) -> Dict[str, Any]
```

*Raise an invalid payload error.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L51)

---


## `hoist._client_ws`

### `ServerSocket`



**Class for handling a WebSocket connection to a server.**

#### `__init__`
```py

def __init__(
    client: Connection,
    ws: ClientWebSocketResponse,
    token: str
) -> None
```



---


#### `close`
```py

def close() -> None
```

*Close the socket.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_client_ws.py#L176)

---

#### `login`
```py

def login(
    listener: Callable
) -> None
```

*Send login message to the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_client_ws.py#L146)

---

#### `send`
```py

def send(
    payload: Dict[str, Any],
    reply: bool
) -> Optional[hoist._client_ws._Response]
```

*Send a message to the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_client_ws.py#L211)

---
#### `logged`

```py
@property
def logged() -> bool
```

*Whether the socket has authenticated with the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_client_ws.py#L171)

---
### `_Response`

*Derives from `builtins.tuple`*

**_Response(success, data, error, message, desc, code)**

#### `__init__`
```py

def __init__()
```

*Initialize self.  See help(type(self)) for accurate signature.*

---




## `hoist._messages`

### `create_message`

```py

def create_message(
    conn: Messagable,
    data: Dict[str, Any]
) -> Message
```

*Generate a message object from a payload.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L31)

---

### `MessageListener`



**Base class for handling message listening.**

#### `__init__`
```py

def __init__(
    extra_listeners: Optional[Dict[Union[Tuple[str, ...], str, None], List[Tuple[Callable[[hoist.message.Message, ~_A], Awaitable[None]], Union[~_A, Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]]]]]]]
)
```



---


#### `receive`
```py

def receive(
    message: Union[str, Tuple[str, ...], None],
    parameter: Union[Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]], ~T, None]
)
```

*Add a listener for message receiving.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L116)

---
#### `current_id`

```py
@property
def current_id() -> int
```

*Current message ID.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L142)

---
#### `message_listeners`

```py
@property
def message_listeners() -> Dict[Union[Tuple[str, ...], str, None], List[Tuple[Callable[[hoist.message.Message, ~_A], Awaitable[None]], Union[~_A, Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]]]]]]
```

*Listener function for messages.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L95)

---
### `_process_listeners`

```py

def _process_listeners(
    listeners: Optional[List[Tuple[Callable[[hoist.message.Message, ~_A], Awaitable[None]], Union[~_A, Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]]]]]],
    msg: str,
    id: int,
    payload: Dict[str, Any],
    conn: Messagable,
    replying: Optional[hoist.message.Message]
) -> None
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L46)

---


## `hoist._logging`

### `hlog`

```py

def hlog(
    key: str,
    value: Any,
    level: int
) -> None
```

*Log a highligted rich message.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_logging.py#L84)

---

### `log`

```py

def log(
    key: str,
    value: Any,
    level: int,
    highlight: bool
) -> None
```

*Log a rich message.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_logging.py#L44)

---

### `setup_logging`

```py

def setup_logging() -> None
```

*Set up logging.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_logging.py#L24)

---


## `hoist._operations`

### `verify_schema`

```py

def verify_schema(
    schema: Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]],
    data: Dict[str, Any]
) -> None
```

*Verify that a payload matches the schema.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_operations.py#L20)

---

### `_Print`

*Derives from `builtins.tuple`*

**_Print(text,)**

#### `__init__`
```py

def __init__()
```

*Initialize self.  See help(type(self)) for accurate signature.*

---



### `_print`

```py

def _print(
    payload: _Print
)
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_operations.py#L13)

---

### `call_operation`

```py

def call_operation(
    op: Callable[[~T], Awaitable[Any]],
    payload: Dict[str, Any]
) -> None
```

*Call an operation.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_operations.py#L35)

---


## `hoist._socket`

### `Socket`



**Class for handling a WebSocket.**

#### `__init__`
```py

def __init__(
    ws: WebSocket
)
```



---


#### `close`
```py

def close(
    code: int
) -> None
```

*Gracefully close the connection.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L145)

---

#### `connect`
```py

def connect() -> None
```

*Establish the WebSocket connection.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L42)

---

#### `error`
```py

def error(
    code: int,
    description: Optional[str],
    payload: Optional[Dict[str, Any]]
) -> NoReturn
```

*Send an error to the client.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L88)

---

#### `recv`
```py

def recv(
    schema: Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]]
) -> List[Any]
```

*Receive a message from the client.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L122)

---

#### `recv_only`
```py

def recv_only(
    schema: Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]]
) -> Any
```

*Receive a single key from the client.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L141)

---

#### `success`
```py

def success(
    payload: Optional[Dict[str, Any]],
    message: Optional[str]
) -> None
```

*Send a success to the client.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L109)

---
#### `address`

```py
@property
def address() -> Optional[starlette.datastructures.Address]
```

*Address object of the connection.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L153)

---
#### `logged`

```py
@property
def logged() -> bool
```

*The authentication status of the current connection.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L57)

---
#### `ws`

```py
@property
def ws() -> WebSocket
```

*Raw WebSocket object.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L52)

---
### `make_client`

```py

def make_client(
    addr: Optional[starlette.datastructures.Address]
) -> str
```

*Make a client string.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L27)

---

### `make_client_msg`

```py

def make_client_msg(
    addr: Optional[starlette.datastructures.Address],
    to: bool
) -> str
```

*Create a client message.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L21)

---


## `hoist._uvicorn`

### `UvicornServer`

*Derives from `uvicorn.server.Server`*

**Threadable uvicorn server.**

#### `__init__`
```py

def __init__() -> None
```



---


#### `close_thread`
```py

def close_thread()
```

*Close the running thread.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_uvicorn.py#L28)

---

#### `run_in_thread`
```py

def run_in_thread()
```

*Run the server in a thread.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_uvicorn.py#L19)

---


## `hoist.utils`

### `connect`

```py

def connect(
    token: str,
    url: Union[str, yarl.URL],
    kwargs: Any
)
```

*Connect to a Hoist server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/contextlib.py#L312)

---

### `connect_to`

```py

def connect_to(
    url: Union[str, yarl.URL],
    token: str,
    kwargs: Any
)
```

*Connect to a server with a decorator.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/utils.py#L75)

---

### `debug`

```py

def debug(
    trace: Union[bool, str],
    enable_uvicorn: bool
) -> None
```

*Enable debug logging.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/utils.py#L117)

---

### `main`

```py

def main(
    func: Callable[[], Coroutine[Any, Any, Any]]
) -> None
```

*Run a main async function.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/utils.py#L26)

---

### `serve`

```py

def serve(
    token: Optional[str],
    server: Optional[hoist.server.Server],
    host: str,
    port: int
)
```

*Serve a Hoist server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/contextlib.py#L279)

---

### `start`

```py

def start(
    token: Optional[str],
    server: Optional[hoist.server.Server],
    host: str,
    port: int
) -> Server
```

*Start a Hoist server in a new thread.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/utils.py#L103)

---
