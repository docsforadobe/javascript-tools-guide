# Dollar ($) object

This global ExtendScript object provides a number of debugging facilities and informational methods. The properties of the $ object allow you to get global information such as the most recent run-time error, and set flags that control debugging and localization behavior. The methods allow you to output text to the JavaScript Console during script execution, control execution and other ExtendScript behavior programmatically, and gather statistics on object use.

---

## Attributes

### $.appEncoding

`$.appEncoding`

#### Description

The Internet name of the application's default character encoding, such as "CP1252" or "X-SHIFT-JIS". Valid values are implementation- and OS-dependent.

Set to change the default encoding for the application. The returned value can differ from the value set. In Windows, for example, if set to "x-latin1", the returned value is the synonymous "ISO-8859-1".

#### Type

String


---

### $.build

`$.build`

#### Description

#### Type

String

The version information for the current ExtendScript build.

Read only.

---

### $.buildDate

`$.buildDate`

#### Description

#### Type

`Date`

The date the current JavaScript engine was built.

Read only.

---

### $.decimalPoint

`$.decimalPoint`

#### Description

#### Type

String

The character used in formatted numeric output for a decimal point, for the current locale.

Read only.

---

### $.engineName

`$.engineName`

#### Description

#### Type

String

The name of the current JavaScript engine, if set.

Read only.

---

### $.error

`$.error`

#### Description

#### Type

`Error`

String

The most recent run-time error information, contained in a JavaScript Error object.

Assigning error text to this property generates a run-time error; however, the preferred way to generate a run-time error is to throw an Error object.

---

### $.fileName

`$.fileName`

#### Description

#### Type

String

The file name of the current script.

Read only.

---

### $.flags

`$.flags`

#### Description

#### Type

Number

Gets or sets low-level debug output flags. A logical AND of the following bit flag values:

- `0x0002` (2): Displays each line with its line number as it is executed.
- `0x0040` (64): Enables excessive garbage collection. Usually, garbage collection starts when the number of objects has increased by a certain amount since the last garbage collection. This flag causes ExtendScript to garbage collect after almost every statement. This impairs performance severely, but is useful when you suspect that an object gets released too soon.
- `0x0080` (128): Displays all calls with their arguments and the return value.
- `0x0100` (256): Enables extended error handling (see strict).
- `0x0200` (512): Enables the localization feature of the toString method. Equivalent to the localize property.

!!! note
    Other bit values are not public and should not be used.

---

### $.global

`$.global`

#### Description

Provides access to the Global object, which contains the JavaScript global namespace.

#### Type

Global

---

### $.hiresTimer

`$.hiresTimer`

#### Description

A high-resolution timer that measures the number of microseconds since this property was last accessed. Value is initialized as early as possible, so the first access returns the startup time for ExtendScript. The property is thread-local; that is, the first access on a thread returns the time needed to create and initialize that thread.

#### Type

Number. Read only.

---

### $.includePath

`$.includePath`

#### Description

The path for include files for the current script.

#### Type

String. Read only.

---

### $.level

`$.level`

#### Description

The current debugging level, which enables or disables the JavaScript debugger.

#### Type

Number. Read only. One of:

- `0`: No debugging
- `1`: Break on runtime errors
- `2`: Full debug mode

---

### $.line

`$.line`

#### Description

The current line of the currently executing script; the first line is number 1.

#### Type

Number. Read only.

---

### $.locale

`$.locale`

#### Description

Gets or sets the current locale. The string contains five characters in the form LL_RR, where LL is an ISO 639 language specifier, and RR is an ISO 3166 region specifier.

Initially, this is the value that the application or the platform returns for the current user. You can set it to temporarily change the locale for testing. To return to the application or platform setting, set to Nothing, `null`, or the empty string.

#### Type

String

---

### $.localize

`$.localize`

#### Description

Enable or disable the extended localization features of the built-in `toString()` method.

See [Localizing ExtendScript strings](./localizing-extendscript-strings.md).

#### Type

Boolean

---

### $.memCache

`$.memCache`

#### Description

Gets or sets the ExtendScript memory cache size in bytes.

#### Type

Number


---

### $.os

`$.os`

#### Description

The current operating system version information.

#### Type

String. Read only.

---

### $.screens

`$.screens`

#### Description

An array of objects containing information about the display screens attached to your computer.

#### Type

Array of objects

#### Properties

| Property  |    Type    |                    Description                     |
| --------- | ---------- | -------------------------------------------------- |
| `left`    | Coordinate | The left corner of the drawable area               |
| `top`     | Coordinate | The top corner of the drawable area                |
| `right`   | Coordinate | The right corner of the drawable area              |
| `bottom`  | Coordinate | The bottom corner of the drawable area             |
| `primary` | Boolean    | `true` if the object describes the primary display |

