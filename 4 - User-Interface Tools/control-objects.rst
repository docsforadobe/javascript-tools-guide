.. _control-objects:

Control objects
===============
UI elements that belong to windows can be containers or controls. Containers share some aspects of
top-level windows, and some aspects of controls, and so are described here with controls.

.. _control-object-constructors:

Control object constructors
---------------------------
Use the add method to create new containers and controls. The add method is available on window and
container (panel and group) objects. (See also add() for dropdownlist and listbox controls.)
add()
containerObj.(type [, bounds, text, { creation_props> } ]);
type

The control type. See :ref:`control-types-and-creation-parameters`.

bounds

Optional. A bounds specification that describes the size and position of the new
control or container, relative to its parent. See Bounds object for specification
formats.
If supplied, this value creates a new Bounds object which is assigned to the new
object’s bounds property.

text

Optional. String. Initial text to be displayed in the control as the title, label, or
contents, depending on the control type. If supplied, this value is assigned to
the new object’s text property.

creation_props

Optional. Object. The properties of this object specify creation parameters,
which are specific to each object type. See :ref:`control-types-and-creation-parameters`.

Creates and returns a new control or container object and adds it to the children of this window or
container.
Returns the new object, or null if unable to create the object.

.. _control-types-and-creation-parameters:

Control types and creation parameters
-------------------------------------
The following keywords can be used in string literals as the type specifier for the add method, available on
Window and container (Panel and Group) objects. The class names can be used in resource specifications
to define controls within a container element (Window, Panel, or Group).
All types of controls, including containers, have an optional creation parameter name that allows you to
give the object a unique name.
Type keyword

Class name

Description

button

Button

A pushbutton containing a mouse-sensitive text string. Calls the
onClick callback if the control is clicked or if its notify() method is
called.
To add to a window w:
w.add ("button" [, bounds, text, creation_properties}]);
bounds: Optional. The control’s position and size.
text: Optional. The text displayed in the control.
creation_properties: Optional. An object that contains any of

the following properties:

name: A unique name for the control. For a modal dialog, the

special name "ok" makes this defaultElement, and the
special name "cancel" makes this the cancelElement of the
parent dialog.
checkbox

Checkbox

A dual-state control showing a box with a checkmark when value is
true, empty when value is false. Calls the onClick callback if the
control is clicked or if its notify() method is called.
To add to a window w:
w.add ("checkbox" [, bounds, text,
{creation_properties}]);
bounds: Optional. The control’s position and size.
text: Optional. The text displayed in the control.
creation_properties: Optional. An object that contains any of

the following properties:

name: A unique name for the control.

CHAPTER 4: User-Interface Tools

Control objects

Type keyword

Class name

dropdownlist

DropDownList A drop-down list with zero or more items. Calls the onChange

Description
callback if the item selection is changed by a script or the user, or if
the object’s notify() method is called.
To add to a window w:
w.add ("dropdownlist", bounds [, items,
{creation_properties}]);
bounds: The control’s position and size.
items: Optional. Supply this argument or the
creation_properties argument, not both. An array of strings
for the text of each list item. A ListItem object is created for
each item. An item with the text string "-" creates a separator

item.

creation_properties: Optional. Supply this argument or the
items argument, not both. This form is most useful for elements

defined using Resource specifications. An object that contains
the following property:
name: A unique name for the control.

items: An array of strings for the text of each list item. A
ListItem object is created for each item. An item with the
text string "-" creates a separator item.
edittext

EditText

An editable text field that the user can change. Calls the onChange
callback if the text is changed and the user types ENTER or the control
loses focus, or if its notify() method is called. Calls the onChanging
callback when any change is made to the text. The textselection
property contains currently selected text.
To add to a window w:
w.add ("edittext" [, bounds, text,
{creation_properties}]);
bounds: Optional. The control’s position and size.
text: Optional. The text displayed in the control.
creation_properties: Optional. An object that contains any of

the following properties:

name: A unique name for the control.
readonly: When false (the default), the control accepts text

input. When true, the control does not accept input but only
displays the contents of the text property.

noecho: When false (the default), the control displays input

text. When true, the control does not display input text
(used for password input fields).

Type keyword

Control objects

Class name

edittext (cont’d)

Description
enterKeySignalsOnChange: When false (the default), the
control signals an onChange event when the editable text is
changed and the control loses the keyboard focus (that is,
the user tabs to another control, clicks outside the control, or
types ENTER). When true, the control only signals an
onChange event when the editable text is changed and the
user types ENTER; other changes to the keyboard focus do
not signal the event.
borderless: When true , the control is drawn with no
border. Default is false.
multiline: When false (the default), the control accepts a

single line of text. When true, the control accepts multiple
lines, in which case the text wraps within the width of the
control.

scrollable: (For multiline elements only) When true (the
default), the text field has a vertical scrollbar that is enabled
when the element contains more text than fits in the visible
area. When false, no vertical scrollbar appears; if the element
contains more text than fits in the visible area, the arrow
keys can be used to scroll the text up and down.
flashplayer

