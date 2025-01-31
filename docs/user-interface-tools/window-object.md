.. _window-object:

Window object
=============
.. _window-object-constructor:

Window object constructor
-------------------------
The constructor creates and returns a new Window object, or null if window creation failed.

::

	new Window (type [, title, bounds, {creation_properties}]);

=======================  ===================================================================================
``type``                 The window type. The value is:

                           - ``dialog`` - Creates a modal dialog.
                           - ``palette`` - Creates a modeless dialog, also called a floating palette.
                             (Not supported by Photoshop CC.)
                           - ``window`` - Creates a simple window that can be used as a main window for
                             an application. (Not supported by Photoshop CC.)

                         This argument can be a ScriptUI resource specification; in this case, all other
                         arguments are ignored. See :ref:`resource-specifications`.
``title``                Optional. The window title. A localizable string.
``bounds``               Optional. The window's position and size.
``creation_properties``  Optional. An object that can contain any of these properties:

                           - ``resizeable`` - When true, the window can be resized by the user. Default
                             is false.
                           - ``su1PanelCoordinates`` - Photoshop only. When true, the child panels of
                             this window automatically adjust the positions of their children for
                             compatability with Photoshop CS (in which the vertical coordinate was
                             measured from outside the frame). Default is false. Individual panels can
                             override the parent window's setting.
                           - ``closeButton`` - When true, the title bar includes a button to close the
                             window, if the platform and window type allow it. When false, it does not.
                             Default is true. Not used for dialogs.
                           - ``maximizeButton`` - When true, the title bar includes a button to expand
                             the window to its maximum size (typically, the entire screen), if the
                             platform and window type allow it. When false, it does not. Default is false
                             for type palette, true for type window. Not used for dialogs.
                           - ``minimizeButton`` - When true, the title bar includes a button to minimize
                             or iconify the window, if the platform and window type allow it. When
                             false, it does not. Default is false for type palette, true for type window.
                             Main windows cannot have a minimize button in Mac OS. Not used for
                             dialogs.
                           - ``independent`` - When true, a window of type window is independent of
                             other application windows, and can be hidden behind them in Windows.
                             In Mac OS, has no effect. Default is false.
                           - ``borderless`` - When true, the window has no title bar or borders.
                             Properties that control those features are ignored.

=======================  ===================================================================================

--------------------------------------------------------------------------------

.. _window-object-properties:

Window object properties
------------------------
The following element properties apply specifically to Window elements:

.. _window-active:

active
******
Type: Boolean

When true, the object is active, false otherwise. Set to true to make a
given control or dialog active.

- A modal dialog that is visible is by definition the active dialog.
- An active palette is the front-most window.
- An active control is the one with focus-that is, the one that
  accepts keystrokes, or in the case of a Button, be selected when
  the user types RETURN or ENTER.

--------------------------------------------------------------------------------

.. _window-cancelelement:

cancelElement
*************
Type: Object

For a window of type dialog, the control to notify when a user types
the ESC key. By default, looks for a button whose name or text is
``"cancel"`` (case disregarded).

--------------------------------------------------------------------------------

.. _window-defaultelement:

defaultElement
**************
Type: Object

For a window of type dialog, the control to notify when a user types
the ENTER key. By default, looks for a button whose name or text is
``"ok"`` (case disregarded).

--------------------------------------------------------------------------------

.. _window-framebounds:

frameBounds
***********
Type: :ref:`Bounds`

A Bounds object for the boundaries of the Window's frame in screen
coordinates. The frame consists of the title bar and borders that
enclose the content region of a window, depending on the
windowing system. Read only.

--------------------------------------------------------------------------------

.. _window-framelocation:

frameLocation
*************
Type: :ref:`Point`

A Point object for the location of the top left corner of the Window's
frame. The same as [frameBounds.x, frameBounds.y]. Set this
value to move the window frame to the specified location on the
screen. The frameBounds value changes accordingly.

--------------------------------------------------------------------------------

.. _window-framesize:

frameSize
*********
Type: :ref:`Dimension`

A Dimension object for the size and location of the Window's frame
in screen coordinates. Read only.

--------------------------------------------------------------------------------

.. _window-maximized:

maximized
*********
Type: Boolean

When true, the window is expanded.

--------------------------------------------------------------------------------

.. _window-minimized:

