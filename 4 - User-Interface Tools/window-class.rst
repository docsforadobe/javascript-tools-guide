.. _window-class:

Window class
============
The Window class defines these static properties and functions. Window instances created with new
Window() do not have these properties and functions defined.

.. _window-class-properties:

Window class properties
-----------------------
frameworkName

String

Deprecated. Use ScriptUI.frameworkName instead.

version

String

Deprecated. Use ScriptUI.version instead.

.. _window-class-functions:

Window class functions
----------------------
Access these function through the class. For example:
Window.alert("Notification to user");
alert()
Window.alert (message[, title, errorIcon]);
message

The string for the displayed message.

title

Optional. A string to appear as the title of the dialog, if the platform supports a
title. Mac OS does not support titles for alert dialogs. The default title string is
"Script Alert."

errorIcon

Optional. When true, the platform-standard alert icon is replaced by the
platform-standard error icon in the dialog. Default is false.

Displays a platform-standard dialog containing a short message and an OK button.
Returns undefined
confirm()
Window.confirm (message[,noAsDflt ,title ]);
message

The string for the displayed message.

noAsDflt

Optional. When true, the No button is the default choice, selected when the user
types ENTER. Default is false, meaning that Yes is the default choice.

title

Optional. A string to appear as the title of the dialog, if the platform supports a
title. Mac OS does not support titles for confirmation dialogs. The default title
string is "Script Alert."

Displays a platform-standard dialog containing a short message and two buttons labeled Yes and
No.
Returns true if the user clicked Yes, false if the user clicked No.
find()
Window.find (resourceName)
Window.find (type, title)
resourceName

The name of a predefined resource available to JavaScript in the current
application.

type

Optional. The window type (see "Window object constructor" on page 112) used if
there is more than one window with the same title. Can be null or the empty
string.

title

The window title.

Use this method to find an existing window. This includes windows already created by a script, and
windows created by the application (if the application supports this case).
NOTE: Not supported in all ScriptUI implementations.
Returns a Window object found or generated from the resource, or null if no such window or
resource exists.

prompt()
Window.prompt (message, preset[, title ]);
message

The string for the displayed message.

preset

The initial value to be displayed in the text edit field.

title

Optional. A string to appear as the title of the dialog. In Windows, this appears in
the window’s frame; in Mac OS it appears above the message. The default title
string is "Script Prompt."

Displays a modal dialog that returns the user’s text input.
Returns the value of the text edit field if the user clicked OK, null if the user clicked Cancel.