FlashPlayer

A control that contains a Flash Player, which can load and play Flash
movies stored in SWF files.
The ScriptUI FlashPlayer element runs the Flash application within an
Adobe application. The Flash application runs ActionScript, a
different implementation of JavaScript from the ExtendScript
version of JavaScript that Adobe applications run.
A control object of this type contains functions that allow your script
to load SWF files, control movie playback, and communicate with the
ActionScript environment. See :ref:`flashplayer-control-functions`.
To add to a window w:
w.add ("flashplayer" [, bounds, movieToLoad,
{creation_properties}]);
bounds: Optional. The control’s position and size.
movieToLoad: Optional. A path or URL string or File object for
the SWF file to load into the player.
creation_properties: Optional. An object that contains any of

the following properties:

name: A unique name for the control.

Type keyword

Class name

Description

group

Group

A container for other controls. Containers have additional properties
that control the children; see :ref:`container-properties`.
Hiding a group hides all its children. Making it visible makes visible
those children that are not individually hidden.
To add to a window w:
w.add ("group" [, bounds, {creation_properties}]);
bounds: Optional. The element’s position and size.
creation_properties: Optional. An object that contains any of

the following properties:

name: A unique name for the control.
iconbutton

IconButton

A mouse-sensitive pushbutton containing an icon. Calls the onClick
callback if the control is clicked or if its notify() method is called.
To add to a window w:
w.add ("iconbutton" [, bounds, icon,
{creation_properties}]);
bounds: Optional. The control’s position and size.
icon: Optional. The named resource for the icon or family of

icons displayed in the button control, or a pathname or File
object for an image file. Images must be in PNG format.

creation_properties: Optional. An object that contains the

following property:

name: A unique name for the control.
style: A string for the visual style, one of:
button: Has a visible border with a raised or 3D

appearance.

toolbutton: Has a flat appearance, appropriate for
inclusion in a toolbar

toggle: For a button-style control, a value of true causes it

to get a button-pressed appearance the first time it is
clicked, and alternate with the unpressed appearance each
time it is clicked. The toggle state is reflected in the control’s
value property.

Control objects

Type keyword

Class name

Description

image

Image

Displays an icon or image.

To add to a window w:
w.add ("image" [, bounds, icon, {creation_properties}]);
bounds: Optional. The control’s position and size.
icon: Optional. The named resource for the icon or family of

icons displayed in the image control, or a pathname or File
object for an image file. Images must be in PNG format.

creation_properties: Optional. An object that contains the

following property:

name: A unique name for the control.
item

Array of
ListItem

The choice items in a list box or drop-down list. The objects are
created when items are specified on creation of the parent list
object, or afterward using the list control’s add() method.
Items in a drop-down list can be of type separator, in which case
they cannot be selected, and are shown as a horizontal line.
Item objects have these properties which are not found in other
controls:
checked
expanded
image
index
selected

listbox

ListBox

A list box with zero or more items. Calls the onChange callback if the
item selection is changed by a script or the user, or if the object’s
notify() method is called. A double click on an item selects that item
and calls the onDoubleClick callback.
To add to a window w:
w.add ("listbox", bounds [, items, {creation_properties}]);
bounds: Optional. The control’s position and size.
items: Optional. An array of strings for the text of each list item.
A ListItem object is created for each item. Supply this
argument, or the items property in creation_properties, not

both.

Type keyword

Control objects

Class name

listbox (cont’d)

Description
creation_properties: Optional. An object that contains any of

the following properties:

name: A unique name for the control.
multiselect: When false (the default), only one item can be

selected. When true, multiple items can be selected.

items: An array of strings for the text of each list item. A

ListItem object is created for each item. An item with the
text string "-" creates a separator item. Supply this
property, or the items argument, not both. This form is most
useful for elements defined using Resource specifications.
numberOfColumns: A number of columns in which to display
the items; default is 1. When there are multiple columns,
each ListItem object represents a single selectable row. Its
text and image values supply the label for the first column,
and the subitems property specifies labels for additional
columns.
showHeaders: True to display column titles.
columnWidths: An array of numbers for the preferred width

in pixels of each column.

columnTitles: A corresponding array of strings for the title
of each column, to be shown if showHeaders is true.
panel

Panel

A container for other types of controls, with an optional frame.
Containers have additional properties that control the children; see
:ref:`container-properties`. Hiding a panel hides all its
children. Making it visible makes visible those children that are not
individually hidden.
To add to a window w:
w.add ("panel" [, bounds, text, {creation_properties}]);
bounds: Optional. The element’s position and size. A panel

whose width is 0 appears as a vertical line. A panel whose height
is 0 appears as a horizontal line.

text: Optional. The text displayed in the border of the panel.

Type keyword

Control objects

Class name

panel (cont’d)

Description
creation_properties: Optional. An object that contains the

following property:

