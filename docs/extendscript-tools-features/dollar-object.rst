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

.. _dollar-appEncoding:

appEncoding
***********
``String``

The Internet name of the application's default character encoding, such as
"CP1252" or "X-SHIFT-JIS". Valid values are implementation- and
OS-dependent.

Set to change the default encoding for the application. The returned value
can differ from the value set. In Windows, for example, if set to "x-latin1",
the returned value is the synonymous "ISO-8859-1".

--------------------------------------------------------------------------------

.. _dollar-build:

build
*****
``String``

The version information for the current ExtendScript build.

Read only.

--------------------------------------------------------------------------------

.. _dollar-buildDate:

buildDate
*********
``Date``

The date the current JavaScript engine was built.

Read only.

--------------------------------------------------------------------------------

.. _dollar-decimalPoint:

decimalPoint
************
``String``

The character used in formatted numeric output for a decimal point, for
the current locale.

Read only.

--------------------------------------------------------------------------------

.. _dollar-engineName:

engineName
**********
``String``

The name of the current JavaScript engine, if set.

Read only.

--------------------------------------------------------------------------------

.. _dollar-error:

error
*****
``Error``
``String``

The most recent run-time error information, contained in a JavaScript
Error object.

Assigning error text to this property generates a run-time error; however,
the preferred way to generate a run-time error is to throw an Error object.

--------------------------------------------------------------------------------

.. _dollar-fileName:

fileName
********
``String``

The file name of the current script.

Read only.

--------------------------------------------------------------------------------

.. _dollar-flags:

flags
******
Number

Gets or sets low-level debug output flags. A logical AND of the following
bit flag values:

- ``0x0002`` (2): Displays each line with its line number as it is executed.
- ``0x0040`` (64): Enables excessive garbage collection. Usually, garbage
  collection starts when the number of objects has increased by a
  certain amount since the last garbage collection. This flag causes
  ExtendScript to garbage collect after almost every statement. This
  impairs performance severely, but is useful when you suspect that an
  object gets released too soon.
- ``0x0080`` (128): Displays all calls with their arguments and the return
  value.
- ``0x0100`` (256): Enables extended error handling (see strict).
- ``0x0200`` (512): Enables the localization feature of the toString
  method. Equivalent to the localize property.

.. note:: Other bit values are not public and should not be used.

--------------------------------------------------------------------------------

.. _dollar-global:

global
******
``Global``

Provides access to the Global object, which contains the JavaScript global
namespace.

--------------------------------------------------------------------------------

.. _dollar-hiresTimer:

hiresTimer
**********
``Number``

A high-resolution timer that measures the number of microseconds since
this property was last accessed. Value is initialized as early as possible, so
the first access returns the startup time for ExtendScript. The property is
thread-local; that is, the first access on a thread returns the time needed to
create and initialize that thread.

Read only.

--------------------------------------------------------------------------------

.. _dollar-includePath:

includePath
***********
``String``

The path for include files for the current script.

Read only.

--------------------------------------------------------------------------------

.. _dollar-level:

level
*****
``Number``

The current debugging level, which enables or disables the JavaScript
debugger. One of:

- ``0``: No debugging
- ``1``: Break on runtime errors
- ``2``: Full debug mode

Read only.

--------------------------------------------------------------------------------

.. _dollar-line:

line
****
``Number``

The current line of the currently executing script; the first line is number 1.

Read only.

--------------------------------------------------------------------------------

.. _dollar-locale:

locale
******
``String``

Gets or sets the current locale. The string contains five characters in the
form LL_RR, where LL is an ISO 639 language specifier, and RR is an ISO
3166 region specifier.

Initially, this is the value that the application or the platform returns for the
current user. You can set it to temporarily change the locale for testing. To
return to the application or platform setting, set to ``undefined``, ``null``, or the
empty string.

--------------------------------------------------------------------------------

.. _dollar-localize:

localize
********
``Boolean``

Enable or disable the extended localization features of the built-in
toString method. See Localizing ExtendScript strings.

--------------------------------------------------------------------------------

.. _dollar-memCache:

memCache
********
``Number``

Gets or sets the ExtendScript memory cache size in bytes.

--------------------------------------------------------------------------------

.. _dollar-os:

os
**
``String``

The current operating system version information.

Read only.

--------------------------------------------------------------------------------

