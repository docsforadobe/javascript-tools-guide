.. _control-objects:

Control objects
===============
UI elements that belong to windows can be containers or controls. Containers
share some aspects of top-level windows, and some aspects of controls, and so
are described here with controls.

.. _control-object-constructors:

Control object constructors
---------------------------
Use the ``add`` method to create new containers and controls. The ``add`` method
is available on ``window`` and container (``panel`` and ``group``) objects.
(See also :ref:`listobj-add` for :ref:`control-type-dropdownlist` and :ref:`control-type-listbox` controls.)

add()
*****
``containerObj.(type [, bounds, text, { creation_props> } ]);``

==================  ============================================================================
``type``            The control type. See :ref:`control-types-and-creation-parameters`.
``bounds``          Optional. A bounds specification that describes the size and
                    position of the new control or container, relative to its parent.
                    See :ref:`Bounds` object for specification formats.

                    If supplied, this value creates a new :ref:`Bounds` object which is assigned
                    to the new object's ``bounds`` property.
``text``            Optional. String. Initial text to be displayed in the control as the
                    title, label, or contents, depending on the control type. If supplied, this
                    value is assigned to the new object's ``text`` property.
``creation_props``  Optional. Object. The properties of this object specify
                    creation parameters, which are specific to each object type. See
                    :ref:`control-types-and-creation-parameters`.
==================  ============================================================================

Creates and returns a new control or container object and adds it to the
children of this window or container.

Returns the new object, or ``null`` if unable to create the object.

--------------------------------------------------------------------------------

.. _control-types-and-creation-parameters:

Control types and creation parameters
-------------------------------------
The following keywords can be used in string literals as the type specifier for
the ``add`` method, available on
``Window`` and container (``Panel`` and ``Group``) objects. The class names can
be used in resource specifications to define controls within a container element
(``Window``, ``Panel``, or ``Group``).

All types of controls, including containers, have an optional creation parameter ``name``
that allows you to give the object a unique name.

--------------------------------------------------------------------------------

.. _control-type-button:

button
******
Class Name: ``Button``

A pushbutton containing a mouse-sensitive text string. Calls the
:ref:`control-event-onClick` callback if the control is clicked or if its
:ref:`controlobj-notify` method is called.

To add to a window ``w``::

  w.add ("button" [, bounds, text, creation_properties}]);

=======================  ======================================================================================
``bounds``               Optional. The control's position and size.
``text``                 Optional. The text displayed in the control.
``creation_properties``  Optional. An object that contains any of the following properties:

                           - ``name``: A unique name for the control. For a modal dialog, the
                             special name "ok" makes this :ref:`window-defaultElement`, and the
                             special name "cancel" makes this the :ref:`window-cancelElement` of the
                             parent dialog.

=======================  ======================================================================================

--------------------------------------------------------------------------------

.. _control-type-checkbox:

checkbox
********
Class Name: ``Checkbox``

A dual-state control showing a box with a checkmark when value is
true, empty when ``value`` is false. Calls the :ref:`control-event-onClick` callback if the
control is clicked or if its :ref:`controlobj-notify` method is called.

To add to a window `w`::

  w.add ("checkbox" [, bounds, text, {creation_properties}]);

=======================  ======================================================================================
``bounds``               Optional. The control's position and size.
``text``                 Optional. The text displayed in the control.
``creation_properties``  Optional. An object that contains any of the following properties:

                           - ``name``: A unique name for the control.

=======================  ======================================================================================

--------------------------------------------------------------------------------

.. _control-type-dropdownlist:

dropdownlist
************
Class Name: ``DropDownList``

A drop-down list with zero or more items. Calls the :ref:`control-event-onchange`
callback if the item selection is changed by a script or the user, or if
the object's :ref:`controlobj-notify` method is called.

To add to a window ``w``::

  w.add( "dropdownlist", bounds [, items, {creation_properties}] );

=======================  ======================================================================================
``bounds``               Optional. The control's position and size.
``items``                Optional. Supply this argument or the
                         ``creation_properties`` argument, not both. An array of strings
                         for the text of each list item.
                         A :ref:`listitem` object is created for each item.
                         An item with the text string ``"-"`` creates a separator item.
``creation_properties``  Optional. Supply this argument or the items argument, not both. This form is most useful
                         for elements defined using :ref:`Resource-specifications`.
                         An object that contains the following property:

                           - ``name``: A unique name for the control.
                           - ``items``: An array of strings for the text of each list item. A
                             ``ListItem`` object is created for each item. An item with the
                             text string ``"-"`` creates a separator item.

=======================  ======================================================================================

--------------------------------------------------------------------------------

.. _control-type-edittext:

edittext
********
Class Name: ``EditText``

An editable text field that the user can change. Calls the :ref:`control-event-onchange`
callback if the text is changed and the user types ``ENTER`` or the control
loses focus, or if its :ref:`controlobj-notify` method is called. Calls the :ref:`control-event-onchanging`
callback when any change is made to the text. The ``textselection``
property contains currently selected text.

To add to a window ``w``::

  w.add ("edittext" [, bounds, text, {creation_properties}]);

=======================  ======================================================================================
``bounds``               Optional. The control's position and size.
``text``                 Optional. The text displayed in the control.
``creation_properties``  Optional. An object that contains any of the following properties:

                           - ``name``: A unique name for the control.
                           - ``readonly``: When false (the default), the control accepts text
                             input. When true, the control does not accept input but only
                             displays the contents of the ``text`` property.
                           - ``noecho``: When false (the default), the control displays input
                             text. When true, the control does not display input text
                             (used for password input fields).
                           - ``enterKeySignalsOnChange``: When false (the default), the
                             control signals an :ref:`control-event-onchange` event when the editable text is
                             changed and the control loses the keyboard focus (that is,
                             the user tabs to another control, clicks outside the control, or
                             types ``ENTER``). When true, the control only signals an
                             ``onChange`` event when the editable text is changed and the
                             user types ``ENTER``; other changes to the keyboard focus do
                             not signal the event.
                           - ``borderless``: When true, the control is drawn with no
                             border. Default is false.
                           - ``multiline``: When false (the default), the control accepts a
                             single line of text. When true, the control accepts multiple
                             lines, in which case the text wraps within the width of the
                             control.
                           - ``scrollable``: (For multiline elements only) When true (the
                             default), the text field has a vertical scrollbar that is enabled
                             when the element contains more text than fits in the visible
                             area. When false, no vertical scrollbar appears; if the element
                             contains more text than fits in the visible area, the arrow
                             keys can be used to scroll the text up and down.

=======================  ======================================================================================

--------------------------------------------------------------------------------

.. _control-type-flashplayer:

flashplayer
***********
Class Name: ``FlashPlayer``

A control that contains a Flash Player, which can load and play Flash
movies stored in SWF files.

The ScriptUI FlashPlayer element runs the Flash application within an
Adobe application. The Flash application runs ActionScript, a
different implementation of JavaScript from the ExtendScript
version of JavaScript that Adobe applications run.

A control object of this type contains functions that allow your script
to load SWF files, control movie playback, and communicate with the
ActionScript environment. See :ref:`flashplayer-control-functions`.