name: A unique name for the control.
borderStyle: A string that specifies the appearance of the
border drawn around the panel. One of black, etched,
gray, raised, sunken. Default is etched.
su1PanelCoordinates: When true, this panel automatically

adjusts the positions of its children for compatability with
Photoshop CS. Default is false, meaning that the panel does
not adjust the positions of its children, even if the parent
window has automatic adjustment enabled.

progressbar

Progressbar

A horizontal rectangle that shows progress of an operation. All
progressbar controls have a horizontal orientation. The value
property contains the current position of the progress indicator; the
default is 0. There is a minvalue property, but it is always 0; attempts
to set it to a different value are silently ignored.
To add to a window w:
w.add ("progressbar" [, bounds, value, minvalue,
maxvalue, creation_properties}]);
bounds: Optional. The control’s position and size.
value: Optional. The initial position of the progress indicator.

Default is 0.

minvalue: Optional. The minimum value that the value
property can be set to. Default is 0. Together with maxvalue,

defines the scrolling range.

maxvalue: Optional. The maximum value that the value
property can be set to. Default is 100. Together with minvalue,
defines the scrolling range.
creation_properties: Optional. An object that contains the

following property:

name: A unique name for the control.

Type keyword

Class name

Description

radiobutton

RadioButton

A dual-state control, grouped with other radiobuttons, of which only
one can be in the selected state. Shows the selected state when
value is true, empty when value is false. Calls the onClick callback if
the control is clicked or if its notify() method is called.
All radiobuttons in a group must be created sequentially, with no
intervening creation of other element types. Only one radiobutton
in a group can be set at a time; setting a different radiobutton
unsets the original one.
To add to a window w:
w.add ("radiobutton" [, bounds, text,
{creation_properties}]);
bounds: Optional. The control’s position and size.
text: Optional. The text displayed in the control.
creation_properties: Optional. An object that contains the

following property:

name: A unique name for the control.
scrollbar

Scrollbar

A scrollbar with a draggable scroll indicator and stepper buttons to
move the indicator. The scrollbar control has a horizontal
orientation if the width is greater than the height at creation time,
or vertical if its height is greater than its width.
Calls the onChange callback after the position of the indicator is
changed or if its notify() method is called. Calls the onChanging
callback repeatedly while the user is moving the indicator.
The value property contains the current position of the
scrollbar’s indicator within the scrolling area, within the range of
minvalue and maxvalue.
The stepdelta property determines the scrolling unit for the up
or down arrow; default is 1.
The jumpdelta property determines the scrolling unit for a
jump (as when the bar is clicked outside the indicator or arrows);
default is 20% of the range between minvalue and maxvalue.

Type keyword

Control objects

Class name

scrollbar (cont’d)

Description
To add to a window w:
w.add ("scrollbar" [, bounds, value, minvalue, maxvalue,
{creation_properties}]);
bounds: Optional. The control’s position and size.
value: Optional. The initial position of the scroll indicator.

Default is 0.

minvalue: Optional. The minimum value that the value
property can be set to. Default is 0. Together with maxvalue,

defines the scrolling range.

maxvalue: Optional. The maximum value that the value
property can be set to. Default is 100. Together with minvalue,
defines the scrolling range.
creation_properties: Optional. An object that contains the

following property:

name: A unique name for the control.
slider

Slider

A slider with a moveable position indicator. All slider controls have
a horizontal orientation. Calls the onChange callback after the
position of the indicator is changed or if its notify() method is called.
Calls the onChanging callback repeatedly while the user is moving
the indicator.
The value property contains the current position of the indicator
within the range of minvalue and maxvalue.
To add to a window w:
w.add ("slider" [, bounds, value, minvalue, maxvalue,
{creation_properties}]);
bounds: Optional. The control’s position and size.
value: Optional. The initial position of the indicator. Default is 0.
minvalue: Optional. The minimum value that the value
property can be set to. Default is 0. Together with maxvalue,
defines the range.
maxvalue: Optional. The maximum value that the value
property can be set to. Default is 100. Together with minvalue,
defines the range
creation_properties: Optional. An object that contains the

following property:

name: A unique name for the control.

Control objects

Type keyword

Class name

Description

statictext

StaticText

A text field that the user cannot change.

To add to a window w:
w.add ("statictext" [, bounds, text,
{creation_properties}]);
bounds: Optional. The control’s position and size.
text: Optional. The text displayed in the control.
creation_properties: Optional. An object that contains any of

the following properties:

name: A unique name for the control.
multiline: When false (the default), the control displays a
single line of text. When true, the control displays multiple
lines, in which case the text wraps within the width of the
control.
scrolling: When false (the default), the displayed text
cannot be scrolled. When true, the displayed text can be
vertically scrolled using scrollbars; this case implies
multiline is true.
truncate: If middle or end, defines where to remove
characters from the text and replace them with an ellipsis if
the specified title does not fit within the space reserved for
it. If none, and the text does not fit, characters are removed
from the end, without any replacement ellipsis character.
tab

