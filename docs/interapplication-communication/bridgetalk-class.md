# BridgeTalk class

Static properties and methods of this class provide a way for your script to determine basic messaging system information before you create any specific message objects. Static methods allow you to check if an application is installed and is already running, and to launch the application. A callback defined on the class determines how the application processes incoming messages.

You can access static properties and methods in the BridgeTalk class, which is available in the global namespace. For example:

```javascript
var thisApp = BridgeTalk.appName;
```

!!! note
    You must instantiate the BridgeTalk class to create the BridgeTalk message object, which is used to send message packets between applications. Dynamic properties and methods can be accessed only in instances.

---

## Attributes

The BridgeTalk class provides these static properties, which are available in the global namespace:

### BridgeTalk.appInstance

`BridgeTalk.appInstance`

#### Description

The instance identifier of an application launched by the messaging framework, the instance portion of an application specifier; see [Application specifiers](application-and-namespace-specifiers.md#application-specifiers).

Used only for those applications, such as InDesign, that support launching and running multiple instances.

#### Type

String. Read only.

---

### BridgeTalk.appLocale

`BridgeTalk.appLocale`

#### Description

The locale of this application, the locale portion of an application specifier; see [Application specifiers](application-and-namespace-specifiers.md#application-specifiers). When a message is sent, this is the locale of the sending application.

#### Type

String. Read only.

---

### BridgeTalk.appName

`BridgeTalk.appName`

#### Description

The name of this application, the appname portion of an application specifier; see [Application specifiers](application-and-namespace-specifiers.md#application-specifiers). When a message is sent, this is the name of the sending application.

#### Type

String. Read only.

---

### BridgeTalk.appSpecifier

`BridgeTalk.appSpecifier`

#### Description

A lower-case string containing the complete specifier for this application; see [Application specifiers](application-and-namespace-specifiers.md#application-specifiers).

#### Type

String.

---

### BridgeTalk.appStatus

`BridgeTalk.appStatus`

#### Description

The current processing status of this application. One of:

- `busy`: The application is currently busy, but not processing messages. This is the case, for example, when a modal dialog is shown.
- `idle`: The application is currently idle, but processes messages regularly.
- `not installed`: The application is not installed.

#### Type

String. Read only.

---

### BridgeTalk.appVersion

`BridgeTalk.appVersion`

#### Description

The version number of this application, the version portion of an application specifier; see [Application specifiers](application-and-namespace-specifiers.md#application-specifiers). When a message is sent, this is the version of the sending application.

#### Type

String. Read only.

---

### BridgeTalk.onReceive

`BridgeTalk.onReceive`

#### Description

#### Returns

callback function that this application applies to unsolicited incoming messages. The default function evaluates the body of the received message and returns the result of evaluation. To change the default behavior, set this to a function definition in the following form:

```javascript
BridgeTalk.onReceive = function( bridgeTalkObject ) {
    // act on received message
};
```

The body property of the received message object contains the received data. The function can return any type. See [Handling unsolicited messages](communicating-through-messages.md#handling-unsolicited-messages).

!!! note
    This function is not applied to a message that is received in response to a message sent from this application. Response messages are processed by the onResult, onReceived, or onError callbacks associated with the sent message.

#### Type

Function

---

## Methods

The BridgeTalk class provides these static methods, which are available in the global namespace:

### BridgeTalk.bringToFront()

`BridgeTalk.bringToFrontapp)`

#### Description

Brings all windows of the specified application to the front of the screen.

In Mac OS, an application can be running but have no windows open. In this case, calling this function might or might not open a new window, depending on the application. For Adobe Bridge, it opens a new browser window.

#### Parameters

| Parameter |                                           Type                                           |              Description               |
| --------- | ---------------------------------------------------------------------------------------- | -------------------------------------- |
| `app`     | [Application specifiers](application-and-namespace-specifiers.md#application-specifiers) | A specifier for the target application |

#### Returns

Nothing

---

### BridgeTalk.getAppPath()

`BridgeTalk.getAppPathapp)`

#### Description

Retrieves the full path of the executable file for a specified application.

#### Parameters

| Parameter |                                           Type                                           |              Description               |
| --------- | ---------------------------------------------------------------------------------------- | -------------------------------------- |
| `app`     | [Application specifiers](application-and-namespace-specifiers.md#application-specifiers) | A specifier for the target application |

#### Returns

String

---

### BridgeTalk.getDisplayName()

`BridgeTalk.getDisplayNameapp)`

#### Description

Returns a localized display name for an application, or `null` if the application is not installed. For example:

#### Parameters

| Parameter |                                           Type                                           |              Description               |
| --------- | ---------------------------------------------------------------------------------------- | -------------------------------------- |
| `app`     | [Application specifiers](application-and-namespace-specifiers.md#application-specifiers) | A specifier for the target application |

#### Returns

String

#### Example

```javascript
BridgeTalk.getDisplayName("photoshop-10.0");
=> Adobe Photoshop CS4
```

---

### BridgeTalk.getSpecifier()

`BridgeTalk.getSpecifierappName[, version][, locale])`

#### Description

Retrieves a complete application specifier.

#### Parameters

+-----------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter |                      Type                       |                                                                      Description                                                                       |
+===========+=================================================+========================================================================================================================================================+
| `appName` | The base name of the application to search for. |                                                                                                                                                        |
+-----------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| `version` | Number                                          | Optional. The specific version number to search for.                                                                                                   |
|           |                                                 | If `0` or not supplied, returns the most recent version.                                                                                               |
|           |                                                 | If negative, returns the highest version up to and including the absolute value.                                                                       |
|           |                                                 |                                                                                                                                                        |
|           |                                                 | If a major version is specified, returns the highest minor-version variation. For example, if Photoshop CS versions 9, 9.1, and 10 are installed:      |
|           |                                                 |                                                                                                                                                        |
|           |                                                 | <pre lang="javascript">BridgeTalk.Specifier( "photoshop", "9" )<br/> => ["photoshop-9.1"]<br/></pre>                                                   |
+-----------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| `locale`  | String                                          | Optional. The specific locale to search for. If not supplied and multiple language versions are installed, prefers the version for the current locale. |
+-----------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+

#### Returns

[Application specifier](application-and-namespace-specifiers.md#application-specifiers) for a messaging-enabled application version installed on this computer, or `null` if the requested version of the application is not installed.

#### Example

For example, assuming installed applications include Photoshop CS4 11.0 `en_us`, Photoshop CS2 8.5 `de_de`, Photoshop CS2 9.0 `de_de`, and Photoshop CS2 9.5 `de_de`, and that the current locale is `en_US`

```javascript
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

### BridgeTalk.getStatus()

`BridgeTalk.getStatus(targetSpec)`

#### Description

Retrieves the processing status of an application.

#### Parameters

|  Parameter   |                                           Type                                           |                                                         Description                                                          |
| ------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `targetSpec` | [Application specifiers](application-and-namespace-specifiers.md#application-specifiers) | Optional. A specifier for the target application. If not supplied, returns the processing status of the current application. |

#### Returns

String, one of:

- `BUSY`: The application is currently busy, but not processing messages. This is the case, for example, when a modal dialog is shown.
- `IDLE`: The application is currently idle, but processes messages regularly.
- `PUMPING`: The application is currently processing messages.
- `ISNOTRUNNING`: The application is installed but not running.
- `ISNOTINSTALLED`: The application is not installed.
- `UNDEFINED`: The application is running but not responding to ping requests. This can be true of a CS2 application that uses an earlier version of the messaging framework.

---

### BridgeTalk.getTargets()

`BridgeTalk.getTargets([version],[locale])`

#### Description

Retrieves a list of messaging-enabled applications installed on this computer.

#### Parameters

+-----------+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter |  Type  |                                                                                                     Description                                                                                                     |
+===========+========+=====================================================================================================================================================================================================================+
| `version` | Number | Optional. The specific version number to search for, or `null` to return the most appropriate version (matching, most recent, or running), with version information.                                                |
|           |        |                                                                                                                                                                                                                     |
|           |        | Specify only a major version number to return the highest minor-version variation.                                                                                                                                  |
|           |        |                                                                                                                                                                                                                     |
|           |        | For example, if Photoshop CS versions 9, 9.5, and 10 are installed                                                                                                                                                  |
|           |        |                                                                                                                                                                                                                     |
|           |        | <pre lang="javascript">BridgeTalk.getTargets( "9" )<br/>=> [photoshop-9.5]</pre>                                                                                                                                    |
|           |        |                                                                                                                                                                                                                     |
|           |        | Specify a negative value to return all versions up to the absolute value of the version number. For example                                                                                                         |
|           |        |                                                                                                                                                                                                                     |
|           |        | <pre lang="javascript">BridgeTalk.getTargets( "-9.9" )<br/>=> [photoshop-9.0, photoshop-9.5]</pre>                                                                                                                  |
+-----------+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `locale`  | String | Optional. The specific locale to search for, or null to `return` applications for all locales, with locale information. If not supplied when version is supplied, returns specifiers with version information only. |
+-----------+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### Returns

Returns an array of [Application specifiers](application-and-namespace-specifiers.md#application-specifiers).

- If version is supplied, specifiers include the base name plus the version information.
- If locale is supplied, specifiers include the full name, with both version and locale information.
- If neither version nor locale is supplied, returns base specifiers with neither version nor locale information, but tries to find the most appropriate version and locale; see [Application specifiers](application-and-namespace-specifiers.md#application-specifiers).

#### Example

For example, assuming installed applications include Photoshop CS3 10.0 `en_US`, Photoshop CS4 11.0 `en_us`, and Illustrator CS4 14.0 `de_de`

```javascript
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

### BridgeTalk.isRunning()

`BridgeTalk.isRunning(specifier)`

#### Description

Checks whether a given application is running and active on the local computer.

#### Parameters

|  Parameter  |                                           Type                                           |              Description               |
| ----------- | ---------------------------------------------------------------------------------------- | -------------------------------------- |
| `specifier` | [Application specifiers](application-and-namespace-specifiers.md#application-specifiers) | A specifier for the target application |

#### Returns

Boolean

---

### BridgeTalk.launch()

`BridgeTalk.launch(specifier[, where])`

#### Description

Launches the given application on the local computer. It is not necessary to launch an application explicitly in order to send it a message; sending a message to an application that is not running automatically launches it.

#### Parameters

|  Parameter  |                                           Type                                           |                                                        Description                                                         |
| ----------- | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `specifier` | [Application specifiers](application-and-namespace-specifiers.md#application-specifiers) | A specifier for the target application                                                                                     |
| `where`     | Unknown.                                                                                 | Optional. If the value "background" is specified, the application's main window is not brought to the front of the screen. |

#### Returns

Boolean. `true` if the application has already been launched, `false` if it was launched by this call.

---

### BridgeTalk.loadAppScript()

`BridgeTalk.loadAppScript(specifier)`

#### Description

Loads the startup script for an application from the common StartupScripts folders. Use to implement late loading of startup scripts.

#### Parameters

|  Parameter  |                                           Type                                           |              Description               |
| ----------- | ---------------------------------------------------------------------------------------- | -------------------------------------- |
| `specifier` | [Application specifiers](application-and-namespace-specifiers.md#application-specifiers) | A specifier for the target application |

#### Returns

Boolean. `true` if the script was successfully loaded.

---

### BridgeTalk.ping()

`BridgeTalk.ping(specifier, pingRequest)`

#### Description

Sends a message to another application to determine whether it can be contacted.

#### Parameters

+---------------+------------------------------------------------------------------------------------------+----------------------------------------+
|   Parameter   |                                           Type                                           |              Description               |
+===============+==========================================================================================+========================================+
| `specifier`   | [Application specifiers](application-and-namespace-specifiers.md#application-specifiers) | A specifier for the target application |
+---------------+------------------------------------------------------------------------------------------+----------------------------------------+
| `pingRequest` | Identifying key string, one of:                                                          | Specific type of return value.         |
|               |                                                                                          |                                        |
|               | - `STATUS`: Returns the processing status; see [getStatus()](#bridgetalkgetstatus).      |                                        |
|               | - `DIAGNOSTICS`: Returns a diagnostic report that includes a list of valid ping keys.    |                                        |
|               | - `ECHO_REQUEST`: Returns `ECHO_RESPONSE` for a simple ping request.                     |                                        |
+---------------+------------------------------------------------------------------------------------------+----------------------------------------+

#### Returns

String

---

### BridgeTalk.pump()

`BridgeTalk.pump()`

#### Description

Checks all active messaging interfaces for outgoing and incoming messages, and processes them if there are any.

!!! note
    Most applications have a message processing loop that continually checks the message queues, so use of this method is rarely required.

#### Returns

Boolean. `true` if any messages have been processed, `false` otherwise.
