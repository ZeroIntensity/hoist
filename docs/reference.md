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
def current() -> typing.Optional[typing.Type[typing.Any]]
```

*Current type.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/exceptions.py#L95)

---
#### `needed`

```py
@property
def needed() -> typing.Union[typing.Type[typing.Any], typing.Tuple[typing.Optional[typing.Type[typing.Any]], ...]]
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
    payload: typing.Optional[typing.Dict[str, typing.Any]]
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
def payload() -> typing.Optional[typing.Dict[str, typing.Any]]
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
    url: typing.Union[str, 'URL'],
    token: typing.Optional[str],
    loop: typing.Optional[asyncio.events.AbstractEventLoop],
    session: typing.Optional[aiohttp.client.ClientSession],
    extra_listeners: typing.Optional[typing.Dict[typing.Union[typing.Tuple[str, ...], str, None], typing.List[ForwardRef('ListenerData')]]],
    minimum_version: typing.Union[str, 'Version', None]
)
```



---


#### `close`
```py

def close()
```

*Close the connection.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L71)

---

#### `connect`
```py

def connect(
    token: typing.Optional[str]
)
```

*Open the connection.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L113)

---

#### `message`
```py

def message(
    msg: str,
    data: typing.Optional[typing.Dict[str, typing.Any]],
    replying: typing.Optional[hoist.message.Message],
    listeners: typing.Optional[typing.Dict[typing.Union[typing.Tuple[str, ...], str, None], typing.List[ForwardRef('ListenerData')]]]
)
```

*Send a message to the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L190)

---
#### `closed`

```py
@property
def closed() -> bool
```

*Whether the client is closed.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L51)

---
#### `connected`

```py
@property
def connected() -> bool
```

*Whether the server is currently connected.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L66)

---
#### `token`

```py
@property
def token() -> typing.Optional[str]
```

*Authentication token of the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L61)

---
#### `url`

```py
@property
def url() -> typing.Union[str, 'URL']
```

*URL of the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L56)

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
    data: typing.Optional[typing.Dict[str, typing.Any]],
    replying: typing.Optional['Message']
)
```



---


#### `receive`
```py

def receive()
```

*Rece*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L109)

---

#### `reply`
```py

def reply(
    msg: str,
    data: typing.Optional[typing.Dict[str, typing.Any]]
)
```

*Send a message to the target.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L85)

---

#### `to_dict`
```py

def to_dict(
    convert_replies: bool
)
```

*Convert the current instance to a dictionary.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L93)

---
#### `id`

```py
@property
def id() -> int
```

*Message ID.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L80)

---
### `BaseMessage`

*Derives from `hoist._messages.MessageListener`*

**Base class for handling a message.**

#### `__init__`
```py

def __init__(
    conn: BaseMessagable,
    msg: str,
    data: typing.Optional[typing.Dict[str, typing.Any]],
    replying: typing.Optional['Message']
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
def data() -> typing.Dict[str, typing.Any]
```

*Raw message payload.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L37)

---
#### `replying`

```py
@property
def replying() -> typing.Optional['Message']
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
    msg: typing.Optional[str],
    data: typing.Optional[typing.Dict[str, typing.Any]],
    replying: typing.Optional['Message']
)
```



---


#### `send`
```py

def send()
```

*Send the message.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L152)

---

#### `to_dict`
```py

def to_dict(
    convert_replies: bool
)
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L138)

---
#### `content`

```py
@property
def content() -> str
```

*None*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L130)

---

## `hoist.server`

### `Server`

*Derives from `hoist._messages.MessageListener`*

**Class for handling a server.**

#### `__init__`
```py

def __init__(
    token: typing.Optional[str],
    default_token_len: int,
    default_token_choices: SupportsLenAndGetItem[str],
    hide_token: bool,
    login_func: typing.Callable[['Server', str], typing.Awaitable[bool]],
    log_level: typing.Optional[int],
    minimum_version: typing.Union[str, 'Version', None],
    extra_operations: typing.Optional[typing.Dict[str, typing.Callable[[~_T], typing.Awaitable[typing.Any]]]],
    unsupported_operations: typing.Optional[typing.Sequence[str]],
    supported_operations: typing.Optional[typing.Sequence[str]],
    extra_listeners: typing.Optional[typing.Dict[typing.Union[typing.Tuple[str, ...], str, None], typing.List[ForwardRef('ListenerData')]]],
    fancy: typing.Optional[bool]
)
```



---


#### `broadcast`
```py

