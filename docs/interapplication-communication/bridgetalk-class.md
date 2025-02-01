# BridgeTalk class

Static properties and methods of this class provide a way for your script to determine basic messaging
system information before you create any specific message objects. Static methods allow you to check if
an application is installed and is already running, and to launch the application. A callback defined on the
class determines how the application processes incoming messages.

You can access static properties and methods in the BridgeTalk class, which is available in the global
namespace. For example:

```default
var thisApp = BridgeTalk.appName;
```

!!! note
    You must instantiate the BridgeTalk class to create the BridgeTalk message object, which is used
to send message packets between applications. Dynamic properties and methods can be accessed only in
instances.

---

## BridgeTalk class properties

The BridgeTalk class provides these static properties, which are available in the global namespace:

### appInstance

Type: `String`

The instance identifier of an application launched by the messaging
framework, the instance portion of an application specifier; see
[Application specifiers](application-and-namespace-specifiers.md#application-specifiers).

Used only for those applications, such as InDesign, that support launching
and running multiple instances.

Read only.

---

### appLocale

Type: `String`

The locale of this application, the locale portion of an application
specifier; see [Application specifiers](application-and-namespace-specifiers.md#application-specifiers). When a message is
sent, this is the locale of the sending application.

Read only.

---

### appName

Type: `String`

The name of this application, the appname portion of an application
specifier; see [Application specifiers](application-and-namespace-specifiers.md#application-specifiers). When a message is
sent, this is the name of the sending application.

Read only.

---

### appSpecifier

Type: `String`

A lower-case string containing the complete specifier for this application;
see [Application specifiers](application-and-namespace-specifiers.md#application-specifiers).

Read/write.

---

### appStatus

Type: `String`

The current processing status of this application. One of:

- `busy`: The application is currently busy, but not processing messages. This is the case, for example, when a modal dialog is shown.
- `idle`: The application is currently idle, but processes messages regularly.
- `not installed`: The application is not installed.

Read only.

---

### appVersion

Type: `String`

The version number of this application, the version portion of an
application specifier; see [Application specifiers](application-and-namespace-specifiers.md#application-specifiers). When a
message is sent, this is the version of the sending application.

Read only.

---

### onReceive

Type: `Function`

A callback function that this application applies to unsolicited incoming
messages. The default function evaluates the body of the received
message and returns the result of evaluation. To change the default
behavior, set this to a function definition in the following form:

```default
BridgeTalk.onReceive = function( bridgeTalkObject ) {
// act on received message
};
```

The body property of the received message object contains the received
data. The function can return any type. See [Handling unsolicited messages](communicating-through-messages.md#handling-unsolicited-messages).

!!! note
    This function is not applied to a message that is received in response
to a message sent from this application. Response messages are processed
by the onResult, onReceived, or onError callbacks associated with the
sent message.

---

## BridgeTalk class functions

The BridgeTalk class provides these static methods, which are available in the global namespace:

### bringToFront()

`BridgeTalk.bringToFront (app)`

| `app`   | A specifier for the target application; see [Application specifiers](application-and-namespace-specifiers.md#application-specifiers).   |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------|

Brings all windows of the specified application to the front of the screen.
In Mac OS, an application can be running but have no windows open. In this case, calling this
function might or might not open a new window, depending on the application. For Adobe Bridge,
it opens a new browser window.

---

### getAppPath()

`BridgeTalk.getAppPath (app)`

| `app`   | A specifier for the target application; see [Application specifiers](application-and-namespace-specifiers.md#application-specifiers).   |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------|

Retrieves the full path of the executable file for a specified application.

Returns a string.

---

### getDisplayName()

`BridgeTalk.getDisplayName (app)`

| `app`   | A specifier for the target application; see [Application specifiers](application-and-namespace-specifiers.md#application-specifiers).   |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------|

Returns a localized display name for an application, or NULL if the application is not installed.
For example:

```default
BridgeTalk.getDisplayName("photoshop-10.0");
=> Adobe Photoshop CS4
```

---

### getSpecifier()

`BridgeTalk.getSpecifier (appName,[version],[locale])`

| `appName`   | The base name of the application to search for.                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `version`   | Optional. The specific version number to search for. If 0 or not supplied, returns the<br/>most recent version. If negative, returns the highest version up to and including the<br/>absolute value.<br/><br/>If a major version is specified, returns the highest minor-version variation. For<br/>example, if Photoshop CS versions 9, 9.1, and 10 are installed:<br/><br/>```default<br/>BridgeTalk.Specifier( "photoshop", "9" )<br/> => ["photoshop-9.1"]<br/>``` |
| `locale`    | Optional. The specific locale to search for.<br/>If not supplied and multiple language versions are installed, prefers the version for<br/>the current locale.                                                                                                                                                                                                                                                                                                         |

Retrieves a complete application specifier.
Returns a complete specifier (see [Application specifiers](application-and-namespace-specifiers.md#application-specifiers)) for a messaging-enabled
application version installed on this computer, or null if the requested version of the application is
not installed.

For example, assuming installed applications include Photoshop CS4 11.0 `en_us`, Photoshop CS2
8.5 `de_de`, Photoshop CS2 9.0 `de_de`, and Photoshop CS2 9.5 `de_de`, and that the current locale is
`en_US`

```default
BridgeTalk.getSpecifier ("photoshop");
 => ["photoshop-11.0-en_us"]

BridgeTalk.getSpecifier ("photoshop", 0, "en_us");
  => ["photoshop-11.0-en_us"]

BridgeTalk.getSpecifier ("photoshop", 0, "de_de");
  => ["photoshop-9.5-de_de"]

BridgeTalk.getSpecifier ("photoshop", -9.2, "de_de");
  => ["photoshop-9.0-de_de"]

BridgeTalk.getSpecifier ("photoshop", 8);
 => ["photoshop-8.5-de_de"]
```

---

### getStatus()

`BridgeTalk.getStatus (targetSpec)`

| `targetSpec`   | Optional, a specifier for the target application; see [Application specifiers](application-and-namespace-specifiers.md#application-specifiers).<br/>If not supplied, returns the processing status of the current application.   |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Retrieves the processing status of an application. Returns a string, one of:

> - `BUSY`: The application is currently busy, but not processing messages.
>   This is the case, for example, when a modal dialog is shown.
> - `IDLE`: The application is currently idle, but processes messages regularly.
> - `PUMPING`: The application is currently processing messages.
> - `ISNOTRUNNING`: The application is installed but not running.
> - `ISNOTINSTALLED`: The application is not installed.
> - `UNDEFINED`: The application is running but not responding to ping requests. This can be true of
>   a CS2 application that uses an earlier version of the messaging framework.

---

### getTargets()

`BridgeTalk.getTargets ([version],[locale])`

| `version`   | Optional. The specific version number to search for, or `null` to return the most<br/>appropriate version (matching, most recent, or running), with version information.<br/>Specify only a major version number to return the highest minor-version<br/>variation.<br/><br/>For example, if Photoshop CS versions 9, 9.5, and 10 are installed:<br/><br/>```default<br/>BridgeTalk.getTargets( "9" )<br/>  => [photoshop-9.5]<br/>```<br/><br/>Specify a negative value to return all versions up to the absolute value of the<br/>version number. For example:<br/><br/>```default<br/>BridgeTalk.getTargets( "-9.9" )<br/>  => [photoshop-9.0, photoshop-9.5]<br/>```   |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `locale`    | Optional. The specific locale to search for, or null to `return` applications for all<br/>locales, with locale information.<br/><br/>If not supplied when version is supplied, returns specifiers with version information only.                                                                                                                                                                                                                                                                                                                                                                                                                                           |

Retrieves a list of messaging-enabled applications installed on this computer.
Returns an array of [Application specifiers](application-and-namespace-specifiers.md#application-specifiers).

- If version is supplied, specifiers include the base name plus the version information.
- If locale is supplied, specifiers include the full name, with both version and locale information.
- If neither version nor locale is supplied, returns base specifiers with neither version nor locale
  information, but tries to find the most appropriate version and locale; see [Application specifiers](application-and-namespace-specifiers.md#application-specifiers).

For example, assuming installed applications include Photoshop CS3 10.0 `en_US`, Photoshop CS4
11.0 `en_us`, and Illustrator CS4 14.0 `de_de`

```default
BridgeTalk.getTargets();
  => [photoshop,illustrator]

BridgeTalk.getTargets( "10.0" );
  => [photoshop-10.0]

BridgeTalk.getTargets( null );
  => [photoshop-11.0, illustrator-14.0]

BridgeTalk.getTargets( null, "en_US" );
  => [photoshop-10.0-en_US, photoshop-11.0-en_US]

BridgeTalk.getTargets( null, null );
  => [photoshop-10.0-en_US, photoshop-11.0-en_us, illustrator-14.0-de_de]
```

---

### isRunning()

`BridgeTalk.isRunning (specifier)`

| `specifier`   | A specifier for the target application; see [Application specifiers](application-and-namespace-specifiers.md#application-specifiers).   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------|

Returns `true` if the given application is running and active on the local computer.

---

### launch()

`BridgeTalk.launch (specifier [, where])`

| `specifier`   | A specifier for the target application; see [Application specifiers](application-and-namespace-specifiers.md#application-specifiers).   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| `where`       | Optional. If the value “background” is specified, the application’s main window is<br/>not brought to the front of the screen.          |

Launches the given application on the local computer. It is not necessary to launch an application
explicitly in order to send it a message; sending a message to an application that is not running
automatically launches it.

Returns `true` if the application has already been launched, `false` if it was launched by this call.

---

### loadAppScript()

`BridgeTalk.loadAppScript (specifier)`

| `specifier`   | A specifier for the target application; see [Application specifiers](application-and-namespace-specifiers.md#application-specifiers).   |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------|

Loads the startup script for an application from the common StartupScripts folders. Use to
implement late loading of startup scripts.

Returns `true` if the script was successfully loaded.

---

### ping()

`BridgeTalk.ping (specifier, pingRequest)`

| `specifier`   | A specifier for the target application; see [Application specifiers](application-and-namespace-specifiers.md#application-specifiers).                                                                                                                                                                                                       |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `pingRequest` | An identifying key string for a specific type of return value. One of:<br/><br/>> - `STATUS`: Returns the processing status; see [getStatus()](#bridgetalk-getstatus).<br/>> - `DIAGNOSTICS`: Returns a diagnostic report that includes a list of valid ping keys.<br/>> - `ECHO_REQUEST`: Returns ECHO_RESPONSE for a simple ping request. |

Sends a message to another application to determine whether it can be contacted.

Returns a string whose meaning is defined by the ping-request key.

---

### pump()

`BridgeTalk.pump ()`

Checks all active messaging interfaces for outgoing and incoming messages, and processes them if
there are any.

!!! note
    Most applications have a message processing loop that continually checks the message queues,
so use of this method is rarely required.

Returns `true` if any messages have been processed, `false` otherwise.