To add to a window ``w``::

  w.add ("flashplayer" [, bounds, movieToLoad, {creation_properties}]);

=======================  ======================================================================================
``bounds``               Optional. The control's position and size.
``moveToLoad``           Optional. A path or URL string or :ref:`File-object` for the SWF file to load into the player.
``creation_properties``  Optional. An object that contains any of the following properties:

                           - ``name``: A unique name for the control.

=======================  ======================================================================================

--------------------------------------------------------------------------------

.. _control-type-group:

group
*****
Class Name: ``Group``

A container for other controls. Containers have additional properties
that control the children; see :ref:`container-properties`.
Hiding a group hides all its children. Making it visible makes visible
those children that are not individually hidden.

To add to a window ``w``::

  w.add ("group" [, bounds, {creation_properties}]);

=======================  ==================================================================
``bounds``               Optional. The control's position and size.
``creation_properties``  Optional. An object that contains any of the following properties:

                           - ``name``: A unique name for the control.

=======================  ==================================================================

--------------------------------------------------------------------------------

.. _control-type-iconbutton:

iconbutton
**********
Class Name: ``IconButton``

A mouse-sensitive pushbutton containing an icon. Calls the :ref:`control-event-onClick`
callback if the control is clicked or if its :ref:`controlobj-notify` method is called.

To add to a window ``w``::

  w.add ("iconbutton" [, bounds, icon, {creation_properties}]);

=======================  ======================================================================================
``bounds``               Optional. The control's position and size.
``icon``                 Optional. The named resource for the icon or family of
                         icons displayed in the button control, or a pathname or :ref:`File-object`
                         for an image file. Images must be in PNG format.
``creation_properties``  Optional. An object that contains any of the following properties:

                           - ``name``: A unique name for the control.
                           - ``style``: A string for the visual style, one of:
                             - ``button``: Has a visible border with a raised or 3D appearance.
                             - ``toolbutton``: Has a flat appearance, appropriate for inclusion in a toolbar
                           - ``toggle``: For a button-style control, a value of true causes it
                             to get a button-pressed appearance the first time it is
                             clicked, and alternate with the unpressed appearance each
                             time it is clicked. The toggle state is reflected in the control's
                             ``value`` property.

=======================  ======================================================================================

--------------------------------------------------------------------------------

.. _control-type-image:

image
*****
Class Name: ``Image``

Displays an icon or image.

To add to a window ``w``::

  w.add ("image" [, bounds, icon, {creation_properties}]);

=======================  ======================================================================================
``bounds``               Optional. The control's position and size.
``icon``                 Optional. The named resource for the icon or family of
                         icons displayed in the button control, or a pathname or :ref:`File-object`
                         for an image file. Images must be in PNG format.
``creation_properties``  Optional. An object that contains the following properties:

                           - ``name``: A unique name for the control.

=======================  ======================================================================================

--------------------------------------------------------------------------------

.. _control-type-item:

item
****
Class Name: ``Array of ListItem``

The choice items in a list box or drop-down list. The objects are
created when items are specified on creation of the parent list
object, or afterward using the list control's :ref:`listobj-add` method.

Items in a drop-down list can be of type ``separator``, in which case
they cannot be selected, and are shown as a horizontal line.

Item objects have these properties which are not found in other
controls:

- :ref:`controlobj-checked`
- :ref:`controlobj-expanded`
- :ref:`controlobj-image`
- :ref:`controlobj-index`
- :ref:`controlobj-selected`

--------------------------------------------------------------------------------

.. _control-type-listbox:

listbox
*******
Class Name: ``ListBox``

A list box with zero or more items. Calls the :ref:`control-event-onChange` callback if the
item selection is changed by a script or the user, or if the object's
:ref:`controlobj-notify` method is called. A double click on an item selects that item
and calls the :ref:`control-event-ondoubleclick` callback.

To add to a window ``w``::

  w.add ("listbox", bounds [, items, {creation_properties}]);

=======================  ======================================================================================
``bounds``               Optional. The control's position and size.
``items``                Optional. An array of strings for the text of each list item.
                         A :ref:`listitem` object is created for each item. Supply this argument,
                         or the items property in ``creation_properties``, not both.
``creation_properties``  Optional. An object that contains any of the following properties:

                           - ``name``: A unique name for the control.
                           - ``multiselect``: When false (the default), only one item can be
                           - ``selected``. When true, multiple items can be selected.
                           - ``items``: An array of strings for the text of each list item. A
                             :ref:`listitem` object is created for each item. An item with the
                             text string ``"-"`` creates a separator item. Supply this
                             property, or the ``items`` argument, not both. This form is most
                             useful for elements defined using :ref:`Resource-specifications`.
                           - ``numberOfColumns``: A number of columns in which to display
                             the items; default is 1. When there are multiple columns,
                             each :ref:`listitem` object represents a single selectable row. Its
                             :ref:`controlobj-text` and :ref:`controlobj-image` values supply the label
                             for the first column, and the ``controlobj-subitems`` property specifies
                             labels for additional columns.
                           - ``showHeaders``: True to display column titles.
                           - ``columnWidths``: An array of numbers for the preferred width
                             in pixels of each column.
                           - ``columnTitles``: A corresponding array of strings for the title
                             of each column, to be shown if ``showHeaders`` is true.

=======================  ======================================================================================

--------------------------------------------------------------------------------

.. _control-type-panel:

panel
*****
Class Name: ``Panel``

A container for other types of controls, with an optional frame.
Containers have additional properties that control the children; see
:ref:`container-properties`. Hiding a panel hides all its
children. Making it visible makes visible those children that are not
individually hidden.

To add to a window ``w``::

  w.add ("panel" [, bounds, text, {creation_properties}]);

=======================  ==================================================================
``bounds``               Optional. The element's position and size.
                         A panel whose width is 0 appears as a vertical line.
                         A panel whose height is 0 appears as a horizontal line.
``text``                 Optional. The text displayed in the border of the panel.
``creation_properties``  Optional. An object that contains any of the following properties:

                           - ``name``: A unique name for the control.
                           - ``borderStyle``: A string that specifies the appearance of the
                             border drawn around the panel. One of ``black``, ``etched``,
                             ``gray``, ``raised`` or ``sunken``. Default is ``etched``.
                           - ``subPanelCoordinates``: When true, this panel automatically
                             adjusts the positions of its children for compatability with
                             Photoshop CS. Default is false, meaning that the panel does
                             not adjust the positions of its children, even if the parent
                             window has automatic adjustment enabled.

=======================  ==================================================================

.. _control-type-progressbar:

progressbar
***********
Class Name: ``Progressbar``

A horizontal rectangle that shows progress of an operation. All
``progressbar`` controls have a horizontal orientation. The ``value``
property contains the current position of the progress indicator; the
default is 0. There is a ``minvalue`` property, but it is always 0; attempts
to set it to a different value are silently ignored.

To add to a window ``w``::

  w.add ("progressbar" [, bounds, value, minvalue, maxvalue, creation_properties}]);