def broadcast(
    message: str,
    payload: typing.Optional[typing.Dict[str, typing.Any]]
)
```

*Send a message to all connections.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L612)

---

#### `close`
```py

def close()
```

*Close the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L639)

---

#### `start`
```py

def start(
    host: str,
    port: int,
    fancy: typing.Optional[bool]
)
```

*Start the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L555)

---

#### `stop`
```py

def stop()
```

*Alias to `Server.close`.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L659)

---
#### `fancy`

```py
@property
def fancy() -> bool
```

*Whether the server is running with fancy output.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L195)

---
#### `running`

```py
@property
def running() -> bool
```

*Whether the server is running.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L654)

---
#### `supported_operations`

```py
@property
def supported_operations() -> typing.Sequence[str]
```

*Operations supported by the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L200)

---
#### `token`

```py
@property
def token() -> str
```

*Authentication token used to connect.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L243)

---
#### `unsupported_operations`

```py
@property
def unsupported_operations() -> typing.Sequence[str]
```

*Operations blacklisted by the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L205)

---
### `_SocketMessageTransport`

*Derives from `hoist._messages.BaseMessagable`*

**Connection class for wrapping message objects.**

#### `__init__`
```py

def __init__(
    ws: Socket,
    server: Server,
    id: typing.Optional[int],
    event_message: str
)
```



---


#### `message`
```py

def message(
    msg: str,
    data: typing.Optional[typing.Dict[str, typing.Any]],
    replying: typing.Optional[hoist.message.Message],
    listeners: typing.Optional[typing.Dict[typing.Union[typing.Tuple[str, ...], str, None], typing.List[ForwardRef('ListenerData')]]]
) -> Message
```

*Send a message to the client.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L100)

---

#### `pend_message`
```py

def pend_message(
    msg: typing.Optional[str],
    data: typing.Optional[typing.Dict[str, typing.Any]],
    replying: typing.Optional[hoist.message.Message]
) -> PendingMessage
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L132)

---

### `_base_login`

```py

def _base_login(
    server: Server,
    sent_token: str
) -> bool
```

*Default login function used by servers.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L80)

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_client_ws.py#L239)

---

#### `login`
```py

def login(
    listener: typing.Callable[['BaseMessagable', str, typing.Dict[str, typing.Any], typing.Optional[dict], int], typing.Awaitable[None]]
)
```

*Send login message to the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_client_ws.py#L208)

---

#### `process_messages`
```py

def process_messages()
```

*Run message listeners with received messages.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_client_ws.py#L192)

---

#### `send`
```py

def send(
    payload: typing.Dict[str, typing.Any],
    id: typing.Optional[int],
    reply: bool
)
```

*Send a message to the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_client_ws.py#L272)

---
#### `logged`

```py
@property
def logged() -> bool
```

*Whether the socket has authenticated with the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_client_ws.py#L234)

---
#### `messages`

```py
@property
def messages() -> Queue
```

*Queue containing unprocessed messages.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_client_ws.py#L74)

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



### `_drain`

```py

def _drain(
    queue: asyncio.Queue[T]
) -> typing.Iterator[~T]
```

*Drain the target queue.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_client_ws.py#L42)

---


## `hoist._logging`

### `hlog`

```py

def hlog(
    key: str,
    value: typing.Any,
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
    value: typing.Any,
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
    category: typing.Optional[typing.Type[Warning]]
)
```

*Display a warning.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_warnings.py#L74)

---

### `_showwarning`

```py

def _showwarning(
    message: typing.Union[Warning, str],
    category: typing.Type[Warning],
    filename: str,
    lineno: int,
    file: typing.Optional[typing.TextIO],
    line: typing.Optional[str]
)
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_warnings.py#L13)

---

### `_warning_no_src_line`

```py