.. _dollar-screens:

screens
*******
``Array``

An array of objects containing information about the display screens
attached to your computer.

Each object has the properties left, top, right, and bottom, which
contain the four corners of the drawable area of each screen in global
coordinates.

A property primary is true if that object describes the primary display.

--------------------------------------------------------------------------------

.. _dollar-stack:

stack
*****
``String``

The current stack trace.

--------------------------------------------------------------------------------

.. _dollar-strict:

strict
******
``Boolean``

When ``true``, any attempt to write to a read-only property causes a runtime
error. Some objects do not permit the creation of new properties when
true.

--------------------------------------------------------------------------------

.. _dollar-version:

version
*******
``String``

The version number of the JavaScript engine as a three-part number and
description; for example: "3.92.95 (debug)"

Read only.

--------------------------------------------------------------------------------


.. _dollar-object-functions:

Dollar ($) object functions
---------------------------

.. _dollar-about:

about()
*******
``$.about()``

Displays the About box for the ExtendScript component, and returns the text of the About
box as a string.

returns: ``String``

--------------------------------------------------------------------------------

.. _dollar-bp:

bp()
****
``$.bp([condition])``

=============  ==========================================================================
``condition``  Optional. A string containing a JavaScript statement to be used as a
               condition. If the statement evaluates to true or nonzero when this point is reached,
               execution stops.
=============  ==========================================================================

Executes a breakpoint at the current position.

If no condition is needed, it is recommended that you use the JavaScript debugger
statement in the script, rather than this method.

returns: ``undefined``

--------------------------------------------------------------------------------

.. _dollar-colorPicker:

colorPicker()
*************
``$.colorPicker(name)``

========  ==========================================================================
``name``  The color to be preselected in the dialog, as a hexadecimal RGB value
          (``0xRRGGBB``), or ``-1`` for the platform default.
========  ==========================================================================

Invokes the platform-specific color selection dialog, and returns the selected color as a
hexadecimal RGB value: ``0xRRGGBB``.

Returns: ``Number``

--------------------------------------------------------------------------------

.. _dollar-evalFile:

evalFile()
**********
``$.evalFile(path[, timeout])``

===========  ==========================================================================
``path``     The name and location of the file.
``timeout``  Optional. A number of milliseconds to wait before returning undefined, if
             the script cannot be evaluated. Default is 10000 milliseconds.
===========  ==========================================================================

Loads a JavaScript script file from disk, evaluates it, and returns the result of evaluation.

Returns: Any type

--------------------------------------------------------------------------------

.. _dollar-gc:

gc()
****
``$.gc()``

Initiates garbage collection in the JavaScript engine.

Returns: ``undefined``

--------------------------------------------------------------------------------

.. _dollar-getenv:

getenv()
********
``$.getenv(envname)``

===========  ======================================
``envname``  The name of the environment variable.
===========  ======================================

Retrieves the value of the specified environment variable, or null if no such variable is
defined.

Returns: ``String``

--------------------------------------------------------------------------------

.. _dollar-setenv:

setenv()
********
``$.setenv(envname, value)``

===========  ======================================
``envname``  The name of the environment variable.
``value``    The new value, a string.
===========  ======================================

Sets the value of the specified environment variable, if no such variable is defined.

Returns: ``undefined``

--------------------------------------------------------------------------------

.. _dollar-sleep:

sleep()
*******
``$.sleep(milliseconds)``

================  ======================================
``milliseconds``  The number of milliseconds to wait.
================  ======================================

Suspends the calling thread for the given number of milliseconds.

During a sleep period, checks at 100 millisecond intervals to see whether the sleep should
be terminated. This can happen if there is a break request, or if the script timeout has
expired.

Returns: ``undefined``

--------------------------------------------------------------------------------

.. _dollar-write:

write()
*******
``$.write(text[, text...]...)``

========  ===============================================
``text``  One or more strings to write, which are concatenated to form a single string.
========  ===============================================

Writes the specified text to the JavaScript Console.

Returns: ``undefined``

--------------------------------------------------------------------------------

.. _dollar-writeln:

writeln()
*********
``$.writeln (text[, text...]...)``

========  ===============================================
``text``  One or more strings to write, which are concatenated to form a single string.
========  ===============================================

Writes the specified text to the JavaScript Console and appends a linefeed sequence.

Returns: ``undefined``
