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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/exceptions.py#L112)

---

#### `format_needed`
```py

def format_needed()
```

*Format the needed type.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/exceptions.py#L117)

---
#### `current`

```py
@property
def current() -> typing.Optional[typing.Type[typing.Any]]
```

*Current type.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/exceptions.py#L107)

---
#### `needed`

```py
@property
def needed() -> typing.Union[typing.Type[typing.Any], typing.Tuple[typing.Optional[typing.Type[typing.Any]], ...]]
```

*Type(s) needed to be valid.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/exceptions.py#L102)

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/exceptions.py#L46)

---
#### `error`

```py
@property
def error() -> str
```

*Error name.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/exceptions.py#L51)

---
#### `message`

```py
@property
def message() -> str
```

*Error message.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/exceptions.py#L56)

---
#### `payload`

```py
@property
def payload() -> typing.Optional[typing.Dict[str, typing.Any]]
```

*Error payload.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/exceptions.py#L61)

---

## `hoist.client`

### `Connection`

*Derives from `hoist._messages.MessageListener`*

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L108)

---

#### `close_sync`
```py

def close_sync()
```

*Close the client synchronously.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L93)

---

#### `connect`
```py

def connect(
    token: typing.Optional[str]
)
```

*Open the connection.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L151)

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L229)

---

#### `operation`
```py

def operation(
    name: str,
    payload: typing.Optional[typing.Dict[str, typing.Any]],
    payload_json: typing.Any
)
```

*Execute an operation on the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L268)

---
#### `closed`

```py
@property
def closed() -> bool
```

*Whether the client is closed.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L73)

---
#### `connected`

```py
@property
def connected() -> bool
```

*Whether the server is currently connected.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L88)

---
#### `opened`

```py
@property
def opened() -> bool
```

*Whether the connection was ever opened.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L68)

---
#### `token`

```py
@property
def token() -> typing.Optional[str]
```

*Authentication token of the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L83)

---
#### `url`

```py
@property
def url() -> typing.Union[str, 'URL']
```

*URL of the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/client.py#L78)

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L118)

---

#### `reply`
```py

def reply(
    msg: str,
    data: typing.Optional[typing.Dict[str, typing.Any]]
)
```

*Send a message to the target.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L94)

---

#### `to_dict`
```py

def to_dict(
    convert_replies: bool
)
```

*Convert the current instance to a dictionary.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L102)

---
#### `id`

```py
@property
def id() -> int
```

*Message ID.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L89)

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L54)

---
#### `content`

```py
@property
def content() -> str
```

*Message content.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L39)

---
#### `data`

```py
@property
def data() -> typing.Dict[str, typing.Any]
```

*Raw message payload.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L44)

---
#### `replying`

```py
@property
def replying() -> typing.Optional['Message']
```

*Message that the current message is replying to.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L49)

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L161)

---

#### `to_dict`
```py

def to_dict(
    convert_replies: bool
)
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L147)

---
#### `content`

```py
@property
def content() -> str
```

*None*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/message.py#L139)

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
    extra_operations: Optional,
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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L679)

---

#### `close`
```py

def close()
```

*Close the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L713)

---

#### `operation`
```py

def operation(
    name: str
)
```

*Add a function for an operation.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L737)

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L622)

---

#### `stop`
```py

def stop()
```

*Alias to `Server.close`.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L733)

---
#### `fancy`

```py
@property
def fancy() -> bool
```

*Whether the server is running with fancy output.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L262)

---
#### `running`

```py
@property
def running() -> bool
```

*Whether the server is running.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L728)

---
#### `supported_operations`

```py
@property
def supported_operations() -> typing.Sequence[str]
```

*Operations supported by the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L267)

---
#### `token`

```py
@property
def token() -> str
```

*Authentication token used to connect.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L310)

---
#### `unsupported_operations`

```py
@property
def unsupported_operations() -> typing.Sequence[str]
```

*Operations blacklisted by the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L272)

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L103)

---

#### `pend_message`
```py

def pend_message(
    msg: typing.Optional[str],
    data: typing.Optional[typing.Dict[str, typing.Any]],
    replying: typing.Optional[hoist.message.Message]
) -> PendingMessage
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L135)

---

### `_base_login`

```py

def _base_login(
    server: Server,
    sent_token: str
) -> bool
```

*Default login function used by servers.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/server.py#L83)

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_client_ws.py#L258)

---

#### `login`
```py

def login(
    listener: typing.Callable[['BaseMessagable', str, typing.Dict[str, typing.Any], typing.Optional[dict], int], typing.Awaitable[None]]
)
```

*Send login message to the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_client_ws.py#L227)

---

#### `process_messages`
```py

def process_messages()
```

*Run message listeners with received messages.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_client_ws.py#L211)

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_client_ws.py#L291)

---
#### `logged`

```py
@property
def logged() -> bool
```

*Whether the socket has authenticated with the server.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_client_ws.py#L253)

---
#### `messages`

```py
@property
def messages() -> Queue
```

*Queue containing unprocessed messages.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_client_ws.py#L93)

---
### `_Response`



**_Response(success: bool, data: Optional[Dict[str, Any]], error: Optional[str], message: Optional[str], desc: Optional[str], code: int, id: Optional[int])**