---

### $.stack

`$.stack`

#### Description

The current stack trace.

#### Type

String

---

### $.strict

`$.strict`

#### Description

When `true`, any attempt to write to a read-only property causes a runtime error.

Some objects do not permit the creation of new properties when `true`.

#### Type

Boolean

---

### $.version

`$.version`

#### Description

The version number of the JavaScript engine as a three-part number and description; for example: "3.92.95 (debug)"

#### Type

String. Read only.

---

## Methods

### $.about()

`$.about()`

#### Description

Displays the About box for the ExtendScript component, and returns the text of the About box as a string.

#### Returns

String

---

### $.bp()

`$.bp([condition])`

#### Description

Executes a breakpoint at the current position.

If no condition is needed, it is recommended that you use the JavaScript `debugger;` statement in the script, rather than this method.

#### Parameters

|  Parameter  |  Type  |                                                                        Description                                                                         |
| ----------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `condition` | String | Optional. The JavaScript statement to be used as a condition. If the statement evaluates to `true` or nonzero when this point is reached, execution stops. |

#### Returns

Nothing

---

### $.colorPicker()

`$.colorPicker(name)`

#### Description

Invokes the platform-specific color selection dialog

#### Parameters

| Parameter |                Type                |                                 Description                                  |
| --------- | ---------------------------------- | ---------------------------------------------------------------------------- |
| `name`    | Hexadecimal RGB value (`0xRRGGBB`) | The color to be preselected in the dialog, or `-1` for the platform default. |


#### Returns

Hexadecimal RGB value, e.g. `0xRRGGBB`.

---

### $.evalFile()

`$.evalFile(path[, timeout=10000])`

#### Description

Loads a JavaScript script file from disk, evaluates it, and returns the result of evaluation.

#### Parameters

| Parameter |  Type  |                                                          Description                                                           |
| --------- | ------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `path`    | String | The name and location of the file.                                                                                             |
| `timeout` | Number | Optional. A number of milliseconds to wait before returning undefined, if the script cannot be evaluated. Defaults to `10000`. |

#### Returns

Any type

---

### $.gc()

`$.gc()`

#### Description

Initiates garbage collection in the JavaScript engine.

#### Returns

Nothing

---

### $.getenv()

`$.getenv(envname)`

#### Description

Retrieves the value of the specified environment variable, or null if no such variable is defined.

!!! note
    On MacOS the only env vars that will be accessible are:

    - System default environment variable
    - Custom environment variables created by the `$.setenv()` metho
    - Custom environment variables created with `launchctl setenv CUSTOM_VAR "custom_value"`

Any env vars set in .bash_profile, .bashrc, .profile, .zshenv, or .zshrc will be ignored.

#### Parameters

| Parameter |  Type  |              Description              |
| --------- | ------ | ------------------------------------- |
| `envname` | String | The name of the environment variable. |

#### Returns

String

---

### $.setenv()

`$.setenv(envname, value)`

#### Description

Sets the value of the specified environment variable, if no such variable is defined.

#### Parameters

| Parameter |  Type  |              Description              |
| --------- | ------ | ------------------------------------- |
| `envname` | String | The name of the environment variable. |
| `value`   | String | The new value, a string.              |

#### Returns

Nothing

---

### $.sleep()

`$.sleep(milliseconds)`

#### Description

Suspends the calling thread for the given number of milliseconds.

During a sleep period, checks at `100` millisecond intervals to see whether the sleep should be terminated. This can happen if there is a break request, or if the script timeout has expired.

#### Parameters

|   Parameter    |  Type  |             Description             |
| -------------- | ------ | ----------------------------------- |
| `milliseconds` | Number | The number of milliseconds to wait. |

#### Returns

Nothing

---

### $.write()

`$.write(text[, text...]...)`

#### Description

Writes the specified text to the JavaScript Console.

#### Parameters

| Parameter |  Type  |                                  Description                                  |
| --------- | ------ | ----------------------------------------------------------------------------- |
| `text`    | String | One or more strings to write, which are concatenated to form a single string. |

#### Returns

Nothing

---

### $.writeln()

`$.writeln (text[, text...]...)`

#### Description

Writes the specified text to the JavaScript Console and appends a linefeed sequence.

#### Parameters

| Parameter |  Type  |                                  Description                                  |
| --------- | ------ | ----------------------------------------------------------------------------- |
| `text`    | String | One or more strings to write, which are concatenated to form a single string. |

#### Returns

Nothing
