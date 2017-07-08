.. _event-handling:

Event handling
==============
Several helper classes provide low-level event-handling capabilities.

- Event objects are normally created by ScriptUI and passed to your event handler. However, you can
  simulate a user action by constructing an event object using :ref:`ScriptUI-events-createEvent`,
  and sending it to a target object's `controlobj-dispatchEvent` function.
- A helper object, :ref:`Keyboard-state-object`, provides global access to the keyboard state during function
  execution, outside the event-handling framework.

--------------------------------------------------------------------------------

.. _uievent-base-class:

UIEvent base class
------------------
Encapsulates input event information for an event that propagates through a container and control
hierarchy. This is a base class for the more specialized :ref:`KeyboardEvent-object` and :ref:`MouseEvent-object`.

UIEvent object properties
*************************
Both keyboard and mouse events have these properties.

--------------------------------------------------------------------------------

.. _eventobj-bubbles:

bubbles
+++++++
Type: ``Boolean``

When true, the event supports the bubbling phase.

--------------------------------------------------------------------------------

.. _eventobj-cancelable:

cancelable
++++++++++
Type: ``Boolean``

When true, the handler can call this object's :ref:`eventobj-preventDefault` method to
cancel the default action of the event.

--------------------------------------------------------------------------------

.. _eventobj-currentTarget:

currentTarget
+++++++++++++
Type: ``Object``

The element object where the currently executing handler was registered.
This could be an ancestor of the target object, if the handler is invoked
during the capture or bubbling phase.

--------------------------------------------------------------------------------

.. _eventobj-eventPhase:

eventPhase
++++++++++
Type: ``Number``

Current event propagation phase. One of these constants:

- ``Event.NOT_DISPATCHING``
- ``Event.CAPTURING_PHASE``
- ``Event.AT_TARGET``
- ``Event.BUBBLING_PHASE``

--------------------------------------------------------------------------------

.. _eventobj-target:

target
++++++
Type: ``Object``

The element object where the event occurred.

--------------------------------------------------------------------------------

.. _eventobj-timeStamp:

timeStamp
+++++++++
Type: ``Object``

Time the event was initiated. A JavaScript Date object.

--------------------------------------------------------------------------------

.. _eventobj-type:

type
++++
Type: ``String``

The name of the event that occurred. Predefined events types are:

======= ========
change  changing
move    moving
resize  resizing
show    enterKey
focus   blur
======= ========

Additional type names apply specifically to keyboard and mouse events.

--------------------------------------------------------------------------------

.. _eventobj-view:

view
++++
Type: ``Object``

The container or control object that dispatched the event.

--------------------------------------------------------------------------------

UIEvent object functions
************************

.. _eventobj-initUIEvent:

initUIEvent()
+++++++++++++
``eventObj.initUIEvent(eventName, bubble, isCancelable, view, detail)``

================  ==============================================================
``eventName``     The event name string.
``bubble``        When true, the event should be triggered in ancestors
                  of the target object during the bubbling phase.
``isCancelable``  When true, the event can be cancelled.
``view``          The container or control object that dispatched the event.
``detail``        Details of the event, which vary according to the event type.
                  The value is 1 or 2 for the click event, indicating a single or double click.
================  ==============================================================

Modifies an event before it is dispatched to its targets. Takes effect only if
:ref:`UIEvent.eventPhase <eventobj-eventPhase>` is ``Event.NOT_DISPATCHING``.
Ignored at all other phases.

Returns undefined.

--------------------------------------------------------------------------------

.. _eventobj-preventDefault:

preventDefault()
++++++++++++++++
``eventObj.preventDefault()``

Cancels the default action of this event, if this event is cancelable (that is, :ref:`eventobj-cancelable` is true). For
example, the default click action of an OK button is to close the containing dialog; this call prevents
that behavior.

Returns ``undefined``.

--------------------------------------------------------------------------------

.. _eventobj-stopPropagation:

stopPropagation()
+++++++++++++++++
``eventObj.stopPropagation()``

Stops event propagation (bubbling and capturing) after executing the handler or handlers at the
current target.

Returns ``undefined``.

--------------------------------------------------------------------------------

.. _keyboardevent-object:

KeyboardEvent object
--------------------
This type of object is passed to your registered event handler when a keyboard-input event occurs. The
properties reflect the keypress and key modifier state at the time the keyboard event was generated. All
properties are read-only.

KeyboardEvent object properties
*******************************
In addition to the properties defined for :ref:`UIEvent-base-class`, a keyboard event has these properties. All
properties are read-only.

--------------------------------------------------------------------------------