minimized
*********
Type: Boolean

When true, the window is minimized or iconified.

--------------------------------------------------------------------------------

.. _window-opacity:

opacity
*******
Type: Number

The opacity of the window, in the range [0..1]. A value of 1.0 (the
default) makes the window completely opaque, a value of 0 makes it
completely transparent. Intermediate values make it partially
transparent to any degree.

--------------------------------------------------------------------------------

.. _window-shortcutkey:

shortcutKey
***********
Type: String

The key sequence that invokes this window's ref:`control-event-onshortcutkey` callback
(in Windows only).

--------------------------------------------------------------------------------

.. _container-properties:

Container properties
--------------------
The following table shows properties that apply to Window objects and container objects (controls of type
panel, tabbedpanel, tab, and group).

--------------------------------------------------------------------------------

.. _container-properties-alignChildren:

alignChildren
*************
Type: String, or Array of 2 Strings

Tells the layout manager how unlike-sized children of a container
should be aligned within a column or row. Order of creation
determines which children are at the top of a column or the left of
a row; the earlier a child is created, the closer it is to the top or left
of its column or row.

If defined, alignment for a child element overrides the alignChildren setting for the parent container.

For a single string value, allowed values depend on the orientation value.

For ``orientation=row``:

  - ``top``
  - ``bottom``
  - ``center`` (default)
  - ``fill``

For ``orientation=column``:

  - ``left``
  - ``right``
  - ``center`` (default)
  - ``fill``

For ``orientation=stack``:

  - ``top``
  - ``bottom``
  - ``left``
  - ``right``
  - ``center`` (default)
  - ``fill``

For an array value, the first string element defines the horizontal
alignment and the second element defines the vertical
alignment. The horizontal alignment value must be one of left,
right, center or fill. The vertical alignment value must be one
of top, bottom, center, or fill.
Values are not case sensitive.

--------------------------------------------------------------------------------

.. _container-properties-alignment:

alignment
*********
Type: String, or Array of 2 Strings

Applies to child elements of a container. If defined, this value
overrides the alignChildren setting for the parent container.
For a single string value, allowed values depend on the
``orientation`` value.

For ``orientation = row``:

  - ``top``
  - ``bottom``
  - ``center`` (default)
  - ``fill``

For ``orientation=column``:

  - ``left``
  - ``right``
  - ``center`` (default)
  - ``fill``

For ``orientation = stack``:

  - ``top``
  - ``bottom``
  - ``left``
  - ``right``
  - ``center`` (default)
  - ``fill``

For an array value, the first string element defines the horizontal
alignment and the second element defines the vertical
alignment. The horizontal alignment value must be one of left,
right, center or fill. The vertical alignment value must be one
of top, bottom, center, or fill.

Values are not case sensitive.

--------------------------------------------------------------------------------

.. _container-properties-bounds:

bounds
******
Type: :ref:`Bounds`

A Bounds object for the boundaries of the window's drawable
area in screen coordinates. Compare `frameBounds`_. Does not
apply to containers of type tab, whose bounds are determined
by the parent tabbedpanel container.

Read only.

--------------------------------------------------------------------------------

.. _container-properties-children:

children
********
Type: Array of Object

The collection of user-interface elements that have been added
to this window or container. An array indexed by number or by a
string containing an element's ``name``. The ``length`` property of this
array is the number of child elements for container elements, and
is zero for controls.

Read only.

.. todo::
    Add note about how to modify children array or a link to section about it

--------------------------------------------------------------------------------

.. _container-properties-graphics:

graphics
********
Type: :ref:`scriptuigraphics-object`

A ScriptUIGraphics object that can be used to customize the
window's appearance, in response to the onDraw event.

--------------------------------------------------------------------------------

.. _container-properties-layout:

layout
******
Type: :ref:`layoutmanager-object`

A LayoutManager object for a window or container. The first time
a container object is made visible, ScriptUI invokes this layout
manager by calling its layout function. Default is an instance of
the LayoutManager class that is automatically created when the
container element is created.

--------------------------------------------------------------------------------

.. _container-properties-location:

location
********
Type: :ref:`Point`

A Point object for the location of the top left corner of the
Window's drawable area, or the top left corner of the frame for a
panel. The same as [bounds.x, bounds.y].

--------------------------------------------------------------------------------