#### `__init__`
```py

def __init__(
    success: bool,
    data: typing.Optional[typing.Dict[str, typing.Any]],
    error: typing.Optional[str],
    message: typing.Optional[str],
    desc: typing.Optional[str],
    code: int,
    id: typing.Optional[int]
)
```



---



### `_drain`

```py

def _drain(
    queue: asyncio.Queue[T]
) -> typing.Iterator[~T]
```

*Drain the target queue.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_client_ws.py#L50)

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_warnings.py#L75)

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



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_warnings.py#L58)

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L388)

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L351)

---

### `ListenerData`



**ListenerData(listener: Union[Callable[[ForwardRef('Message'), Any], Awaitable[NoneType]], Callable[[ForwardRef('Message')], Awaitable[NoneType]], Callable[[], Awaitable[NoneType]]], param: Union[src.hoist._DataclassLike, Dict[str, Union[Type[Any], Tuple[Optional[Type[Any]], ...]]], NoneType], param_type: src.hoist._messages.ListenerParam)**

#### `__init__`
```py

def __init__(
    listener: typing.Union[typing.Callable[[ForwardRef('Message'), typing.Any], typing.Awaitable[None]], typing.Callable[[ForwardRef('Message')], typing.Awaitable[None]], typing.Callable[[], typing.Awaitable[None]]],
    param: Union,
    param_type: ListenerParam
)
```



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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L222)

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L232)

---

#### `lookup`
```py

def lookup(
    id: int
)
```

*Lookup a message by its ID.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L318)

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L273)

---

#### `receive`
```py

def receive(
    message: typing.Union[str, typing.Tuple[str, ...], None],
    parameter: typing.Union[typing.Dict[str, typing.Union[typing.Type[typing.Any], typing.Tuple[typing.Optional[typing.Type[typing.Any]], ...]]], ~T, None]
)
```

*Add a listener for message receiving.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L181)

---
#### `current_id`

```py
@property
def current_id() -> int
```

*Current message ID.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L217)

---
#### `message_listeners`

```py
@property
def message_listeners() -> typing.Dict[typing.Union[typing.Tuple[str, ...], str, None], typing.List[ForwardRef('ListenerData')]]
```

*Listener function for messages.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L137)

---
### `_process_listeners`

```py

def _process_listeners(
    listeners: typing.Optional[typing.List[hoist._messages.ListenerData]],
    message: Message,
    hide_warning: bool
)
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_messages.py#L61)

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_schema.py#L14)

---

### `invalid_payload`

```py

def invalid_payload(
    exc: SchemaValidationError
)
```

*Raise an invalid payload error.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_schema.py#L42)

---


## `hoist._operations`

### `OperatorParam`

*Derives from `enum.Enum`*

**Operator parameter type.**

#### `__init__`
```py

def __init__()
```

*Initialize self.  See help(type(self)) for accurate signature.*

---



### `_print`

```py

def _print(
    text: str
)
```



[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_operations.py#L22)

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L197)

---

#### `connect`
```py

def connect()
```

*Establish the WebSocket connection.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L87)

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L135)

---

#### `make_address`
```py

def make_address()
```

*Get the current address as rich text.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L68)

---

#### `recv`
```py

def recv(
    schema: typing.Dict[str, typing.Union[typing.Type[typing.Any], typing.Tuple[typing.Optional[typing.Type[typing.Any]], ...]]]
)
```

*Receive a message from the client.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L174)

---

#### `recv_only`
```py

def recv_only(
    schema: typing.Dict[str, typing.Union[typing.Type[typing.Any], typing.Tuple[typing.Optional[typing.Type[typing.Any]], ...]]]
)
```

*Receive a single key from the client.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L193)

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L159)

---
#### `address`

```py
@property
def address() -> typing.Optional[starlette.datastructures.Address]
```

*Address object of the connection.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L205)

---
#### `logged`

```py
@property
def logged() -> bool
```

*The authentication status of the current connection.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L102)

---
#### `rich_status`

```py
@property
def rich_status() -> str
```

*Rich connection status.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L82)

---
#### `status`

```py
@property
def status() -> Status
```

*Current connection status.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L73)

---
#### `ws`

```py
@property
def ws() -> WebSocket
```

*Raw WebSocket object.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_socket.py#L97)

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_uvicorn.py#L52)

---

#### `run_in_thread`
```py

def run_in_thread(
    hide_token: bool,
    token: str
)
```

*Run the server in a thread.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/_uvicorn.py#L25)

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

### `connect_no_ctx`

```py

def connect_no_ctx(
    token: str,
    url: typing.Union[str, 'URL'],
    kwargs: typing.Any
)
```

*Connect to a Hoist server without a context manager.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/utils.py#L58)

---

### `connect_with`

```py

def connect_with(
    token: str,
    url: typing.Union[str, 'URL'],
    kwargs: typing.Any
)
```

*Call a function with the connection.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/utils.py#L88)

---

### `debug`

```py

def debug(
    trace: typing.Union[bool, str],
    enable_uvicorn: bool
)
```

*Enable debug logging.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/utils.py#L136)

---

### `main`

```py

def main(
    func: typing.Callable[[], typing.Coroutine[typing.Any, typing.Any, typing.Any]]
)
```

*Run a main async function.*

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/utils.py#L27)

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

[Source](https://github.com/ZeroIntensity/hoist/blob/master/src/hoist/utils.py#L121)

---
