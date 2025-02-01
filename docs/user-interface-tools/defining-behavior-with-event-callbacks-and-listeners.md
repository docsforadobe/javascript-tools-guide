# Defining behavior with event callbacks and listeners

You must define the behavior of your controls in order for them to respond to user interaction. You can do
this by defining event-handling callback functions as part of the definition of the control or window. To
respond to a specific event, define a handler function for it, and assign a reference to that function in the
corresponding property of the window or control object. Different types of windows and controls respond
to different actions, or events:

- Windows generate events when the user moves or resizes the window. To handle these events, define
  callback functions for `onMove`, `onMoving`, `onResize`, `onResizing`.
  To respond to the user opening or closing the window, define callback functions for
  `onShow` and `onClose`.
- Button, RadioButton, and Checkbox controls generate events when the user clicks within the control
  bounds. To handle the event, define a callback function for [onClick](control-objects.md#control-event-onclick).
- EditNumber, EditText, Scrollbar, and Slider controls generate events when the content or value changes-that
  is, when the user types into an edit field, or moves the scroll or slider indicator. To handle these events,
  define callback functions for [onChange](control-objects.md#control-event-onchange) and [onChanging](control-objects.md#control-event-onchanging).
- ListBox, DropDownList, and TreeView controls generate events whenever the selection in the list
  changes. To handle the event, define a callback function for [onChange](control-objects.md#control-event-onchange).
  The TreeView control also generates events when the user expands or collapses a node,
  handled by the [onExpand](control-objects.md#control-event-onexpand) and [onCollapse](control-objects.md#control-event-oncollapse) callback functions.
- The ListBox also generates an event when the user double-clicks an item. To handle it, define a
  callback function for the [onDoubleClick](control-objects.md#control-event-ondoubleclick) event.
- Both containers and controls generate events just before they are drawn, that allow you to customize
  their appearance. To handle these events, define callback functions for [onDraw](control-objects.md#control-event-ondraw).
  Your handler can modify or control how the container or control is drawn using the methods
  defined in the control’s associated [ScriptUIGraphics object](graphic-customization-objects.md#scriptuigraphics-object).
- In Windows only, you can register a key sequence as a [shortcutKey](control-objects.md#controlobj-shortcutkey) for a window or
  for most types of controls. To handle the key sequence, define a callback function for
  [onShortcutKey](control-objects.md#control-event-onshortcutkey) in that control.

---

## Defining event-handler callback functions

Your script can define an event handler as a named function referenced by the callback property, or as an
unnamed function defined inline in the callback property.

- If you define a named function, assign its name as the value of the corresponding callback property.
  For example:
  ```default
  function hasBtnsCbOnClick() { /* do something interesting */ }
  hasBtnsCb.onClick = hasBtnsCbOnClick;
  ```
- For a simple, unnamed function, set the property value directly to the function definition:
  ```default
  UI-element.callback-name = function () { handler-definition };
  ```

Event-handler functions take no arguments.

For example, the following sets the onClick property of the hasBtnsCb checkbox to a function that
enables another control in the same dialog:

```default
hasBtnsCb.onClick = function () {
  this.parent.alertBtnsPnl.enabled = this.value;
};
```

The following statements set the `onClick` event handlers for buttons that close the containing dialog,
returning different values to the `show` method that invoked the dialog, so the calling script can tell which
button was clicked:

```default
buildBtn.onClick = function() {
  this.parent.parent.close( 1 );
};
cancelBtn.onClick = function() {
  this.parent.parent.close( 2 );
};
```

---

## Simulating user events

You can simulate user actions by sending an event notification directly to a window or control with the
notify method. A script can use this method to generate events in the controls of a window, as if a user
was clicking buttons, entering text, or moving the window. If you have defined an event-handler callback
for the element, the `notify` method invokes it.

The notify method takes an optional argument that specifies which event it should simulate. If a control
can generate only one kind of event, notification generates that event by default.

The following controls generate the `onClick` event:

- `Button`
- `Checkbox`
- `IconButton`
- `RadioButton`

The following controls generate the `onChange` event:

- `DropDownList`
- `EditNumber`
- `EditText`
- `ListBox`
- `Scrollbar`
- `Slider`
- `TreeView`

The following controls generate the `onChanging` event:

- `EditNumber`
- `EditText`
- `Scrollbar`
- `Slider`

In the ListBox, double-clicking an item generates the `onDoubleClick` event.

In RadioButton and Checkbox controls, the boolean value property automatically changes when the
user clicks the control. If you use `notify()` to simulate a click, the value changes just as if the user had
clicked. For example, if the value of a checkbox `hasBtnsCb` is true, this code changes the value to false:

```default
if ( dlg.hasBtnsCb.value == true ) {
  dlg.hasBtnsCb.notify(); // dlg.hasBtnsCb.value is now false
}
```

---

## Registering event listeners for windows or controls

Another way to define the behavior of your windows and controls is register a handler function that
responds to a specific type of event in that window or control. This technique allows you to respond to the
cascading of an event through a hierarchy of containers and controls.

Use [addEventListener()](window-object.md#window-object-functions-addeventlistener) or [addEventListener()](control-objects.md#controlobj-addeventlistener)
to register a handler. The function you register receives an event object (from the [UIEvent base class](event-handling.md#uievent-base-class))
that encapsulates the event information. As an event cascades down through a hierarchy and back up
through the hierarchy, your handler can respond at any level, or use the UIEvent object’s
[stopPropagation()](event-handling.md#eventobj-stoppropagation) method to stop the event propagation at some level.

You can register:

- The name of a handler function defined in the extension that takes one argument, the event object.
  For example:
  ```default
  myButton.addEventListener( "click", myFunction );
  ```

- A locally defined handler function that takes one argument, the event object. For example:
  ```default
  myButton.addEventListener( "click", "function( e ) { /*handler code*/ }" );
  ```

The handler or registered code statement is executed when the specified event occurs in the target. A
script can programmatically simulate an event by creating an event objects with
[ScriptUI.events.createEvent()](scriptui-class.md#scriptui-events-createevent), and passing it to an event target’s
[dispatchEvent()](control-objects.md#controlobj-dispatchevent) function.

You can remove a handler that has been previously registered by calling the event target’s
[removeEventListener()](control-objects.md#controlobj-removeeventlistener) function. The parameters you pass to this function must be identical to those
passed to the [addEventListener()](control-objects.md#controlobj-addeventlistener) call that registered the handler. Typically, a script would register all event
handlers during initialization, and unregister them during termination; however, unregistering handlers
on termination is not required.

You can register for an event in a parent or ancestor object of the actual target; see the following section.

The predefined types of `UIEvent` correspond to the event callbacks, as follows:

| Callback      | UIEvent type       |
|---------------|--------------------|
| onChange      | change             |
| onChanging    | changing           |
| onClick       | click (detail = 1) |
| onDoubleClick | click (detail = 2) |
| onEnterKey    | enterKey           |
| onMove        | move               |
| onMoving      | moving             |
| onResize      | resize             |
| onResizing    | resizing           |
| onShow        | show               |
| onActivate    | focus              |
| onDeactivate  | blur               |

In addition, ScriptUI implements all types of W3C events according to the W3C DOM level 3 functional
specification [for UI events](https://www.w3.org/TR/uievents/), with these modifications and
exceptions:

- ScriptUI does not implement the `hasFeature()` method of the `DOMImplementation` interface; there
  is no way to query whether a given W3C DOM feature is implemented in ScriptUI.
- In ScriptUI, the W3C `EventTarget` interface is implemented by UI element objects (such as `Button`,
  `Window`, and so on).
- In ScriptUI, the W3C `AbstractView` object is a UI element (such as `Button`, `Window`, and so on).
- None of the “namespace” properties or methods are supported (such as `initEventNS` and
  `initMouseEventNS`).

The ScriptUI implementation of W3C mouse events follows the W3C DOM level 3 functional specification [for MouseEvent](https://www.w3.org/TR/uievents/#mouseevent), with
these differences:

- To create a `MouseEvent` instance, call `ScriptUI.events.createEvent( "MouseEvent" )`, rather than
  `DocumentEvent.createEvent( "MouseEvent" )`.
- The `getModifierState` method of the `MouseEvent` interface is not supported.

The ScriptUI implementation of W3C keyboard events follows the W3C DOM level 3 functional
specification [for KeyboardEvent](https://www.w3.org/TR/uievents/#keyboardevent).

---

## How registered event-handlers are called

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

- **Capture phase** - When an event occurs in an object hierarchy, it is captured by the topmost ancestor
  object at which a handler is registered (the window, for example). If no handler is registered for the
  topmost ancestor, ScriptUI looks for a handler for the next ancestor (the dialog, for example), on down
  through the hierarchy to the direct parent of actual target. When ScriptUI finds a handler registered for
  any ancestor of the target, it executes that handler then proceeds to the next phase.
- **At-target phase** - ScriptUI calls any handlers that are registered with the actual target object.
- **Bubble phase** - The event bubbles back out through the hierarchy; ScriptUI again looks for handlers
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
argument to [addEventListener()](control-objects.md#controlobj-addeventlistener), so that the ancestor’s handler responds only in the
capture phase, not in the bubbling phase. For example, the following click handler, registered with the
parent dialog object, responds only in the capture phase:

```default
myDialog.addEventListener( "click", handleAllItems, true );
```

This value is false by default, so if it is not supplied, the handler can respond only in the bubbling phase
when the object’s descendent is the target, or when the object is itself the target of the event (the
at-target phase).

To distinguish which of multiple registered handlers is being executed at any given time, the event object
provides the [eventPhase](event-handling.md#eventobj-eventphase), and the [currentTarget](event-handling.md#eventobj-currenttarget), which In the capture and bubbling
phases contains the ancestor of the target object at which the currently executing handler was
registered.