def _warning_no_src_line(
    message: typing.Union[Warning, str],
    category: typing.Type[Warning],
    filename: str,
    lineno: int,
    file: typing.Optional[typing.TextIO],
    line: typing.Optional[str]
) -> str
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_warnings.py#L57)

---


## `hoist._messages`

### `BaseMessagable`

*Derives from `abc.ABC`*

**Abstract class representing a messagable target.**

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
    data: typing.Optional[typing.Dict[str, typing.Any]],
    replying: typing.Optional['Message'],
    listeners: typing.Optional[typing.Dict[typing.Union[typing.Tuple[str, ...], str, None], typing.List[ForwardRef('ListenerData')]]]
)
```

*Send a message.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L380)

---

#### `message_later`
```py

def message_later(
    msg: typing.Optional[str],
    data: typing.Optional[typing.Dict[str, typing.Any]],
    replying: typing.Optional['Message']
)
```

*Send a message after the context has finished.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/contextlib.py#L312)

---

#### `pend_message`
```py

def pend_message(
    msg: typing.Optional[str],
    data: typing.Optional[typing.Dict[str, typing.Any]],
    replying: typing.Optional['Message']
)
```

*Get a message to be sent later.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L343)

---

### `ListenerData`

*Derives from `builtins.tuple`*

**ListenerData(listener, param, param_type)**

#### `__init__`
```py

def __init__()
```

*Initialize self.  See help(type(self)) for accurate signature.*

---



### `ListenerParam`

*Derives from `enum.Enum`*

**Type of parameter(s) that the listener should take.**

#### `__init__`
```py

def __init__()
```

*Initialize self.  See help(type(self)) for accurate signature.*

---



### `MessageListener`



**Base class for handling message listening.**

#### `__init__`
```py

def __init__(
    extra_listeners: typing.Optional[typing.Dict[typing.Union[typing.Tuple[str, ...], str, None], typing.List[ForwardRef('ListenerData')]]]
)
```



---


#### `create_message`
```py

def create_message(
    conn: BaseMessagable,
    data: typing.Dict[str, typing.Any]
)
```

*Build a message from a payload.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L214)

---

#### `create_or_lookup`
```py

def create_or_lookup(
    conn: BaseMessagable,
    content: str,
    message_data: typing.Dict[str, typing.Any],
    id: int,
    replying: typing.Union['Message', dict, None],
    listeners: typing.Optional[typing.Dict[typing.Union[typing.Tuple[str, ...], str, None], typing.List[ForwardRef('ListenerData')]]]
)
```

*Create a new message wtih the specified ID, or look it up if it already exists.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L224)

---

#### `lookup`
```py

def lookup(
    id: int
)
```

*Lookup a message by its ID.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L310)

---

#### `new_message`
```py

def new_message(
    conn: BaseMessagable,
    content: str,
    message_data: typing.Dict[str, typing.Any],
    replying: typing.Union['Message', dict, None],
    id: typing.Optional[int],
    listeners: typing.Optional[typing.Dict[typing.Union[typing.Tuple[str, ...], str, None], typing.List[ForwardRef('ListenerData')]]]
)
```

*Create a new message.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L265)

---

#### `receive`
```py

def receive(
    message: typing.Union[str, typing.Tuple[str, ...], None],
    parameter: typing.Union[typing.Dict[str, typing.Union[typing.Type[typing.Any], typing.Tuple[typing.Optional[typing.Type[typing.Any]], ...]]], ~T, None]
)
```

*Add a listener for message receiving.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L173)

---
#### `current_id`

```py
@property
def current_id() -> int
```

*Current message ID.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L209)

---
#### `message_listeners`

```py
@property
def message_listeners() -> typing.Dict[typing.Union[typing.Tuple[str, ...], str, None], typing.List[ForwardRef('ListenerData')]]
```

*Listener function for messages.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L129)

---
### `_process_listeners`

```py