Tab

A container for other types of controls. Differs from a Panel element
in that is must be a direct child of a TabbedPanel element, the title is
shown in the selection tab, and it does not have a script-definable
border. The currently active tab is the value of the parent’s
selection property.
Containers have additional properties that control the children; see
:ref:`container-properties`. Hiding a panel hides all its
children. Making it visible makes visible those children that are not
individually hidden.
To add a tab to a tabbed panel t in window w:
w.t.add ("tab" [, bounds, text,
{creation_properties}]);
bounds: Not used, pass undefined. The size and position is

determined by the parent.

text: Optional. The text displayed in the tab.

Type keyword

Control objects

Class name

tab (cont’d)

Description
creation_properties: Optional. An object that contains the

following property:

name: A unique name for the control.
tabbedpanel

TabbedPanel

A container for selectable Tab containers. Differs from a Panel
element in that it can contain only Tab elements as direct children.
Containers have additional properties that control the children; see
:ref:`container-properties`. Hiding a panel hides all its
children. Making it visible makes visible those children that are not
individually hidden.
The selected tab child is the value of the parent’s selection
property. One and only one of the tab children must be selected;
selecting one deselects the others. When the value of the selection
property changes, either by a user selecting a different tab, or by a
script setting the property, the tabbedpanel receives an onChange
notification.
To add to a window w:
w.add ("tabbedpanel" [, bounds, text,
{creation_properties}]);
bounds: Optional. The element’s position and size. This

determines the sizes and positions of the tab children.

text: Ignored.
creation_properties: Optional. An object that contains the

following property:

name: A unique name for the control.
treeview

TreeView

A hierarchical list whose items can contain child items. Items at any
level of the tree can be individually selected. Calls the onChange
callback if the item selection is changed by a script or the user, or if
the object’s notify() method is called.
To add to a window w:
w.add ("treeview" [, bounds, items,
{creation_properties}])
bounds: Optional. The control’s position and size.
items: Optional. An array of strings for the text of each top-level
list item. A ListItem object is created for each item. An item
with the type node can contain child items. Supply this
argument, or the items property in creation_properties, not

both.

Type keyword

Control objects

Class name

treeview (cont’d)

Description
creation_properties: Optional. An object that contains any of

the following properties:

name: A unique name for the control.
items: An array of strings for the text of each top-level list
item. A ListItem object is created for each item. An item
with the type node can contain child items. Supply this
property, or the items argument, not both. This form is most

useful for elements defined using Resource specifications.

.. _control-object-properties:

Control object properties
-------------------------
The following table shows the properties of ScriptUI control elements. Some values apply only to controls
of particular types, as indicated. See Container properties for properties that apply to container elements
(controls of type panel, tabbedpanel, tab, and group).
active

Boolean

When true, the object is active, false otherwise. Set to true to make a
given control or dialog active.
A modal dialog that is visible is by definition the active dialog.
An active palette is the front-most window.
An active control is the one with focus-that is, the one that
accepts keystrokes, or in the case of a Button, be selected when
the user types ENTER in Windows, or presses the spacebar in Mac
OS.

alignment

String or
Array of 2
Strings

Applies to child elements of a container. If defined, this value
overrides the alignChildren setting for the parent container.
For a single string value, allowed values depend on the orientation
value in the parent container. For orientation=row:
top
bottom

center (default)
fill

For orientation=column:
left
right

center (default)
fill

For orientation=stack:
top
bottom
left

right
center (default)
fill

Control objects

alignment (cont’d)

For an array value, the first string element defines the horizontal
alignment and the second element defines the vertical alignment.
The horizontal alignment value must be one of left, right, center
or fill. The vertical alignment value must be one of top, bottom,
center, or fill.
Values are not case sensitive.

bounds

Bounds

A Bounds object describing the boundaries of the element, in screen
coordinates for Window elements, and parent-relative coordinates for
child elements (compare windowBounds). For windows, the bounds
refer only to the window’s content region.
Setting an element’s size or location changes its bounds property,
and vice-versa.

characters

Number

Used by the LayoutManager object to determine the default
preferredSize for a StaticText or EditText control. The control will be
made wide enough to display the given number of 'X' characters in
the font used by the control. Setting this property is the best way to
reserve space in a control for a maximum number of characters to
display.

checked

Boolean

For ListItem objects only. When true, the item is marked with the
platform-appropriate checkmark. When false, no checkmark is drawn,
but space is reserved for it in the left margin, so that the item lines up
with other checkable items. When undefined, no space is reserved
for a checkmark.

columns

Object

For ListBox objects only. A JavaScript object with two read-only
properties whose values are set by the creation parameters:
titles - An array of column title strings, whose length matches

the number of columns specified at creation.

preferredWidths - An array of column widths, whose length

matches the number of columns specified at creation.
enabled

Boolean

