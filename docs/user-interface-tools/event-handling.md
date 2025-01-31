<a id="event-handling"></a>

# Event handling

Several helper classes provide low-level event-handling capabilities.

- Event objects are normally created by ScriptUI and passed to your event handler. However, you can
  simulate a user action by constructing an event object using [ScriptUI.events.createEvent()](scriptui-class.md#scriptui-events-createevent),
  and sending it to a target object’s controlobj-dispatchEvent function.
- A helper object, [Keyboard state object](environment.md#environment-keyboard-state), provides global access to the keyboard state during function
  execution, outside the event-handling framework.

---

<a id="uievent-base-class"></a>

## UIEvent base class

Encapsulates input event information for an event that propagates through a container and control
hierarchy. This is a base class for the more specialized [KeyboardEvent object](#keyboardevent-object) and [MouseEvent object](#mouseevent-object).

### UIEvent object properties

Both keyboard and mouse events have these properties.

---

<a id="eventobj-bubbles"></a>

#### bubbles

Type: `Boolean`

When true, the event supports the bubbling phase.

---

<a id="eventobj-cancelable"></a>

#### cancelable

Type: `Boolean`

When true, the handler can call this object’s [preventDefault()](#eventobj-preventdefault) method to
cancel the default action of the event.

---

<a id="eventobj-currenttarget"></a>

#### currentTarget

Type: `Object`

The element object where the currently executing handler was registered.
This could be an ancestor of the target object, if the handler is invoked
during the capture or bubbling phase.

---

<a id="eventobj-eventphase"></a>

#### eventPhase

Type: `Number`

Current event propagation phase. One of these constants:

- `Event.NOT_DISPATCHING`
- `Event.CAPTURING_PHASE`
- `Event.AT_TARGET`
- `Event.BUBBLING_PHASE`

---

<a id="eventobj-target"></a>

#### target

Type: `Object`

The element object where the event occurred.

---

<a id="eventobj-timestamp"></a>

#### timeStamp

Type: `Object`

Time the event was initiated. A JavaScript Date object.

---

<a id="eventobj-type"></a>

#### type

Type: `String`

The name of the event that occurred. Predefined events types are:

| change   | changing   |
|----------|------------|
| move     | moving     |
| resize   | resizing   |
| show     | enterKey   |
| focus    | blur       |

Additional type names apply specifically to keyboard and mouse events.

---

<a id="eventobj-view"></a>

#### view

Type: `Object`

The container or control object that dispatched the event.

---

### UIEvent object functions

<a id="eventobj-inituievent"></a>

#### initUIEvent()

`eventObj.initUIEvent(eventName, bubble, isCancelable, view, detail)`

| `eventName`    | The event name string.                                                                                                                          |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| `bubble`       | When true, the event should be triggered in ancestors<br/>of the target object during the bubbling phase.                                       |
| `isCancelable` | When true, the event can be cancelled.                                                                                                          |
| `view`         | The container or control object that dispatched the event.                                                                                      |
| `detail`       | Details of the event, which vary according to the event type.<br/>The value is 1 or 2 for the click event, indicating a single or double click. |

Modifies an event before it is dispatched to its targets. Takes effect only if
[UIEvent.eventPhase](#eventobj-eventphase) is `Event.NOT_DISPATCHING`.
Ignored at all other phases.

Returns undefined.

---

<a id="eventobj-preventdefault"></a>

#### preventDefault()

`eventObj.preventDefault()`

Cancels the default action of this event, if this event is cancelable (that is, [cancelable](#eventobj-cancelable) is true). For
example, the default click action of an OK button is to close the containing dialog; this call prevents
that behavior.

Returns `undefined`.

---

<a id="eventobj-stoppropagation"></a>

#### stopPropagation()

`eventObj.stopPropagation()`

Stops event propagation (bubbling and capturing) after executing the handler or handlers at the
current target.

Returns `undefined`.

---

<a id="keyboardevent-object"></a>

## KeyboardEvent object

This type of object is passed to your registered event handler when a keyboard-input event occurs. The
properties reflect the keypress and key modifier state at the time the keyboard event was generated. All
properties are read-only.

### KeyboardEvent object properties

In addition to the properties defined for [UIEvent base class](#uievent-base-class), a keyboard event has these properties. All
properties are read-only.

---

#### altKey

Type: `Boolean`

When true, the `ALT` key was active. Value is `undefined` if the
`keyIdentifier` is for a modifier key.

---

#### ctrlKey

Type: `Boolean`

When true, the `CTRL` key was active. Value is `undefined` if the
`keyIdentifier` is for a modifier key.

---

#### metaKey

Type: `Boolean`

When true, the `META` or `COMMAND` key was active. Value is `undefined` if the
`keyIdentifier` is for a modifier key.

---

#### shiftKey

Type: `Boolean`

When true, the `SHIFT` key was active. Value is `undefined` if the
`keyIdentifier` is for a modifier key.

---

#### keyIdentifier

Type: `String`

The key whose keypress generated the event, as a W3C identifier
contained in a string; for example, `"U+0044"`. See [W3 Keyset Article](https://www.w3.org/TR/2003/WD-DOM-Level-3-Events-20030331/keyset.html).

---

#### keyLocation

Type: `Number`

A constant that identifies where on the keyboard the keypress occurred.
One of:

- `DOM_KEY_LOCATION_STANDARD`
- `DOM_KEY_LOCATION_LEFT`
- `DOM_KEY_LOCATION_RIGHT`
- `DOM_KEY_LOCATION_NUMPAD`

---

#### keyName

Type: `String`

The key whose keypress generated the event, as a simple key name; for
example `"A"`.

---

#### type

Type: `String`

The name of the event that occurred. Key events types are:

- `keyup`
- `keydown`

---

<a id="keyboardevent-object-functions"></a>

### KeyboardEvent object functions

In addition to the functions defined for [UIEvent base class](#uievent-base-class), a keyboard event has these functions.

---

<a id="keyboardevent-object-getmodifierstate"></a>

#### getModifierState()

`eventObj.getModifierState(keyIdentifier)`

| `keyIdentifier`   | A string containing a modifier key identifier, one of:<br/><br/>> - `Alt`<br/>> - `CapsLock`<br/>> - `Control`<br/>> - `Meta`<br/>> - `NumLock`<br/>> - `Scroll`<br/>> - `Shift`   |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Returns true if the given modifier was active when the event occurred, false otherwise.

#### NOTE
If you’re trying to check whether keyboard modifier keys (alt/ctrl/meta/shift) are held down at any time in your script, not just in an event, see [Keyboard state object](environment.md#environment-keyboard-state).

---

<a id="keyboardevent-object-initkeyboardevent"></a>

#### initKeyboardEvent()

`eventObj.initKeyboardEvent (eventName, bubble, isCancelable, view, keyID, keyLocation, modifiersList)`

| `eventName`     | The event name string.                                                                                    |
|-----------------|-----------------------------------------------------------------------------------------------------------|
| `bubble`        | When true, the event should be triggered in ancestors of<br/>the target object during the bubbling phase. |
| `isCancelable`  | When true, the event can be cancelled.                                                                    |
| `view`          | The container or control object that dispatched the event.                                                |
| `keyID`         | Sets the `keyIdentifier` value.                                                                           |
| `keyLocation`   | Sets the `keyLocation`. value.                                                                            |
| `modifiersList` | A whitespace-separated string of modifier key names, such as “Control Alt”.                               |

Reinitializes the object, allowing you to change the event properties after construction. Arguments
set the corresponding properties. Returns `undefined`.

---

<a id="mouseevent-object"></a>

## MouseEvent object

This type of object is passed to your registered event handler when a mouse-input event occurs. The
properties reflect the button and modifier-key state and pointer position at the time the event was
generated.
In the case of nested elements, mouse event types are always targeted at the most deeply nested element.
Ancestors of the targeted element can use bubbling to obtain notification of mouse events which occur
within its descendent elements.

### MouseEvent object properties

In addition to the properties defined for [UIEvent base class](#uievent-base-class), a mouse event has these properties. All
properties are read-only.

---

#### altKey

Type: `Boolean`

When true, the `ALT` key was active. Value is `undefined` if the
`keyIdentifier` is for a modifier key.

---

#### button

Type: `Number`

Which mouse button changed state.

| `0`   | The left button of a two- or three-button mouse or the one button<br/>on a one-button mouse, used to activate a UI button or select text.   |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------|
| `1`   | The middle button of a three-button mouse, or the mouse wheel.                                                                              |
| `2`   | The right button, used to display a context menu, if present.                                                                               |

Some mice may provide or simulate more buttons, and values higher than
2 represent such buttons.

---

#### clientX and clientY

Type: `Number`

The horizontal and vertical coordinates at which the event occurred
relative to the target object. The origin is the top left of the control or
window, inside any border decorations.

---

#### ctrlKey

Type: `Boolean`

When true, the `CTRL` key was active. Value is `undefined` if the
`keyIdentifier` is for a modifier key.

---

#### detail

Type: `Number`

Details of the event, which vary according to the event type. For the
`click`, `mousedown`, and `mouseup` events, the value is `1` for a single click, or
`2` for a double click.

---

#### metaKey

Type: `Boolean`

When true, the `META` or `COMMAND`` key was active. Value is `undefined` if the
`keyIdentifier` is for a modifier key.

---

#### relatedTarget

Type: `Object`

- For a `mouseover` event, the UI element the pointer is leaving, if any.
- For a `mouseout` event, the UI element the pointer is entering, if any.

Otherwise `undefined`.

---

#### screenX and screenY

Type: `Number`

The horizontal and vertical coordinates at which the event occurred
relative to the screen.

---

#### shiftKey

Type: `Boolean`

When true, the `SHIFT` key was active. Value is `undefined` if the
`keyIdentifier` is for a modifier key.

---

#### type

Type: `String`

The name of the event that occurred. Mouse events types are:

- `mousedown`
- `mouseup`
- `mousemove`
- `mouseover`
- `mouseout`
- `click (detail = 1 for single, 2 for double)`

The sequence of click events is: `mousedown`, `mouseup`, `click`.

---

<a id="mouseevent-object-functions"></a>

### MouseEvent object functions

In addition to the functions defined for [UIEvent base class](#uievent-base-class), a mouse event has these functions.

---

<a id="mouseevent-object-getmodifierstate"></a>

#### getModifierState()

`eventObj.getModifierState(keyIdentifier)`

| `keyIdentifier`   | A string containing a modifier key identifier, one of:<br/><br/>> - `Alt`<br/>> - `CapsLock`<br/>> - `Control`<br/>> - `Meta`<br/>> - `NumLock`<br/>> - `Scroll`<br/>> - `Shift`   |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Returns true if the given modifier was active when the event occurred, false otherwise.

---

<a id="mouseevent-object-initmouseevent"></a>

#### initMouseEvent()

> ```default
> eventObj.initMouseEvent(
>     eventName,
>     bubble,
>     isCancelable,
>     view,
>     detail,
>     screenX,
>     screenY,
>     clientX,
>     clientY,
>     ctrlKey,
>     altKey,
>     shiftKey,
>     metaKey,
>     button,
>     relatedTarge
> )
> ```

| `eventName`                | The event name string.                                                                                                                            |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| `bubble`                   | When true, the event should be triggered in ancestors of<br/>the target object during the bubbling phase.                                         |
| `isCancelable`             | When true, the event can be cancelled.                                                                                                            |
| `view`                     | The container or control object that dispatched the event.                                                                                        |
| `detail`                   | Sets the single-double click value for the `click` event.                                                                                         |
| `screenX, screenY`         | Sets the event coordinates relative to the screen.                                                                                                |
| `clientX, clientY`         | Sets the event coordinates relative to the target object.<br/>The origin is the top left of the control or window, inside any border decorations. |
| `ctrlKey, altKey, metaKey` | Sets the modifier key states.                                                                                                                     |
| `button`                   | Sets the mouse button.                                                                                                                            |
| `relatedTarget`            | Optional. Sets the related target, if any, for a `mouseover` or `mouseout` event.                                                                 |

Reinitializes the object, allowing you to change the event properties after construction. Arguments
set the corresponding properties.

Returns `undefined`.
