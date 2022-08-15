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


### `InternalServerError`



**Exception occured on the server.**

---


### `InvalidOperationError`



**Operation was not found.**

---


### `InvalidVersionError`



**Version is not high enough.**

---


### `NotConnectedError`



**Socket is not connected to the server.**

---


### `SchemaValidationError`



**Schema validation failed.**

---

#### `format_current`
```py

def format_current()
```

*Format the current type.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/exceptions.py#L100)

---

#### `format_needed`
```py

def format_needed()
```

*Format the needed type.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/exceptions.py#L105)

---
#### `current`

```py
@property
def current() -> Optional[Type[Any]]
```

*Current type.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/exceptions.py#L95)

---
#### `needed`

```py
@property
def needed() -> Union[Type[Any], Tuple[Optional[Type[Any]], ...]]
```

*Type(s) needed to be valid.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/exceptions.py#L90)

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
)
```



---


#### `code`

```py
@property
def code() -> int
```

*Error code.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/exceptions.py#L39)

---
#### `error`

```py
@property
def error() -> str
```

*Error name.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/exceptions.py#L44)

---
#### `message`

```py
@property
def message() -> str
```

*Error message.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/exceptions.py#L49)

---
#### `payload`

```py
@property
def payload() -> Optional[Dict[str, Any]]
```

*Error payload.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/exceptions.py#L54)

---

## `hoist.client`

### `Connection`

*Derives from `hoist._messages.BaseMessagable`*

**Class handling a connection to a server.**

#### `__init__`
```py

def __init__(
    url: Union[str, ForwardRef('URL')],
    token: Optional[str],
    loop: Optional[asyncio.events.AbstractEventLoop],
    session: Optional[aiohttp.client.ClientSession],
    extra_listeners: Optional[Dict[Union[Tuple[str, ...], str, None], List[Tuple[Callable[[ForwardRef('Message'), ~_A], Awaitable[None]], Union[~_A, Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]]]]]]],
    minimum_version: Union[str, ForwardRef('Version'), None]
)
```



---


#### `close`
```py

def close()
```

*Close the connection.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L70)

---

#### `connect`
```py

def connect(
    token: Optional[str]
)
```

*Open the connection.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L113)

---

#### `message`
```py

def message(
    msg: str,
    data: Optional[Dict[str, Any]],
    replying: Optional[hoist.message.Message],
    listeners: Optional[Dict[Union[Tuple[str, ...], str, None], List[Tuple[Callable[[ForwardRef('Message'), ~_A], Awaitable[None]], Union[~_A, Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]]]]]]]
)
```

*Send a message to the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L185)

---
#### `closed`

```py
@property
def closed() -> bool
```

*Whether the client is closed.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L50)

---
#### `connected`

```py
@property
def connected() -> bool
```

*Whether the server is currently connected.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L65)

---
#### `token`

```py
@property
def token() -> Optional[str]
```

*Authentication token of the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L60)

---
#### `url`

```py
@property
def url() -> Union[str, yarl.URL]
```

*URL of the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L55)

---

## `hoist.message`

### `Message`

*Derives from `hoist.message.BaseMessage`*

**Object handling a message.**

#### `__init__`
```py

def __init__(
    conn: BaseMessagable,
    msg: str,
    id: int,
    data: Optional[Dict[str, Any]],
    replying: Optional[ForwardRef('Message')]
)
```



---


#### `receive`
```py

def receive()
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L105)

---

#### `reply`
```py

def reply(
    msg: str,
    data: Optional[Dict[str, Any]]
)
```

*Send a message to the target.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L82)

---

#### `to_dict`
```py

def to_dict(
    convert_replies: bool
)
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L90)

---
#### `id`

```py
@property
def id() -> int
```

*Message ID.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L77)

---
### `BaseMessage`

*Derives from `hoist._messages.MessageListener`*

**Base class for handling a message.**

#### `__init__`
```py

