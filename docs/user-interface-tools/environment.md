.. _environment-object:

Environment object
==================

This global object is available through the :ref:`scriptui-environment` property.

It defines attributes of the ScriptUI environment, and only contains one property.

Due to this object including only a single property (that is itself an object), all of the relevant documentation will be contained in this page.

--------------------------------------------------------------------------------

.. _environment-object-properties:

Environment object properties
-----------------------------

The following element properties apply specifically to Environment elements:

.. _environment-keyboard-state:

Keyboard state object
---------------------

This JavaScript object reports the active state of the keyboard at any time; that is, the current key that is down and any modifiers that are pressed.

This is independent of the event-handling system, which means that at any time in your script, you can use this object to check whether specific keys (such as keyboard modifiers) are pressed, and trigger alternative actions as a result.

It is available through the :ref:`ScriptUI-environment` object::

  var myKeyState = ScriptUI.environment.keyboardState;

The Keyboard State object contains the following properties:

--------------------------------------------------------------------------------

.. _keyboard-state-keyName:

keyName
*******
Type: ``String``

The name of the key currently pressed. This is the JavaScript name, a string such as ``"A"`` or ``"a"``.

.. note::

  - This only works for single keys being pressed; holding multiple will report ``undefined``.
  - Modifier keys will report ``undefined``; to get those, see :ref:`keyboard-state-metaKeys`

For example, with 'a' pressed::

  var currentPressedKey = ScriptUI.environment.keyboardState.keyName;

  alert(currentPressedKey); // "A"

--------------------------------------------------------------------------------

.. _keyboard-state-metaKeys:

shiftKey, ctrlKey, altKey, metaKey
**********************************
Type: ``Boolean``

``true`` if the named modifier key is currently active.

.. note::

  ``metaKey`` captures both the ``META`` and ``COMMAND`` keys.

Examples
++++++++

For example, checking whether a modifier key is held during script execution::

  var shiftHeld = ScriptUI.environment.keyboardState.shiftKey;

  if (shiftHeld) {
    alert("User is holding shift!");
  }

Or to check for keyboard modifier combinations::

  var keyboardState = ScriptUI.environment.keyboardState;

  if (keyboardState.shiftKey && keyboardState.altKey) {
    alert("Shift and alt held!");
  }

This can also be used within interface buttons as alternative to :ref:`checking the modifiers via keyboard events <keyboardevent-object-getModifierState>`, which can be more confusing and less user-intuitive, unless you're confident you're handling event states properly.

For example::

  button.onClick = function () {
    if (ScriptUI.environment.keyboardState.shiftKey) {
      // Special functionality for 'shift' key here
      return;
    }

    // normal button behaviour here
  }
