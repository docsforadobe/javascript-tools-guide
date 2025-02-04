# Event handling

Several helper classes provide low-level event-handling capabilities.

Event objects are normally created by ScriptUI and passed to your event handler. However, you can simulate a user action by constructing an event object using [ScriptUI.events.createEvent()](scriptui-class.md#scriptuieventscreateevent), and sending it to a target object's controlobj-dispatchEvent function.

A helper object, [Keyboard state object](environment.md#keyboard-state-object), provides global access to the keyboard state during function execution, outside the event-handling framework.

---

## UIEvent Base Class

Encapsulates input event information for an event that propagates through a container and control hierarchy. This is a base class for the more specialized [KeyboardEvent object](#keyboardevent-object) and [MouseEvent object](#mouseevent-object).

---

### UIEvent Object Attributes

Both keyboard and mouse events have these properties.

#### bubbles

`eventObj.bubbles`

##### Description

When `true`, the event supports the bubbling phase.

##### Type

Boolean

---

#### cancelable

`eventObj.cancelable`

##### Description

When `true`, the handler can call this object's [preventDefault()](#preventdefault) method to cancel the default action of the event.

##### Type

Boolean

---

#### currentTarget

`eventObj.currentTarget`

##### Description

The element object where the currently executing handler was registered.

This could be an ancestor of the target object, if the handler is invoked during the capture or bubbling phase.

##### Type

Object

---

#### eventPhase

`eventObj.eventPhase`

##### Description

Current event propagation phase. One of these constants:

- `Event.NOT_DISPATCHING`
- `Event.CAPTURING_PHASE`
- `Event.AT_TARGET`
- `Event.BUBBLING_PHASE`

##### Type

Number

---

#### target

`eventObj.target`

##### Description

The element object where the event occurred.

##### Type

Object


---

#### timeStamp

`eventObj.timeStamp`

##### Description

Time the event was initiated. A JavaScript Date object.

##### Type

Object

---

#### type

`eventObj.type`

##### Description

The name of the event that occurred. Predefined events types are:

- `"blur"`
- `"change"`
- `"changing"`
- `"enterKey"`
- `"focus"`
- `"move"`
- `"moving"`
- `"resize"`
- `"resizing"`
- `"show"`

Additional type names apply specifically to keyboard and mouse events.

##### Type

String

---

#### view

`eventObj.view`

##### Description

The container or control object that dispatched the event.

##### Type

[Container](./window-object.md) or [Control](./control-objects.md) object

---

### UIEvent Object Methods

#### initUIEvent()

`eventObj.initUIEvent(eventName, bubble, isCancelable, view, detail)`

##### Description

Modifies an event before it is dispatched to its targets. Takes effect only if [UIEvent.eventPhase](#eventphase) is `Event.NOT_DISPATCHING`.

Ignored at all other phases.

##### Parameters

|   Parameter    |                                   Type                                    |                                                                   Description                                                                   |
| -------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `eventName`    | String                                                                    | The event name string.                                                                                                                          |
| `bubble`       | Boolean                                                                   | When `true`, the event should be triggered in ancestors of the target object during the bubbling phase.                                         |
| `isCancelable` | Boolean                                                                   | When `true`, the event can be cancelled.                                                                                                        |
| `view`         | [Container](./window-object.md) or [Control](./control-objects.md) object | The container or control object that dispatched the event.                                                                                      |
| `detail`       | Any                                                                       | Details of the event, which vary according to the event type. The value is `1` or `2` for the click event, indicating a single or double click. |

##### Returns

Nothing

---

#### preventDefault()

`eventObj.preventDefault()`

##### Description

Cancels the default action of this event, if this event is cancelable (that is, [cancelable](#cancelable) is true).

For example, the default click action of an OK button is to close the containing dialog; this call prevents that behavior.

##### Returns

Nothing

---

#### stopPropagation()

`eventObj.stopPropagation()`

##### Description

Stops event propagation (bubbling and capturing) after executing the handler or handlers at the current target.

##### Returns

Nothing

---

## KeyboardEvent Object

This type of object is passed to your registered event handler when a keyboard-input event occurs. The properties reflect the keypress and key modifier state at the time the keyboard event was generated.

!!! info
    All properties are read only.

### KeyboardEvent Object Methods

In addition to the properties defined for [UIEvent base class](#uievent-base-class), a keyboard event has these properties.

#### altKey

`eventObj.altKey`

##### Description

When `true`, the `ALT` key was active.

Value is `undefined` if the `keyIdentifier` is for a modifier key.

##### Type

Boolean

---

#### ctrlKey

`eventObj.ctrlKey`

##### Description

When `true`, the `CTRL` key was active.

Value is `undefined` if the `keyIdentifier` is for a modifier key.

##### Type

Boolean

---

#### metaKey

`eventObj.metaKey`

##### Description

When `true`, the `META` or `COMMAND` key was active.

Value is `undefined` if the `keyIdentifier` is for a modifier key.

##### Type

Boolean

---

#### shiftKey

`eventObj.shiftKey`

##### Description

When `true`, the `SHIFT` key was active.

Value is `undefined` if the `keyIdentifier` is for a modifier key.

##### Type

Boolean

---

#### keyIdentifier

`eventObj.keyIdentifier`

##### Description

The key whose keypress generated the event, as a W3C identifier contained in a string; for example, `"U+0044"`. See [W3 Keyset Article](https://www.w3.org/TR/2003/WD-DOM-Level-3-Events-20030331/keyset.html).

##### Type

String

---

#### keyLocation

`eventObj.keyLocation`

##### Description

A constant that identifies where on the keyboard the keypress occurred.

One of:

- `DOM_KEY_LOCATION_STANDARD`
- `DOM_KEY_LOCATION_LEFT`
- `DOM_KEY_LOCATION_RIGHT`
- `DOM_KEY_LOCATION_NUMPAD`

##### Type

Number

---

#### keyName

`eventObj.keyName`

##### Description

The key whose keypress generated the event, as a simple key name; for example `"A"`.

##### Type

String

---

#### type

`eventObj.type`

##### Description

The name of the event that occurred. Key events types are:

- `keyup`
- `keydown`

##### Type

String

---

### KeyboardEvent Object Methods

In addition to the functions defined for [UIEvent base class](#uievent-base-class), a keyboard event has these functions.

#### getModifierState()

`eventObj.getModifierState(keyIdentifier)`

##### Description

Get the current modifier keys being used in this event.

!!! note
    If you're trying to check whether keyboard modifier keys (alt/ctrl/meta/shift) are held down at any time in your script, not just in an event, see [Keyboard state object](environment.md#keyboard-state-object).

##### Parameters

+-----------------+--------+--------------------------------------------------------+
|    Parameter    |  Type  |                      Description                       |
+=================+========+========================================================+
| `keyIdentifier` | String | A string containing a modifier key identifier, one of: |
|                 |        | - `Alt`                                                |
|                 |        | - `CapsLock`                                           |
|                 |        | - `Control`                                            |
|                 |        | - `Meta`                                               |
|                 |        | - `NumLock`                                            |
|                 |        | - `Scroll`                                             |
|                 |        | - `Shift`                                              |
+-----------------+--------+--------------------------------------------------------+

##### Returns

Boolean. `true` if the given modifier was active when the event occurred, `false` otherwise.

---

#### initKeyboardEvent()

`eventObj.initKeyboardEvent(eventName, bubble, isCancelable, view, keyID, keyLocation, modifiersList)`

##### Description

Reinitializes the object, allowing you to change the event properties after construction. Arguments set the corresponding properties.

##### Parameters

|    Parameter    |                                   Type                                    |                                               Description                                               |
| --------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `eventName`     | String                                                                    | The event name string.                                                                                  |
| `bubble`        | Boolean                                                                   | When `true`, the event should be triggered in ancestors of the target object during the bubbling phase. |
| `isCancelable`  | Boolean                                                                   | When `true`, the event can be cancelled.                                                                |
| `view`          | [Container](./window-object.md) or [Control](./control-objects.md) object | The container or control object that dispatched the event.                                              |
| `keyID`         | String                                                                    | Sets the `keyIdentifier` value.                                                                         |
| `keyLocation`   | String                                                                    | Sets the `keyLocation`. value.                                                                          |
| `modifiersList` | String                                                                    | A whitespace-separated string of modifier key names, such as "Control Alt".                             |

##### Returns

Nothing

---

## MouseEvent Object

This type of object is passed to your registered event handler when a mouse-input event occurs. The properties reflect the button and modifier-key state and pointer position at the time the event was generated.

In the case of nested elements, mouse event types are always targeted at the most deeply nested element. Ancestors of the targeted element can use bubbling to obtain notification of mouse events which occur within its descendent elements.

### MouseEvent Object Attributes

In addition to the properties defined for [UIEvent base class](#uievent-base-class), a mouse event has these properties.

!!! info
    All properties are read only.

---

#### altKey

`eventObj.altKey`

##### Description

When `true`, the `ALT` key was active.

Value is `undefined` if the `keyIdentifier` is for a modifier key.

##### Type

Boolean

---

#### button

`eventObj.button`

##### Description

Which mouse button changed state.

One of:

- `0`: The left button of a two- or three-button mouse or the one button on a one-button mouse, used to activate a UI button or select text.
- `1`: The middle button of a three-button mouse, or the mouse wheel.
- `2`: The right button, used to display a context menu, if present.

Some mice may provide or simulate more buttons, and values higher than `2` represent such buttons.

##### Type

Number

---

#### clientX and clientY

`eventObj.clientX`

`eventObj.clientY`

##### Description

The horizontal and vertical coordinates at which the event occurred relative to the target object. The origin is the top left of the control or window, inside any border decorations.

##### Type

Number

---

#### ctrlKey

`eventObj.ctrlKey`

##### Description

When `true`, the `CTRL` key was active.

Value is `undefined` if the `keyIdentifier` is for a modifier key.

##### Type

Boolean

---

#### detail

`eventObj.detail`

##### Description

Details of the event, which vary according to the event type.

For the `click`, `mousedown`, and `mouseup` events, the value is `1` for a single click, or `2` for a double click.

##### Type

Number

---

#### metaKey

`eventObj.metaKey`

##### Description

When `true`, the `META` or `COMMAND` key was active.

Value is `undefined` if the `keyIdentifier` is for a modifier key.

##### Type

Boolean

---

#### relatedTarget

`eventObj.relatedTarget`

##### Description

- For a `mouseover` event, the UI element the pointer is leaving, if any.
- For a `mouseout` event, the UI element the pointer is entering, if any.

Otherwise `undefined`.

##### Type

Object

---

#### screenX and screenY

`eventObj.screenX`

`eventObj.screenY`

##### Description

The horizontal and vertical coordinates at which the event occurred relative to the screen.

##### Type

Number

---

#### shiftKey

`eventObj.shiftKey`

##### Description

When `true`, the `SHIFT` key was active.

Value is `undefined` if the `keyIdentifier` is for a modifier key.

##### Type

Boolean

---

#### type

`eventObj.type`

##### Description

The name of the event that occurred. Mouse events types are:

- `"mousedown"`
- `"mouseup"`
- `"mousemove"`
- `"mouseover"`
- `"mouseout"`
- `"click"` (detail = 1 for single, 2 for double)

The sequence of click events is: `mousedown`, `mouseup`, `click`.

##### Type

String

---

### MouseEvent Object Methods

In addition to the functions defined for [UIEvent base class](#uievent-base-class), a mouse event has these functions.

---

#### getModifierState()

`eventObj.getModifierState(keyIdentifier)`

##### Description

Get the current modifier keys being used in this event.

#### Parameters

+-----------------+--------+--------------------------------------------------------+
|    Parameter    |  Type  |                      Description                       |
+=================+========+========================================================+
| `keyIdentifier` | String | A string containing a modifier key identifier, one of: |
|                 |        |                                                        |
|                 |        | - `"Alt"`                                              |
|                 |        | - `"CapsLock"`                                         |
|                 |        | - `"Control"`                                          |
|                 |        | - `"Meta"`                                             |
|                 |        | - `"NumLock"`                                          |
|                 |        | - `"Scroll"`                                           |
|                 |        | - `"Shift"`                                            |
+-----------------+--------+--------------------------------------------------------+

##### Returns

Boolean. `true` if the given modifier was active when the event occurred, `false` otherwise.

---

#### initMouseEvent()

```javascript
eventObj.initMouseEvent(
    eventName,
    bubble,
    isCancelable,
    view,
    detail,
    screenX,
    screenY,
    clientX,
    clientY,
    ctrlKey,
    altKey,
    shiftKey,
    metaKey,
    button,
    relatedTarge
)
```

##### Description

Reinitializes the object, allowing you to change the event properties after construction. Arguments set the corresponding properties.

##### Parameters

|         Parameter          |                                   Type                                    |                                                                  Description                                                                  |
| -------------------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `eventName`                | String                                                                    | The event name string.                                                                                                                        |
| `bubble`                   | Boolean                                                                   | When `true`, the event should be triggered in ancestors of the target object during the bubbling phase.                                       |
| `isCancelable`             | Boolean                                                                   | When `true`, the event can be cancelled.                                                                                                      |
| `view`                     | [Container](./window-object.md) or [Control](./control-objects.md) object | The container or control object that dispatched the event.                                                                                    |
| `detail`                   | Number                                                                    | Sets the single-double click value for the `click` event.                                                                                     |
| `screenX, screenY`         | Number                                                                    | Sets the event coordinates relative to the screen.                                                                                            |
| `clientX, clientY`         | Number                                                                    | Sets the event coordinates relative to the target object. The origin is the top left of the control or window, inside any border decorations. |
| `ctrlKey, altKey, metaKey` | Boolean                                                                   | Sets the modifier key states.                                                                                                                 |
| `button`                   | Number                                                                    | Sets the mouse button.                                                                                                                        |
| `relatedTarget`            | Object                                                                    | Optional. Sets the related target, if any, for a `mouseover` or `mouseout` event.                                                             |

##### Returns

Nothing
