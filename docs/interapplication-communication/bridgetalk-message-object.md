# BridgeTalk message object

The message object defines the basic communication packet that is sent between applications. Its
properties allow you to specify the receiving application (the target), the data to send to the target (the
body), and the type of data that is sent. The messaging protocol is extensible; it allows you to define new
types of data for the type property, and to send and receive arbitrary additional information with the
headers property.

---

## BridgeTalk message object constructor

Create a new message object using a simple constructor:

```default
var bt = new BridgeTalk;
```

Before you send a message to another application, you must set the target property to the receiving
application, and the body property to the data message (typically a script) you want to send.

---

## BridgeTalk message object properties

### body

Type: `String`

The data payload of the message.

- If this is an unsolicited message to another application, typically contains a
  script packaged as a string. The target application’s full document object
  model (DOM) is available within the script.
- If this message is a result returned from the static BridgeTalk onReceive
  method of a target application, directed to an onResult callback in this object,
  contains the return result from that method flattened into a string. See
  [Passing values between applications](communicating-through-messages.md#passing-values-between-applications).
- If this message contains an error notification for the onError callback, contains
  the error message.

Read/write.

---

### headers

Type: `Object`

A JavaScript object containing script-defined headers.

Use this property to define custom header data to send supplementary
information between applications. You can add any number of new headers. The
headers are name/value pairs, and can be accessed with the JavaScript dot
notation (`msgObj.headers.propName`), or bracket notation
(`msgObj.headers[propName]`). If the header name conforms to JavaScript symbol
syntax, use the dot notation. If not, use the bracket notation.

The predefined header `["Error-Code"]` is used to return error messages to a
sender; see [Messaging error codes](messaging-error-codes.md#messaging-error-codes).

Examples of setting headers:

```default
bt.headers.info = "Additional Information";
bt.headers ["Error-Code"] = 8;
```

Examples of getting header values:

```default
var info = bt.headers.info;
var error = bt.headers ["Error-Code"];
```

Read/write.

---

### sender

Type: `String`

The application specifier for the sending application (see [Application specifiers](application-and-namespace-specifiers.md#application-specifiers)).

Read/write.

---

### target

Type: `String`

The application specifier for the target, or receiving, application (see [Application specifiers](application-and-namespace-specifiers.md#application-specifiers)).

Read/write.

---

### timeout

Type: `Number`

The number of seconds before the message times out.

If a message has not been removed from the input queue for processing before
this time elapses, the message is discarded. If the sender has defined an
[onTimeout()](#bridgetalk-message-object-ontimeout) callback for the message, the target application sends a time-out
message back to the sender.

Read/write.

---

### type

Type: `String`

The message type, which indicates what type of data the body contains.
Default is `ExtendScript`.

You can define a type for script-defined data. If you do so, the target application
must have a static `BridgeTalk` `onReceive_` method that checks for and processes
that type.

Read/write.

---

## BridgeTalk message object callbacks

!!! note
    The message callbacks are optional, and are not implemented by all message-enabled applications.

### onError()

`bridgeTalkObj.onError ()`

A callback function that the target application invokes to return an error
response to the sender. It can send JavaScript run-time errors or exceptions,
or C++ exceptions.

To define error-response behavior, set this to a function definition in the
following form:

```default
bridgeTalkObj.onError = function( errorMsgObject ) {
  // error handler defined here
};
```

The body property of the received message object contains the error
message, and the headers property contains the error code in its
`Error-Code` property. See [Messaging error codes](messaging-error-codes.md#messaging-error-codes).

The function returns `undefined`.

---

### onReceived()

`bridgeTalkObj.onReceived ()`

A callback function that the target application invokes to confirm that the
message was received. (Note that this is different from the static `onReceive_`
method of the `BridgeTalk` class that handles unsolicited messages.)

To define a response to receipt notification, set this to a function definition
in the following form:

```default
bridgeTalkObj.onReceived = function( origMsgObject ) {
  // handler defined here
};
```

The target passes back the original message object, with the body property
set to the empty string.

The function returns `undefined`.

---

### onResult()

`bridgeTalkObj.onResult ()`

A callback function that the target application invokes to return a response
to the sender. This can be an intermediate response or the final result of
processing the message.

To handle the response, set this to a function definition in the following form:

```default
bridgeTalkObj.onResult = function( responseMsgObject ) {
  // handler defined here
};
```

The target passes a new message object, with the body property set to the result string.
This is the result of the target application’s static BridgeTalk [onReceive](bridgetalk-class.md#bridgetalk-onreceive) method,
packaged as a UTF-8-encoded string. See [Passing values between applications](communicating-through-messages.md#passing-values-between-applications).

---

### onTimeout()

`bridgeTalkObj.onTimeout ()`

A callback function that the target application invokes with a time-out
message if time-out occurred before the target finished processing another
message previously sent by this application.

To enable this callback, the message must specify a value for the timeout property.

To define a response to the timeout event, set this to a function definition in
the following form:

```default
bridgeTalkObj.onTimeout = function( timeoutMsgObject ) {
  // handler defined here
};
```

---

## BridgeTalk message object functions

### send()

`bridgeTalkObj.send ([timoutInSecs[, launchParameters]])`

| `timoutInSecs`     | Optional. A maximum number of seconds to wait for a result before returning<br/>from this function. The message is sent synchronously, and the function does<br/>not return until the target has processed the message or this number of<br/>seconds have passed.<br/><br/>If not supplied or 0, the message is sent asynchronously, and the function<br/>returns immediately without waiting for a result.   |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `launchParameters` | Optional. A string of parameters to append to the name of the target<br/>application when launching it, if the application is not already running.<br/><br/>If the target application is already running, this value is ignored.                                                                                                                                                                              |

Sends this message to the target application.

If the target application is not running and the message contains a body, the messaging system
automatically launches the target application, passing in any supplied launch parameters. In this
case, the message is queued rather than sent immediately, and this method returns false. The
message is processed once the application is running.

Sending the message does not guarantee that the target actually receives it. You can request
notification of receipt by defining an onReceived callback for this message object. (Note that this is
different from the static onReceive method of the BridgeTalk class that handles unsolicited
messages.)

Returns `true` if the message could be sent immediately, `false` if it could not be sent or was queued
for sending later.

---

### sendResult()

`bridgeTalkObj.sendResult (result)`

| `result`   | You can send data of any type as the result value. The messaging framework<br/>creates a BridgeTalk message object, and flattens this value into a string<br/>which it stores in the body of that message. See [Passing values between applications](communicating-through-messages.md#passing-values-between-applications).   |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

When processing an unsolicited message, the static BridgeTalk onReceive method can return an
intermediate result to the sender by calling this method in the received message object. It invokes
the onResult callback of the original message, passing a new message object containing the
specified result value.

This allows you to send multiple responses to messages.

Returns `true` if the received message has an onResult callback defined and the response message
can be sent, `false` otherwise.