.. _container-properties-margins:

margins
***************
Type: :ref:`Margins`

A Margins object describing the number of pixels between the
edges of this container and the outermost child elements. You
can specify different margins for each edge of the container. The
default value is based on the type of container, and is chosen to
match the standard Adobe user-interface guidelines.

--------------------------------------------------------------------------------

.. _container-properties-maximumSize:

maximumSize
***********
Type: :ref:`Dimension`

A Dimension object for the largest rectangle to which the
window can be resized, used in automatic layout and resizing.

--------------------------------------------------------------------------------

.. _container-properties-minimumSize:

minimumSize
***********
Type: :ref:`Dimension`

A Dimension object for the smallest rectangle to which the
window can be resized, used in automatic layout and resizing.

--------------------------------------------------------------------------------

.. _container-properties-orientation:

orientation
***********
Type: String

How elements are organized within this container. Interpreted by
the layout manager for the container. The default LayoutManager
object accepts the (case-insensitive) values:

  - ``row``
  - ``column``
  - ``stack``

The default orientation depends on the type of container. For
``Window`` and ``Panel``, the default is ``column``, and for ``Group`` the
default is ``row``.

The allowed values for the container's alignChildren and its
children's alignment properties depend on the orientation.

--------------------------------------------------------------------------------

.. _container-properties-parent:

parent
******
Type: Object

The immediate parent object of this element, a window or
container element. The value is ``null`` for Window objects.

Read only.

--------------------------------------------------------------------------------

.. _container-properties-preferredSize:

preferredSize
*************
Type: :ref:`Dimension`

A Dimension object for the preferred size of the window, used in
automatic layout and resizing. To set a specific value for only one
dimension, specify other dimension as ``-1``.

--------------------------------------------------------------------------------

.. _container-properties-properties-properties:

properties
**********
Type: Object

An object that contains one or more creation properties of the
container (properties used only when the element is created).

--------------------------------------------------------------------------------

.. _container-properties-selection:

selection
*********
Type: :ref:`control-type-tab`

For a :ref:`control-type-tabbedpanel` only, the currently active :ref:`control-type-tab` child. Setting
this property changes the active tab. The value can only be ``null``
when the panel has no children; setting it to ``null`` is an error.
When the value changes, either by a user selecting a different tab,
or by a script setting the property, the :ref:`control-event-onChange` callback for the
panel is called.

--------------------------------------------------------------------------------

.. _container-properties-size:

size
****
Type: :ref:`Dimension`

A Dimension object for the current size and location of a group or
panel element, or of the content area of a window.

--------------------------------------------------------------------------------

.. _container-properties-spacing:

spacing
*******
Type: Number

The number of pixels separating one child element from its
adjacent sibling element. Because each container holds only a
single row or column of children, only a single spacing value is
needed for a container. The default value is based on the type of
container, and is chosen to match standard Adobe user-interface
guidelines.

--------------------------------------------------------------------------------

.. _container-properties-text:

text
****
Type: String

The title, label, or displayed text. Does not apply to containers of
type group or tabbedpanel. This is a localizable string: see
:ref:`localization-in-scriptui-objects`.

--------------------------------------------------------------------------------

.. _container-properties-visible:

visible
*******
Type: Boolean

When true, the element is shown, when false it is hidden.


When a container is hidden, its children are also hidden, but they
retain their own visibility values, and are shown or hidden
accordingly when the parent is next shown.

--------------------------------------------------------------------------------

.. _container-properties-window:

window
******
Type: :ref:`Window <window-object>`

The top-level parent window of this container, a :ref:`Window object <window-object>`.

--------------------------------------------------------------------------------

.. _container-properties-windowBounds:

windowBounds
************
Type: :ref:`Bounds`

A Bounds object for the size and location of this container relative
to its top-level parent window.

--------------------------------------------------------------------------------

.. _window-object-functions:

Window object functions
-----------------------
These functions are defined for Window instances, and as indicated for container objects of type Panel and
Group.

--------------------------------------------------------------------------------

.. _window-object-functions-add:

add()
*****
``windowOrContainerObj.add (type [, bounds, text, { creation_props> } ]);``

==================  ====================================================================================
``type``            The control type. See :ref:`control-types-and-creation-parameters`.
``bounds``          Optional. A bounds specification that describes the size and position of the new
                    control or container, relative to its parent. See Bounds object for specification
                    formats.

                    If supplied, this value creates a new Bounds object which is assigned to the new
                    object's bounds property.