def __init__(
    conn: BaseMessagable,
    msg: str,
    data: Optional[Dict[str, Any]],
    replying: Optional[ForwardRef('Message')]
)
```



---


#### `to_dict`
```py

def to_dict(
    convert_replies: bool
) -> dict
```

*Convert the message to a dictionary.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L47)

---
#### `content`

```py
@property
def content() -> str
```

*Message content.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L32)

---
#### `data`

```py
@property
def data() -> Dict[str, Any]
```

*Raw message payload.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L37)

---
#### `replying`

```py
@property
def replying() -> Optional[hoist.message.Message]
```

*Message that the current message is replying to.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L42)

---
### `PendingMessage`

*Derives from `hoist.message.BaseMessage`*

**Object handling a message that has not yet been sent to the server.**

#### `__init__`
```py

def __init__(
    conn: BaseMessagable,
    msg: Optional[str],
    data: Optional[Dict[str, Any]],
    replying: Optional[ForwardRef('Message')]
)
```



---


#### `send`
```py

def send()
```

*Send the message.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L147)

---

#### `to_dict`
```py

def to_dict(
    convert_replies: bool
)
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L133)

---
#### `content`

```py
@property
def content() -> str
```

*None*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L125)

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
    default_token_choices: SupportsLenAndGetItem[str],
    hide_token: bool,
    login_func: Callable[[ForwardRef('Server'), str], Awaitable[bool]],
    log_level: Optional[int],
    minimum_version: Union[str, ForwardRef('Version'), None],
    extra_operations: Optional[Dict[str, Callable[[~_T], Awaitable[Any]]]],
    unsupported_operations: Optional[Sequence[str]],
    supported_operations: Optional[Sequence[str]],
    extra_listeners: Optional[Dict[Union[Tuple[str, ...], str, None], List[Tuple[Callable[[ForwardRef('Message'), ~_A], Awaitable[None]], Union[~_A, Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]]]]]]]
)
```



---


#### `broadcast`
```py

def broadcast(
    message: str,
    payload: Optional[Dict[str, Any]]
)
```

*Send a message to all connections.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L489)

---

#### `close`
```py

def close()
```

*Close the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L515)

---

#### `start`
```py

def start(
    host: str,
    port: int
)
```

*Start the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L451)

---

#### `stop`
```py

def stop()
```

*Alias to `Server.close`.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L540)

---
#### `running`

```py
@property
def running() -> bool
```

*Whether the server is running.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L535)

---
#### `supported_operations`

```py
@property
def supported_operations() -> Sequence[str]
```

*Operations supported by the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L160)

---
#### `token`

```py
@property
def token() -> str
```

*Authentication token used to connect.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L203)

---
#### `unsupported_operations`

```py
@property
def unsupported_operations() -> Sequence[str]
```

*Operations blacklisted by the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L165)

---
### `_SocketMessageTransport`

*Derives from `hoist._messages.BaseMessagable`*

**Connection class for wrapping message objects.**

#### `__init__`
```py

def __init__(
    ws: Socket,
    server: Server,
    event_message: str
)
```



---


#### `message`
```py

def message(
    id: Optional[int],
    msg: str,
    data: Optional[Dict[str, Any]],
    replying: Optional[hoist.message.Message],
    listeners: Optional[Dict[Union[Tuple[str, ...], str, None], List[Tuple[Callable[[ForwardRef('Message'), ~_A], Awaitable[None]], Union[~_A, Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]]]]]]]
) -> Message
```

*Send a message to the client.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L77)

---

#### `pend_message`
```py

def pend_message(
    msg: Optional[str],
    data: Optional[Dict[str, Any]],
    replying: Optional[hoist.message.Message]
) -> PendingMessage
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L110)

---

### `_base_login`

```py

def _base_login(
    server: Server,
    sent_token: str
) -> bool
```

*Default login function used by servers.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L59)

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
)
```



---


#### `close`
```py

def close()
```

*Close the socket.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_client_ws.py#L196)

---

#### `login`
```py