When true, the control is enabled, meaning that it accepts input.
When false, control elements do not accept input, and all types of
elements have a dimmed appearance. A disabled ListItem is not
selectable in a ListBox, DropDownList or TreeView list.

expanded

Boolean

For ListItem objects of type node in TreeView list controls. When true,
the item is in the expanded state and its children are shown, when
false, it is collapsed and children are hidden.

graphics

Object

A ScriptUIGraphics object that can be used to customize the control’s
appearance, in response to the onDraw event.

helpTip

String

A brief help message (also called a tool tip) that is displayed in a small
floating window when the mouse cursor hovers over a user-interface
control element. Set to an empty string or null to remove help text.

icon

String or
File

Deprecated. Use image instead.

image

Control objects

Object

A ScriptUIImage object, or the name of an icon resource, or the
pathname or File object for a file that contains a platform-specific
image in PNG or JPEG format, or for a shortcut or alias to such a file.
For an IconButton, the icon appears as the content of the button.
For an Image, the image is the entire content of the image
element.
For a ListItem, the image is displayed to the left of the text.
If the parent is a multi-column ListBox, this is the display image
for the label in the first column, and labels for further columns are
specified in the subitems array. See :ref:`creating-multi-column-lists`.

indent

Number

A number of pixels by which to indent the element during automatic
layout. Applies for column orientation and left alignment, or row
orientation and top alignment.

index

Number

For ListItem objects only. The index of this item in the items
collection of its parent list control. Read only.

items

Array of
Object

For a list object (ListBox, DropDownList or TreeView list), a collection
of ListItem objects for the items in the list. Access by 0-based index. To
obtain the number of items in the list, use items.length. Read only.

itemSize

Dimension For a list object (ListBox, DropDownList or TreeView list), a Dimension
object describing the width and height in pixels of each item in the
list. Used by auto-layout to determine the preferredSize of the list,
if not otherwise specified.
If not set explicitly, the size of each item is set to match the largest
height and width among all items in the list

jumpdelta

Number

The amount to increment or decrement a Scrollbar indicator’s
position when the user clicks ahead or behind the moveable element.
Default is 20% of the range between the maxvalue and minvalue
property values.

justify

String

The justification of text in static text and edit text controls. One of:
left (default)
center
right

NOTE: Justification only works if the value is set on creation, using a
resource specification or creation parameters.

location

Control objects

Point

A Point object describing the location of the element as an array,

[x, y], representing the coordinates of the upper left corner of the
element. These are screen coordinates for Window elements, and

parent-relative coordinates for other elements.

The location is defined as [bounds.x, bounds.y]. Setting an
element’s location changes its bounds property, and vice-versa. By
default, location is undefined until the parent container’s layout
manager is invoked.
maximumSize

Dimension A Dimension object that specifies the maximum height and width for
an element.
The default is 50 pixels less than the screen size in each dimension. In
Windows, this can occupy the entire screen; you must define a
maximumSize to be large enough for your intended usage.

minimumSize

Dimension A Dimension object that specifies the minimum height and width for
an element. Default is [0,0].

maxvalue

Number

The maximum value that the value property can have.
If maxvalue is reset less than value, value is reset to maxvalue. If
maxvalue is reset less than minvalue, minvalue is reset to maxvalue.

minvalue

Number

The minimum value that the value property can have.
If minvalue is reset greater than value, value is reset to minvalue. If
minvalue is reset greater than maxvalue, maxvalue is reset to
minvalue.

parent

Object

The immediate parent object of this element. Read only.

preferredSize

Dimension A Dimension object used by layout managers to determine the best
size for each element. If not explicitly set by a script, value is
established by the user-interface framework in which ScriptUI is
employed, and is based on such attributes of the element as its text,
font, font size, icon size, and other user-interface framework-specific
attributes.
A script can explicitly set preferredSize before the layout manager
is invoked in order to establish an element size other than the default.
To set a specific value for only one dimension, specify the other
dimension as -1.

properties

Object

selected

Boolean

An object that contains one or more creation properties of the
element (properties used only when the element is created).
For ListItem objects only. When true, the item is part of the

selection for its parent list. When false, the item is not selected. Set

to true to select this item in a single-selection list, or to add it to the
selection array for a multi-selection list.

CHAPTER 4: User-Interface Tools

selection
(ListBox)

Control objects

Array of
ListItem

139

For a ListBox, an array of ListItem objects for the current selection in a
multi-selection list. Setting this value causes the selected item to be
highlighted and to be scrolled into view if necessary. If no items are
selected, the value is null. Set to null to deselect all items.
The value can also change because the user clicked or double-clicked
an item, or because an item was removed with remove() or
removeAll(). Whenever the value changes, the onChange callback is
called. If the value is changed by a double click, calls the
onDoubleClick callback.
You can set the value using the index of an item or an array of indices,
rather than object references. If set to an index value that is out of
range, the operation is ignored. When set with index values, the
property still returns object references.
If you set the value to an array for a single-selection list, only the
first item in the array is selected.
If you set the value to a single item for a multi-selection list, that
item is added to the current selection.