``text``            Optional. String. Initial text to be displayed in the control as the title, label, or
                    contents, depending on the control type. If supplied, this value is assigned to
                    the new object's text property.
``creation_props``  Optional. Object. The properties of this object specify creation parameters,
                    which are specific to each object type. See :ref:`control-types-and-creation-parameters`.
==================  ====================================================================================

Creates and returns a new control or container object and adds it to the children of this window or
container.

Returns the new object, or ``null`` if unable to create the object.

--------------------------------------------------------------------------------

.. _window-object-functions-addeventlistener:

addEventListener()
******************
``windowObj.addEventListener (eventName, handler[, capturePhase]);``

================  =================================================================================================
``eventName``     The event name string. Predefined event names include:

                    - ``change``
                    - ``changing``
                    - ``move``
                    - ``moving``
                    - ``resize``
                    - ``resizing``
                    - ``show``
                    - ``enterKey``
                    - ``focus``
                    - ``blur``
                    - ``mousedown``
                    - ``mouseup``
                    - ``mousemove``
                    - ``mouseover``
                    - ``mouseout``
                    - ``click`` (detail = 1 for single, 2 for double)

``handler``       The function to register for the specified event in this target. This can be the
                  name of a function defined in the extension, or a locally defined handler
                  function to be executed when the event occurs. A handler function takes one
                  argument, the UIEvent base class. See :ref:`registering-event-listeners-for-windows-or-controls`.
``capturePhase``  Optional. When true, the handler is called only in the capturing phase of the
                  event propagation. Default is false, meaning that the handler is called in the
                  bubbling phase if this object is an ancestor of the target, or in the at-target
                  phase if this object is itself the target.
================  =================================================================================================

Registers an event handler for a particular type of event occurring in this window.

Returns ``undefined``.

--------------------------------------------------------------------------------

.. _window-object-functions-center:

center()
********
``windowObj.center ([window])``

==========  ==========================
``window``  Optional. A Window object.
==========  ==========================

Centers this window on the screen, or with respect to another specified window.

Returns ``undefined``.

--------------------------------------------------------------------------------

.. _window-object-functions-close:

close()
*******
``windowObj.close ([result])``

==========  ========================================================================
``result``  Optional. A number to be returned from the show method that invoked this
            window as a modal dialog.
==========  ========================================================================

Closes this window. If an onClose callback is defined for the window, calls that function before
closing the window.

Returns undefined.

--------------------------------------------------------------------------------

.. _window-object-functions-dispatchevent:

dispatchEvent()
***************
``windowObj.dispatchEvent(eventObj)``

============  =====================
``eventObj``  A UIEvent base class.
============  =====================

Simulates the occurrence of an event in this target. A script can create a UIEvent base class for a
specific event and pass it to this method to start the event propagation for the event.

Returns ``false`` if any of the registered listeners that handled the event called the event object's
:ref:`preventDefault() <eventobj-preventDefault>` method, ``true`` otherwise.

--------------------------------------------------------------------------------

.. _window-object-functions-findelement:

findElement()
*************
``windowOrContainerObj.findElement(name)``

========  ====================================================================
``name``  The name of the element, as specified in the name creation property.
========  ====================================================================

Searches for the named element among the children of this window or container, and returns the
object if found.

Returns the control object or ``null``.

--------------------------------------------------------------------------------

.. _window-object-functions-hide:

hide()
******
``windowObj.hide()``

Hides this window. When a window is hidden, its children are also hidden, but when it is shown
again, the children retain their own visibility states.

For a modal dialog, closes the dialog and sets its result to 0.

Returns ``undefined``.

--------------------------------------------------------------------------------

.. _window-object-functions-notify:

notify()
********
``windowObj.notify([event])``

=========  =================================================================
``event``  Optional. The name of the window event handler to call. One of:

             - ``onClose``
             - ``onMove``
             - ``onMoving``
             - ``onResize``
             - ``onResizing``
             - ``onShow``

=========  =================================================================

Sends a notification message, simulating the specified user interaction event. For example, to
simulate a dialog being moved by a user::

  myDlg.notify("onMove")

Returns ``undefined``.

