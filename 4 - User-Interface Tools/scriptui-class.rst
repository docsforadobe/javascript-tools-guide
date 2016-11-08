.. _scriptui-class:

ScriptUI class
==============
The globally available ScriptUI class provides central information about the ScriptUI module. This object
is not instantiable.

.. _scriptui-class-properties:

ScriptUI class properties
-------------------------
Alignment

Object

Collects the enumerated values that can be used in the alignment and
alignChildren properties of controls and containers, and in the alignment
property used to set a control’s titleLayout property. Read only.
Use these constants to set the alignment. For example:
myGroup.alignment = [ScriptUI.Alignment.LEFT,
ScriptUI.Alignment.TOP]

When you query the alignment property, it returns index values that
correspond to the constants as shown. Constant values are:
ScriptUI.Alignment.TOP
ScriptUI.Alignment.BOTTOM
ScriptUI.Alignment.LEFT
ScriptUI.Alignment.RIGHT
ScriptUI.Alignment.FILL
ScriptUI.Alignment.CENTER
applicationFonts Object

(1)
(2)
(3)
(4)
(5)
(6)

Collects the enumerated values that specify the default application fonts.
The available fonts vary according to the application and system
configuration.

compatability

Object

An object whose properties are the names of compatibility modes
supported by the host application. For example, the presence of
ScriptUI.compatability.su1PanelCoordinates means that the
application allows backward compatibility with the coordinate system of
Panel elements in ScriptUI version 1.

coreVersion

String

The internal core version number of the ScriptUI components. Read only.

environment

Object

A JavaScript object that provides access to attributes of the ScriptUI
environment; contains a Keyboard state object that reports the active
state of the keyboard at any time, independent of the event-handling
framework.

events

Object

A JavaScript object that contains one function, events.createEvent(),
which allows you to create event objects in order to simulate
user-interaction events.

FontStyle

String

Collects the enumerated values that can be used as the style argument
to the ScriptUI.newFont() method. For example:
var font = ScriptUI.newFont ('Helvetica",
ScriptUI.FontStyle.BOLD)

Read only. Values are:
REGULAR
BOLD
ITALIC
BOLDITALIC
frameworkName

String

The name of the user-interface framework with which this ScriptUI
component is compatible. Read only.

version

String

The main version number of the ScriptUI component framework. Read
only.

.. _scriptui-class-functions:

ScriptUI class functions
------------------------
events.createEvent()
ScriptUi.events.createEvent (eventType)
eventType

The type of event, one of:
UIEvent
KeyboardEvent
MouseEvent

This function is in the JavaScript object contained in the events property. It returns an event object
of the appropriate type:
A UIEvent base class encapsulates input event information for an event that propagates
through a container and control hierarchy. This is a base class for the more specialized keyboard
and mouse event types.
A KeyboardEvent object encapsulates information about keyboard input events.
A MouseEvent object encapsulates information about mouse events.
This object is passed to a function that you register to respond to events of a certain type that occur
in a window or control. Use windowObj.addEventListener() or controlObj.addEventListener() to
register a handler function. See "Registering event listeners for windows or controls" on page 82.
getResourceText()
ScriptUI.getResourceText (text)
text

The text to match.

Finds and returns the resource for a given text string from the host application’s resource data. If no
string resource matches the given text, the text itself is returned.
Returns a String.
newFont()
ScriptUI.newFont ( name, style, size );
name

The font or font family name string.

style

The font style string or an enumerated value from ScriptUI.FontStyle.

size

The font size in points, a number.

Creates a new font object for use in text controls and titles.
Returns a ScriptUIFont object.

CHAPTER 4: User-Interface Tools

108

Common properties

newImage()
ScriptUI.newImage ( normal, disabled, pressed, rollover );
normal

The resource name or path to the image to use for the normal or default state.

disabled

The resource name or path to the image to use for the disabled state, shown when the
control containing the image is disabled (enabled=false).

pressed

The resource name or path to the image to use for the pressed state, shown when the
user clicks on the image.

rollover

The resource name or path to the image to use for the rollover state, which is shown
when the cursor moves over the image.

Creates a new image object for use in controls that can display images, loading the associated
images from the specified resources or image files.
Returns a ScriptUIImage object.

.. _environment-object:

Environment object
------------------
This global object is available through the ScriptUI.environment property. It defines attributes of the
ScriptUI environment. In the current release, it contains one property:
keyboardState

Object

A Keyboard state object that reports the active state of the keyboard at
any time, independent of the event-handling framework.