selection
(DropDownList,
TreeView)

ListItem

For a DropDownList or TreeView list object, the currently selected
ListItem object.
Setting this value causes the selected item to be highlighted and to
be scrolled into view if necessary. If no item is selected, the value is
null. Set to null to deselect all items.
The value can also change because the user clicked on an item, or
because an item was removed with remove() or removeAll().
Whenever the value changes, the onChange callback is called.
You can set the value using the index of an item or an array of indices,
rather than object references. If set to an index value that is out of
range, the operation is ignored. When set with an index value, the
property still returns an object reference.

shortcutKey

String

The key sequence that invokes the onShortcutKey callback for this
element (in Windows only).

size

Dimension A Dimension object that defines the actual dimensions of an element.
Initially undefined, and unless explicitly set by a script, it is defined
by a LayoutManager.
Although a script can explicitly set size before the layout manager is
invoked to establish an element size other than the preferredSize
or the default size, this is not recommended.
Defined as [bounds.width, bounds.height]. Setting an element’s
size changes its bounds property, and vice-versa.

stepdelta

Number

The amount by which to increment or decrement a Scrollbar
element’s position when the user clicks a stepper button.


subitems

Control objects

Array

For ListItem objects only. When the parent is a multi-column ListBox,
the ListItem.text and ListItem.image values describe the label in
the first column, and this specifies additional labels for that row in the
remaining columns.
This contains an array of JavaScript objects, whose length is one less
than the number of columns. Each member specifies a label in the
corresponding column, with the first member (subitems[0])
describing the label in the second column.
Each object has two properties, of which one or both can be supplied:
text - A localizable display string for this label.
image - An Image object for this label.

text

String

The title, label, or displayed text. Ignored for containers of type group.
For controls, the meaning depends on the control type. Buttons use
the text as a label, for example, while edit fields use the text to
access the content.
For ListItem objects, this is the display string for the list choice. If the
parent is a multi-column list box, this is the display string for the label
in the first column, and labels for further columns are specified in the
subitems array. See :ref:`creating-multi-column-lists`.
This is a localizable string: see :ref:`localization-in-scriptui-objects`.

textselection

String

The currently selected text in a control that displays text, or the empty
string if there is no text selected.
Setting the value replaces the current text selection and modifies the
value of the text property. If there is no current selection, inserts the
new value into the text string at the current insertion point. The
textselection value is reset to an empty string after it modifies the
text value.
NOTE: Setting the textselection property before the edittext
control’s parent Window exists is an undefined operation.

title

String

For a DropDownList, FlashPlayer, IconButton, Image, or TabbedPanel
only, a text label for the element. The title can appear to the left or
right of the element, or above or below it, or you can superimpose the
title over the center of the element. The placement is controlled by
the titleLayout value.


titleLayout

Control objects

Object


For a DropDownList, FlashPlayer, IconButton, Image, or TabbedPanel
with a title value, the way the text label is shown in relation to the
element. A JavaScript object with these properties:
alignment -The position of the title relative to the element, an
array of [horizontal_alignment, vertical_alignment]. For possible
alignment values, see :ref:`alignment`. Note that fill is
not a valid alignment value for either horizontal or vertical
alignment in this context.
characters - A number; if 1 or greater, reserves a title width
wide enough to hold the specified number of "X" characters in
the font for this element. If 0, the title width is calculated based
on the value of the title property during layout operations.
spacing - A number; 0 or greater. The number of pixels

separating the title from the element.

margins - An array of numbers, [left, top, right, bottom]

for the number of pixels separating each edge of an element and
the visible content within that element. This overrides the default
margins.
justify - One of 'left', 'center', or 'right', how to justify

the text when the space allocated for the title width is greater
than the actual width of the text.

truncate - If 'middle ' or 'end', defines where to remove
characters from the text and replace them with an ellipsis (...) if
the specified title does not fit within the space reserved for it. If
'none', and the text does not fit, characters are removed from
the end, without any replacement ellipsis character.
type

String

Contains the type name of the element, as specified on creation.
For Window objects, one of the type names window, palette, or
dialog.
For controls, the type of the control, as specified in the add
method that created it.
Read only.

value

Boolean

For a Checkbox or RadioButton, true if the control is in the selected or
set state, false if it is not.

value

Number

For a Scrollbar or Slider, the current position of the indicator. If set to a
value outside the range specified by minvalue and maxvalue, it is
automatically reset to the closest boundary.

visible

Boolean

When true, the element is shown, when false it is hidden.
When a container is hidden, its children are also hidden, but they
retain their own visibility values, and are shown or hidden accordingly
when the parent is next shown.


Control objects


window

Window

The Window object that contains this control. Read only.

windowBounds

Bounds

A Bounds object that contains the bounds of this control in the
containing window’s coordinates. Compare bounds, in which
coordinates are relative to the immediate parent container. Read only.

function_name

Function