=======================  =======================================================================
``bounds``               Optional. The control's position and size.
``value``                Optional. The initial position of the progress indicator. Default is 0.
``minvalue``             Optional. The minimum value that the ``value``
                         property can be set to. Default is 0. Together with ``maxvalue``,
                         defines the range.
``maxvalue``             Optional. The maximum value that the ``value``
                         property can be set to. Default is 100. Together with ``minvalue``,
                         defines the range.
``creation_properties``  Optional. An object that contains the following property:

                           - ``name``: A unique name for the control.

=======================  =======================================================================

--------------------------------------------------------------------------------

.. _control-type-radiobutton:

radiobutton
***********
Class Name: ``RadioButton``

A dual-state control, grouped with other radiobuttons, of which only
one can be in the selected state. Shows the selected state when
``value`` is true, empty when value is false. Calls the :ref:`control-event-onClick`
callback if the control is clicked or if its :ref:`controlobj-notify` method
is called.

All radiobuttons in a group must be created sequentially, with no
intervening creation of other element types. Only one ``radiobutton``
in a group can be set at a time; setting a different ``radiobutton``
unsets the original one.

To add to a window ``w``::

  w.add ("radiobutton" [, bounds, text, {creation_properties}]);

=======================  ==================================================================
``bounds``               Optional. The element's position and size.
``text``                 Optional. The text displayed in the control.
``creation_properties``  Optional. An object that contains any of the following properties:

                           - ``name``: A unique name for the control.

=======================  ==================================================================

--------------------------------------------------------------------------------

.. _control-type-scrollbar:

scrollbar
*********
Class Name: ``Scrollbar``

A scrollbar with a draggable scroll indicator and stepper buttons to
move the indicator. The ``scrollbar`` control has a horizontal
orientation if the ``width`` is greater than the ``height`` at creation time,
or vertical if its ``height`` is greater than its ``width``.

Calls the :ref:`control-event-onChange` callback after the position of the indicator is
changed or if its :ref:`controlobj-notify` method is called. Calls the :ref:`control-event-onchanging`
callback repeatedly while the user is moving the indicator.

=======================  =======================================================================
``value``                Contains the current position of the scrollbar's indicator
                         within the scrolling area, within the range of ``minvalue`` and ``maxvalue``.
``stepdelta``            Determines the scrolling unit for the up or down arrow. Default is 1.
``jumpdelta``            Determines the scrolling unit for a jump (as when the bar is clicked
                         outside the indicator or arrows); default is 20% of the range between
                         ``minvalue`` and ``maxvalue``.
=======================  =======================================================================

To add to a window ``w``::

  w.add ("scrollbar" [, bounds, value, minvalue, maxvalue, {creation_properties}]);

=======================  =======================================================================
``bounds``               Optional. The control's position and size.
``value``                Optional. The initial position of the scroll indicator. Default is 0.
``minvalue``             Optional. The minimum value that the ``value``
                         property can be set to. Default is 0. Together with ``maxvalue``,
                         defines the scrolling range.
``maxvalue``             Optional. The maximum value that the ``value``
                         property can be set to. Default is 100. Together with ``minvalue``,
                         defines the scrolling range.
``creation_properties``  Optional. An object that contains the following property:

                           - ``name``: A unique name for the control.

=======================  =======================================================================

--------------------------------------------------------------------------------

.. _control-type-slider:

slider
******
Class Name: ``Slider``

A slider with a moveable position indicator. All ``slider`` controls have
a horizontal orientation. Calls the :ref:`control-event-onChange` callback after the
position of the indicator is changed or if its :ref:`controlobj-notify` method is called.
Calls the onChanging callback repeatedly while the user is moving
the indicator.

The ``value`` property contains the current position of the indicator
within the range of ``minvalue`` and ``maxvalue``.

To add to a window ``w``::

  w.add ("slider" [, bounds, value, minvalue, maxvalue, {creation_properties}]);

=======================  =======================================================================
``bounds``               Optional. The control's position and size.
``value``                Optional. The initial position of the scroll indicator. Default is 0.
``minvalue``             Optional. The minimum value that the ``value``
                         property can be set to. Default is 0. Together with ``maxvalue``,
                         defines the range.
``maxvalue``             Optional. The maximum value that the ``value``
                         property can be set to. Default is 100. Together with ``minvalue``,
                         defines the range.
``creation_properties``  Optional. An object that contains the following property:

                           - ``name``: A unique name for the control.

=======================  =======================================================================

--------------------------------------------------------------------------------

.. _control-type-statictext:

statictext
**********
Class Name: ``StaticText``

A text field that the user cannot change.

To add to a window ``w``::

  w.add ("statictext" [, bounds, text, {creation_properties}]);

=======================  ==================================================================
``bounds``               Optional. The element's position and size.
``text``                 Optional. The text displayed in the control.
``creation_properties``  Optional. An object that contains any of the following properties:

                           - ``name``: A unique name for the control.
                           - ``multiline``: When false (the default), the control displays a
                             single line of text. When true, the control displays multiple
                             lines, in which case the text wraps within the width of the
                             control.
                           - ``scrolling``: When false (the default), the displayed text
                             cannot be scrolled. When true, the displayed text can be
                             vertically scrolled using scrollbars; this case implies
                             ``multiline`` is true.
                           - ``truncate``: If ``middle`` or ``end``, defines where to remove
                             characters from the text and replace them with an ellipsis if
                             the specified title does not fit within the space reserved for
                             it. If ``none``, and the text does not fit, characters are removed
                             from the end, without any replacement ellipsis character.

=======================  ==================================================================

--------------------------------------------------------------------------------

.. _control-type-tab:

tab
***
Class Name: ``Tab``

A container for other types of controls. Differs from a :ref:`control-type-panel` element
in that is must be a direct child of a :ref:`control-type-tabbedpanel` element, the title is
shown in the selection tab, and it does not have a script-definable
border. The currently active tab is the value of the parent's
``selection`` property.

Containers have additional properties that control the children; see
:ref:`container-properties`. Hiding a panel hides all its
children. Making it visible makes visible those children that are not
individually hidden.

To add a tab to a tabbed panel ``t`` in window ``w``::

  w.t.add ("tab" [, bounds, text, {creation_properties}]);

=======================  ==================================================================
``bounds``               Not used, pass ``undefined``. The size and position is determined by the parent.
``text``                 Optional. The text displayed in the tab.
``creation_properties``  Optional. An object that contains any of the following properties:

                           - ``name``: A unique name for the control.

=======================  ==================================================================

--------------------------------------------------------------------------------

.. _control-type-tabbedpanel:

tabbedpanel
***********
Class Name: ``TabbedPanel``

A container for selectable :ref:`control-type-tab` containers. Differs from a :ref:`control-type-panel`
element in that it can contain only :ref:`control-type-tab` elements as direct children.

Containers have additional properties that control the children; see
:ref:`container-properties`. Hiding a panel hides all its
children. Making it visible makes visible those children that are not
individually hidden.

The selected `tab` child is the value of the parent's ``selection``
property. One and only one of the ``tab`` children must be selected;
selecting one deselects the others. When the value of the ``selection``
property changes, either by a user selecting a different tab, or by a
script setting the property, the ``tabbedpanel`` receives an
ref:`control-event-onChange` notification.