altKey
++++++
Type: ``Boolean``

When true, the ``ALT`` key was active. Value is ``undefined`` if the
``keyIdentifier`` is for a modifier key.

--------------------------------------------------------------------------------

ctrlKey
+++++++
Type: ``Boolean``

When true, the ``CTRL`` key was active. Value is ``undefined`` if the
``keyIdentifier`` is for a modifier key.

--------------------------------------------------------------------------------

metaKey
+++++++
Type: ``Boolean``

When true, the ``META`` or ``COMMAND`` key was active. Value is ``undefined`` if the
``keyIdentifier`` is for a modifier key.

--------------------------------------------------------------------------------

shiftKey
++++++++
Type: ``Boolean``

When true, the ``SHIFT`` key was active. Value is ``undefined`` if the
``keyIdentifier`` is for a modifier key.

--------------------------------------------------------------------------------

keyIdentifier
+++++++++++++
Type: ``String``

The key whose keypress generated the event, as a W3C identifier
contained in a string; for example, ``"U+0044"``. See
http://www.w3.org/TR/DOM-Level-3-Events/keyset.html#KeySet-Set.

.. todo:: fix link

--------------------------------------------------------------------------------

keyLocation
+++++++++++
Type: ``Number``

A constant that identifies where on the keyboard the keypress occurred.
One of:

- ``DOM_KEY_LOCATION_STANDARD``
- ``DOM_KEY_LOCATION_LEFT``
- ``DOM_KEY_LOCATION_RIGHT``
- ``DOM_KEY_LOCATION_NUMPAD``

--------------------------------------------------------------------------------

keyName
+++++++
Type: ``String``

The key whose keypress generated the event, as a simple key name; for
example ``"A"``.

--------------------------------------------------------------------------------

type
++++
Type: ``String``

The name of the event that occurred. Key events types are:

- ``keyup``
- ``keydown``

--------------------------------------------------------------------------------

.. _keyboardevent-object-functions:

KeyboardEvent object functions
******************************
In addition to the functions defined for :ref:`UIEvent-base-class`, a keyboard event has these functions.

--------------------------------------------------------------------------------

.. _keyboardevent-object-getModifierState:

getModifierState()
++++++++++++++++++
``eventObj.getModifierState(keyIdentifier)``

=================  ======================================================
``keyIdentifier``  A string containing a modifier key identifier, one of:

                     - ``Alt``
                     - ``CapsLock``
                     - ``Control``
                     - ``Meta``
                     - ``NumLock``
                     - ``Scroll``
                     - ``Shift``

=================  ======================================================

Returns true if the given modifier was active when the event occurred, false otherwise.

--------------------------------------------------------------------------------

.. _keyboardevent-object-initKeyboardEvent:

initKeyboardEvent()
+++++++++++++++++++
``eventObj.initKeyboardEvent (eventName, bubble, isCancelable, view, keyID, keyLocation, modifiersList)``

=================  ===========================================================================
``eventName``      The event name string.
``bubble``         When true, the event should be triggered in ancestors of
                   the target object during the bubbling phase.
``isCancelable``   When true, the event can be cancelled.
``view``           The container or control object that dispatched the event.
``keyID``          Sets the ``keyIdentifier`` value.
``keyLocation``    Sets the ``keyLocation``. value.
``modifiersList``  A whitespace-separated string of modifier key names, such as "Control Alt".
=================  ===========================================================================

Reinitializes the object, allowing you to change the event properties after construction. Arguments
set the corresponding properties. Returns ``undefined``.

--------------------------------------------------------------------------------

.. _mouseevent-object:

MouseEvent object
-----------------
This type of object is passed to your registered event handler when a mouse-input event occurs. The
properties reflect the button and modifier-key state and pointer position at the time the event was
generated.
In the case of nested elements, mouse event types are always targeted at the most deeply nested element.
Ancestors of the targeted element can use bubbling to obtain notification of mouse events which occur
within its descendent elements.

MouseEvent object properties
****************************
In addition to the properties defined for :ref:`UIEvent-base-class`, a mouse event has these properties. All
properties are read-only.

--------------------------------------------------------------------------------

altKey
++++++
Type: ``Boolean``

When true, the ``ALT`` key was active. Value is ``undefined`` if the
``keyIdentifier`` is for a modifier key.

--------------------------------------------------------------------------------

button
++++++
Type: ``Number``

Which mouse button changed state.

=====  ===================================================================
``0``  The left button of a two- or three-button mouse or the one button
       on a one-button mouse, used to activate a UI button or select text.
``1``  The middle button of a three-button mouse, or the mouse wheel.
``2``  The right button, used to display a context menu, if present.
=====  ===================================================================

