.. _dollar-object:

Dollar ($) object
=================
This global ExtendScript object provides a number of debugging facilities and informational methods. The
properties of the $ object allow you to get global information such as the most recent run-time error, and
set flags that control debugging and localization behavior. The methods allow you to output text to the
JavaScript Console during script execution, control execution and other ExtendScript behavior
programmatically, and gather statistics on object use.

.. _dollar-object-properties:

Dollar ($) object properties
----------------------------
appEncoding

String

The Internet name of the application's default character encoding, such as
"CP1252" or "X-SHIFT-JIS". Valid values are implementation- and
OS-dependent.
Set to change the default encoding for the application. The returned value
can differ from the value set. In Windows, for example, if set to "x-latin1",
the returned value is the synonymous "ISO-8859-1".

build

String

The version information for the current ExtendScript build. Read only.

buildDate

Date

The date the current JavaScript engine was built. Read only.

decimalPoint

String

The character used in formatted numeric output for a decimal point, for
the current locale. Read only.

engineName

String

The name of the current JavaScript engine, if set. Read only.

error

Error
String

The most recent run-time error information, contained in a JavaScript
Error object.

217

Assigning error text to this property generates a run-time error; however,
the preferred way to generate a run-time error is to throw an Error object.
fileName

String

The file name of the current script. Read only.

flags

Number

Gets or sets low-level debug output flags. A logical AND of the following
bit flag values:
0x0002 (2): Displays each line with its line number as it is executed.
0x0040 (64): Enables excessive garbage collection. Usually, garbage

collection starts when the number of objects has increased by a
certain amount since the last garbage collection. This flag causes
ExtendScript to garbage collect after almost every statement. This
impairs performance severely, but is useful when you suspect that an
object gets released too soon.
0x0080 (128): Displays all calls with their arguments and the return

value.

0x0100 (256): Enables extended error handling (see strict).
0x0200 (512): Enables the localization feature of the toString
method. Equivalent to the localize property.

.. note:: Other bit values are not public and should not be used.

global

Global

Provides access to the Global object, which contains the JavaScript global
namespace.

hiresTimer

Number

A high-resolution timer that measures the number of microseconds since
this property was last accessed. Value is initialized as early as possible, so
the first access returns the startup time for ExtendScript. The property is
thread-local; that is, the first access on a thread returns the time needed to
create and initialize that thread. Read only.

includePath

String

The path for include files for the current script. Read only.

level

Number

The current debugging level, which enables or disables the JavaScript
debugger. Read only. One of:
0: No debugging
1: Break on runtime errors
2: Full debug mode

line

Number

The current line of the currently executing script; the first line is number 1.
Read only.

locale

String

Gets or sets the current locale. The string contains five characters in the
form LL_RR, where LL is an ISO 639 language specifier, and RR is an ISO
3166 region specifier.
Initially, this is the value that the application or the platform returns for the
current user. You can set it to temporarily change the locale for testing. To
return to the application or platform setting, set to undefined, null, or the
empty string.

localize

Boolean

Enable or disable the extended localization features of the built-in

toString method. See Localizing ExtendScript strings.

memCache

Number

Gets or sets the ExtendScript memory cache size in bytes.

os

String

The current operating system version information. Read only.

screens

Array

An array of objects containing information about the display screens
attached to your computer.
Each object has the properties left, top, right, and bottom, which
contain the four corners of the drawable area of each screen in global
coordinates.
A property primary is true if that object describes the primary display.

stack

String

The current stack trace.

strict

Boolean

When true, any attempt to write to a read-only property causes a runtime
error. Some objects do not permit the creation of new properties when
true.

version

String

The version number of the JavaScript engine as a three-part number and
description; for example: "3.92.95 (debug)" Read only.

.. _dollar-object-functions:

Dollar ($) object functions
---------------------------
Function

Return type

about()
$.about ()

String

Displays the About box for the ExtendScript component, and returns the text of the About
box as a string.
bp()
$.bp ([condition])

Executes a breakpoint at the current position.
condition: Optional. A string containing a JavaScript statement to be used as a
condition. If the statement evaluates to true or nonzero when this point is reached,
execution stops.

If no condition is needed, it is recommended that you use the JavaScript debugger
statement in the script, rather than this method.

undefined

Function

Return type

colorPicker()
$.colorPicker (name)

Number

Invokes the platform-specific color selection dialog, and returns the selected color as a
hexadecimal RGB value: 0xRRGGBB.
name: The color to be preselected in the dialog, as a hexadecimal RGB value
(0xRRGGBB), or -1 for the platform default.
evalFile()
$.evalFile (path[, timeout])

Any

Loads a JavaScript script file from disk, evaluates it, and returns the result of evaluation.
path: The name and location of the file.
timeout: Optional. A number of milliseconds to wait before returning undefined, if

the script cannot be evaluated. Default is 10000 milliseconds.
gc()
$.gc ()

undefined

Initiates garbage collection in the JavaScript engine.
getenv()
$.getenv (envname)

String

Retrieves the value of the specified environment variable, or null if no such variable is
defined.
envname: The name of the environment variable.
setenv()
$.setenv (envname, value)

undefined

Sets the value of the specified environment variable, if no such variable is defined.
envname: The name of the environment variable.
value: The new value, a string.
sleep()
$.sleep (milliseconds)

Suspends the calling thread for the given number of milliseconds.
milliseconds: The number of milliseconds to wait.

During a sleep period, checks at 100 millisecond intervals to see whether the sleep should
be terminated. This can happen if there is a break request, or if the script timeout has
expired.

undefined

Function

Return type

write()
$.write (text[, text...]...)

undefined

Writes the specified text to the JavaScript Console.
text: One or more strings to write, which are concatenated to form a single string.
writeln()
$.writeln (text[, text...]...)

Writes the specified text to the JavaScript Console and appends a linefeed sequence.
text: One or more strings to write, which are concatenated to form a single string.

undefined
