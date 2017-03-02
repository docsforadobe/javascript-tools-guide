.. _scriptui-class:

ScriptUI class
==============
The globally available ScriptUI class provides central information about the ScriptUI module. This object
is not instantiable.

.. _scriptui-class-properties:

ScriptUI class properties
-------------------------

.. _scriptui-alignment:

ScriptUI.Alignment
******************
``Object``

Collects the enumerated values that can be used in the :ref:`alignment <container-alignment>` and
:ref:`alignchildren <container-alignchildren>` properties of controls and containers, and in the alignment
property used to set a control's :ref:`titleLayout <control-object-titleLayout>` property. Read only.

Use these constants to set the alignment. For example::

  myGroup.alignment = [ScriptUI.Alignment.LEFT, ScriptUI.Alignment.TOP]

When you query the :ref:`container-alignment` property, it returns index values that
correspond to the constants as shown. Constant values are:

- ``ScriptUI.Alignment.TOP`` (1)
- ``ScriptUI.Alignment.BOTTOM`` (2)
- ``ScriptUI.Alignment.LEFT`` (3)
- ``ScriptUI.Alignment.RIGHT`` (4)
- ``ScriptUI.Alignment.FILL`` (5)
- ``ScriptUI.Alignment.CENTER`` (6)

.. _scriptui-applicationfonts:

ScriptUI.applicationFonts
*************************
``Object``

Collects the enumerated values that specify the default application fonts.
The available fonts vary according to the application and system
configuration.

.. _scriptui-compatability:

ScriptUI.compatability
**********************
``Object``

An object whose properties are the names of compatibility modes
supported by the host application. For example, the presence of
``ScriptUI.compatability.su1PanelCoordinates`` means that the
application allows backward compatibility with the coordinate system of
Panel elements in ScriptUI version 1.

.. _scriptui-coreversion:

ScriptUI.coreVersion
********************
``String``

The internal core version number of the ScriptUI components. Read only.

.. _scriptui-environment:

ScriptUI.environment
********************
``Object``

A JavaScript object that provides access to attributes of the ScriptUI
environment; contains a Keyboard state object that reports the active
state of the keyboard at any time, independent of the event-handling
framework.

.. _scriptui-events:

ScriptUI.events
***************
``Object``

A JavaScript object that contains one function, :ref:`scriptui-events-createevent`,
which allows you to create event objects in order to simulate
user-interaction events.

.. _scriptui-fontstyle:

ScriptUI.FontStyle
******************
``String``

Collects the enumerated values that can be used as the style argument
to the :ref:`scriptui-newfont` method. For example::

  var font = ScriptUI.newFont( 'Helvetica', ScriptUI.FontStyle.BOLD )

Read only. Values are:

- ``REGULAR``
- ``BOLD``
- ``ITALIC``
- ``BOLDITALIC``

.. _scriptui-frameworkname:

ScriptUI.frameworkName
**********************
``String``

The name of the user-interface framework with which this ScriptUI
component is compatible. Read only.

.. _scriptui-version:

ScriptUI.version
****************
``String``

The main version number of the ScriptUI component framework. Read only.

.. _scriptui-class-functions:

ScriptUI class functions
------------------------

.. _scriptui-events-createevent:

ScriptUI.events.createEvent()
*****************************
``ScriptUi.events.createEvent( eventType )``

- ``eventType``: The type of event, one of:

  - UIEvent
  - KeyboardEvent
  - MouseEvent

This function is in the JavaScript object contained in the :ref:`events <scriptui-events>` property. It returns an event object
of the appropriate type:

- A :ref:`UIEvent-base-class` encapsulates input event information for an event that propagates
  through a container and control hierarchy. This is a base class for the more specialized keyboard
  and mouse event types.
- A :ref:`KeyboardEvent-object` encapsulates information about keyboard input events.
- A :ref:`MouseEvent-object` encapsulates information about mouse events.

This object is passed to a function that you register to respond to events of a certain type that occur
in a window or control. Use :ref:`windowObj.addEventListener() <window-object-addeventlistener>`
or :ref:`controlObj.addEventListener() <control-object-addeventlistener>`
to register a handler function. See :ref:`registering-event-listeners-for-windows-or-controls`.

.. _scriptui-getresourcetext:

ScriptUI.getResourceText()
**************************
``ScriptUI.getResourceText( text )``

- ``text``: The text to match.

Finds and returns the resource for a given text string from the host application's resource data. If no
string resource matches the given text, the text itself is returned.

Returns a String.

.. _scriptui-newfont:

ScriptUI.newFont()
******************
``ScriptUI.newFont( name, style, size );``

- ``name``: The font or font family name string.
- ``style``: The font style string or an enumerated value from :ref:`scriptui-fontstyle`
- ``size``: The font size in points, a number.

Creates a new font object for use in text controls and titles.

Returns a :ref:`ScriptUIFont-object`.

.. _scriptui-newimage:

ScriptUI.newImage()
*******************
``ScriptUI.newImage( normal, disabled, pressed, rollover );``

- ``normal``: The resource name or path to the image to use for the normal or default state.
- ``disabled``: The resource name or path to the image to use for the disabled state, shown when the
  control containing the image is disabled (enabled=false).
- ``pressed``: The resource name or path to the image to use for the pressed state, shown when the
  user clicks on the image.
- ``rollover``: The resource name or path to the image to use for the rollover state, which is shown
  when the cursor moves over the image.

Creates a new image object for use in controls that can display images, loading the associated
images from the specified resources or image files.

Returns a :ref:`ScriptUIImage-object`.

.. _environment-object:

Environment object
------------------
This global object is available through the :ref:`ScriptUI.environment <scriptui-environment>` property. It defines attributes of the
ScriptUI environment. In the current release, it contains one property:

keyboardState
*************
``Object``

A :ref:`Keyboard-state-object` that reports the active state of the keyboard at
any time, independent of the event-handling framework.