def login(
    listener: Callable[[ForwardRef('BaseMessagable'), str, Dict[str, Any], Optional[dict], int], Awaitable[None]]
)
```

*Send login message to the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_client_ws.py#L165)

---

#### `send`
```py

def send(
    payload: Dict[str, Any],
    id: Optional[int],
    reply: bool
)
```

*Send a message to the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_client_ws.py#L229)

---
#### `logged`

```py
@property
def logged() -> bool
```

*Whether the socket has authenticated with the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_client_ws.py#L191)

---
### `_Response`

*Derives from `builtins.tuple`*

**_Response(success, data, error, message, desc, code, id)**

#### `__init__`
```py

def __init__()
```

*Initialize self.  See help(type(self)) for accurate signature.*

---




## `hoist._logging`

### `hlog`

```py

def hlog(
    key: str,
    value: Any,
    level: int
)
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
)
```

*Log a rich message.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_logging.py#L44)

---

### `setup_logging`

```py

def setup_logging()
```

*Set up logging.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_logging.py#L24)

---


## `hoist._warnings`

### `warn`

```py

def warn(
    message: str,
    category: Optional[Type[Warning]]
)
```

*Display a warning.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_warnings.py#L71)

---

### `_showwarning`

```py

def _showwarning(
    message: Union[Warning, str],
    category: Type[Warning],
    filename: str,
    lineno: int,
    file: Optional[TextIO],
    line: Optional[str]
)
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_warnings.py#L20)

---

### `_warning_no_src_line`

```py

def _warning_no_src_line(
    message: Union[Warning, str],
    category: Type[Warning],
    filename: str,
    lineno: int,
    file: Optional[TextIO],
    _: Optional[str]
) -> str
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_warnings.py#L57)

---


## `hoist._messages`

### `BaseMessagable`



#### `__init__`
```py

def __init__()
```

*Initialize self.  See help(type(self)) for accurate signature.*

---


#### `message`
```py

def message(
    msg: str,
    data: Optional[Dict[str, Any]],
    replying: Optional[ForwardRef('Message')],
    listeners: Optional[Dict[Union[Tuple[str, ...], str, None], List[Tuple[Callable[[ForwardRef('Message'), ~_A], Awaitable[None]], Union[~_A, Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]]]]]]]
)
```

*Send a message.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L324)

---

#### `message_later`
```py

def message_later(
    msg: Optional[str],
    data: Optional[Dict[str, Any]],
    replying: Optional[ForwardRef('Message')]
)
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/contextlib.py#L312)

---

#### `pend_message`
```py

def pend_message(
    msg: Optional[str],
    data: Optional[Dict[str, Any]],
    replying: Optional[ForwardRef('Message')]
)
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L289)

---

### `MessageListener`



**Base class for handling message listening.**

#### `__init__`
```py

def __init__(
    extra_listeners: Optional[Dict[Union[Tuple[str, ...], str, None], List[Tuple[Callable[[ForwardRef('Message'), ~_A], Awaitable[None]], Union[~_A, Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]]]]]]]
)
```



---


#### `create_message`
```py

def create_message(
    conn: BaseMessagable,
    data: Dict[str, Any]
)
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L184)

---

#### `create_or_lookup`
```py

def create_or_lookup(
    conn: BaseMessagable,
    content: str,
    message_data: Dict[str, Any],
    id: int,
    replying: Union[ForwardRef('Message'), dict, None],
    listeners: Optional[Dict[Union[Tuple[str, ...], str, None], List[Tuple[Callable[[ForwardRef('Message'), ~_A], Awaitable[None]], Union[~_A, Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]]]]]]]
)
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L193)

---

#### `lookup`
```py

def lookup(
    id: int
)
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L267)

---

