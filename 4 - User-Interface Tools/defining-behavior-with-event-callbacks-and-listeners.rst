.. _defining-behavior-with-event-callbacks-and-listeners:

Defining behavior with event callbacks and listeners
====================================================
You must define the behavior of your controls in order for them to respond to user interaction. You can do
this by defining event-handling callback functions as part of the definition of the control or window. To
respond to a specific event, define a handler function for it, and assign a reference to that function in the
corresponding property of the window or control object. Different types of windows and controls respond
to different actions, or events:
Windows generate events when the user moves or resizes the window. To handle these events, define
callback functions for onMove, onMoving, onResize, and onResizing. To respond to the user opening
or closing the window, define callback functions for onShow and onClose.

Button, RadioButton, and Checkbox controls generate events when the user clicks within the control
bounds. To handle the event, define a callback function for onClick.
EditText, Scrollbar, and Slider controls generate events when the content or value changes-that is,
when the user types into an edit field, or moves the scroll or slider indicator. To handle these events,
define callback functions for onChange and onChanging.
ListBox, DropDownList, and TreeView controls generate events whenever the selection in the list
changes. To handle the event, define a callback function for onChange. The TreeView control also
generates events when the user expands or collapses a node, handled by the onExpand and
onCollapse callback functions.
The ListBox also generates an event when the user double-clicks an item. To handle it, define a
callback function for the onDoubleClick event.
Both containers and controls generate events just before they are drawn, that allow you to customize
their appearance. To handle these events, define callback functions for onDraw. Your handler can
modify or control how the container or control is drawn using the methods defined in the control’s
associated ScriptUIGraphics object.
In Windows only, you can register a key sequence as a shortcutKey for a window or for most types of
controls. To handle the key sequence, define a callback function for onShortcutKey in that control.

.. _defining-event-handler-callback-functions:

Defining event-handler callback functions
-----------------------------------------
Your script can define an event handler as a named function referenced by the callback property, or as an
unnamed function defined inline in the callback property.
If you define a named function, assign its name as the value of the corresponding callback property.
For example:
function hasBtnsCbOnClick() { /* do something interesting */ }
hasBtnsCb.onClick = hasBtnsCbOnClick;

For a simple, unnamed function, set the property value directly to the function definition:
UI-element.callback-name = function () { handler-definition};

Event-handler functions take no arguments.
For example, the following sets the onClick property of the hasBtnsCb checkbox to a function that
enables another control in the same dialog:
hasBtnsCb.onClick = function ()
{ this.parent.alertBtnsPnl.enabled = this.value; };

The following statements set the onClick event handlers for buttons that close the containing dialog,
returning different values to the show method that invoked the dialog, so the calling script can tell which
button was clicked:
buildBtn.onClick = function () { this.parent.parent.close(1); };
cancelBtn.onClick = function () { this.parent.parent.close(2); };

.. _simulating-user-events:

Simulating user events
----------------------
You can simulate user actions by sending an event notification directly to a window or control with the
notify method. A script can use this method to generate events in the controls of a window, as if a user
was clicking buttons, entering text, or moving the window. If you have defined an event-handler callback
for the element, the notify method invokes it.
The notify method takes an optional argument that specifies which event it should simulate. If a control
can generate only one kind of event, notification generates that event by default.
The following controls generate the onClick event:
Button
Checkbox
IconButton
RadioButton

The following controls generate the onChange event:
DropDownList
EditText
ListBox
Scrollbar
Slider
TreeView

The following controls generate the onChanging event:
EditText
Scrollbar
Slider

In the ListBox, double-clicking an item generates the onDoubleClick event.
In RadioButton and Checkbox controls, the boolean value property automatically changes when the
user clicks the control. If you use notify() to simulate a click, the value changes just as if the user had
clicked. For example, if the value of a checkbox hasBtnsCb is true, this code changes the value to false:
if (dlg.hasBtnsCb.value == true) dlg.hasBtnsCb.notify();
// dlg.hasBtnsCb.value is now false

.. _registering-event-listeners-for-windows-or-controls:

Registering event listeners for windows or controls
---------------------------------------------------
Another way to define the behavior of your windows and controls is register a handler function that
responds to a specific type of event in that window or control. This technique allows you to respond to the
cascading of an event through a hierarchy of containers and controls.
Use windowObj.addEventListener() or controlObj.addEventListener() to register a handler. The function
you register receives an event object (from the UIEvent base class) that encapsulates the event
information. As an event cascades down through a hierarchy and back up through the hierarchy, your
handler can respond at any level, or use the UIEvent object’s stopPropagation() method to stop the event
propagation at some level.
You can register:
The name of a handler function defined in the extension that takes one argument, the event object.
For example:

myButton.addEventListener( ’click’, myFunction );

A locally defined handler function that takes one argument, the event object. For example:
myButton.addEventListener( ’click’, ’function(e){/*handler code*/}’);

The handler or registered code statement is executed when the specified event occurs in the target. A
script can programmatically simulate an event by creating an event objects with
ScriptUI.events.events.createEvent(), and passing it to an event target’s dispatchEvent() function.
You can remove a handler that has been previously registered by calling the event target’s
removeEventListener() function. The parameters you pass to this function must be identical to those
passed to the addEventListener() call that registered the handler. Typically, a script would register all event
handlers during initialization, and unregister them during termination; however, unregistering handlers
on termination is not required.
You can register for an event in a parent or ancestor object of the actual target; see the following section.
The predefined types of UIEvent correspond to the event callbacks, as follows:
Callback

UIEvent type

onChange

change

onChanging

changing

onClick

click (detail = 1)

onDoubleClick

click (detail = 2)

onEnterKey

enterKey

onMove

move

onMoving

moving

onResize

resize

onResizing

resizing

onShow

show

onActivate

focus

onDeactivate

blur