To add to a window ``w``::

  w.add ("tabbedpanel" [, bounds, text, {creation_properties}]);

=======================  ==================================================================
``bounds``               Optional. The element's position and size. This determines the sizes
                         and positions of the tab children.
``text``                 Ignored.
``creation_properties``  Optional. An object that contains any of the following properties:

                           - ``name``: A unique name for the control.

=======================  ==================================================================

--------------------------------------------------------------------------------

.. _control-type-treeview:

treeview
********
Class Name: ``TreeView``

A hierarchical list whose items can contain child items. Items at any
level of the tree can be individually selected. Calls the :ref:`control-event-onChange`
callback if the item selection is changed by a script or the user, or if
the object's :ref:`controlobj-notify` method is called.

To add to a window ``w``::

  w.add ("treeview" [, bounds, items, {creation_properties}])

=======================  ======================================================================================
``bounds``               Optional. The control's position and size.
``items``                Optional. An array of strings for the text of each top-level
                         list item. A :ref:`listitem` object is created for each item. An item
                         with the type node can contain child items. Supply this
                         argument, or the ``items`` property in ``creation_properties``, not both.
``creation_properties``  Optional. An object that contains any of the following properties:

                           - ``name``: A unique name for the control.
                           - ``items``: An array of strings for the text of each top-level list
                             item. A :ref:`listitem` object is created for each item. An item
                             with the type ``node``` can contain child items. Supply this
                             property, or the ``items`` argument, not both. This form is most
                             useful for elements defined using :ref:`Resource-specifications`.

=======================  ======================================================================================

--------------------------------------------------------------------------------

.. _control-object-properties:

Control object properties
-------------------------
The following table shows the properties of ScriptUI control elements. Some values apply only to controls
of particular types, as indicated. See Container properties for properties that apply to container elements
(controls of type panel, tabbedpanel, tab, and group).

--------------------------------------------------------------------------------

.. _controlobj-active:

active
******
Type: ``Boolean``

When true, the object is active, false otherwise. Set to true to make a
given control or dialog active.

- A modal dialog that is visible is by definition the active dialog.
- An active palette is the front-most window.
- An active control is the one with focus-that is, the one that
  accepts keystrokes, or in the case of a :ref:`Button`, be selected when
  the user types ENTER in Windows, or presses the spacebar in Mac
  OS.

--------------------------------------------------------------------------------

.. _controlobj-alignment:

alignment
*********
Type: ``String or Array of 2 Strings``

Applies to child elements of a container. If defined, this value
overrides the ``alignChildren`` setting for the parent container.

For a single string value, allowed values depend on the ``orientation``
value in the parent container. For ``orientation = 'row'``:

  ======= ================
  top     center (default)
  bottom  fill
  ======= ================

For ``orientation = 'column'``:

  ======= ================
  left    center (default)
  right   fill
  ======= ================

For ``orientation = 'stack'``:

  ======= ================
  top     right
  bottom  center (default)
  left    fill
  ======= ================

For an array value, the first string element defines the horizontal
alignment and the second element defines the vertical alignment.
The horizontal alignment value must be one of ``left``, ``right``, ``center``
or ``fill``. The vertical alignment value must be one of ``top``, ``bottom``, ``center``,
or ``fill``.

Values are not case sensitive.

--------------------------------------------------------------------------------

.. _controlobj-bounds:

bounds
******
Type: ``Bounds``

A :ref:`Bounds` object describing the boundaries of the element, in screen
coordinates for Window elements, and parent-relative coordinates for
child elements (compare :ref:`controlobj-windowBounds`). For windows, the bounds
refer only to the window's content region.

Setting an element's ``size`` or ``location`` changes its ``bounds`` property,
and vice-versa.

--------------------------------------------------------------------------------

.. _controlobj-characters:

characters
**********
Type: ``Number``

Used by the :ref:`LayoutManager-object` to determine the default
:ref:`controlobj-preferredSize` for a :ref:`StaticText` or :ref:`EditText` control. The control will be made wide enough to display the given number of `X` characters in
the font used by the control. Setting this property is the best way to
reserve space in a control for a maximum number of characters to
display.

--------------------------------------------------------------------------------

.. _controlobj-checked:

checked
*******
Type: ``Boolean``

For :ref:`listitem` objects only. When true, the item is marked with the
platform-appropriate checkmark. When false, no checkmark is drawn,
but space is reserved for it in the left margin, so that the item lines up
with other checkable items. When ``undefined``, no space is reserved
for a checkmark.

--------------------------------------------------------------------------------

.. _controlobj-columns:

columns
*******
Type: ``Object``

For :ref:`control-type-listbox` objects only. A JavaScript object with two read-only
properties whose values are set by the creation parameters:

===================  ======================================================
``titles``           An array of column title strings, whose length matches
                     the number of columns specified at creation.
``preferredWidths``  An array of column widths, whose length
                     matches the number of columns specified at creation.
===================  ======================================================

--------------------------------------------------------------------------------

.. _controlobj-enabled:

enabled
*******
Type: ``Boolean``

When true, the control is enabled, meaning that it accepts input.
When false, control elements do not accept input, and all types of
elements have a dimmed appearance. A disabled :ref:`listitem` is not
selectable in a :ref:`control-type-listbox`, :ref:`control-type-dropdownlist` or :ref:`control-type-treeview` list.

--------------------------------------------------------------------------------

.. _controlobj-expanded:

expanded
********
Type: ``Boolean``

For :ref:`listitem` objects of type ``node`` in :ref:`control-type-treeview` list controls. When true,
the item is in the expanded state and its children are shown, when
false, it is collapsed and children are hidden.

--------------------------------------------------------------------------------

.. _controlobj-graphics:

graphics
********
Type: ``Object``

A :ref:`ScriptUIGraphics-object` that can be used to customize the control's
appearance, in response to the :ref:`control-event-ondraw` event.

--------------------------------------------------------------------------------

.. _controlobj-helpTip:

helpTip
*******
Type: ``String``

A brief help message (also called a *tool tip*) that is displayed in a small
floating window when the mouse cursor hovers over a user-interface
control element. Set to an empty string or ``null`` to remove help text.

--------------------------------------------------------------------------------

.. _controlobj-icon:

icon
****
Type: ``String or File``

Deprecated. Use :ref:`image` instead.

--------------------------------------------------------------------------------

.. _controlobj-image:

image
*****
Type: ``Object``

A :ref:`ScriptUIImage-object`, or the name of an icon resource, or the
pathname or :ref:`File-object` for a file that contains a platform-specific
image in PNG or JPEG format, or for a shortcut or alias to such a file.

- For an :ref:`IconButton`, the icon appears as the content of the button.
- For an :ref:`Image`, the image is the entire content of the image element.
- For a :ref:`listitem`, the image is displayed to the left of the text.

  If the parent is a multi-column :ref:`control-type-listbox`, this is the display image
  for the label in the first column, and labels for further columns are
  specified in the :ref:`controlobj-subitems` array.
  See :ref:`creating-multi-column-lists`.

--------------------------------------------------------------------------------

.. _controlobj-indent:

indent
******
Type: ``Number``

A number of pixels by which to indent the element during automatic
layout. Applies for ``column`` orientation and ``left`` alignment, or ``row``
orientation and ``top`` alignment.

--------------------------------------------------------------------------------

.. _controlobj-index:

index
*****
Type: ``Number``

For :ref:`listitem` objects only. The index of this item in the ``items``
collection of its parent list control. Read only.

--------------------------------------------------------------------------------

.. _controlobj-items:

items
*****
Type: ``Array of Object``

For a list object (:ref:`control-type-listbox`, :ref:`control-type-dropdownlist` or :ref:`control-type-treeview` list), a collection
of :ref:`listitem` objects for the items in the list. Access by 0-based index. To
obtain the number of items in the list, use ``items.length``. Read only.

--------------------------------------------------------------------------------

.. _controlobj-itemSize:

itemSize
********
Type: ``Dimension``

For a list object (:ref:`control-type-listbox`, :ref:`control-type-dropdownlist` or :ref:`control-type-treeview` list),
a :ref:`Dimension` object describing the width and height in pixels of each item in the
list. Used by auto-layout to determine the ``preferredSize`` of the list,
if not otherwise specified.

If not set explicitly, the size of each item is set to match the largest
height and width among all items in the list

--------------------------------------------------------------------------------

.. _controlobj-jumpdelta:

jumpdelta
*********
Type: ``Number``

The amount to increment or decrement a :ref:`Scrollbar` indicator's
position when the user clicks ahead or behind the moveable element.
Default is 20% of the range between the maxvalue and minvalue
property values.

--------------------------------------------------------------------------------

.. _controlobj-justify:

justify
*******
Type: ``String``

The justification of text in static text and edit text controls. One of:

- left (default)
- center
- right

.. note:: Justification only works if the value is set on creation, using a
  resource specification or creation parameters.

--------------------------------------------------------------------------------

.. _controlobj-location:

location
********
Type: ``Point``

A :ref:`Point` object describing the location of the element as an array, ``[x, y]``,
representing the coordinates of the upper left corner of the
element. These are screen coordinates for ``Window`` elements, and
parent-relative coordinates for other elements.

The ``location`` is defined as ``[bounds.x, bounds.y]``. Setting an
element's ``location`` changes its ``bounds`` property, and vice-versa. By
default, ``location`` is ``undefined`` until the parent container's layout
manager is invoked.

--------------------------------------------------------------------------------

.. _controlobj-maximumSize:

maximumSize
***********
Type: ``Dimension``

A :ref:`Dimension` object that specifies the maximum height and width for
an element.

The default is 50 pixels less than the screen size in each dimension. In
Windows, this can occupy the entire screen; you must define a ``maximumSize``
to be large enough for your intended usage.

--------------------------------------------------------------------------------

.. _controlobj-minimumSize:

minimumSize
***********
Type: ``Dimension``

A :ref:`Dimension` object that specifies the minimum height and width for
an element. Default is ``[0,0]``.

--------------------------------------------------------------------------------

.. _controlobj-maxvalue:

maxvalue
********
Type: ``Number``

The maximum value that the ``value`` property can have.

- If ``maxvalue`` is reset less than ``value``, ``value`` is reset to ``maxvalue``.
- If ``maxvalue`` is reset less than ``minvalue``, ``minvalue`` is reset to ``maxvalue``.

--------------------------------------------------------------------------------

.. _controlobj-minvalue:

minvalue
********
Type: ``Number``

The minimum value that the ``value`` property can have.

- If ``minvalue`` is reset greater than ``value``, ``value`` is reset to ``minvalue``.
- If ``minvalue`` is reset greater than ``maxvalue``, ``maxvalue`` is reset to ``minvalue``.

--------------------------------------------------------------------------------

.. _controlobj-parent:

parent
******
Type: ``Object``

The immediate parent object of this element. Read only.

--------------------------------------------------------------------------------

.. _controlobj-preferredSize:

preferredSize
*************
Type: ``Dimension``

A :ref:`Dimension` object used by layout managers to determine the best
size for each element. If not explicitly set by a script, value is
established by the user-interface framework in which ScriptUI is
employed, and is based on such attributes of the element as its text,
font, font size, icon size, and other user-interface framework-specific
attributes.

A script can explicitly set ``preferredSize`` before the layout manager
is invoked in order to establish an element size other than the default.
To set a specific value for only one dimension, specify the other
dimension as -1.

--------------------------------------------------------------------------------

.. _controlobj-properties:

properties
**********
Type: ``Object``

An object that contains one or more creation properties of the
element (properties used only when the element is created).

--------------------------------------------------------------------------------

.. _controlobj-selected:

selected
********
Type: ``Boolean``

For :ref:`listitem` objects only. When true, the item is part of the ``selection``
for its parent list. When false, the item is not selected. Set
to true to select this item in a single-selection list, or to add it to the
selection array for a multi-selection list.

--------------------------------------------------------------------------------

.. _controlobj-selection-listbox:

selection
*********
(For ListBox only)

Type: ``Array of ListItem``

For a :ref:`control-type-listbox`, an array of :ref:`listitem` objects for the current selection in a
multi-selection list. Setting this value causes the selected item to be
highlighted and to be scrolled into view if necessary. If no items are
selected, the value is ``null``. Set to ``null`` to deselect all items.

The value can also change because the user clicked or double-clicked
an item, or because an item was removed with :ref:`listobj-remove` or
:ref:`listobj-removeAll`. Whenever the value changes, the :ref:`control-event-onChange` callback is
called. If the value is changed by a double click, calls the
:ref:`control-event-ondoubleclick` callback.

You can set the value using the index of an item or an array of indices,
rather than object references. If set to an index value that is out of
range, the operation is ignored. When set with index values, the
property still returns object references.

- If you set the value to an array for a single-selection list, only the
  first item in the array is selected.
- If you set the value to a single item for a multi-selection list, that
  item is added to the current selection.

--------------------------------------------------------------------------------

.. _controlobj-selection:

selection
*********
(For DropDownList and TreeView only)

Type: ``ListItem``

For a :ref:`control-type-dropdownlist` or :ref:`control-type-treeview` list object, the currently selected
:ref:`listitem` object.

Setting this value causes the selected item to be highlighted and to
be scrolled into view if necessary. If no item is selected, the value is ``null``.
Set to ``null`` to deselect all items.

The value can also change because the user clicked on an item, or
because an item was removed with :ref:`listobj-remove` or :ref:`listobj-removeall`.
Whenever the value changes, the :ref:`control-event-onChange` callback is called.

You can set the value using the index of an item or an array of indices,
rather than object references. If set to an index value that is out of
range, the operation is ignored. When set with an index value, the
property still returns an object reference.

--------------------------------------------------------------------------------

.. _controlobj-shortcutKey:

shortcutKey
***********
Type: ``String``

The key sequence that invokes the :ref:`control-event-onshortcutkey` callback for this
element (in Windows only).

--------------------------------------------------------------------------------

.. _controlobj-size:

size
****
Type: ``Dimension``

A :ref:`Dimension` object that defines the actual dimensions of an element.
Initially ``undefined``, and unless explicitly set by a script, it is defined
by a ``LayoutManager``.

Although a script can explicitly set size before the layout manager is
invoked to establish an element size other than the ``preferredSize``
or the default size, this is not recommended.

Defined as ``[bounds.width, bounds.height]``. Setting an element's
size changes its ``bounds`` property, and vice-versa.

--------------------------------------------------------------------------------

.. _controlobj-stepdelta:

stepdelta
*********
Type: ``Number``

The amount by which to increment or decrement a :ref:`Scrollbar`
element's position when the user clicks a stepper button.

--------------------------------------------------------------------------------

.. _controlobj-subitems:

subitems
********
Type: ``Array``

For :ref:`listitem` objects only. When the parent is a multi-column :ref:`control-type-listbox`,
the :ref:`ListItem.text <controlobj-text>` and :ref:`ListItem.image <controlobj-image>`
values describe the label in the first column, and this specifies additional
labels for that row in the remaining columns.

This contains an array of JavaScript objects, whose length is one less
than the number of columns. Each member specifies a label in the
corresponding column, with the first member (``subitems[0]``)
describing the label in the second column.

Each object has two properties, of which one or both can be supplied:

=========  ============================================
``text``   A localizable display string for this label.
``image``  An Image object for this label.
=========  ============================================

--------------------------------------------------------------------------------

.. _controlobj-text:

text
****
Type: ``String``

The title, label, or displayed text. Ignored for containers of type ``group``.
For controls, the meaning depends on the control type. Buttons use
the ``text`` as a label, for example, while edit fields use the text to
access the content.

For :ref:`listitem` objects, this is the display string for the list choice. If the
parent is a multi-column list box, this is the display string for the label
in the first column, and labels for further columns are specified in the
:ref:`controlobj-subitems` array. See :ref:`creating-multi-column-lists`.

This is a localizable string: see :ref:`localization-in-scriptui-objects`.

--------------------------------------------------------------------------------

.. _controlobj-textselection:

textselection
*************
Type: ``String``

The currently selected text in a control that displays text, or the empty
string if there is no text selected.

Setting the value replaces the current text selection and modifies the
value of the ``text`` property. If there is no current selection, inserts the
new value into the ``text`` string at the current insertion point. The
``textselection`` value is reset to an empty string after it modifies the
``text`` value.

.. note:: Setting the ``textselection`` property before the edittext
  control's parent Window exists is an undefined operation.

--------------------------------------------------------------------------------

.. _controlobj-title:

title
*****
Type: ``String``

For a :ref:`control-type-dropdownlist`, :ref:`FlashPlayer`, :ref:`IconButton`, :ref:`Image`,
or :ref:`control-type-tabbedpanel` only, a text label for the element. The title can appear
to the left or right of the element, or above or below it, or you can superimpose
the title over the center of the element. The placement is controlled by
the :ref:`controlobj-titlelayout` value.

--------------------------------------------------------------------------------

.. _controlobj-titlelayout:

titleLayout
***********
``Object``


For a :ref:`control-type-dropdownlist`, :ref:`FlashPlayer`, :ref:`IconButton`, :ref:`Image`,
or :ref:`control-type-tabbedpanel` with a title value, the way the text label is shown in
relation to the element. A JavaScript object with these properties:

==============  ========================================================================
``alignment``   The position of the title relative to the element, an
                array of [horizontal_alignment, vertical_alignment]. For possible
                alignment values, see :ref:`controlobj-alignment`. Note that ``fill`` is
                not a valid alignment value for either horizontal or vertical
                alignment in this context.
``characters``  A number; if 1 or greater, reserves a title width
                wide enough to hold the specified number of "X" characters in
                the font for this element. If 0, the title width is calculated based
                on the value of the ``title`` property during layout operations.
``spacing``     A number; 0 or greater. The number of pixels
                separating the title from the element.
``margins``     An array of numbers, ``[left, top, right, bottom]``
                for the number of pixels separating each edge of an element and
                the visible content within that element. This overrides the default
                margins.
``justify``     One of ``'left'``, ``'center'``, or ``'right'``, how to justify
                the text when the space allocated for the title width is greater
                than the actual width of the text.
``truncate``    If ``'middle'`` or ``'end'``, defines where to remove
                characters from the text and replace them with an ellipsis (…) if
                the specified title does not fit within the space reserved for it. If
                ``'none'``, and the text does not fit, characters are removed from
                the end, without any replacement ellipsis character.
==============  ========================================================================

--------------------------------------------------------------------------------

.. _controlobj-type:

type
****
Type: ``String``

Contains the type name of the element, as specified on creation.

- For ``Window`` objects, one of the type names window, palette, or dialog.
- For ``controls``, the type of the control, as specified in the add method that
  created it.

Read only.

--------------------------------------------------------------------------------

.. _controlobj-value-boolean:

value
*****
Type: ``Boolean``

For a :ref:`Checkbox` or :ref:`RadioButton`, true if the control is in the
selected or set state, false if it is not.

--------------------------------------------------------------------------------

.. _controlobj-value-number:

value
*****
Type: ``Number``

For a :ref:`Scrollbar` or :ref:`Slider`, the current position of the indicator.
If set to a value outside the range specified by minvalue and maxvalue, it is
automatically reset to the closest boundary.

--------------------------------------------------------------------------------

.. _controlobj-visible:

visible
*******
Type: ``Boolean``

When true, the element is shown, when false it is hidden.

When a container is hidden, its children are also hidden, but they
retain their own visibility values, and are shown or hidden accordingly
when the parent is next shown.

--------------------------------------------------------------------------------

.. _controlobj-window:

window
******
Type: ``Window``

The :ref:`Window-object` that contains this control. Read only.

--------------------------------------------------------------------------------

.. _controlobj-windowBounds:

windowBounds
************
Type: ``Bounds``

A :ref:`Bounds` object that contains the bounds of this control in the
containing window's coordinates. Compare :ref:`bounds`, in which
coordinates are relative to the immediate parent container. Read only.

--------------------------------------------------------------------------------

.. _controlobj-function_name:

function_name
*************
Type: ``Function``

For the :ref:`FlashPlayer` control, a function definition for a callback from
the Flash ActionScript environment.

There are no special naming requirements, but the function must
take and return only the supported data types:

======= =========
Number  undefined
String  Object
Boolean Array
Null
======= =========

.. note:: The ActionScript ``class`` and ``date`` objects are not supported as
  parameter values.

--------------------------------------------------------------------------------

.. _control-object-functions:

Control object functions
------------------------
The following table shows the methods defined for each element type, and for specific control types as
indicated.

--------------------------------------------------------------------------------

.. _controlobj-addeventlistener:

addEventListener()
******************
``controlObj.addEventListener(eventName, handler, capturePhase);``

================  =====================================================================================
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
                    - ``keyup``
                    - ``keydown``
                    - ``click`` (detail = 1 for single, 2 for double)

``handler``       The function to register for the specified event in this target. This can be the name
                  of a function defined in the extension, or a locally defined handler function to be
                  executed when the event occurs.

                  A handler function takes one argument, an object of the UIEvent base class. See
                  :ref:`registering-event-listeners-for-windows-or-controls`.

``capturePhase``  Optional. When true, the handler is called only in the capturing phase of the event
                  propagation. Default is false, meaning that the handler is called in the bubbling
                  phase if this object is an ancestor of the target, or in the at-target phase if this
                  object is itself the target.
================  =====================================================================================

Registers an event handler for a particular type of event occurring in this control.

Returns undefined.

--------------------------------------------------------------------------------

.. _controlobj-dispatchEvent:

dispatchEvent()
***************
``controlObj.dispatchEvent (eventObj)``

============  ====================================
``eventObj``  An object of the UIEvent base class.
============  ====================================

Simulates the occurrence of an event in this target. A script can create an event
object for a specific event, using :ref:`ScriptUI-events-createEvent`, and pass
it to this method to start the event propagation for the event.

Returns false if any of the registered listeners that handled the event called
the event object's :ref:`eventobj-preventDefault` method, true otherwise.

--------------------------------------------------------------------------------

.. _controlobj-hide:

hide()
******
``controlObj.hide()``

Hides this container or control. When a window or container is hidden, its
children are also hidden, but when it is shown again, the children retain their
own visibility states.

Returns ``undefined``.

--------------------------------------------------------------------------------

.. _controlobj-notify:

notify()
********
``controlObj.notify([event])``

=========  ================================================================
``event``  Optional. The name of the control event handler to call. One of:

             - ``onClick``
             - ``onChange``
             - ``onChanging``

           By default, simulates the :ref:`control-event-onChange` event for
           an :ref:`EditText` control, an :ref:`control-event-onClick` event
           for controls that support that event.
=========  ================================================================

Sends a notification message, simulating the specified user interaction event.

Returns ``undefined``.

--------------------------------------------------------------------------------

.. _controlobj-removeEventListener:

removeEventListener()
*********************
``controlbj.removeEventListener (eventName, handler[, capturePhase]);``

================  =======================================================================
``eventName``     The event name string.
``handler``       The function that was registered to handle the event.
``capturePhase``  Optional. Whether the handler was to respond only in the capture phase.
================  =======================================================================

Unregisters an event handler for a particular type of event occurring in this control. All arguments
must be identical to those that were used to register the event handler.

Returns ``undefined``.

--------------------------------------------------------------------------------

.. _controlobj-show:

show()
******
``controlObj.show()``

Shows this container or control. When a window or container is hidden, its children
are also hidden, but when it is shown again, the children retain their own
visibility states.

Returns ``undefined``.

--------------------------------------------------------------------------------

.. _controlobj-toString:

toString()
**********
``listItemObj.toString()``

For :ref:`listitem` controls only. Retrieves the value of this item's text
property as a string.

Returns a String.

--------------------------------------------------------------------------------

.. _controlobj-valueOf:

valueOf()
*********
``listItemObj.valueOf()``

For :ref:`listitem` controls only. Retrieves the index number of this item in
the parent list's items array.

Returns a Number.

--------------------------------------------------------------------------------

List control object functions
-----------------------------
The following table shows the methods defined for list objects only.

--------------------------------------------------------------------------------

.. _listobj-add:

add()
*****
``listObj.add (type, text[, index])``

=========  ============================================================================================
``type``   The type of item to add. One of:

             - ``item``: A basic, selectable item with a text label.
             - ``separator``: A separator. For dropdownlist controls only. In this case, the text value
               is ignored, and the method returns null.

``text``   The localizable text label for the item.
``index``  Optional. The index into the current item list after which this item is inserted. If not
           supplied, or greater than the current list length, the new item is added at the end.
=========  ============================================================================================

For list objects (:ref:`control-type-listbox`, :ref:`control-type-dropdownlist` or :ref:`control-type-treeview`) only.
Adds an ``item`` to the items array at the given index.

Returns the ``item`` control object for ``type = 'item'``, or ``null`` for
``type = 'separator'``.

--------------------------------------------------------------------------------

.. _listobj-find:

find()
******
``listObj.find(text)``

text

The text of the item to find.

For list objects (:ref:`control-type-listbox`, :ref:`control-type-dropdownlist` or :ref:`control-type-treeview`) only.
Looks in this object's ``items`` array for an item object with the given ``text``
value.

Returns the ``item`` object if found; otherwise, returns ``null``.

--------------------------------------------------------------------------------

.. _listobj-remove:

remove()
********
``containerObj.remove(index)``
``containerObj.remove(text)``
``containerObj.remove(child)``

==============================  ====================================================================================================
``index``, ``text``, ``child``  The item or child to remove, specified by 0-based index, ``text`` value, or as a ``control`` object.
==============================  ====================================================================================================

For containers (:ref:`control-type-panel`, :ref:`control-type-group`), removes the specified child control from
the container's ``children`` array.

For list objects (:ref:`control-type-listbox`, :ref:`control-type-dropdownlist` or :ref:`control-type-treeview`) only, removes the specified item from this
object's items array. No error results if the item does not exist.

Returns ``undefined``.

--------------------------------------------------------------------------------

.. _listobj-removeAll:

removeAll()
***********
``listObj.removeAll()``

For list objects (:ref:`control-type-listbox`, :ref:`control-type-dropdownlist` or :ref:`control-type-treeview`) only.
Removes all items from the object's ``items`` array.

Returns ``undefined``.

--------------------------------------------------------------------------------

.. _listobj-revealItem:

revealItem()
************
``listObj.revealItem(item)``

========  ==============================================
``item``  The item or child to reveal, a control object.
========  ==============================================

For :ref:`control-type-listbox` only. Scrolls the list to make the specified item visible,
if necessary.

Returns ``undefined``.

--------------------------------------------------------------------------------

.. _flashplayer-control-functions:

FlashPlayer control functions
-----------------------------
These functions apply only to controls of type flashplayer.

.. note:: There are limitations on how these functions can be used to control
  playback of Flash movies:

  - Do not use :ref:`flashplayerobj-stopMovie` and :ref:`flashplayerobj-playMovie` to suspend and subsequently
    resume or restart an SWF file produced by Flex™.
  - The :ref:`flashplayerobj-stopMovie` and :ref:`flashplayerobj-playMovie` sequence does not make sense
    for some SWF files produced by Flash Authoring, depending on the exact details
    of how they were implemented. The sequence may not correctly reset the file to
    the initial state (when the ``rewind`` argument to :ref:`flashplayerobj-playMovie` is
    true) nor suspend then resume the execution of the file (when ``rewind`` is false).
  - Using :ref:`flashplayerobj-stopMovie` from the player's hosting environment has no effect
    on an SWF file playing in a ScriptUI Flash Player element. It is, however,
    possible to produce an SWF using Flash Authoring that can stop itself in
    response to user interaction.
  - Do not call :ref:`flashplayerobj-playMovie` when an SWF file is already playing.

--------------------------------------------------------------------------------

.. _flashplayerobj-invokePlayerFunction:

invokePlayerFunction()
**********************
``flashPlayerObj.invokePlayerFunction(fnName, [arg1[,…argN]] )``

==========  ==============================================================================
``fnName``  String. The name of a Flash ActionScript function that has been
            registered with the ExternalInterface object by the currently loaded SWF file;
            see :ref:`calling-actionscript-functions-from-a-scriptui-script`.
``args``    Optional. One or more arguments to pass through to the function, of
            these types:

              - ``Array``
              - ``Boolean``
              - ``Null``
              - ``Number``
              - ``Object``
              - ``String``
              - ``undefined``

==========  ==============================================================================

Invokes an ActionScript function defined in the Flash application.

Returns the result of the invoked function, which must be one of the allowed types. The ActionScript
``class`` and ``date`` objects are not supported as return values.

--------------------------------------------------------------------------------

.. _flashplayerobj-loadMovie:

loadMovie()
***********
``flashPlayerObj.loadMovie(file)``

========  ========================================
``file``  The :ref:`File-object` for the SWF file.
========  ========================================

Loads a movie into the Flash Player, and begins playing it. If you do not specify an associated movie file
when creating the control, you must use this function to load one.

Returns ``undefined``.

--------------------------------------------------------------------------------

.. _flashplayerobj-playMovie:

playMovie()
***********
``flashPlayerObj.playMovie(rewind)``

==========  ==============================================================
``rewind``  When true, restarts the movie from the beginning;
            otherwise, starts playing from the point where it was stopped.
==========  ==============================================================

Restarts a movie that has been stopped.

.. note:: Do not call when a movie is currently playing.

Returns ``undefined``.

--------------------------------------------------------------------------------

.. _flashplayerobj-stopMovie:

stopMovie()
***********
``flashPlayerObj.stopMovie()``

Halts playback of the current movie.

.. note:: Does not work when called from the player's hosting environment.

Returns ``undefined``.

--------------------------------------------------------------------------------

.. _control-event-handling-callbacks:

Control event-handling callbacks
--------------------------------
The following events are signalled in certain types of controls. To handle the event, define a function with
the corresponding name in the control object. Handler functions take no arguments and have no
expected return values; see :ref:`defining-behavior-with-event-callbacks-and-listeners`.

--------------------------------------------------------------------------------

.. _control-event-onactivate:

onActivate
**********
Called when the user gives a control the keyboard focus by clicking it or
tabbing into it.

--------------------------------------------------------------------------------

.. _control-event-onclick:

onClick
*******
Called when the user clicks one of the following control types:

=============== ==================
:ref:`Button`   :ref:`IconButton`
:ref:`Checkbox` :ref:`RadioButton`
=============== ==================

--------------------------------------------------------------------------------

.. _control-event-onchange:

onChange
********

Called when the user finishes making a change in one of the following control
types:

================================  ================
:ref:`control-type-dropdownlist`  :ref:`Scrollbar`
:ref:`EditText`                   :ref:`Slider`
:ref:`control-type-listbox`       :ref:`control-type-treeview`
================================  ================

- For an :ref:`EditText` control, called only when the change is complete-that is, when
  focus moves to another control, or the user types ``ENTER``. The exact behavior
  depends on the creation parameter ``enterKeySignalsOnChange``; see the
  :ref:`edittext <control-type-edittext>` description.
- For a :ref:`Slider` or :ref:`Scrollbar`, called when the user has finished
  dragging the position marker or has clicked the control.
- For a :ref:`control-type-listbox`, :ref:`control-type-dropdownlist` or :ref:`control-type-treeview` control, called
  whenever the selection property changes. This can happen when a script sets the
  property directly or removes a selected item from the list, or when the user
  changes the selection.

--------------------------------------------------------------------------------

.. _control-event-onchanging:

onChanging
**********
Called for each incremental change in one of the following control types:

=============== ================ =============
:ref:`EditText` :ref:`Scrollbar` :ref:`Slider`
=============== ================ =============

- For an :ref:`EditText` control, called for each keypress while the control has focus.
- For a :ref:`Slider` or :ref:`Scrollbar`, called for any motion of the position marker.

--------------------------------------------------------------------------------

.. _control-event-oncollapse:

onCollapse
**********
Called when the user collapses (closes) a node in a :ref:`control-type-treeview` control.
The parameter to this function is the :ref:`listitem` node object that was
collapsed.

--------------------------------------------------------------------------------

.. _control-event-ondeactivate:

onDeactivate
************
Called when the user removes keyboard focus from a previously active control by
clicking outside it or tabbing out of it.

--------------------------------------------------------------------------------

.. _control-event-ondoubleclick:

onDoubleClick
*************
Called when the user double clicks an item in a :ref:`control-type-listbox` control.
The list's ``selection`` property is set to the clicked item.

--------------------------------------------------------------------------------

.. _control-event-onenterkey:

onEnterKey
*************
Called when the user presses return or enter in a :ref:`control-type-edittext` control.

--------------------------------------------------------------------------------

.. _control-event-ondraw:

onDraw
******
Called when a container or control is about to be drawn. Allows the script to modify
or control the appearance, using the control's associated :ref:`ScriptUIGraphics-object`.
Handler takes one argument, a :ref:`DrawState-object`.

--------------------------------------------------------------------------------

.. _control-event-onexpand:

onExpand
********
Called when the user expands (opens) a node in a :ref:`control-type-treeview` control. The parameter
to this function is the :ref:`listitem` node object that was expanded.

--------------------------------------------------------------------------------

.. _control-event-onshortcutkey:

onShortcutKey
*************
(In Windows only) Called when a shortcut-key sequence is typed that matches the
:ref:`controlobj-shortcutKey` value for an element in the active window.

--------------------------------------------------------------------------------

.. _drawstate-object:

DrawState object
----------------
A helper object that describes an input state at the time of the triggering
:ref:`control-event-ondraw` event. Contains properties that report whether the current control
has the input focus, and the particular mouse button and key-press state.
There is no object constructor.

DrawState object properties
***************************
The object contains the following read-only properties:

=================== =========== ==================================================================
altKeyPressed       Boolean     When true, the ALT key was pressed. (In Windows only.)
capsLockKeyPressed  Boolean     When true, the CAPSLOCK key was pressed.
cmdKeyPressed       Boolean     When true, the CMD key was pressed. (In Mac OS only.)
ctrlKeyPressed      Boolean     When true, the CTRL key was pressed.
hasFocus            Boolean     When true, the control containing this object has the input focus.
leftButtonPressed   Boolean     When true, the left mouse button was pressed.
middleButtonPressed Boolean     When true, the middle mouse button was pressed.
mouseOver           Boolean     When true, the cursor position was within the bounds of the
                                control containing this object.
numLockKeyPressed   Boolean     When true, the NUMLOCK key was pressed.
optKeyPressed       Boolean     When true, the OPT key was pressed. (In Mac OS only.)
rightButtonPressed  Boolean     When true, the right mouse button was pressed.
shiftKeyPressed     Boolean     When true, the SHIFT key was pressed.
=================== =========== ==================================================================