For the FlashPlayer control, a function definition for a callback from
the Flash ActionScript environment.
There are no special naming requirements, but the function must
take and return only the supported data types:
Number
String
Boolean
Null

undefined
Object
Array

NOTE: The ActionScript class and date objects are not supported as
parameter values.

.. _control-object-functions:

Control object functions
------------------------
The following table shows the methods defined for each element type, and for specific control types as
indicated.
addEventListener()
controlObj.addEventListener (eventName, handler, capturePhase);
eventName

The event name string. Predefined event names include:
change
changing
move
moving
resize
resizing
show
enterKey
focus
blur
mousedown
mouseup
mousemove
mouseover
mouseout
keyup
keydown
click (detail = 1 for single, 2 for double)

handler

The function to register for the specified event in this target. This can be the name
of a function defined in the extension, or a locally defined handler function to be
executed when the event occurs.
A handler function takes one argument, an object of the UIEvent base class. See
:ref:`registering-event-listeners-for-windows-or-controls`.

capturePhase

Optional. When true, the handler is called only in the capturing phase of the event
propagation. Default is false, meaning that the handler is called in the bubbling
phase if this object is an ancestor of the target, or in the at-target phase if this
object is itself the target.

Registers an event handler for a particular type of event occurring in this control.
Returns undefined.


Control objects


dispatchEvent()
controlObj.dispatchEvent (eventObj)
eventObj

An object of the UIEvent base class.

Simulates the occurrence of an event in this target. A script can create an event object for a specific
event, using ScriptUI.events.events.createEvent(), and pass it to this method to start the event
propagation for the event.
Returns false if any of the registered listeners that handled the event called the event object’s
preventDefault() method, true otherwise.
find()
listObj.find(text)
text

The text of the item to find.

For list objects (ListBox, DropDownList or TreeView) only. Looks in this object’s items array for an
item object with the given text value.
Returns the item object if found; otherwise, returns null.
hide()
controlObj.hide()

Hides this container or control. When a window or container is hidden, its children are also hidden,
but when it is shown again, the children retain their own visibility states.
Returns undefined.
notify()
controlObj.notify([event])
event

Optional. The name of the control event handler to call. One of:
onClick
onChange
onChanging

By default, simulates the onChange event for an EditText control, an onClick event
for controls that support that event.
Sends a notification message, simulating the specified user interaction event.
Returns undefined.
removeEventListener()
controlbj.removeEventListener (eventName, handler[, capturePhase]);
eventName

The event name string.

handler

The function that was registered to handle the event.

capturePhase

Optional. Whether the handler was to respond only in the capture phase.

Unregisters an event handler for a particular type of event occurring in this control. All arguments
must be identical to those that were used to register the event handler.
Returns undefined.


Control objects


show()
controlObj.show()

Shows this container or control. When a window or container is hidden, its children are also hidden,
but when it is shown again, the children retain their own visibility states.
Returns undefined.
toString()
listItemObj.toString()

For ListItem controls only. Retrieves the value of this item’s text property as a string.
Returns a String.
valueOf()
listItemObj.valueOf()

For ListItem controls only. Retrieves the index number of this item in the parent list’s items array.
Returns a Number.

List control object functions
The following table shows the methods defined for list objects only.
add()
listObj.add (type, text[, index])
type

The type of item to add. One of:
item-A basic, selectable item with a text label.
separator-A separator. For dropdownlist controls only. In this case, the text value
is ignored, and the method returns null.

text

The localizable text label for the item.

index

Optional. The index into the current item list after which this item is inserted. If not
supplied, or greater than the current list length, the new item is added at the end.

For list objects (ListBox, DropDownList or TreeView) only. Adds an item to the items array at the
given index.
Returns the item control object for type=item, or null for type=separator.

remove()
containerObj.remove(index)
containerObj.remove(text)
containerObj.remove(child)
index
text
child

The item or child to remove, specified by 0-based index, text value, or as a control object.

For containers (Panel, Group), removes the specified child control from the container’s children
array.
For list objects (ListBox, DropDownList or TreeView) only, removes the specified item from this
object’s items array. No error results if the item does not exist.
Returns undefined.
removeAll()
listObj.removeAll()

For list objects (ListBox, DropDownList or TreeView) only. Removes all items from the object’s items
array.
Returns undefined.
revealItem()
listObj.revealItem(item)
item

The item or child to reveal, a control object.

For ListBox only. Scrolls the list to make the specified item visible, if necessary.
Returns undefined.

FlashPlayer control functions
These functions apply only to controls of type flashplayer.
NOTE: There are limitations on how these functions can be used to control playback of Flash movies:
Do not use stopMovie() and playMovie() to suspend and subsequently resume or restart an SWF
file produced by Flex™.
The stopMovie() and playMovie() sequence does not make sense for some SWF files produced by
Flash Authoring, depending on the exact details of how they were implemented. The sequence
may not correctly reset the file to the initial state (when the rewind argument to playMovie() is
true) nor suspend then resume the execution of the file (when rewind is false).
Using stopMovie() from the player’s hosting environment has no effect on an SWF file playing in a
ScriptUI Flash Player element. It is, however, possible to produce an SWF using Flash Authoring
that can stop itself in response to user interaction.
Do not call playMovie() when an SWF file is already playing.