In addition, ScriptUI implements all types of W3C events according to the W3C DOM level 3 functional
specification (http://www.w3.org/TR/DOM-Level-3-Events/events.html), with these modifications and
exceptions:
ScriptUI does not implement the hasFeature() method of the DOMImplementation interface; there
is no way to query whether a given W3C DOM feature is implemented in ScriptUI.
In ScriptUI, the W3C EventTarget interface is implemented by UI element objects (such as Button,
Window, and so on).
In ScriptUI, the W3C AbstractView object is a UI element (such as Button, Window, and so on).
None of the "namespace" properties or methods are supported (such as initEventNS and
initMouseEventNS).

The ScriptUI implementation of W3C mouse events follows the W3C DOM level 3 functional specification
(http://www.w3.org/TR/DOM-Level-3-Events/events.html#Events-eventgroupings-mouseevents), with
these differences:
To create a MouseEvent instance, call ScriptUI.events.createEvent('MouseEvent'), rather than
DocumentEvent.createEvent('MouseEvent').
The getModifierState method of the MouseEvent interface is not supported.
The ScriptUI implementation of W3C keyboard events follows the W3C DOM level 3 functional
specification {http://www.w3.org/TR/DOM-Level-3-Events/events.html#Events-KeyboardEvent).

.. _how-registered-event-handlers-are-called:

How registered event-handlers are called
----------------------------------------
When an event occurs in a target, all handlers that have been registered for that event and target are
called. Multiple event handlers can be registered for the same event in different targets, even in targets of
the same type. For example, if there is a dialog with two checkboxes, you might want to register a click
handler for each checkbox object. You would do this, for example, if each checkbox reacts differently to
the click.
You can also register events for child objects with a parent object. If both checkboxes should react the
same way to a mouse click, they require the same handler. In this case, you can register the handler with
the parent window or container instead. When the click event occurs in either child control, the handler
registered for the parent window is called.
You can combine these two techniques, so that more than one action occurs in response to the event. That
is, you can register a general event handler with the parent, and register a different, more specific handler
for the same event with the child object that is the actual target.
The rules for how multiple event handlers are called depend on three phases of event propagation, as
follows:
Capture phase - When an event occurs in an object hierarchy, it is captured by the topmost ancestor
object at which a handler is registered (the window, for example). If no handler is registered for the
topmost ancestor, ScriptUI looks for a handler for the next ancestor (the dialog, for example), on down
through the hierarchy to the direct parent of actual target. When ScriptUI finds a handler registered for
any ancestor of the target, it executes that handler then proceeds to the next phase.
At-target phase - ScriptUI calls any handlers that are registered with the actual target object.
Bubble phase - The event bubbles back out through the hierarchy; ScriptUI again looks for handlers
registered for the event with ancestor objects, starting with the immediate parent, and working back
up the hierarchy to the topmost ancestor. When ScriptUI finds a handler, it executes it and the event
propagation is complete.
For example, suppose a dialog window contains a group which contains a button. A script registers an
event handler function for the click event at the Window object, another handler at the group object, and
a third handler at the button object (the actual target).
When the user clicks the button, the Window object’s handler is called first (during the capture phase), then
the button object’s handler (during the at-target phase). Finally, ScriptUI calls the handler registered with
the group object (during the bubble phase).
If you register a handler at an ancestor object of the actual event target, you can specify the third
argument to addEventListener(), so that the ancestor’s handler responds only in the capture phase, not in

the bubbling phase. For example, the following click handler, registered with the parent dialog object,
responds only in the capture phase:
myDialog.addEventListener("click", handleAllItems, true);

This value is false by default, so if it is not supplied, the handler can respond only in the bubbling phase
when the object’s descendent is the target, or when the object is itself the target of the event (the
at-target phase).
To distinguish which of multiple registered handlers is being executed at any given time, the event object
provides the eventPhase property, and the currentTarget property, which In the capture and bubbling
phases contains the ancestor of the target object at which the currently executing handler was
registered.

.. _communicating-with-the-flash-application:

Communicating with the Flash application
----------------------------------------
ScriptUI supports a Flash Player, which runs the Flash application within a window in an Adobe
application. The Flash application runs ActionScript, a different implementation of JavaScript from the
ExtendScript version of JavaScript that Adobe applications run.
To open a Flash Player, add a control of type flashplayer to your ScriptUI window. A control object of this
type contains functions that allow your script to load SWF files and control movie playback. It also contains
functions that allow your Adobe application script to communicate with the ActionScript environment of
the Flash application. See "FlashPlayer control functions" on page 145.
A limited set of data types can be passed between the two scripting environments:
Number
String
Boolean
Null
undefined
Object
Array

The ActionScript class and date objects are not supported as parameter values.
In the ActionScript script for your Flash application, you must prepare for two-way communication by
providing access to the External API. Do this by importing the ExternalInterface class into your Flash
application:
import flash.external.ExternalInterface;

Calling ExtendScript functions from ActionScript
The ActionScript ExternalInterface class allows you to call an ExtendScript function that has been
defined in the FlashPlayer element in the Adobe application script, and run it in the ActionScript
environment. You must define the method in your FlashPlayer element with a matching function name.
For example, in order for the SWF code to call an ExtendScript function named myExtendScriptFunction,
define a function with the name myExtendScriptFunction as a method of your FlashPlayer control
object. There are no special requirements for function names, but the function must take and return only
data of the supported types.

You do not need to register the ExtendScript function in the ActionScript environment. Your ActionScript
script can simply call the external function using the ExternalInterface.call() method:
var res = ExternalInterface.call("myJavaScriptFunction");

When the Flash Player executes the ExternalInterface call, ScriptUI looks for a function with the same
name as a method of the FlashPlayer element, and invokes it with the specified arguments. In the
context of the function, the JavaScript this object refers to the FlashPlayer object.

Calling ActionScript functions from a ScriptUI script
From the ExtendScript side, use the FlashPlayer method invokePlayerFunction() to call ActionScript
methods that have been defined within the Flash application:
result = flashElement.invokePlayerFunction ("ActionScript_function_name",
[arg1, ..., argN] );

You can use the optional arguments to pass data (of supported types) to the ActionScript method.
Before you can call any ActionScript function from your Adobe application script, your Flash application
must register that function with the ExternalInterface object, as a callback from the Flash container. To
register a function, use the ExternalInterface.addCallback() method:
public static addCallback (methodName:String, instance:Object, method:Function);

This registers a function defined in your Adobe application script named getActionScriptArray():
ExternalInterface.addCallback("getActionScriptArray", this, getActionScriptArray);

Flash Examples
These examples in the Adobe ExtendScript SDK demonstrate how to use the Flash Player:
UsingFlashPlayer.jsx

Shows how to create a Flash Player, and use it to load a play back a
movie defined in an SWF file.

ActionScriptDemo.jsx

Shows how to communicate between the Adobe application scripting
environment and the ActionScript scripting environment of the Flash
Player.