def _process_listeners(
    listeners: typing.Optional[typing.List[hoist._messages.ListenerData]],
    message: Message,
    hide_warning: bool
)
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L60)

---


## `hoist._schema`

### `verify_schema`

```py

def verify_schema(
    schema: typing.Dict[str, typing.Union[typing.Type[typing.Any], typing.Tuple[typing.Optional[typing.Type[typing.Any]], ...]]],
    data: typing.Dict[str, typing.Any]
)
```

*Verify that a payload matches the schema.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_schema.py#L12)

---

### `invalid_payload`

```py

def invalid_payload(
    exc: SchemaValidationError
)
```

*Raise an invalid payload error.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_schema.py#L37)

---


## `hoist._operations`

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



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_operations.py#L14)

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L191)

---

#### `connect`
```py

def connect()
```

*Establish the WebSocket connection.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L81)

---

#### `error`
```py

def error(
    code: int,
    id: typing.Optional[int],
    description: typing.Optional[str],
    payload: typing.Optional[typing.Dict[str, typing.Any]]
)
```

*Send an error to the client.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L129)

---

#### `make_address`
```py

def make_address()
```

*Get the current address as rich text.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L62)

---

#### `recv`
```py

def recv(
    schema: typing.Dict[str, typing.Union[typing.Type[typing.Any], typing.Tuple[typing.Optional[typing.Type[typing.Any]], ...]]]
)
```

*Receive a message from the client.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L168)

---

#### `recv_only`
```py

def recv_only(
    schema: typing.Dict[str, typing.Union[typing.Type[typing.Any], typing.Tuple[typing.Optional[typing.Type[typing.Any]], ...]]]
)
```

*Receive a single key from the client.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L187)

---

#### `success`
```py

def success(
    id: typing.Optional[int],
    payload: typing.Optional[typing.Dict[str, typing.Any]],
    message: typing.Optional[str]
)
```

*Send a success to the client.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L153)

---
#### `address`

```py
@property
def address() -> typing.Optional[starlette.datastructures.Address]
```

*Address object of the connection.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L199)

---
#### `logged`

```py
@property
def logged() -> bool
```

*The authentication status of the current connection.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L96)

---
#### `rich_status`

```py
@property
def rich_status() -> str
```

*Rich connection status.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L76)

---
#### `status`

```py
@property
def status() -> Status
```

*Current connection status.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L67)

---
#### `ws`

```py
@property
def ws() -> WebSocket
```

*Raw WebSocket object.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L91)

---
### `Status`

*Derives from `enum.Enum`*

**Current connection status.**

#### `__init__`
```py

def __init__()
```

*Initialize self.  See help(type(self)) for accurate signature.*

---



### `make_client`

```py

def make_client(
    addr: typing.Optional[starlette.datastructures.Address]
)
```

*Make a client string.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L29)

---

### `make_client_msg`

```py

def make_client_msg(
    addr: typing.Optional[starlette.datastructures.Address],
    to: bool
)
```

*Create a client message.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L23)

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_uvicorn.py#L50)

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
    url: typing.Union[str, 'URL'],
    kwargs: typing.Any
)
```

*Connect to a Hoist server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/contextlib.py#L312)

---

### `connect_to`

```py

def connect_to(
    url: typing.Union[str, 'URL'],
    token: str,
    kwargs: typing.Any
)
```

*Call a function with the connection.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/utils.py#L76)

---

### `debug`

```py

def debug(
    trace: typing.Union[bool, str],
    enable_uvicorn: bool
)
```

*Enable debug logging.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/utils.py#L124)

---

### `main`

```py

def main(
    func: typing.Callable[[], typing.Coroutine[typing.Any, typing.Any, typing.Any]]
)
```

*Run a main async function.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/utils.py#L26)

---

### `serve`

```py

def serve(
    token: typing.Optional[str],
    server: typing.Optional[hoist.server.Server],
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
    token: typing.Optional[str],
    server: typing.Optional[hoist.server.Server],
    host: str,
    port: int,
    fancy: bool
)
```

*Start a Hoist server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/utils.py#L109)

---