invokePlayerFunction()
flashPlayerObj.invokePlayerFunction(fnName, [arg1[,...argn]] )
fnName

String. The name of a Flash ActionScript function that has been registered with the
ExternalInterface object by the currently loaded SWF file; see :ref:`calling-actionscript-functions-from-a-scriptui-script`.

args

Optional. One or more arguments to pass through to the function, of these types:
Number
String
Boolean
Null

undefined
Object
Array

Invokes an ActionScript function defined in the Flash application.
Returns the result of the invoked function, which must be one of the allowed types. The ActionScript
class and date objects are not supported as return values.
loadMovie()
flashPlayerObj.loadMovie(file)
file

The File object for the SWF file.

Loads a movie into the Flash Player, and begins playing it. If you do not specify an associated movie file
when creating the control, you must use this function to load one.
Returns undefined.
playMovie()
flashPlayerObj.playMovie(rewind)
rewind

When true, restarts the movie from the beginning; otherwise, starts playing from the point
where it was stopped.

Restarts a movie that has been stopped.
NOTE: Do not call when a movie is currently playing.
Returns undefined.
stopMovie()
flashPlayerObj.stopMovie()

Halts playback of the current movie.
NOTE: Does not work when called from the player’s hosting environment.
Returns undefined.

.. _control-event-handling-callbacks:

Control event-handling callbacks
--------------------------------
The following events are signalled in certain types of controls. To handle the event, define a function with
the corresponding name in the control object. Handler functions take no arguments and have no
expected return values; see :ref:`defining-behavior-with-event-callbacks-and-listeners`.
onActivate

Called when the user gives a control the keyboard focus by clicking it or tabbing into
it.

onClick

Called when the user clicks one of the following control types:
Button
Checkbox

onChange

IconButton
RadioButton

Called when the user finishes making a change in one of the following control types:
DropDownList
EditText
ListBox

Scrollbar
Slider
TreeView

For an EditText control, called only when the change is complete-that is, when
focus moves to another control, or the user types ENTER. The exact behavior
depends on the creation parameter enterKeySignalsOnChange; see the
edittext description.
For a Slider or Scrollbar, called when the user has finished dragging the position
marker or has clicked the control.
For a ListBox, DropDownList or TreeView control, called whenever the
selection property changes. This can happen when a script sets the property
directly or removes a selected item from the list, or when the user changes the
selection.
onChanging

Called for each incremental change in one of the following control types:
EditText
Scrollbar
Slider
For an EditText control, called for each keypress while the control has focus.
For a Slider or Scrollbar, called for any motion of the position marker.

onCollapse

Called when the user collapses (closes) a node in a TreeView control. The parameter
to this function is the ListItem node object that was collapsed.

onDeactivate

Called when the user removes keyboard focus from a previously active control by
clicking outside it or tabbing out of it.

onDoubleClick

Called when the user double clicks an item in a ListBox control. The list’s selection
property is set to the clicked item.

onDraw

Called when a container or control is about to be drawn. Allows the script to modify
or control the appearance, using the control’s associated ScriptUIGraphics object.
Handler takes one argument, a DrawState object.

onExpand

Called when the user expands (opens) a node in a TreeView control. The parameter
to this function is the ListItem node object that was expanded.

onShortcutKey

(In Windows only) Called when a shortcut-key sequence is typed that matches the
shortcutKey value for an element in the active window.

.. _drawstate-object:

DrawState object
----------------
A helper object that describes an input state at the time of the triggering onDraw event. Contains
properties that report whether the current control has the input focus, and the particular mouse button
and key-press state. There is no object constructor.

DrawState object properties
The object contains the following read-only properties:
altKeyPressed

Boolean

When true, the ALT key was pressed. (In Windows only.)

capsLockKeyPressed

Boolean

When true, the CAPSLOCK key was pressed.

cmdKeyPressed

Boolean

When true, the CMD key was pressed. (In Mac OS only.)

ctrlKeyPressed

Boolean

When true, the CTRL key was pressed.

hasFocus

Boolean

When true, the control containing this object has the input
focus.

leftButtonPressed

Boolean

When true, the left mouse button was pressed.

middleButtonPressed

Boolean

When true, the middle mouse button was pressed.

mouseOver

Boolean

When true, the cursor position was within the bounds of the
control containing this object.

numLockKeyPressed

Boolean

When true, the NUMLOCK key was pressed.

optKeyPressed

Boolean

When true, the OPT key was pressed. (In Mac OS only.)

rightButtonPressed

Boolean

When true, the right mouse button was pressed.

shiftKeyPressed

Boolean

When true, the SHIFT key was pressed.