Some mice may provide or simulate more buttons, and values higher than
2 represent such buttons.

--------------------------------------------------------------------------------

clientX and clientY
+++++++++++++++++++
Type: ``Number``

The horizontal and vertical coordinates at which the event occurred
relative to the target object. The origin is the top left of the control or
window, inside any border decorations.

--------------------------------------------------------------------------------

ctrlKey
+++++++
Type: ``Boolean``

When true, the ``CTRL`` key was active. Value is ``undefined`` if the
``keyIdentifier`` is for a modifier key.

--------------------------------------------------------------------------------

detail
++++++
Type: ``Number``

Details of the event, which vary according to the event type. For the
``click``, ``mousedown``, and ``mouseup`` events, the value is ``1`` for a single click, or
``2`` for a double click.

--------------------------------------------------------------------------------

metaKey
+++++++
Type: ``Boolean``

When true, the ``META`` or ``COMMAND``` key was active. Value is ``undefined`` if the
``keyIdentifier`` is for a modifier key.

--------------------------------------------------------------------------------

relatedTarget
+++++++++++++
Type: ``Object``

- For a ``mouseover`` event, the UI element the pointer is leaving, if any.
- For a ``mouseout`` event, the UI element the pointer is entering, if any.

Otherwise ``undefined``.

--------------------------------------------------------------------------------

screenX and screenY
+++++++++++++++++++
Type: ``Number``

The horizontal and vertical coordinates at which the event occurred
relative to the screen.

--------------------------------------------------------------------------------

shiftKey
++++++++
Type: ``Boolean``

When true, the ``SHIFT`` key was active. Value is ``undefined`` if the
``keyIdentifier`` is for a modifier key.

--------------------------------------------------------------------------------

type
++++
Type: ``String``

The name of the event that occurred. Mouse events types are:

- ``mousedown``
- ``mouseup``
- ``mousemove``
- ``mouseover``
- ``mouseout``
- ``click (detail = 1 for single, 2 for double)``

The sequence of click events is: ``mousedown``, ``mouseup``, ``click``.

--------------------------------------------------------------------------------

.. _mouseevent-object-functions:

MouseEvent object functions
***************************
In addition to the functions defined for :ref:`UIEvent-base-class`, a mouse event has these functions.

--------------------------------------------------------------------------------

.. _mouseevent-object-getModifierState:

getModifierState()
++++++++++++++++++
``eventObj.getModifierState(keyIdentifier)``

=================  ======================================================
``keyIdentifier``  A string containing a modifier key identifier, one of:

                     - ``Alt``
                     - ``CapsLock``
                     - ``Control``
                     - ``Meta``
                     - ``NumLock``
                     - ``Scroll``
                     - ``Shift``

=================  ======================================================

Returns true if the given modifier was active when the event occurred, false otherwise.

--------------------------------------------------------------------------------

.. _mouseevent-object-initMouseEvent:

initMouseEvent()
++++++++++++++++

  ::

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

============================  ==============================================================================
``eventName``                 The event name string.
``bubble``                    When true, the event should be triggered in ancestors of
                              the target object during the bubbling phase.
``isCancelable``              When true, the event can be cancelled.
``view``                      The container or control object that dispatched the event.
``detail``                    Sets the single-double click value for the ``click`` event.
``screenX, screenY``          Sets the event coordinates relative to the screen.
``clientX, clientY``          Sets the event coordinates relative to the target object.
                              The origin is the top left of the control or window, inside any border decorations.
``ctrlKey, altKey, metaKey``  Sets the modifier key states.
``button``                    Sets the mouse button.
``relatedTarget``             Optional. Sets the related target, if any, for a ``mouseover`` or ``mouseout`` event.
============================  ==============================================================================

Reinitializes the object, allowing you to change the event properties after construction. Arguments
set the corresponding properties.

Returns ``undefined``.

--------------------------------------------------------------------------------

.. _keyboard-state-object:

Keyboard state object
---------------------
This JavaScript object reports the active state of the keyboard at any time; that is, the current key that is
down and any modifiers that are pressed. It is independent of the event-handling system, and is available
through the :ref:`ScriptUI-environment` object::

  myKeyState = ScriptUI.environment.keyboardState;

The object has the following properties:

keyName
*******
Type: ``String``

The name of the key currently pressed. This is the JavaScript name, a
string such as ``"A"`` or ``"a"``.

--------------------------------------------------------------------------------

shiftKey, ctrlKey, altKey, metaKey
**********************************
Type: ``Boolean``

True if the named modifier key is currently active.