--------------------------------------------------------------------------------

.. _window-object-functions-remove:

remove()
********
``windowOrContainerObj.remove(index)``
``windowOrContainerObj.remove(text)``
``windowOrContainerObj.remove(child)``

============================  ===========================================================================
``index``/``text``/``child``  The child control to remove, specified by 0-based index, the contained text
                              value, or as a control object.
============================  ===========================================================================

Removes the specified child control from this window's or container's children array. No error
results if the child does not exist.

Returns ``undefined``.

--------------------------------------------------------------------------------

.. _window-object-functions-removeeventlistener:

removeEventListener()
*********************
``windowObj.removeEventListener(eventName, handler[, capturePhase])``

================  ========================================================================
``eventName``     The event name string.
``handler``       The function that was registered to handle the event.
``capturePhase``  Optional. Whether the handler was to respond only in the capture phase.
================  ========================================================================

Unregisters an event handler for a particular type of event occurring in this window. All arguments
must be identical to those that were used to register the event handler.

Returns ``undefined``.

--------------------------------------------------------------------------------

.. _window-object-functions-show:

show()
******
``windowObj.show()``

Shows this window, container, or control. If an :ref:`onShow <window-event-handling-callbacks>` callback is defined for a window, calls that
function before showing the window.

When a window or container is hidden, its children are also hidden, but when it is shown again, the
children retain their own visibility states.

For a modal dialog, opens the dialog and does not return until the dialog is dismissed. If it is
dismissed via the :ref:`close() <window-object-functions-close>` method, this method returns any result value passed to that method.
Otherwise, returns 0.

--------------------------------------------------------------------------------

.. _window-object-functions-update:

update()
********
``windowObj.update()``

Allows a script to run a long operation (such as copying a large file) and update UI elements to show
the status of the operation.

Normally, drawing updates to UI elements occur during idle periods, when the application is not
doing anything and the OS event queue is being processed, but during a long scripted operation,
the normal event loop is not running. Use this method to perform the necessary synchronous
drawing updates, and also process certain mouse and keyboard events in order to allow a user to
cancel the current operation (by clicking a Cancel button, for instance).

During the update() operation, the application is put into a modal state, so that it does not handle
any events that would activate a different window, or give focus to a control outside the window
being updated. The modal state allows drawing events for controls in other windows to occur (as is
the case during a modal :ref:`show() <window-object-functions-show>` operation), so that the script does not prevent the update of other
parts of the application's UI while in the operation loop.

It is an error to call the update() method for a window that is not currently visible.

--------------------------------------------------------------------------------

.. _window-event-handling-callbacks:

Window event-handling callbacks
-------------------------------
The following callback functions can be defined to respond to events in windows. To respond to an event,
define a function with the corresponding name in the ``Window`` instance. These callbacks are not available
for other container types (controls of type ``panel`` or ``group``).

=================  =========================================================================================
Callback           Description
=================  =========================================================================================
**onActivate**     Called when the user make the window active by clicking it or otherwise making it
                   the keyboard focus.
**onClose**        Called when a request is made to close the window, either by an explicit call to the
                   :ref:`close() <window-object-functions-close>` function or by a user action
                   (clicking the OS-specific close icon in the title bar).

                   The function is called before the window actually closes; it can return false to cancel
                   the close operation.
**onDeactivate**   Called when the user makes a previously active window inactive; for instance by
                   closing it, or by clicking another window to change the keyboard focus.
**onDraw**         Called when a container or control is about to be drawn. Allows the script to modify
                   or control the appearance, using the control's associated :ref:`scriptuigraphics-object` object.
                   Handler takes one argument, a :ref:`drawstate-object` object.
**onMove**         Called when the window has been moved.
**onMoving**       Called while a window in being moved, each time the position changes. A handler
                   can monitor the move operation.
**onResize**       Called when the window has been resized.
**onResizing**     Called while a window is being resized, each time the height or width changes. A
                   handler can monitor the resize operation.
**onShortcutKey**  (In Windows only) Called when a shortcut-key sequence is typed that matches the
                   shortcutKey value for this window.
**onShow**         Called when a request is made to open the window using the :ref:`show() <window-object-functions-show>` method, before
                   the window is made visible, but after automatic layout is complete. A handler can
                   modify the results of the automatic layout.
=================  =========================================================================================