#### `new_message`
```py

def new_message(
    conn: BaseMessagable,
    content: str,
    message_data: Dict[str, Any],
    replying: Union[ForwardRef('Message'), dict, None],
    id: Optional[int],
    listeners: Optional[Dict[Union[Tuple[str, ...], str, None], List[Tuple[Callable[[ForwardRef('Message'), ~_A], Awaitable[None]], Union[~_A, Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]]]]]]]
)
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L223)

---

#### `receive`
```py

def receive(
    message: Union[str, Tuple[str, ...], None],
    parameter: Union[Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]], ~T, None]
)
```

*Add a listener for message receiving.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L153)

---
#### `current_id`

```py
@property
def current_id() -> int
```

*Current message ID.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L179)

---
#### `message_listeners`

```py
@property
def message_listeners() -> Dict[Union[Tuple[str, ...], str, None], List[Tuple[Callable[[hoist.message.Message, ~_A], Awaitable[None]], Union[~_A, Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]]]]]]
```

*Listener function for messages.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L108)

---
### `_process_listeners`

```py

def _process_listeners(
    listeners: Optional[List[Tuple[Callable[[ForwardRef('Message'), ~_A], Awaitable[None]], Union[~_A, Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]]]]]],
    message: Message,
    hide_warning: bool
)
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L49)

---


## `hoist._operations`

### `verify_schema`

```py

def verify_schema(
    schema: Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]],
    data: Dict[str, Any]
)
```

*Verify that a payload matches the schema.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_operations.py#L22)

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



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_operations.py#L15)

---

### `call_operation`

```py

def call_operation(
    op: Callable[[~T], Awaitable[Any]],
    payload: Dict[str, Any]
)
```

*Call an operation.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_operations.py#L47)

---

### `invalid_payload`

```py

def invalid_payload(
    exc: SchemaValidationError
)
```

*Raise an invalid payload error.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_operations.py#L56)

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
)
```

*Gracefully close the connection.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L152)

---

#### `connect`
```py

def connect()
```

*Establish the WebSocket connection.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L42)

---

#### `error`
```py

def error(
    code: int,
    id: Optional[int],
    description: Optional[str],
    payload: Optional[Dict[str, Any]]
)
```

*Send an error to the client.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L90)

---

#### `recv`
```py

def recv(
    schema: Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]]
)
```

*Receive a message from the client.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L129)

---

#### `recv_only`
```py

def recv_only(
    schema: Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]]
)
```

*Receive a single key from the client.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L148)

---

#### `success`
```py

def success(
    id: Optional[int],
    payload: Optional[Dict[str, Any]],
    message: Optional[str]
)
```

*Send a success to the client.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L114)

---
#### `address`

```py
@property
def address() -> Optional[starlette.datastructures.Address]
```

*Address object of the connection.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L160)

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
)
```

*Make a client string.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L27)

---

### `make_client_msg`

```py

def make_client_msg(
    addr: Optional[starlette.datastructures.Address],
    to: bool
)
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

def __init__()
```



---


#### `close_thread`
```py

def close_thread()
```

*Close the running thread.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_uvicorn.py#L46)

---

#### `run_in_thread`
```py

def run_in_thread(
    hide_token: bool,
    token: str
)
```

*Run the server in a thread.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_uvicorn.py#L23)

---


## `hoist.utils`

### `connect`

```py

def connect(
    token: str,
    url: Union[str, ForwardRef('URL')],
    kwargs: Any
)
```

*Connect to a Hoist server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/contextlib.py#L312)

---

### `connect_to`

```py

def connect_to(
    url: Union[str, ForwardRef('URL')],
    token: str,
    kwargs: Any
)
```

*Call a function with the connection.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/utils.py#L78)

---

### `debug`

```py

def debug(
    trace: Union[bool, str],
    enable_uvicorn: bool
)
```

*Enable debug logging.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/utils.py#L125)

---

### `main`

```py

def main(
    func: Callable[[], Coroutine[Any, Any, Any]]
)
```

*Run a main async function.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/utils.py#L28)

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
)
```

*Start a Hoist server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/utils.py#L111)

---
