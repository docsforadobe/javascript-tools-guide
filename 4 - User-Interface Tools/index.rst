User-Interface Tools
Adobe provides the ScriptUI component, which works with the ExtendScript JavaScript interpreter to
provide JavaScript scripts with the ability to create and interact with user interface elements. It provides an
object model for windows and user-interface control elements within an Adobe application.
The first part of this chapter describes the features and programming model, with details of how you
can use JavaScript to build a user interface with ScriptUI objects.
"ScriptUI object reference" on page 105 provides reference details of the objects, properties, methods,
and creation parameters. You can also choose the ScriptUI Classes dictionary from the Help menu in
the ExtendScript Toolkit to inspect the objects in the Object Model Viewer.

Code examples for ScriptUI
The sample code distributed with the Adobe ExtendScript SDK includes code examples that specifically
demonstrate different ways of building and populating a ScriptUI dialog.
Building ScriptUI dialogs
SnpCreateDialog.jsx

Creates a very simple, modeless dialog (a palette) with OK
and Cancel button behavior.

SnpCreateUIAddMethod.jsx

Shows how to add controls to a dialog using the add
method.

SnpCreateUIResourceSpec.jsx

Shows how to define a resource string that creates the
control hierarchy in a dialog.

SnpCreateTreeView.jsx

Shows how to create a hierarchical list with subitems.

SnpCreateProgressBar.jsx

Shows how to create, initialize, and update a progress bar.

SnpCreateSlider.jsx

Shows how to create and handle input from a slider control.

UsingFlashPlayer.jsx

Shows how to create a Flash® Player, and use it to load a play
back a movie defined in an SWF file.

ActionScriptDemo.jsx

Shows how to communicate between the Adobe
application scripting environment and the ActionScript™
scripting environment of the Flash Player.

ColorSelector.jsx

Shows how to use the graphics objects to change colors in a
window.

ColorPicker.jsx

A more complex version of the color-selection dialog shows
how to use additional graphics objects, including fonts and
paths.

SnpAlignElements.jsx

Shows how to align elements along two dimensions in order
to control the relative positions of controls within rows and
columns.

62

CHAPTER 4: User-Interface Tools

ScriptUI programming model

SnpCreateDynamicScriptUI.jsx

Shows how to use automatic layout, switching component
layout between "row" and "stack" orientation.

AlertBoxBuilder1.jsx

Shows a way to use resource specifications. Uses the add()
method to build a dialog that collects values from the user,
and creates a resource string from those values. Saves the
string to a file, then uses it to build a new dialog. See "Using
resource strings" on page 79.

AlertBoxBuilder2.jsx

Shows another way to use a resource specification, building
the same user-input dialog itself from a resource string. See
"Using resource strings" on page 79.

SnpCustomLayoutManager.jsx

Shows how to create a customized layout manager. See
"Custom layout-manager example" on page 95.

63

ScriptUI programming model
ScriptUI defines Window objects that represent platform-specific windows, and various control elements
such as Button and StaticText, that represent user-interface controls. These objects share a common set
of properties and methods that allow you to query the type, move the element around, set the title,
caption or content, and so on. Many element types also have properties unique to that class of elements.

Creating a window
ScriptUI defines the following types of windows:
Modal dialog box: Holds focus when shown, does not allow activity in other application windows until
dismissed.
Floating palette: Also called modeless dialog, allows activity in other application windows. (Adobe
Photoshop® does not support script creation of palette windows.)
Main window: Suitable for use as an application’s main window. (Main windows are not normally
created by script developers for Adobe applications. Photoshop does not support script creation of
main windows.)
To create a new window, use the Window constructor function. The constructor takes the desired type of
the window. The type is "dialog" for a modal dialog, or "palette" for a modeless dialog or floating
palette. You can supply optional arguments to specify an initial window title and bounds; or you can set
the location and size separately.
The following example creates an empty dialog with the variable name dlg, which is used in subsequent
examples:
// Create an empty dialog window near the upper left of the screen
var dlg = new Window(’dialog’, ’Alert Box Builder’);
dlg.frameLocation = [100,100];

Initially, new windows are hidden. The show method makes them visible and responsive to user
interaction; for example:
dlg.show();

CHAPTER 4: User-Interface Tools

ScriptUI programming model

64

Container elements
All Windows are containers-that is, they contain other elements within their bounds. Within a Window, you
can create other types of container elements: Panels and Groups. These can contain control elements,
and can also contain other Panel and Group containers. However, a Window cannot be added to any
container.
A Group is the simplest container used to visually organize related controls. You would typically define
a group and populate it with related elements, for instance an edittext box and its descriptive
statictext label.
A Panel is a frame object, also typically used to visually organize related controls. It has a text property
to specify a title, and can have a border to visually separate the collection of elements from other
elements of a dialog.
A TabbedPanel is a frame that contains only Tab elements. Each Tab is a frame with a localizable title
in the selection tab, which contains a set of controls. When a tab is active, the Tab object is the value of
the TabbedPanel.selection property.
You might create a Panel and populate it with several Groups, each with their own elements. You can
create nested containers, with different layout properties for different containers, in order to define a
relatively complex layout without any explicit placement.
You can add elements to any container using the add method (see "Adding elements to containers" on
page 65). An element added to a container is considered a child of that container. Certain operations on a
container apply to its children; for example, when you hide a container, its children are also hidden.

Window layout
When a script creates a Window and adds various user-interface elements to it, the locations and sizes of
elements and spacing between elements is known as the layout of the window. Each user-interface
element has properties which define its location and dimensions: location, size, and bounds. These
properties are initially undefined, and a script that employs Automatic layout should leave them
undefined for the main window as well as its contained elements, allowing the automatic layout
mechanism to set their values.
Your script can access these values, and (if not using auto-layout) set them as follows:
The location of a window is defined by a Point object containing a pair of coordinates (x and y) for
the top left corner (the origin), specified in the screen coordinate system. The location of an element
within a window or other container is defined as the origin point specified in the container’s
coordinate system. That is, the x and y values are relative to the origin of the container.
The following examples show equivalent ways of placing the content region of an existing window at
screen coordinates [10, 50]:
win.location = [10, 50];
win.location = {x:10, y:50};
win.location = "x:10, y:50";

The size of an element’s region is defined by a Dimension object containing a width and height in
pixels.

CHAPTER 4: User-Interface Tools

ScriptUI programming model

65

The following examples show equivalent ways of changing an existing window’s width and height to
200 and 100:
win.size = [200, 100];
win.size = {width:200, height:100};
win.size = "width:200, height:100";

This example shows how to change a window’s height to 100, leaving its location and width
unchanged:
win.size.height = 100;

The bounds of an element are defined by a Bounds object containing both the origin point (x, y) and
size (width, height) To define the size and location of windows and controls in one step, use the
bounds property.
The value of the bounds property can be a string with appropriate contents, an inline JavaScript
Bounds object, or a four-element array. The following examples show equivalent ways of placing a 380
by 390 pixel window near the upper left corner of the screen:
var dlg = new Window(’dialog’, ’Alert Box Builder’, [100,100,480,490]);
dlg.bounds = [100,100,480,490];
dlg.bounds = {x:100, y:100, width:380, height:390};
dlg.bounds = {left:100, top:100, right:480, bottom:490};
dlg.bounds = "left:100, top:100, right:480, bottom:490";

The window dimensions define the size of the content region of the window, or that portion of the window
that a script can directly control. The actual window size is typically larger, because the host platform’s
window system typically adds title bars and borders. The bounds property for a Window refers only to its
content region. To determine the bounds of the frame surrounding the content region of a window, use
the Window.frameBounds property.

Adding elements to containers
To add elements to a window, panel, or group, use the container’s add method. This method accepts the
type of the element to be created and some optional parameters, depending on the element type. It
creates and returns an object of the specified type.
In additions to windows, ScriptUI defines the following user-interface elements and controls:
Panels (frames) and groups, to collect and organize other control types
Push buttons with text or icons, radio buttons, checkbox buttons
Static text or images, edit text
Progress bars, scrollbars, sliders
Lists, which include list boxes, drop-down (also called popup) lists, and tree views. Each item in a list is
a control of type item, and the parent list’s items property contains an array of child items. Tree views
can also have collapsible node-type items, which contain child items. You can add list items with the
parent’s add method.
You can specify the initial size and position of any new element relative to the working area of the parent
container, in an optional bounds parameter. Different types of elements have different additional
parameters. For elements which display text, for example, you can specify the initial text. See the ScriptUI
Classes dictionary in the ExtendScript Toolkit’s Object Model Viewer for details.

CHAPTER 4: User-Interface Tools

ScriptUI programming model

66

The order of optional parameters must be maintained. Use the value undefined for a parameter you do
not wish to set. For example, if you want to use automatic layout to determine the bounds, but still set the
title and text in a panel and button, the following creates Panel and Button elements with an initial text
value, but no bounds value:
dlg.btnPnl = dlg.add(’panel’, undefined, ’Build it’);
dlg.btnPnl.testBtn = dlg.btnPnl.add(’button’, undefined, ’Test’);

TIP: This example creates a dynamic property, btnPnl, on the parent window object, which contains the
returned reference to the child control object. This is not required, but provides a useful way to access your
controls.
A new element is initially set to be visible, but is not shown unless its parent object is shown.

Creation properties
Some element types have attributes that can only be specified when the element is created. These are not
normal properties of the element, in that they cannot be changed during the element’s lifetime, and they
are only needed once. For these element types, you can supply an optional creation-properties
argument to the add method. This argument is an object with one or more properties that control aspects
of the element’s appearance, or special functions such as whether an edit text element is editable or Read
only. See "Control object constructors" on page 123 for details.
You can also specify the creation properties for new objects using the resource specification format; for
details, see "Resource specifications" on page 78.
All user-interface elements have an optional creation property called name, which assigns a name for
identifying that element. For example, the following creates a new Button element with the name ok:
dlg.btnPnl.buildBtn = dlg.btnPnl.add(‘button’, undefined, ‘Build’, {name:’ok’});

NOTE: In Photoshop CS, panel coordinates were measured from outside the frame (including the title bar),
but in Photoshop CS2, panel coordinates are measured from the inside the frame (the content area). This
means that if you use the same values to set the vertical positions of child controls in a panel, the positions
are slightly different in the two versions. When you add a panel to a window, you can choose to set a
creation property (su1PanelCoordinates), which causes that panel to automatically adjust the positions
of its children; see the add method for panel. When automatic adjustment is enabled, you provide
position values that were correct for Photoshop CS, and the result is the same in Photoshop CS2, CS3, CS4,
CS5, or CC. You can also set automatic adjustment for a window; in this case, it applies to all child panels of
that window unless it is explicitly disabled in the child panel. See Window object constructor.

Accessing child elements
A reference to each element added to a container is appended to the container’s children property. You
can access the child elements through this array, using a 0-based index. For controls that are not
containers, the children collection is empty.
In this example, the msgPnl panel was the first element created in dlg, so the script can access the panel
object at index 0 of the parent’s children property to set the text for the title:
var dlg = new Window('dialog', 'Alert Box Builder');
dlg.msgPnl = dlg.add('panel');
dlg.children[0].text = 'Messages';

CHAPTER 4: User-Interface Tools

Types of controls

67

If you use a creation property to assign a name to a newly created element, you can access that child by its
name, either in the children array of its parent, or directly as a property of its parent. For example, the
Button in a previous example was named ok, so it can be referenced as follows:
dlg.btnPnl.children['ok'].text = "Build";
dlg.btnPnl.ok.text = "Build";

You can also access named elements through the parent window’s findElement() method:
var myOkButton = dlg.findElement("ok");

For list controls (type list and dropdown), you can access the child list-item objects through the items
array.

Removing elements
To remove elements from a Window, Panel, or Group, use the container’s remove method. This method
accepts an object representing the element to be removed, or the name of the element, or the index of the
element in the container’s children collection (see "Accessing child elements" on page 66).
The specified element is removed from view if it was currently visible, and it is no longer accessible from
the container or window. The results of any further references by a script to the object representing the
element are undefined.
To remove list items from a list, use the parent list control’s remove method in the same way. It removes the
item from the parent’s items list, hides it from view, and deletes the item object.

Types of controls
The following sections introduce the types of controls you can add to a Window or other container element
(panel or group). For details of the properties and functions, and of how to create each type of element,
see "Control object constructors" on page 123.

Containers
These are types of Control objects which are contained in windows, and which contain and group other
controls.
Panel

Typically used to visually organize related controls.
Set the text property to define a title that appears at the top of the panel.
An optional borderStyle creation property controls the appearance of the border
drawn around the panel.
You can use panels as separators: those with width of 0 appear as vertical lines and
those with height of 0 appear as horizontal lines.
var dlg = new Window(’dialog’, ’Alert Box Builder’);
dlg.msgPnl = dlg.add(’panel’, [25,15,355,130], ’Messages’);

CHAPTER 4: User-Interface Tools

Types of controls

Group

Used to visually organize related controls. Unlike Panels, Groups have no title or
visible border. You can use them to create hierarchies of controls, and for fine control
over layout attributes of certain groups of controls within a larger panel. For examples,
see "Creating more complex arrangements" on page 92.

TabbedPanel

A panel that contains only Tab objects as its immediate children. It has a selection
property that contains the currently active Tab child. When the value of the selection
property changes, either by a user selecting a different tab, or by a script setting the
property, the TabbedPanel receives an onChange notification.

68

The title property provides an optional label; the titleLayout property places the
label within the panel.
Tab

A general container whose parent is a TabbedPanel, with a selectable tab showing a
localizable text value. Its size and position are determined by the parent.

User-interface controls
These are types of Control objects that are contained in windows, panels, and groups, and that provide
specific kinds of display and user interaction. Control instances are created by passing the corresponding
type keyword to the add() method of a Window or container; see "Control types and creation parameters"
on page 124.
These examples do not set bounds explicitly on creation, because it is often more useful to set a preferred
size, then allow the layout manager to set the bounds; see "Automatic layout" on page 86.
Button

Typically used to initiate some action from a window when a user clicks the button;
for example, accepting a dialog’s current settings, canceling a dialog, bringing up a
new dialog, and so on.
Set the text property to assign a label to identify a Button’s function.
The onClick callback method provides behavior.
var dlg = new Window(‘dialog’, ‘Alert Box Builder’);
dlg.btnPnl = dlg.add(‘panel’, undefined, ‘Build it’);
dlg.btnPnl.testBtn = dlg.btnPnl.add(‘button’, undefined, ‘Test’);
dlg.btnPnl.buildBtn = dlg.btnPnl.add(‘button’, undefined, ‘Build’,
{name:’ok’});
dlg.btnPnl.cancelBtn = dlg.btnPnl.add(‘button’, undefined, ‘Cancel’,
{name:’cancel’});
dlg.show();

IconButton

A button that displays an icon, with or without a text label. Like a text button, typically
initiates an action in response to a click.
The image property identifies the icon image; see "Displaying images" on
page 72.
The title or text property provides an optional label; the titleLayout property
places the label with respect to the image.
The onClick callback method provides behavior.

CHAPTER 4: User-Interface Tools

Image

Types of controls

Displays an iconic image.
The image property identifies the icon image; see "Displaying images" on
page 72.
The title property provides an optional label; the titleLayout property places
the label with respect to the image.

StaticText

Typically used to display text strings that are not intended for direct manipulation by
a user, such as informative messages or labels.
This example creates a Panel and adds several StaticText elements:
var dlg = new Window(‘dialog’, ‘Alert Box Builder’);
dlg.msgPnl = dlg.add(‘panel’, undefined, ‘Messages’);
dlg.msgPnl.titleSt = dlg.msgPnl.add(‘statictext’, undefined,
‘Alert box title:’);
dlg.msgPnl.msgSt = dlg.msgPnl.add(‘statictext’, undefined,
‘Alert message:’);
dlg.show();

EditText

Allows users to enter text, which is returned to the script when the dialog is
dismissed. Text in EditText elements can be selected, copied, and pasted.
Set the text property to assign the initial displayed text in the element, and read
it to obtain the current text value, as entered or modified by the user.
Set the textselection property to replace the current selection with new text,
or to insert text at the cursor (insertion point). Read this property to obtain the
current selection, if any.
This example adds some EditText elements, with initial values that a user can accept
or replace:
var dlg = new Window(‘dialog’, ‘Alert Box Builder’);
dlg.msgPnl = dlg.add(‘panel’, undefined, ‘Messages’);
dlg.msgPnl.titleSt = dlg.msgPnl.add(‘statictext’, undefined,
‘Alert box title:’);
dlg.msgPnl.titleEt = dlg.msgPnl.add(‘edittext’, undefined,
‘Sample Alert’);
dlg.msgPnl.msgSt = dlg.msgPnl.add(‘statictext’, undefined,
‘Alert message:’);
dlg.msgPnl.msgEt = dlg.msgPnl.add(‘edittext’, undefined,
‘<your message here>’, {multiline:true});
dlg.show();

Note the creation property on the second EditText field, where multiline:true
indicates a field in which a long text string can be entered. The text wraps to appear
as multiple lines.

69

CHAPTER 4: User-Interface Tools

Checkbox

Types of controls

Allows the user to set a boolean state.
Set the text property to assign an identifying text string that appears next to the
clickable box.
The user can click to select or deselect the box, which shows a checkmark when
selected. The value is true when it is selected (checked) and false when it is not.
When you create a Checkbox, you can set its value property to specify its initial state
and appearance.
// Add a checkbox to control the buttons that dismiss an alert box
dlg.hasBtnsCb = dlg.add(‘checkbox’, undefined,
‘Should there be alert buttons?’);
dlg.hasBtnsCb.value = true;

RadioButton

Allows the user to select one choice among several.
Set the text property to assign an identifying text string that appears next to the
clickable button.
The value is true when the button is selected. The button shows the state in a
platform-specific manner, with a filled or empty dot, for example.
You group a related set of radio buttons by creating all the related elements one after
another. When any button’s value becomes true, the value of all other buttons in the
group becomes false. When you create a group of radio buttons, you should set the
state of one of them true:
var dlg = new Window(‘dialog’, ‘Alert Box Builder’);
dlg.alertBtnsPnl = dlg.add(‘panel’, undefined, ‘Button alignment’);
dlg.alertBtnsPnl.alignLeftRb = dlg.alertBtnsPnl.add(‘radiobutton’,
undefined, ‘Left’);
dlg.alertBtnsPnl.alignCenterRb = dlg.alertBtnsPnl.add(‘radiobutton’,
undefined, ‘Center’);
dlg.alertBtnsPnl.alignRightRb = dlg.alertBtnsPnl.add(‘radiobutton’,
undefined, ‘Right’);
dlg.alertBtnsPnl.alignCenterRb.value = true;
dlg.show();

Progressbar

Typically used to display the progress of a time-consuming operation. A colored bar
covers a percentage of the area of the control, representing the percentage
completion of the operation. The value property reflects and controls how much of
the visible area is colored, relative to the maximum value (maxvalue). By default the
range is 0 to 100, so the value=50 when the operation is half done.

Slider

Typically used to select within a range of values. The slider is a horizontal bar with a
draggable indicator, and you can click a point on the slider bar to jump the indicator
to that location. The value property reflects and controls the position of the indicator,
within the range determined by minvalue and maxvalue. By default the range is 0 to
100, so setting value=50 moves the indicator to the middle of the bar.

70

CHAPTER 4: User-Interface Tools

Scrollbar

Types of controls

Like a slider, the scrollbar is a bar with a draggable indicator. It also has "stepper"
buttons at each end, that you can click to jump the indicator by the amount in the
stepdelta property. If you click a point on the bar outside the indicator, the indicator
jumps by the amount in the jumpdelta property.
You can create scrollbars with horizontal or vertical orientation; if width is greater
than height, it is horizontal, otherwise it is vertical. Arguments to the add method
that creates the scrollbar define values for the value, minvalue and maxvalue
properties.
Scrollbars are often created with an associated EditText field to display the current
value of the scrollbar, and to allow setting the scrollbar’s position to a specific value.
This example creates a scrollbar with associated StaticText and EditText elements
within a panel:
dlg.sizePnl = dlg.add(‘panel’, undefined, ‘Dimensions’);
dlg.sizePnl.widthSt = dlg.sizePnl.add(‘statictext’, undefined,
‘Width:’);
dlg.sizePnl.widthScrl = dlg.sizePnl.add(‘scrollbar’, undefined,
300, 300, 800);
dlg.sizePnl.widthEt = dlg.sizePnl.add(‘edittext’);

ListBox
DropDownList
TreeView

These controls display lists of items, which are represented by ListItem objects in
the items property. You can access the items in this array using a 0-based index.
A ListBox control displays a list of choices. When you create the object, you
specify whether it allows the user to select only one or multiple items. If a list
contains more items than can be displayed in the available area, a scrollbar may
appear that allows the user to scroll through all the list items. A list box can
display items in multiple columns; see "Creating multi-column lists" on page 73.
A DropDownList control displays a single visible item. When you click the control,
a list drops down and allows you to select one of the other items in the list.
Drop-down lists can have nonselectable separator items for visually separating
groups of related items, as in a menu.
A TreeView control is similar to a ListBox, except that the items can have child
items. Items with children can be expanded or collapsed to show or hide the child
items. Child items can in turn contain children.
The title property provides an optional label; the titleLayout property places
the label with respect to the list.
You can specify the choice items on creation of the list object, or afterward using the
list object’s add() method. You can remove items programmatically with the list
object’s remove() and removeAll() methods.

71

CHAPTER 4: User-Interface Tools

ListItem

Types of controls

72

Items added to or inserted into any type of list control are ListItem objects, with
properties that can be manipulated from a script. ListItem elements can be of the
following types:
item: the typical item in any type of list. It displays text or an image, and can be
selected. To display an image, set the item object’s image property; see

"Displaying images" on page 72.

separator: a separator is a nonselectable visual element in a drop-down list.
Although it has a text property, the value is ignored, and the item is displayed as

a horizontal line.

node: a displayable and selectable item in a TreeView control which can contain
other ListItem objects, including other items of type node.
FlashPlayer

Runs a Flash movie within a ScriptUI window. Its control’s methods allow you to load a
movie from an SWF file and control the playback. See "FlashPlayer control functions"
on page 145.
You can also use the control object to communicate with the Flash application, calling
ActionScript methods, and making JavaScript methods defined in your Adobe
application script available to the Flash ActionScript code. See "Calling ActionScript
functions from a ScriptUI script" on page 86.
The title property provides an optional label; the titleLayout property places the
label with respect to the player.

Displaying images
You can display icon images in Image or IconButton controls, or display images in place of strings or in
addition to strings as the selectable items in a Listbox or DropdownList control. In each case, the image
is defined by setting the element’s image property. You can set it to a ScriptUIImage object; a named icon
resource; a File object; or the pathname of a file containing the iconic image, or of an alias or shortcut to
that file (see "Specifying paths" on page 39).
The image data for an icon can be in Portable Network Graphics (PNG) format, or in Joint Photographic
Experts Group (JPEG) format. See http://www.libpng.org and http://www.jpeg.org/ for detailed
information on these formats.
You can set or reset the image property at any time to change the image displayed in the element.
The scripting environment can define icon resources, which are available to scripts by name. To specify an
icon resource, set a control’s image property to the resource’s JavaScript name, or refer to the resource by
name when creating the control. For example, to create a button with an application-defined icon
resource:
myWin.upBtn = myWin.add ("iconbutton", undefined, "SourceFolderIcon");

Photoshop CC, for example, defines these icon resources:
Step1Icon
Step2Icon
Step3Icon
Step4Icon
SourceFolderIcon
DestinationFolderIcon

CHAPTER 4: User-Interface Tools

Types of controls

73

If a script does not explicitly set the preferredSize or size property of an element that displays a icon
image, the value of preferredSize is determined by the dimensions of the iconic image. If the size values
are explicitly set to dimensions smaller than those of the actual image graphic, the displayed image is
clipped. If they are set to dimensions larger than those of the image graphic, the displayed image is
centered in the larger space. An image is never scaled to fit the available space.

Creating multi-column lists
In list controls (ListBox, DropDownList, TreeView), a set of ListItem objects represents the individual
choices in the list. Each choice can be labeled with a localizable string, an image, or both, as specified by
the text and image properties of the ListItem (see "Displaying images" on page 72).
You can define a ListBox to have multiple columns, by specifying the numberOfColumns creation
parameter. By default, the number of columns is 1. If you specify multiple columns, you can also use the
creation parameters to specify whether headers are shown, and the header text for each column.
If you specify more than one column, each ListItem object that you add to the box specifies one selectable
row. The text and image of the ListItem object specifies the label in the first column, and the subitems
property specifies labels that appear in that row for the remaining columns.
The subitems value is an array, whose length is one less than the number of columns. That is, the first
member, ListItem.subitems[0], specifies the label in the second column. Each member specifies one
label, as a JavaScript object with two properties:
{ text : displayString , image : imageFileReference }

For example, the following fragment defines a list box with two columns, and specifies the labels in each
column for the two choices:
...
// create list box with two titled columns
var list = dlg.add ('ListBox', [0, 0, 150, 75], 'asd',
{numberOfColumns: 2, showHeaders: true,
columnTitles: ['First Name', 'Last Name']});
// add an item for the first row, with the label value for the first column
var item1 = list.add ('item', 'John');
// add the label value for the second column in that row.
item1.subItems[0].text = 'Doe';
// add an item for the second row, with the text for the first column label
var item2 = list.add ('item', 'Jane');
// add the label text and image for the second column in the second row
item2.subItems[0].text = 'Doe';
item2.subItems[0].image = File ("~/Desktop/Step1.png");
...

This creates a control that looks like this:

CHAPTER 4: User-Interface Tools

Types of controls

74

Notice that the columns have headers, and the label in the second column of the second row has both text
and an image.

Prompts and alerts
Static functions on the Window class are globally available to display short messages in standard dialogs.
The host application controls the appearance of these simple dialogs, so they are consistent with other
alert and message boxes displayed by the application. You can often use these standard dialogs for simple
interactions with your users, rather than designing special-purpose dialogs of your own.
Use the static functions alert, confirm, and prompt on the Window class to invoke these dialogs with your
own messages. You do not need to create a Window object to call these functions.

Modal dialogs
A modal dialog is initially invisible. Your script invokes it using the show method, which does not return
until the dialog has been dismissed. The user can dismiss it by using a platform-specific window gesture,
or by using one of the dialog controls that you supply, typically an OK or Cancel button. The onClick
method of such a button must call the close or hide method to close the dialog. The close method
allows you to pass a value to be returned by the show method.
For an example of how to define such buttons and their behavior, see "Defining behavior with event
callbacks and listeners" on page 80.

Creating and using modal dialogs
A dialog typically contains some controls that the user must interact with, to make selections or enter
values that your script will use. In some cases, the result of the user action is stored in the object, and you
can retrieve it after the dialog has been dismissed. For example, if the user changes the state of a Checkbox
or RadioButton, the new state is found in the control’s value property.
However, if you need to respond to a user action while the dialog is still active, you must assign the control
a callback function for the interaction event, either onClick or onChange. The callback function is the
value of the onClick or onChange property of the control.
For example, if you need to validate a value that the user enters in a edittext control, you can do so in an
onChange callback handler function for that control. The callback can perform the validation, and perhaps

display an alert to inform the user of errors.

Sometimes, a modal dialog presents choices to the user that must be correct before your script allows the
dialog to be dismissed. If your script needs to validate the state of a dialog after the user clicks OK, you can
define an onClose event handler for the dialog. This callback function is invoked whenever a window is

CHAPTER 4: User-Interface Tools

Types of controls

75

closed. If the function returns true, the window is closed, but if it returns false, the close operation is
cancelled and the window remains open.
Your onClose handler can examine the states of any controls in the dialog to determine their correctness,
and can show alert messages or use other modal dialogs to alert the user to any errors that must be
corrected. It can then return true to allow the dialog to be dismissed, or false to allow the user to correct
any errors.

Dismissing a modal dialog
Every modal dialog should have at least one button that the user can click to dismiss the dialog. Typically
modal dialogs have an OK and a Cancel button to close the dialog with or without accepting changes that
were made in it.
You can define onClick callbacks for the buttons that close the parent dialog by calling its close method.
You have the option of sending a value to the close method, which is in turn passed on to and returned
from the show method that invoked the dialog. This return value allows your script to distinguish different
closing events; for example, clicking OK can return 1, clicking Cancel can return 2. However, for this typical
behavior, you do not need to define these callbacks explicitly; see "Default and cancel elements" on
page 75.
For some dialogs, such as a simple alert with only an OK button, you do not need to return any value. For
more complex dialogs with several possible user actions, you might need to distinguish more outcomes. If
you need to distinguish more than two closing states, you must define your own closing callbacks rather
than relying on the default behavior.
If, by mistake, you create a modal dialog with no buttons to dismiss it, or if your dialog does have buttons,
but their onClick handlers do not function properly, a user can still dismiss the dialog by typing ESC. In this
case, the system will execute a call to the dialog’s close method, passing a value of 2. This is not, of course,
a recommended way to design your dialogs, but is provided as an escape hatch to prevent the application
from hanging in case of an error in the operations of your dialog.

Default and cancel elements
The user can typically dismiss a modal dialog by clicking an OK or Cancel button, or by typing certain
keyboard shortcuts. By convention, typing ENTER is the same as clicking OK or the default button, and
typing ESC is the same as clicking Cancel. The keyboard shortcut has the same effect as calling notify for
the associated button control.
To determine which control is notified by which keyboard shortcut, set the Dialog object’s
defaultElement and cancelElement properties. The value is the control object that should be notified
when the user types the associated keyboard shortcut.
For buttons assigned as the defaultElement, if there is no onClick handler associated with the
button, clicking the button or typing ENTER calls the parent dialog’s close method, passing a value of 1
to be returned by the show call that opened the dialog.
For buttons assigned as the cancelElement, if there is no onClick handler associated with the
button, clicking the button or typing ESC calls the parent dialog’s close method, passing a value of 2
to be returned by the show call that opened the dialog.
If you do not set the defaultElement and cancelElement properties explicitly, ScriptUI tries to choose
reasonable defaults when the dialog is about to be shown for the first time. For the default element, it
looks for a button whose name or text value is "ok" (disregarding case). For the cancel element, it looks for

CHAPTER 4: User-Interface Tools

Size and location objects

76

a button whose name or text value is "cancel" (disregarding case). Because it looks at the name value first,
this works even if the text value is localized. If there is no suitable button in the dialog, the property value
remains null, which means that the keyboard shortcut has no effect in that dialog.
To make this feature most useful, it is recommended that you always provide the name creation property
for buttons meant to be used in this way.

Size and location objects
ScriptUI defines objects to represent the complex values of properties that place and size windows and
user-interface elements. These objects cannot be created directly, but are created when you set the
corresponding property. That property then returns that object. For example, the bounds property returns
a Bounds object.
You can set these properties as objects, strings, or arrays.
e.prop = Object - The object must contain the set of properties defined for this type, as shown in
the table below. The properties have integer values.
e.prop = String - The string must be an executable JavaScript inline object declaration,
conforming to the same object description.
e.prop = Array - The array must have integer coordinate values in the order defined for this type,

as shown in the table below. For example:

The following examples show equivalent ways of placing a 380 by 390 pixel window near the upper left
corner of the screen:
var dlg = new Window(’dialog’, ’Alert Box Builder’);
dlg.bounds = {x:100, y:100, width:380, height:390}; //object
dlg.bounds = {left:100, top:100, right:480, bottom:490}; //object
dlg.bounds = "x:100, y:100, width:380, height:390"; //string
dlg.bounds = "left:100, top:100, right:480, bottom:490"; //string
dlg.bounds = [100,100,480,490]; //array

You can access the resulting object as an array with values in the order defined for the type, or as an object
with the properties supported for the type.

Size and location object types
The following table shows the property-value object types, the element properties that create and contain
them, and their array and object-property formats.

CHAPTER 4: User-Interface Tools

Bounds

Drawing objects

77

Defines the boundaries of a window within the screen’s coordinate space, or of a
user-interface element within the container’s coordinate space. Contains an array, [left,
top, right, bottom], that defines the coordinates of the upper left and lower right
corners of the element.
A Bounds object is created when you set an element’s bounds property, and this property
returns a Bounds object.
An object must contain properties named left, top, right, bottom, or x, y, width,
height.
An array must have values in the order [left, top, right, bottom].

Dimension

Defines the size of a Window or user-interface element. Contains an array, [width,
height], that defines the element’s size in pixels.
A Dimension object is created when you set an element’s size or preferredSize
property. (A preferredSize of -1 causes the size to be calculated automatically.)
An object must contain properties named width and height.
An array must have values in the order [width, height].

Margins

Defines the number of pixels between the edges of a container and its outermost child
elements. Contains an array [left, top, right, bottom] whose elements define the
margins between the left edge of a container and its leftmost child element, and so on.
A Margins object is created when you set an element’s margins property.
An object must contain properties named left, top, right, and bottom.
An array must have values in the order [left, top, right, bottom].
You can also set the margins property to a number; all of the array values are then set to
this number.

Point

Defines the location of a Window or user-interface element. Contains an array, [x, y],
whose values represent the origin point of the element as horizontal and vertical pixel
offsets from the origin of the element's coordinate space.
A Point object is created when you set an element’s location property.
An object must contain properties named x and y.
An array must have values in the order [x, y].

Drawing objects
ScriptUI allows you to draw directly on controls to customize their appearance. You do this by calling
methods of the ScriptUIGraphics object in response to the onDraw event (see "Defining behavior with
event callbacks and listeners" on page 80). These methods take as parameters a number of helper objects
that encapsulate drawing information, including the following:

CHAPTER 4: User-Interface Tools

Resource specifications

ScriptUIGraphics

Encapsulates the drawing methods. The graphics object is associated with each
control is found in the control object’s graphics property.

ScriptUIBrush

Describes the brush used to paint textures in a control.

ScriptUIFont

Describes the font used to write text into a control.

ScriptUIImage

Describes an image to be drawn in a control.

ScriptUIPath

Describes a drawing path for a figure to be drawn into a control.

ScriptUIPen

Describes the pen used to draw lines in a control.

78

For details of these objects, see "Graphic customization objects" on page 155.
The ScriptUIGraphics object contains methods that create the other graphics objects; for example,
ScriptUIGraphics.newBrush()creates a ScriptUIBrush instance with a specific color. These graphic
objects are then used as property values in the ScriptUIGraphics object, which controls how a
user-interface element is drawn on the screen. For example, if you put the new Brush object in the
backgroundColor property, the element is drawn using that color for the background.
To make the background of a window light gray, you could use this code:
g = myWindow.graphics;
myBrush = g.newBrush(g.BrushType.SOLID_COLOR, [0.75, 0.75, 0.75, 1]);
g.backgroundColor = myBrush;

These examples in the Adobe ExtendScript SDK demonstrates how to use graphic customization objects:
ColorSelector.jsx

Uses graphic objects to change the background color of a window as the user
selects the color value with a slider.

ColorPicker.jsx

A more complex version of the color-selection dialog shows how to use
additional graphics objects, including fonts and paths.

In addition, the Custom element class allows you to define completely customized elements of several
types (ranges, buttons, lists), whose appearance is rendered entirely by your onDraw implementation.

Resource specifications
You can create one or more user-interface elements at a time using a resource specification. This specially
formatted string provides a simple and compact means of creating an element, including any container
element and its component elements. The resource-specification string is passed as the type parameter to
the Window() or add() constructor function.
The general structure of a resource specification is an element type specification (such as dialog),
followed by a set of braces enclosing one or more property definitions.
var myResource = "dialog{ control_specs }";
var myDialog = new Window ( myResource );

Controls are defined as properties within windows and other containers. For each control, give the class
name of the control, followed by the properties of the control enclosed in braces. For example, the
following specifies a button:

CHAPTER 4: User-Interface Tools

Resource specifications

79

testBtn: Button { text: ’Test’ }

The following resource string specifies a panel that contains grouped StaticText and EditText controls:
"msgPnl: Panel { orientation:’column’, alignChildren:[’right’, ’top’],\
text: ’Messages’, \
title: Group { \
st: StaticText { text:’Alert box title:’ }, \
et: EditText { text:’Sample Alert’, characters:35 } \
}
msg: Group { \
st: StaticText { text:’Alert message:’ }, \
et: EditText { properties:{multiline:true}, \
text:’<your message here>’ \
} \
}"

The property with name properties specifies creation properties; see "Creation properties" on page 66.
A property value can be specified as null, true, false, a string, a number, an inline array, or an object.
An inline array contains one or more values in the form:
[value, value,...]

An object can be an inline object, or a named object, in the form:
{classname inlineObject}

In this case, the classname must be one of the control class names list in "Types of controls" on
page 67.
An inline object contains one or more properties, in the form:
{propertyName:propertyValue,propertyName:propertyValue,... }

Using resource strings
These examples in the Adobe ExtendScript SDK demonstrate how to use resource specification strings:
AlertBoxBuilder1.jsx

Demonstrates one way to use resource strings, creating a dialog that allows
the user to enter some values, and then using those values to construct the
resource string for a customizable alert dialog.

AlertBoxBuilder2.jsx

Constructs the same dialog, using a resource string (rather than the add()
method) to specify all of the dialog contents for the user-input dialog.

The two Alert Box Builder examples create the same dialog to collect values from the user.

CHAPTER 4: User-Interface Tools

Defining behavior with event callbacks and listeners

80

The Build button event handler builds a resource string from the collected values, and returns it from the
dialog invocation function; the script then saves the resource string to a file. That resource string can later
be used to create and display the user-configured alert box.
The resource specification format can also be used to create a single element or container and its child
elements. For instance, if the alertBuilderResource in the example did not contain the panel
btnPnlResource, you could define that resource separately, then add it to the dialog as follows:
var btnPnlResource =
"btnPnl: Panel { orientation:’row’, \
text: ’Build it’, \
testBtn: Button { text:’Test’ }, \
buildBtn: Button { text:’Build’, properties:{name:’ok’} }, \
cancelBtn: Button { text:’Cancel’, properties:{name:’cancel’} } \
}";
dlg = new Window(alertBuilderResource);
dlg.btnPnl = dlg.add(btnPnlResource);
dlg.show();

Defining behavior with event callbacks and listeners
You must define the behavior of your controls in order for them to respond to user interaction. You can do
this by defining event-handling callback functions as part of the definition of the control or window. To
respond to a specific event, define a handler function for it, and assign a reference to that function in the
corresponding property of the window or control object. Different types of windows and controls respond
to different actions, or events:
Windows generate events when the user moves or resizes the window. To handle these events, define
callback functions for onMove, onMoving, onResize, and onResizing. To respond to the user opening
or closing the window, define callback functions for onShow and onClose.

CHAPTER 4: User-Interface Tools

Defining behavior with event callbacks and listeners

81

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

Defining event-handler callback functions
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

CHAPTER 4: User-Interface Tools

Defining behavior with event callbacks and listeners

82

Simulating user events
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

Registering event listeners for windows or controls
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

CHAPTER 4: User-Interface Tools

Defining behavior with event callbacks and listeners

83

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

CHAPTER 4: User-Interface Tools

Defining behavior with event callbacks and listeners

84

The ScriptUI implementation of W3C mouse events follows the W3C DOM level 3 functional specification
(http://www.w3.org/TR/DOM-Level-3-Events/events.html#Events-eventgroupings-mouseevents), with
these differences:
To create a MouseEvent instance, call ScriptUI.events.createEvent('MouseEvent'), rather than
DocumentEvent.createEvent('MouseEvent').
The getModifierState method of the MouseEvent interface is not supported.
The ScriptUI implementation of W3C keyboard events follows the W3C DOM level 3 functional
specification {http://www.w3.org/TR/DOM-Level-3-Events/events.html#Events-KeyboardEvent).

How registered event-handlers are called
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

CHAPTER 4: User-Interface Tools

Communicating with the Flash application

85

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

Communicating with the Flash application
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

CHAPTER 4: User-Interface Tools

Automatic layout

86

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

Automatic layout
When a script creates a window and its associated user-interface elements, it can explicitly control the size
and location of each element and of the container elements, or it can take advantage of the automatic
layout capability provided by ScriptUI. The automatic layout mechanism uses certain available information
about user-interface elements, along with a set of layout rules, to establish a visually pleasing layout of the
controls in a dialog, automatically determining the proper sizes for elements and containers.
Automatic layout is easier to program than explicit layout. It makes a script easier to modify and maintain,
and easier to localize for different languages. It also makes the script automatically adapt to the default
font and font size used by the host application for ScriptUI windows.

CHAPTER 4: User-Interface Tools

Automatic layout

87

The script programmer has considerable control over the automatic layout process. Each container has an
associated layout manager object, specified in the layout property. The layout manager controls the sizes
and positions of the contained elements, and also sizes the container itself.
There is a default layout manager object, or you can create a new one:
myWin.layout = new AutoLayoutManager(myWin);

Default layout behavior
By default, the autoLayoutManager object implements the default layout behavior. A script can modify
the properties of the default layout manager object, or create a new, custom layout manager if it needs
more specialized layout behavior. See "Custom layout-manager example" on page 95.
Child elements of a container can be organized in a single row or column, or in a stack, where the elements
overlap one other in the same region of the container, and only the top element is fully visible. This is
controlled by the container’s orientation property, which can have the value row, column, or stack.
You can nest Panel and Group containers to create more complex organizations. For example, to display
two columns of controls, you can create a panel with a row orientation that in turn contains two groups,
each with a column orientation.
Containers have properties to control inter-element spacing and margins within their edges. The layout
manager provides defaults if these are not set.
The alignment of child elements within a container is controlled by the alignChildren property of the
container, and the alignment property of the individual controls. The alignChildren property
determines an overall strategy for the container, which can be overridden by a particular child element’s
alignment value.
A layout manager can determine the best size for a child element through the element’s preferredSize
property. The value defaults to dimensions determined by ScriptUI based on characteristics of the control
type and variable characteristics such as a displayed text string, and the font and size used to display text.
A value of -1 for either the width or height in the preferredSize value causes the layout manager to
calculate that dimension, while using the specified value for the other.
For details of how you can set these property values to affect the automatic layout, see "Automatic layout
properties" on page 87.
NOTE: The default font and font size are chosen differently on different platforms, and by different
applications on the same platform, so ScriptUI windows that are created the same way can appear
different in different contexts.

Automatic layout properties
Your script establishes rules for the layout manager by setting the values of certain properties, both in the
container object and in the child elements. The following examples show the effects of various
combinations of values for these properties. The examples are based on a simple window containing a
StaticText, Button and EditText element, created (using Resource specifications) as follows:
var w = new Window(
"window { \
orientation: ’row’, \
st: StaticText { }, \
pb: Button { text: ’OK’ }, \

CHAPTER 4: User-Interface Tools

Automatic layout

88

et: EditText { characters:4, justify:’right’ } \
}");
w.show();

Each example shows the effects of setting particular layout properties in various ways. In each window, w.
text is set so that the window title shows which property is being varied, and w.st.text is set to display

the particular property value being demonstrated.

Container orientation
The orientation property of a container specifies the organization of child elements within it. It can have
these values:
row - Child elements are arranged next to each other, in a single row from left to right across the
container. The height of the container is based on the height of the tallest child element in the row,
and the width of the container is based on the combined widths of all the child elements.
column - Child elements are arranged above and below each other, in a single column from top to

bottom across the container. The height of the container is based on the combined heights of all the
child elements, and the width of the container is based on the widest child element in the column.

stack - Child elements are arranged overlapping one another, as in a stack of papers. The elements

overlie one another in the same region of the container. Only the top element is fully visible. The
height of the container is based on the height of the tallest child element in the stack, and the width of
the container is based on the widest child element in the stack.

The following figure shows the results of laying out the sample window with each of these orientations:

Aligning children
The alignment of child elements within a container is controlled by two properties: alignChildren in the
parent container, and alignment in each child. The alignChildren value in the parent container controls
the alignment of all children within that container, unless it is overridden by the alignment value set on an
individual child element.
These properties use the same values, which specify alignment along one axis, depending on the
orientation of the container. You can specify an array of two of these strings, to specify alignment along
both axes. The first string specifies the horizontal value, the second specifies the vertical value. The
property values are not case-sensitive; for example, the strings FILL, Fill, and fill are all valid.
You can also set the value using the corresponding constants from the Alignment property of the ScriptUI
class; for example:
myGroup.alignment = [ScriptUI.Alignment.LEFT,
ScriptUI.Alignment.TOP]

CHAPTER 4: User-Interface Tools

Automatic layout

89

If you set the alignment value using a constant and then query the property, it returns an index number
corresponding to the constant, rather than a string value.
Elements in a row can be aligned along the vertical axis, in these ways:
top - The element’s top edge is located at the top margin of its container.
bottom - element’s bottom edge is located at the bottom margin of its container.
center - The element is centered within the top and bottom margins of its container.
fill - The element’s height is adjusted to fill the height of the container between the top and

bottom margins.

Elements in a column can be aligned along the horizontal axis, in these ways:
left - The element’s left edge is located at the left margin of its container.
right - The element’s right edge is located at the right margin of its container.
center - The element is centered within the right and left margins of its container.
fill - The element’s width is adjusted to fill the width of the container between the right and left

margins.

Elements in a stack can be aligned along either the vertical or the horizontal axis, in these ways:
top - The element’s top edge is located at the top margin of its container, and the element is
centered within the right and left margins of its container.
bottom - element’s bottom edge is located at the bottom margin of its container, and the element is

centered within the right and left margins of its container.

left - element’s left edge is located at the left margin of its container, and the element is centered

within the top and bottom margins of its container.

right - The element’s right edge is located at the right margin of its container, and the element is

centered within the top and bottom margins of its container.

center - The element is centered within the top, bottom, right and left margins of its container.
fill - The element’s height is adjusted to fill the height of the container between the top and

bottom margins., and the element’s width is adjusted to fill the width of the container between the
right and left margins.

The following figure shows the results of creating the sample window with row orientation and the
bottom and top alignment settings in the parent’s alignChildren property:

The following figure shows the results of creating the sample window with column orientation and the
right, left, and fill alignment settings in the parent’s alignChildren property. Notice how in the
fill case, each element is made as wide as the widest element in the container:

CHAPTER 4: User-Interface Tools

Automatic layout

90

You can override the container’s child alignment, as specified by alignChildren, by setting the
alignment property of a particular child element. The following diagram shows the result of setting
alignment to right for the EditText element, when the parent’s alignChildren value is left:

Alignment in two dimensions
You can set the alignment property with a two-string array instead of a single string, where the first string
is the horizontal alignment and the second is the vertical alignment. This allows you to control the
horizontal placement of children in a container with row orientation, and the vertical placement of
children in a container with column orientation.
The following figures show the results of the sample script SnpAlignElements.jsx, that demonstrates
how to specify alignment in two dimensions.
In the first, each control is centered vertically within its row, and placed at a specific horizontal
position, using an alignment value such as ['left', 'center'] for each element:

The vertical alignment example creates four columns, and places the controls within each column
along the vertical axis. It uses alignment values such as ['fill', 'top'] to distribute controls within
the column, while still controlling the relative vertical positions:

CHAPTER 4: User-Interface Tools

Automatic layout

91

Setting margins
The margins property of a container specifies the number of pixels between the edges of a container and
the outermost edges of the child elements. You can set this property to a simple number to specify equal
margins, or using a Margins object, which allows you to specify different margins for each edge of the
container.
The following figure shows the results of creating the sample window with row orientation and margins of
5 and 15 pixels:

This figure shows the results of creating the sample window with column orientation, a top margin of 0
pixels, a bottom margin of 20 pixels, and left and right margins of 15 pixels:

Spacing between children
The spacing property of a container specifies the number of pixels separating one child element from its
adjacent sibling element.
This figure shows the results of creating the sample window with row orientation, and spacing of 15 and 5
pixels, respectively:

This figure shows the results of creating the sample window with column orientation, and spacing of 20
pixels:

CHAPTER 4: User-Interface Tools

Automatic layout

92

Determining a preferred size
Each element has a preferredSize property, which is initially defined with reasonable default
dimensions for the element. The default value is calculated by ScriptUI, and is based on constant
characteristics of each type of element, and variable characteristics such as the text string to be displayed
in a button or text element.
If an element’s size property is not defined, the layout manager uses the value of preferredSize to
determine the dimensions of each element during the layout process. Generally, you should avoid setting
the preferredSize property explicitly, and let ScriptUI determine the best value based on the state of an
element at layout time. This allows you to set the text properties of your user-interface elements using
localizable strings (see "Localization in ScriptUI objects" on page 103). The width and height of each
element are calculated at layout time based on the chosen language-specific text string, rather than
relying on the script to specify a fixed size for each element.
However, a script can explicitly set the preferredSize property to give hints to the layout manager about
the intended sizes of elements for which a reasonable default size is not easily determined, such as an
IconButton element that has no initial image to measure.
You can set just one of the dimensions using the preferredSize; a value of -1 for either width or height
causes the layout manager to calculate that dimension, while using the supplied value for the other.
You can also set a maximum and/or minimum size value for a control, that limit how it can be resized.
There is a default maximum size that prevents automatic layout from creating elements larger than the
screen.
You can explicitly resize the controls in a window to fit the current text contents, or after the window is
resized by the user, using the resize() method of the layout object.

Creating more complex arrangements
You can easily create more complex arrangements by nesting Group containers within Panel containers
and other Group containers.
Many dialogs consist of rows of information to be filled in, where each row has columns of related types of
controls. For instance, an edit field is typically in a row next to a static text label that identifies it, and a
series of such rows are arranged in a column. This example (created using Resource specifications) shows a
simple dialog in which a user can enter information into two EditText fields, each arranged in a row with
its StaticText label. To create the layout, a Panel with a column orientation contains two Group elements
with row orientation. These groups contain the control rows. A third Group, outside the panel, contains the
row of buttons.
res =
"dialog { \

CHAPTER 4: User-Interface Tools

Automatic layout

93

info: Panel { orientation: ’column’, \
text: ’Personal Info’, \
name: Group { orientation: ’row’, \
s: StaticText { text:’Name:’ }, \
e: EditText { characters: 30 } \
}, \
addr: Group { orientation: ’row’, \
s: StaticText { text:’Street / City:’ }, \
e: EditText { characters: 30 } \
} \
}, \
buttons: Group { orientation: ’row’, \
okBtn: Button { text:’OK’, properties:{name:’ok’} }, \
cancelBtn: Button { text:’Cancel’, properties:{name:’cancel’} } \
} \
}";
win = new Window (res);
win.center();
win.show();

In this simplest example, the columns are not vertically aligned. When you are using fixed-width controls
in your rows, a simple way to get an attractive alignment of the StaticText labels for your EditText
fields is to align the child rows in the Panel to the right of the panel. In the example, add the following to
the Panel specification:
info: Panel { orientation: ’column’, alignChildren:’right’, \

This creates the following result:

Suppose now that you need two panels, and want each panel to have the same width in the dialog. You
can specify this at the level of the dialog window object, the parent of both panels. Specify
alignChildren='fill', which makes each child of the dialog match its width to the widest child.
res =
"dialog { alignChildren: ’fill’, \
info: Panel { orientation: ’column’, alignChildren:’right’, \
text: ’Personal Info’, \
name: Group { orientation: ’row’, \
s: StaticText { text:’Name:’ }, \
e: EditText { characters: 30 } \

CHAPTER 4: User-Interface Tools

Automatic layout

94

} \
}, \
workInfo: Panel { orientation: ’column’, \
text: ’Work Info’, \
name: Group { orientation: ’row’, \
s: StaticText { text:’Company name:’ }, \
e: EditText { characters: 30 } \
} \
}, \
buttons: Group { orientation: ’row’, alignment: ’right’, \
okBtn: Button { text:’OK’, properties:{name:’ok’} }, \
cancelBtn: Button { text:’Cancel’, properties:{name:’cancel’} } \
} \
}";
win = new Window (res); win.center(); win.show();

To make the buttons to appear at the right of the dialog, the buttons group overrides the fill alignment
of its parent (the dialog), and specifies alignment='right'.

Creating dynamic content
Many dialogs need to present different sets of information based on the user selecting some option within
the dialog. You can use the stack orientation to present different views in the same region of a dialog.
A stack orientation of a container places child elements so they are centered in a space which is wide
enough to hold the widest child element, and tall enough to contain the tallest child element. If you
arrange groups or panels in such a stack, you can show and hide them in different combinations to display
a different set of controls in the same space, depending on other choices in the dialog.
For example, this dialog changes dynamically according to the user’s choice in the DropDownList.

The following script creates this dialog. It compresses the "Personal Info" and "Work Info" panels from the
previous example into a single Panel that has two Groups arranged in a stack. A DropDownList allows the
user to choose which set of information to view. When the user makes a choice in the list, its onChange
function shows one group, and hides the other.

CHAPTER 4: User-Interface Tools

Automatic layout

95

res =
"dialog { \
whichInfo: DropDownList { alignment:’left’ }, \
allGroups: Panel { orientation:’stack’, \
info: Group { orientation: ’column’, \
name: Group { orientation: ’row’, \
s: StaticText { text:’Name:’ }, \
e: EditText { characters: 30 } \
} \
}, \
workInfo: Group { orientation: ’column’, \
name: Group { orientation: ’row’, \
s: StaticText { text:’Company name:’ }, \
e: EditText { characters: 30 } \
} \
}, \
}, \
buttons: Group { orientation: ’row’, alignment: ’right’, \
okBtn: Button { text:’OK’, properties:{name:’ok’} }, \
cancelBtn: Button { text:’Cancel’, properties:{name:’cancel’} } \
} \
}";
win = new Window (res);
win.whichInfo.onChange = function () {
if (this.selection != null) {
for (var g = 0; g < this.items.length; g++)
this.items[g].group.visible = false; //hide all other groups
this.selection.group.visible = true;//show this group
}
}
var item = win.whichInfo.add (’item’, ’Personal Info’);
item.group = win.allGroups.info;
item = win.whichInfo.add (’item’, ’Work Info’);
item.group = win.allGroups.workInfo;
win.whichInfo.selection = win.whichInfo.items[0];
win.center();
win.show();

Custom layout-manager example
This script creates a dialog almost identical to the one in the previous example, except that it defines a
layout-manager subclass, and assigns an instance of this class as the layout property for the last Group in
the dialog. (The example also demonstrates the technique for defining a reusable class in JavaScript.)
This script-defined layout manager positions elements in its container in a stair-step fashion, so that the
buttons are staggered rather than in a straight line.

CHAPTER 4: User-Interface Tools

Automatic layout

/* Define a custom layout manager that arranges the children
** of ’container’ in a stair-step fashion.*/
function StairStepButtonLayout (container) { this.initSelf(container); }
// Define its ’method’ functions
function SSBL_initSelf (container) { this.container = container; }
function SSBL_layout() {
var top = 0, left = 0;
var width;
var vspacing = 10, hspacing = 20;
for (i = 0; i < this.container.children.length; i++) {
var child = this.container.children[i];
if (typeof child.layout != "undefined")
// If child is a container, call its layout method
child.layout.layout();
child.size = child.preferredSize;
child.location = [left, top];
width = left + child.size.width;
top += child.size.height + vspacing;
left += hspacing;
}
this.container.preferredSize = [width, top - vspacing];
}
// Attach methods to Object’s prototype
StairStepButtonLayout.prototype.initSelf = SSBL_initSelf;
StairStepButtonLayout.prototype.layout = SSBL_layout;
// Define a string containing the resource specification for the controls
res = "dialog { \
whichInfo: DropDownList { alignment:’left’ }, \
allGroups: Panel { orientation:’stack’, \
info: Group { orientation: ’column’, \
name: Group { orientation: ’row’, \
s: StaticText { text:’Name:’ }, \
e: EditText { characters: 30 } \
} \
}, \
workInfo: Group { orientation: ’column’, \
name: Group { orientation: ’row’, \
s: StaticText { text:’Company name:’ }, \
e: EditText { characters: 30 } \
} \
}, \
}, \
buttons: Group { orientation: ’row’, alignment: ’right’, \
okBtn: Button { text:’OK’, properties:{name:’ok’} }, \
cancelBtn: Button { text:’Cancel’, properties:{name:’cancel’} } \
} \
}";

96

CHAPTER 4: User-Interface Tools

Automatic layout

97

// Create window using resource spec
win = new Window (res);
// Create list items, select first one
win.whichInfo.onChange = function () {
if (this.selection != null) {
for (var g = 0; g < this.items.length; g++)
this.items[g].group.visible = false;
this.selection.group.visible = true;
}
}
var item = win.whichInfo.add (’item’, ’Personal Info’);
item.group = win.allGroups.info;
item = win.whichInfo.add (’item’, ’Work Info’);
item.group = win.allGroups.workInfo;
win.whichInfo.selection = win.whichInfo.items[0];
// Override the default layout manager for the ’buttons’ group
// with custom layout manager
win.buttons.layout = new StairStepButtonLayout(win.buttons);
win.center();
win.show();

The AutoLayoutManager algorithm
When a script creates a Window object and its elements and shows it the first time, the visible
user-interface-platform window and controls are created. At this point, if no explicit placement of controls
was specified by the script, all the controls are located at [0, 0] within their containers, and have default
dimensions. Before the window is made visible, the layout manager’s layout method is called to assign
locations and sizes for all the elements and their containers.
The default AutoLayoutManager’s layout method performs these steps when invoked during the initial
call to a Window object’s show method:
1. Read the bounds property for the managed container; if undefined, proceed with auto layout. If
defined, assume that the script has explicitly placed the elements in this container, and cancel the
layout operation (if both the location and size property have been set, this is equivalent to setting
the bounds property, and layout does not proceed).
2. Determine the container’s margins and inter-element spacing from its margins and spacing
properties, and the orientation and alignment of its child elements from the container’s orientation
and alignChildren properties. If any of these properties are undefined, use default settings obtained
from platform and user-interface framework-specific default values.
3. Enumerate the child elements, and for each child:
If the child is a container, call its layout manager (that is, execute this entire algorithm again for the
container).
Read its alignment property; if defined, override the default alignment established by the parent
container with its alignChildren property.
Read its size property: if defined, use it to determine the child’s dimensions. If undefined, read its
preferredSize property to get the child’s dimensions. Ignore the child’s location property.
All the per-child information is collected for later use.
4. Based on the orientation, calculate the trial location of each child in the row or column, using
inter-element spacing and the container’s margins.

CHAPTER 4: User-Interface Tools

Managing control titles

98

5. Determine the column, row, or stack dimensions, based on the dimensions of the children.
6. Using the desired alignment for each child element, adjust its trial location relative to the edges of its
container.
7. Set the bounds property for each child element.
8. Set the container’s preferredSize property, based on the margins and dimensions of the row or
column of child elements.

Automatic layout restrictions
The following restrictions apply to the automatic layout mechanism:
The default layout manager does not attempt to lay out a container that has a defined bounds
property. The script programmer can override this behavior by defining a custom layout manager for
the container.
The layout mechanism does not track changes to element sizes after the initial layout has occurred.
The script can initiate another layout by calling the layout manager’s layout method, and can force
the manager to recalculate the sizes of all child containers by passing the optional argument as true.

Managing control titles
User interface elements often need a title or label to identify their purpose, with the title placed near the
element it identifies. As shown by examples in "Automatic layout" on page 86, you can use a statictext
element as a title or label, and use the automatic layout mechanism to control the placement of such a title
relative to the element it identifies.
The title-layout mechanism provides a simpler way to accomplish this task for many common cases. It
allows you to define an element's title and its spacial relationship with the graphic representation of the
object it identifies, without the need for additional statictext and container elements. Title layout
operates on an element's optional title and titleLayout properties. It treats this title and the element's
graphic representation as two separate objects whose relative positions are controlled according to layout
rules within a virtual container that encloses both objects. This is similar to the operation of the automatic
layout mechanism, but within a more limited scope.
Title layout is available for these types of UI elements:
DropDownList
FlashPlayer
IconButton
Image
TabbedPanel
For most of these element types, the title typically appears outside the element itself, and the virtual
container is an imaginary line surrounding the title and the separate element. For the IconButton, the title
appears inside the bounds of the button, and the virtual container is defined by the outer bounds of the
element. The same principles apply in both cases.

CHAPTER 4: User-Interface Tools

Managing control titles

99

The title property is a String that defines a text label for a UI element. The title can appear to the left or
right of the graphic element, above or below it, or superimposed over the center of the graphic
element; the placement is controlled by the titleLayout property.
The titleLayout property is an Object containing properties that specify:
The title's character width;
The title's justification within the character width;
How the title should be truncated if necessary;
The orientation, alignment, and spacing of the title with respect to the object it identifies;
The margins within the virtual container that surrounds the title and its related object.
All titleLayout properties are optional; the element types that use this mechanism have default values
for each property. Complete details are provided in the reference section; see "titleLayout" on page 141.
The following sections provide examples that show how to use title layout to achieve many different
layouts.

Title alignment and orientation
Unlike automatic layout, title layout uses the alignment property to specify the orientation of the title and
graphic element, and how the title aligns to the graphic element. This property contains a 2-element array,
where the first element specifies horizontal alignment and the second specifies vertical alignment. The
allowed values for these are the same as those used by automatic layout (see "Aligning children" on
page 88), except that the fill value is not allowed.
To achieve a row orientation where the title appears to the left or right of the graphic element, define
horizontal alignment as left or right and vertical alignment as center, top, or bottom:
button.titleLayout = { alignment: ['right', 'center'] };

CHAPTER 4: User-Interface Tools

Managing control titles

100

To achieve a column orientation where the title appears above or below the graphic element, define
vertical alignment as top or bottom, and horizontal alignment as center:
image.titleLayout = { alignment: ['center', 'bottom'] };

To achieve a stack orientation where the title appears superimposed upon the graphic element, define
both vertical and horizontal alignment as center. This orientation is mainly useful with the
iconbutton or image element types; it does not make sense to superimpose a title over a
dropdownlist, for instance. In this example, the button's title is centered over its iconic image:
button.title = 'Get information';
button.titleLayout = { alignment: ['center', 'center'] };

With row orientation, you can control whether the title aligns to the top, center, or bottom of the
graphic element. In this example, the title is placed to the left of the image, aligned at the top edge:
image.titleLayout = { alignment: ['left', 'top'] };

CHAPTER 4: User-Interface Tools

Managing control titles

101

Use spacing to override the default number of pixels separating the title from the graphic element. In
this example, titleLayout is configured to place the title 15 pixels above the panel:
panel.title = 'Image format';
panel.titleLayout = { alignment: ['center', 'top'], spacing: 15 };

Title character width and justification
To override the automatically calculated title width, define a positive non-zero value for the
characters property. This reserves enough space in the title area to hold the specified number of "X"
characters. This is useful when an element's title can change (for localized values, for instance) and you
want to reserve enough space to fit all the expected values without truncation or affecting the overall
layout.
droplist.titleLayout = { alignment: ['left', 'center'], characters: 20 };

When a characters value specifies a width greater than the default title width, you can set the
justify property to control how the text of the title is justified within the space reserved for it. The
value left places the text at the left end of the space, leaving blank space on the right; right places
the text at the right end of the space, leaving blank space on the left; and center places the text in the
middle of the space, dividing any blank space evenly on both sides of the text.
droplist.titleLayout = { alignment: ['left', 'center'],
characters: 20,
justify: 'right' };

CHAPTER 4: User-Interface Tools

Managing control titles

102

This example demonstrates using characters and justify to vertically align the colons at the ends
of all the dropdownlist control titles in a group. The same characters value is used for each
element's title, and all are right-justified:
w.ddl1 = w.add("dropdownlist { title: 'Image format:' }");
w.ddl2 = w.add("dropdownlist { title: 'Background color:' }");
w.ddl3 = w.add("dropdownlist { title: 'Text color:' }");
w.ddl1.titleLayout = { alignment: ['left', 'center'], spacing: 3,
characters: 16, justify: 'right' };
w.ddl2.titleLayout = { alignment: ['left', 'center'], spacing: 3,
characters: 16, justify: 'right' };
w.ddl3.titleLayout = { alignment: ['left', 'center'], spacing: 3,
characters: 16, justify: 'right' };

Title truncation
If the space reserved for a title is not wide enough to display its entire text, set the truncate property to
control the appearance of the truncated text. If truncate is middle, characters are removed from the
middle of the text and replaced with an ellipsis (...). For the value end, characters are removed from the
end of the text and replaced with an ellipsis. If truncate is none or is not defined, characters are removed
from the end, without any replacement ellipsis character.
This example demonstrates the effect of all three options on the same title string:
w.btn1 = w.add("iconbutton { title: 'Start 123456 End', image: 'SystemWarningIcon' }");
w.btn2 = w.add("iconbutton { title: 'Start 123456 End', image: 'SystemWarningIcon' }");
w.btn3 = w.add("iconbutton { title: 'Start 123456 End', image: 'SystemWarningIcon' }");
w.btn1.titleLayout = { characters: 8, truncate: 'middle' };
w.btn2.titleLayout = { characters: 8, truncate: 'end' };
w.btn3.titleLayout = { characters: 8, truncate: 'none' };

CHAPTER 4: User-Interface Tools

Localization in ScriptUI objects

103

Margins around the title and graphic object
The margins property specifies the number of pixels separating each edge of an element from the visible
content within that element. This value overrides the default margin settings (no margins for most
element types, 6 pixels at each edge for iconbutton).
For iconbutton, the margins value controls the padding between the button's frame and its title and
icon image.
For other element types, margins controls the padding between the imaginary border surrounding
the union of the bounding boxes of the title and graphic object, which makes the space occupied by
an element larger than its default measurements.
This example demonstrates overriding the default margins for iconbutton and dropdownlist elements.
The lists are enclosed in panels to create artificial borders around them:
w.btn1 = w.add("iconbutton { title: 'Default margins', image: 'SystemWarningIcon' }");
w.btn2 = w.add("iconbutton { title: 'Extra T/B margins',
image: 'SystemWarningIcon' }");
var defaultBtnMargins = w.btn2.titleLayout.margins;
w.btn2.titleLayout = { margins: [defaultBtnMargins[0], 15, defaultBtnMargins[2], 15] };
w.panel1 = w.add("panel { margins: 0, ddl1: DropDownList
{ title: 'Default margins' } }");
w.panel2 = w.add("panel { margins: 0, ddl2: DropDownList
{ title: 'Extra L/R margins' } }");
w.panel2.ddl2.titleLayout = { margins: [15, 0, 15, 0] };

Localization in ScriptUI objects
For portions of your user interface that are displayed on the screen, you may want to localize the displayed
text. You can localize the display strings in any ScriptUI object simply and efficiently, using the global
localize function. This function takes as its argument a localization object containing the localized
versions of a string.
For complete details of this ExtendScript feature, see "Localizing ExtendScript strings" on page 224.
A localization object is a JavaScript object literal whose property names are locale names, and whose
property values are the localized text strings. The locale name is an identifier as specified in the ISO 3166

CHAPTER 4: User-Interface Tools

Localization in ScriptUI objects

104

standard. In this example, a btnText object contains localized text strings for several locales. This object
supplies the text for a Button to be added to a window w:
btnText = { en: "Yes", de: "Ja", fr: "Oui" };
b1 = w.add ("button", undefined, localize (btnText));

The localize function extracts the proper string for the current locale. It matches the current locale and
platform to one of the object’s properties and returns the associated string. On a German system, for
example, the property de provides the string "Ja".
When your script uses localization to provide language-appropriate strings for user-interface elements, it
should also take advantage of the Automatic layout feature. The layout manager can determine the best
size for each user-interface element based on its localized text value, automatically adjusting the layout
of your script-defined dialogs to allow for the varying widths of strings for different languages.

Variable values in localized strings
The localize function allows you to include variables in the string values. Each variable is replaced with
the result of evaluating an additional argument. For example:
today = {
en: "Today is %1/%2.",
de: "Heute ist der %2.%1."
};
d = new Date();
Window.alert (localize (today, d.getMonth()+1, d.getDate()));

Enabling automatic localization
If you do not need variable replacement, you can use automatic localization. To turn on automatic
localization, set the global value:
$.localization=true

When it is enabled, you can specify a localization object directly as the value of any property that takes a
localizable string, without using the localize function. For example:
btnText = { en: "Yes", de: "Ja", fr: "Oui" };
b1 = w.add ("button", undefined, btnText);

The localize function always performs its translation, regardless of the setting of the $.localize
variable. For example:
//Only works if the $.localize=true
b1 = w.add ("button", undefined, btnText);
//Always works, regardless of $.localize value
b1 = w.add ("button", undefined, localize (btnText));

If you need to include variables in the localized strings, use the localize function.

CHAPTER 4: User-Interface Tools

ScriptUI object reference

105

ScriptUI object reference
ScriptUI is a component that works with the ExtendScript JavaScript interpreter to provide JavaScript
programs with the ability to create and interact with user interface elements. It provides an object model
for windows and user-interface control elements within an application.
This section provides the details of the ScriptUI classes and objects with their properties, methods, and
creation parameters.
ScriptUI class
Common properties
Window class
Window object
Control objects
UIEvent base class
Graphic customization objects
LayoutManager object

ScriptUI class
The globally available ScriptUI class provides central information about the ScriptUI module. This object
is not instantiable.

ScriptUI class properties
Alignment

Object

Collects the enumerated values that can be used in the alignment and
alignChildren properties of controls and containers, and in the alignment
property used to set a control’s titleLayout property. Read only.
Use these constants to set the alignment. For example:
myGroup.alignment = [ScriptUI.Alignment.LEFT,
ScriptUI.Alignment.TOP]

When you query the alignment property, it returns index values that
correspond to the constants as shown. Constant values are:
ScriptUI.Alignment.TOP
ScriptUI.Alignment.BOTTOM
ScriptUI.Alignment.LEFT
ScriptUI.Alignment.RIGHT
ScriptUI.Alignment.FILL
ScriptUI.Alignment.CENTER
applicationFonts Object

(1)
(2)
(3)
(4)
(5)
(6)

Collects the enumerated values that specify the default application fonts.
The available fonts vary according to the application and system
configuration.

CHAPTER 4: User-Interface Tools

ScriptUI class

106

compatability

Object

An object whose properties are the names of compatibility modes
supported by the host application. For example, the presence of
ScriptUI.compatability.su1PanelCoordinates means that the
application allows backward compatibility with the coordinate system of
Panel elements in ScriptUI version 1.

coreVersion

String

The internal core version number of the ScriptUI components. Read only.

environment

Object

A JavaScript object that provides access to attributes of the ScriptUI
environment; contains a Keyboard state object that reports the active
state of the keyboard at any time, independent of the event-handling
framework.

events

Object

A JavaScript object that contains one function, events.createEvent(),
which allows you to create event objects in order to simulate
user-interaction events.

FontStyle

String

Collects the enumerated values that can be used as the style argument
to the ScriptUI.newFont() method. For example:
var font = ScriptUI.newFont ('Helvetica",
ScriptUI.FontStyle.BOLD)

Read only. Values are:
REGULAR
BOLD
ITALIC
BOLDITALIC
frameworkName

String

The name of the user-interface framework with which this ScriptUI
component is compatible. Read only.

version

String

The main version number of the ScriptUI component framework. Read
only.

CHAPTER 4: User-Interface Tools

ScriptUI class

107

ScriptUI class functions
events.createEvent()
ScriptUi.events.createEvent (eventType)
eventType

The type of event, one of:
UIEvent
KeyboardEvent
MouseEvent

This function is in the JavaScript object contained in the events property. It returns an event object
of the appropriate type:
A UIEvent base class encapsulates input event information for an event that propagates
through a container and control hierarchy. This is a base class for the more specialized keyboard
and mouse event types.
A KeyboardEvent object encapsulates information about keyboard input events.
A MouseEvent object encapsulates information about mouse events.
This object is passed to a function that you register to respond to events of a certain type that occur
in a window or control. Use windowObj.addEventListener() or controlObj.addEventListener() to
register a handler function. See "Registering event listeners for windows or controls" on page 82.
getResourceText()
ScriptUI.getResourceText (text)
text

The text to match.

Finds and returns the resource for a given text string from the host application’s resource data. If no
string resource matches the given text, the text itself is returned.
Returns a String.
newFont()
ScriptUI.newFont ( name, style, size );
name

The font or font family name string.

style

The font style string or an enumerated value from ScriptUI.FontStyle.

size

The font size in points, a number.

Creates a new font object for use in text controls and titles.
Returns a ScriptUIFont object.

CHAPTER 4: User-Interface Tools

108

Common properties

newImage()
ScriptUI.newImage ( normal, disabled, pressed, rollover );
normal

The resource name or path to the image to use for the normal or default state.

disabled

The resource name or path to the image to use for the disabled state, shown when the
control containing the image is disabled (enabled=false).

pressed

The resource name or path to the image to use for the pressed state, shown when the
user clicks on the image.

rollover

The resource name or path to the image to use for the rollover state, which is shown
when the cursor moves over the image.

Creates a new image object for use in controls that can display images, loading the associated
images from the specified resources or image files.
Returns a ScriptUIImage object.

Environment object
This global object is available through the ScriptUI.environment property. It defines attributes of the
ScriptUI environment. In the current release, it contains one property:
keyboardState

Object

A Keyboard state object that reports the active state of the keyboard at
any time, independent of the event-handling framework.

Common properties

ListBox

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

alignChildren

x

x

x

x

x

alignment

x

x

x

x

bounds

x

x

x

cancelElement

x
x

x

characters
checked

x

TreeView

Image

x

StaticText

IconButton

x

Slider

FlashPlayer

x

Scrollbar

EditText

x

RadioButton

DropDownList

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

ProgressBar

CheckBox

x

active

ListItem

Button

x

Group

x

Tab

TabbedPanel

Panel

Property

Window

All types of user-interface elements, including windows, containers, and controls, share many of the same
properties, although some have slightly different meanings for different types of objects. The following
table summarizes which properties are used in which object types.

FlashPlayer

IconButton

Image

ListBox

x

x

x

x

x

x

x

TreeView

EditText

x

StaticText

DropDownList

x

Slider

CheckBox

x

Scrollbar

Button

x

109

RadioButton

Group

x

Common properties

ProgressBar

Tab

x

ListItem

TabbedPanel

children

Panel

Property

Window

CHAPTER 4: User-Interface Tools

x

x

x

x

x

x

x

x

x

x

x

x

x

columns
defaultElement

x

enabled

x

x

x

x

x

x

x

x

x

x

x

x

x

x
x

expanded
frameBounds

x

frameLocation

x

frameSize

x

graphics

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

helpTip

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

icon

x

x

x

image

x

x

x
x

index
items

x

x

x

itemSize

x

x

x
x

jumpdelta
justify
layout

x

x

x

x

x

location

x

x

x

x

x

margins

x

x

x

x

x

maximumSize

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

maxvalue
minimumSize

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

minvalue
orientation

x

x

x

x

x

parent

x

x

x

x

x

x

x

x

x

x

x

x

x

preferredSize

x

x

x

x

x

x

x

x

x

x

x

x

x

properties

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

resizeable

StaticText

Slider

110

x
x

selected

x

selection

x

shortcutKey

x

size

x

x

x

x

x

spacing

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

stepdelta

x

subitems

x x

text

Scrollbar

RadioButton

ProgressBar

ListItem

ListBox

Image

IconButton

FlashPlayer

EditText

DropDownList

CheckBox

Button

Group

Tab

TabbedPanel

Panel

Window

Property

Window class

TreeView

CHAPTER 4: User-Interface Tools

x

x

x

x

textselection

x

x

x

x

x

x

x

x x

x

x

x

x

x

x

x

x

x

x

title

x

titleLayout

x

type

x

x

x
x

x

x

x

x

x

x

x

x

x

x

x

x

value

x

x

visible

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

window

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

windowBounds

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

x

Window class
The Window class defines these static properties and functions. Window instances created with new
Window() do not have these properties and functions defined.

Window class properties
frameworkName

String

Deprecated. Use ScriptUI.frameworkName instead.

version

String

Deprecated. Use ScriptUI.version instead.

CHAPTER 4: User-Interface Tools

Window class

111

Window class functions
Access these function through the class. For example:
Window.alert("Notification to user");
alert()
Window.alert (message[, title, errorIcon]);
message

The string for the displayed message.

title

Optional. A string to appear as the title of the dialog, if the platform supports a
title. Mac OS does not support titles for alert dialogs. The default title string is
"Script Alert."

errorIcon

Optional. When true, the platform-standard alert icon is replaced by the
platform-standard error icon in the dialog. Default is false.

Displays a platform-standard dialog containing a short message and an OK button.
Returns undefined
confirm()
Window.confirm (message[,noAsDflt ,title ]);
message

The string for the displayed message.

noAsDflt

Optional. When true, the No button is the default choice, selected when the user
types ENTER. Default is false, meaning that Yes is the default choice.

title

Optional. A string to appear as the title of the dialog, if the platform supports a
title. Mac OS does not support titles for confirmation dialogs. The default title
string is "Script Alert."

Displays a platform-standard dialog containing a short message and two buttons labeled Yes and
No.
Returns true if the user clicked Yes, false if the user clicked No.
find()
Window.find (resourceName)
Window.find (type, title)
resourceName

The name of a predefined resource available to JavaScript in the current
application.

type

Optional. The window type (see "Window object constructor" on page 112) used if
there is more than one window with the same title. Can be null or the empty
string.

title

The window title.

Use this method to find an existing window. This includes windows already created by a script, and
windows created by the application (if the application supports this case).
NOTE: Not supported in all ScriptUI implementations.
Returns a Window object found or generated from the resource, or null if no such window or
resource exists.

CHAPTER 4: User-Interface Tools

Window object

112

prompt()
Window.prompt (message, preset[, title ]);
message

The string for the displayed message.

preset

The initial value to be displayed in the text edit field.

title

Optional. A string to appear as the title of the dialog. In Windows, this appears in
the window’s frame; in Mac OS it appears above the message. The default title
string is "Script Prompt."

Displays a modal dialog that returns the user’s text input.
Returns the value of the text edit field if the user clicked OK, null if the user clicked Cancel.

Window object
Window object constructor
The constructor creates and returns a new Window object, or null if window creation failed.
new Window (type [, title, bounds, {creation_properties}]);
type

The window type. The value is:
dialog - Creates a modal dialog.
palette - Creates a modeless dialog, also called a floating palette. (Not

supported by Photoshop CC.)

window - Creates a simple window that can be used as a main window for

an application. (Not supported by Photoshop CC.)

This argument can be a ScriptUI resource specification; in this case, all other
arguments are ignored. See "Resource specifications" on page 78.
title

Optional. The window title. A localizable string.

bounds

Optional. The window’s position and size.

creation_properties

Optional. An object that can contain any of these properties:
resizeable - When true, the window can be resized by the user. Default

is false.

su1PanelCoordinates - Photoshop only. When true, the child panels of

this window automatically adjust the positions of their children for
compatability with Photoshop CS (in which the vertical coordinate was
measured from outside the frame). Default is false. Individual panels can
override the parent window’s setting.

closeButton - When true, the title bar includes a button to close the

window, if the platform and window type allow it. When false, it does not.
Default is true. Not used for dialogs.

CHAPTER 4: User-Interface Tools

Window object

113

maximizeButton - When true, the title bar includes a button to expand

the window to its maximum size (typically, the entire screen), if the
platform and window type allow it. When false, it does not. Default is false
for type palette, true for type window. Not used for dialogs.
minimizeButton - When true, the title bar includes a button to minimize

or iconify the window, if the platform and window type allow it. When
false, it does not. Default is false for type palette, true for type window.
Main windows cannot have a minimize button in Mac OS. Not used for
dialogs.

independent - When true, a window of type window is independent of
other application windows, and can be hidden behind them in Windows.
In Mac OS, has no effect. Default is false.
borderless - When true, the window has no title bar or borders.
Properties that control those features are ignored.

Window object properties
The following element properties apply specifically to Window elements:
active

Boolean

When true, the object is active, false otherwise. Set to true to make a
given control or dialog active.
A modal dialog that is visible is by definition the active dialog.
An active palette is the front-most window.
An active control is the one with focus-that is, the one that
accepts keystrokes, or in the case of a Button, be selected when
the user types RETURN or ENTER.

cancelElement

Object

For a window of type dialog, the control to notify when a user types
the ESC key. By default, looks for a button whose name or text is
"cancel" (case disregarded).

defaultElement

Object

For a window of type dialog, the control to notify when a user types
the ENTER key. By default, looks for a button whose name or text is
"ok" (case disregarded).

frameBounds

Bounds

A Bounds object for the boundaries of the Window’s frame in screen
coordinates. The frame consists of the title bar and borders that
enclose the content region of a window, depending on the
windowing system. Read only.

frameLocation

Point

A Point object for the location of the top left corner of the Window’s
frame. The same as [frameBounds.x, frameBounds.y]. Set this
value to move the window frame to the specified location on the
screen. The frameBounds value changes accordingly.

frameSize

Dimension

A Dimension object for the size and location of the Window’s frame
in screen coordinates. Read only.

CHAPTER 4: User-Interface Tools

Window object

114

maximized

Boolean

When true, the window is expanded.

minimized

Boolean

When true, the window is minimized or iconified.

opacity

Number

The opacity of the window, in the range [0..1]. A value of 1.0 (the
default) makes the window completely opaque, a value of 0 makes it
completely transparent. Intermediate values make it partially
transparent to any degree.

shortcutKey

String

The key sequence that invokes this window’s onShortcutKey callback
(in Windows only).

CHAPTER 4: User-Interface Tools

Window object

115

Container properties
The following table shows properties that apply to Window objects and container objects (controls of type
panel, tabbedpanel, tab, and group).
alignChildren

String, or Array
of 2 Strings

Tells the layout manager how unlike-sized children of a container
should be aligned within a column or row. Order of creation
determines which children are at the top of a column or the left of
a row; the earlier a child is created, the closer it is to the top or left
of its column or row.
If defined, alignment for a child element overrides the

alignChildren setting for the parent container.

For a single string value, allowed values depend on the
orientation value. For orientation=row:
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

For an array value, the first string element defines the horizontal
alignment and the second element defines the vertical
alignment. The horizontal alignment value must be one of left,
right, center or fill. The vertical alignment value must be one
of top, bottom, center, or fill.
Values are not case sensitive.

CHAPTER 4: User-Interface Tools

alignment

Window object

String, or Array
of 2 Strings

116

Applies to child elements of a container. If defined, this value
overrides the alignChildren setting for the parent container.
For a single string value, allowed values depend on the
orientation value. For orientation=row:
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

For an array value, the first string element defines the horizontal
alignment and the second element defines the vertical
alignment. The horizontal alignment value must be one of left,
right, center or fill. The vertical alignment value must be one
of top, bottom, center, or fill.
Values are not case sensitive.
bounds

Bounds

A Bounds object for the boundaries of the window’s drawable
area in screen coordinates. Compare frameBounds. Does not
apply to containers of type tab, whose bounds are determined
by the parent tabbedpanel container. Read only.

children

Array of Object

The collection of user-interface elements that have been added
to this window or container. An array indexed by number or by a
string containing an element’s name. The length property of this
array is the number of child elements for container elements, and
is zero for controls. Read only.

graphics

Graphics

A ScriptUIGraphics object that can be used to customize the
window’s appearance, in response to the onDraw event.

layout

LayoutManager

A LayoutManager object for a window or container. The first time
a container object is made visible, ScriptUI invokes this layout
manager by calling its layout function. Default is an instance of
the LayoutManager class that is automatically created when the
container element is created.

location

Point

A Point object for the location of the top left corner of the
Window’s drawable area, or the top left corner of the frame for a
panel. The same as [bounds.x, bounds.y].

CHAPTER 4: User-Interface Tools

Window object

117

margins

Margins

A Margins object describing the number of pixels between the
edges of this container and the outermost child elements. You
can specify different margins for each edge of the container. The
default value is based on the type of container, and is chosen to
match the standard Adobe user-interface guidelines.

maximumSize

Dimension

A Dimension object for the largest rectangle to which the
window can be resized, used in automatic layout and resizing.

minimumSize

Dimension

A Dimension object for the smallest rectangle to which the
window can be resized, used in automatic layout and resizing.

orientation

String

How elements are organized within this container. Interpreted by
the layout manager for the container. The default LayoutManager
object accepts the (case-insensitive) values:
row
column
stack

The default orientation depends on the type of container. For
Window and Panel, the default is column, and for Group the
default is row.
The allowed values for the container’s alignChildren and its
children’s alignment properties depend on the orientation.
parent

Object

The immediate parent object of this element, a window or
container element. The value is null for Window objects. Read
only.

preferredSize

Dimension

A Dimension object for the preferred size of the window, used in
automatic layout and resizing. To set a specific value for only one
dimension, specify other dimension as -1.

properties

Object

An object that contains one or more creation properties of the
container (properties used only when the element is created).

selection

Tab

For a TabbedPanel only, the currently active Tab child. Setting
this property changes the active tab. The value can only be null
when the panel has no children; setting it to null is an error.
When the value changes, either by a user selecting a different tab,
or by a script setting the property, the onChange callback for the
panel is called.

size

Dimension

A Dimension object for the current size and location of a group or
panel element, or of the content area of a window.

spacing

Number

The number of pixels separating one child element from its
adjacent sibling element. Because each container holds only a
single row or column of children, only a single spacing value is
needed for a container. The default value is based on the type of
container, and is chosen to match standard Adobe user-interface
guidelines.

CHAPTER 4: User-Interface Tools

Window object

118

text

String

The title, label, or displayed text. Does not apply to containers of
type group or tabbedpanel. This is a localizable string: see
"Localization in ScriptUI objects" on page 103.

visible

Boolean

When true, the element is shown, when false it is hidden.
When a container is hidden, its children are also hidden, but they
retain their own visibility values, and are shown or hidden
accordingly when the parent is next shown.

window

Window

The top-level parent window of this container, a Window object.

windowBounds

Bounds

A Bounds object for the size and location of this container relative
to its top-level parent window.

Window object functions
These functions are defined for Window instances, and as indicated for container objects of type Panel and
Group.
add()
windowOrContainerObj.add (type [, bounds, text, { creation_props> } ]);
type

The control type. See "Control types and creation parameters" on page 124.

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
which are specific to each object type. See "Control types and creation
parameters" on page 124.

Creates and returns a new control or container object and adds it to the children of this window or
container.
Returns the new object, or null if unable to create the object.

CHAPTER 4: User-Interface Tools

Window object

119

addEventListener()
windowObj.addEventListener (eventName, handler[, capturePhase]);
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
click (detail = 1 for single, 2 for double)

handler

The function to register for the specified event in this target. This can be the
name of a function defined in the extension, or a locally defined handler
function to be executed when the event occurs. A handler function takes one
argument, the UIEvent base class. See "Registering event listeners for windows
or controls" on page 82.

capturePhase

Optional. When true, the handler is called only in the capturing phase of the
event propagation. Default is false, meaning that the handler is called in the
bubbling phase if this object is an ancestor of the target, or in the at-target
phase if this object is itself the target.

Registers an event handler for a particular type of event occurring in this window.
Returns undefined.
center()
windowObj.center ([window])
window

Optional. A Window object.

Centers this window on the screen, or with respect to another specified window.
Returns undefined.
close()
windowObj.close ([result])
result

Optional. A number to be returned from the show method that invoked this
window as a modal dialog.

Closes this window. If an onClose callback is defined for the window, calls that function before
closing the window.
Returns undefined.
dispatchEvent()
windowObj.dispatchEvent (eventObj)
eventObj

A UIEvent base class.

Simulates the occurrence of an event in this target. A script can create a UIEvent base class for a
specific event and pass it to this method to start the event propagation for the event.
Returns false if any of the registered listeners that handled the event called the event object’s
preventDefault() method, true otherwise.

CHAPTER 4: User-Interface Tools

Window object

findElement()
windowOrContainerObj.findElement (name)
name

The name of the element, as specified in the name creation property.

Searches for the named element among the children of this window or container, and returns the
object if found.
Returns the control object or null.
hide()
windowObj.hide()

Hides this window. When a window is hidden, its children are also hidden, but when it is shown
again, the children retain their own visibility states.
For a modal dialog, closes the dialog and sets its result to 0.
Returns undefined.
notify()
windowObj.notify([event])
event

Optional. The name of the window event handler to call. One of:
onClose
onMove
onMoving

onResize
onResizing
onShow

Sends a notification message, simulating the specified user interaction event. For example, to
simulate a dialog being moved by a user:
myDlg.notify("onMove")

Returns undefined.
remove()
windowOrContainerObj.remove(index)
windowOrContainerObj.remove(text)
windowOrContainerObj.remove(child)
index
text
child

The child control to remove, specified by 0-based index, the contained text
value, or as a control object.

Removes the specified child control from this window’s or container’s children array. No error
results if the child does not exist.
Returns undefined.

120

CHAPTER 4: User-Interface Tools

Window object

121

removeEventListener()
windowObj.removeEventListener (eventName, handler[, capturePhase]);
eventName

The event name string.

handler

The function that was registered to handle the event.

capturePhase

Optional. Whether the handler was to respond only in the capture phase.

Unregisters an event handler for a particular type of event occurring in this window. All arguments
must be identical to those that were used to register the event handler.
Returns undefined.
show()
windowObj.show()

Shows this window, container, or control. If an onShow callback is defined for a window, calls that
function before showing the window.
When a window or container is hidden, its children are also hidden, but when it is shown again, the
children retain their own visibility states.
For a modal dialog, opens the dialog and does not return until the dialog is dismissed. If it is
dismissed via the close() method, this method returns any result value passed to that method.
Otherwise, returns 0.
update()
windowObj.update()

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
the case during a modal show() operation), so that the script does not prevent the update of other
parts of the application's UI while in the operation loop.
It is an error to call the update() method for a window that is not currently visible.

CHAPTER 4: User-Interface Tools

Window object

122

Window event-handling callbacks
The following callback functions can be defined to respond to events in windows. To respond to an event,
define a function with the corresponding name in the Window instance. These callbacks are not available
for other container types (controls of type panel or group).
Callback

Description

onActivate

Called when the user make the window active by clicking it or otherwise making it
the keyboard focus.

onClose

Called when a request is made to close the window, either by an explicit call to the
close() function or by a user action (clicking the OS-specific close icon in the title
bar).
The function is called before the window actually closes; it can return false to cancel
the close operation.

onDeactivate

Called when the user makes a previously active window inactive; for instance by
closing it, or by clicking another window to change the keyboard focus.

onDraw

Called when a container or control is about to be drawn. Allows the script to modify
or control the appearance, using the control’s associated ScriptUIGraphics object.
Handler takes one argument, a DrawState object.

onMove

Called when the window has been moved.

onMoving

Called while a window in being moved, each time the position changes. A handler
can monitor the move operation.

onResize

Called when the window has been resized.

onResizing

Called while a window is being resized, each time the height or width changes. A
handler can monitor the resize operation.

onShortcutKey

(In Windows only) Called when a shortcut-key sequence is typed that matches the
shortcutKey value for this window.

onShow

Called when a request is made to open the window using the show() method, before
the window is made visible, but after automatic layout is complete. A handler can
modify the results of the automatic layout.

CHAPTER 4: User-Interface Tools

Control objects

123

Control objects
UI elements that belong to windows can be containers or controls. Containers share some aspects of
top-level windows, and some aspects of controls, and so are described here with controls.

Control object constructors
Use the add method to create new containers and controls. The add method is available on window and
container (panel and group) objects. (See also add() for dropdownlist and listbox controls.)
add()
containerObj.(type [, bounds, text, { creation_props> } ]);
type

The control type. See "Control types and creation parameters" on page 124.

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
which are specific to each object type. See "Control types and creation
parameters" on page 124.

Creates and returns a new control or container object and adds it to the children of this window or
container.
Returns the new object, or null if unable to create the object.

CHAPTER 4: User-Interface Tools

Control objects

124

Control types and creation parameters
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

125

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

CHAPTER 4: User-Interface Tools

Type keyword

Control objects

Class name

edittext (cont’d)

126

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
ActionScript environment. See "FlashPlayer control functions" on
page 145.
To add to a window w:
w.add ("flashplayer" [, bounds, movieToLoad,
{creation_properties}]);
bounds: Optional. The control’s position and size.
movieToLoad: Optional. A path or URL string or File object for
the SWF file to load into the player.
creation_properties: Optional. An object that contains any of

the following properties:

name: A unique name for the control.

CHAPTER 4: User-Interface Tools

Control objects

127

Type keyword

Class name

Description

group

Group

A container for other controls. Containers have additional properties
that control the children; see "Container properties" on page 115.
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

CHAPTER 4: User-Interface Tools

Control objects

Type keyword

Class name

Description

image

Image

Displays an icon or image.

128

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

CHAPTER 4: User-Interface Tools

Type keyword

Control objects

Class name

listbox (cont’d)

129

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
"Container properties" on page 115. Hiding a panel hides all its
children. Making it visible makes visible those children that are not
individually hidden.
To add to a window w:
w.add ("panel" [, bounds, text, {creation_properties}]);
bounds: Optional. The element’s position and size. A panel

whose width is 0 appears as a vertical line. A panel whose height
is 0 appears as a horizontal line.

text: Optional. The text displayed in the border of the panel.

CHAPTER 4: User-Interface Tools

Type keyword

Control objects

Class name

panel (cont’d)

130

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

CHAPTER 4: User-Interface Tools

Control objects

131

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

CHAPTER 4: User-Interface Tools

Type keyword

Control objects

Class name

scrollbar (cont’d)

132

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

CHAPTER 4: User-Interface Tools

Control objects

Type keyword

Class name

Description

statictext

StaticText

A text field that the user cannot change.

133

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
"Container properties" on page 115. Hiding a panel hides all its
children. Making it visible makes visible those children that are not
individually hidden.
To add a tab to a tabbed panel t in window w:
w.t.add ("tab" [, bounds, text,
{creation_properties}]);
bounds: Not used, pass undefined. The size and position is

determined by the parent.

text: Optional. The text displayed in the tab.

CHAPTER 4: User-Interface Tools

Type keyword

Control objects

Class name

tab (cont’d)

134

Description
creation_properties: Optional. An object that contains the

following property:

name: A unique name for the control.
tabbedpanel

TabbedPanel

A container for selectable Tab containers. Differs from a Panel
element in that it can contain only Tab elements as direct children.
Containers have additional properties that control the children; see
"Container properties" on page 115. Hiding a panel hides all its
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

CHAPTER 4: User-Interface Tools

Type keyword

Control objects

Class name

treeview (cont’d)

135

Description
creation_properties: Optional. An object that contains any of

the following properties:

name: A unique name for the control.
items: An array of strings for the text of each top-level list
item. A ListItem object is created for each item. An item
with the type node can contain child items. Supply this
property, or the items argument, not both. This form is most

useful for elements defined using Resource specifications.

Control object properties
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

CHAPTER 4: User-Interface Tools

Control objects

alignment (cont’d)

136

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

CHAPTER 4: User-Interface Tools

image

Control objects

Object

137

A ScriptUIImage object, or the name of an icon resource, or the
pathname or File object for a file that contains a platform-specific
image in PNG or JPEG format, or for a shortcut or alias to such a file.
For an IconButton, the icon appears as the content of the button.
For an Image, the image is the entire content of the image
element.
For a ListItem, the image is displayed to the left of the text.
If the parent is a multi-column ListBox, this is the display image
for the label in the first column, and labels for further columns are
specified in the subitems array. See "Creating multi-column lists"
on page 73.

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

CHAPTER 4: User-Interface Tools

location

Control objects

Point

138

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

CHAPTER 4: User-Interface Tools

subitems

Control objects

Array

140

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
subitems array. See "Creating multi-column lists" on page 73.
This is a localizable string: see "Localization in ScriptUI objects" on
page 103.

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

CHAPTER 4: User-Interface Tools

titleLayout

Control objects

Object

141

For a DropDownList, FlashPlayer, IconButton, Image, or TabbedPanel
with a title value, the way the text label is shown in relation to the
element. A JavaScript object with these properties:
alignment -The position of the title relative to the element, an
array of [horizontal_alignment, vertical_alignment]. For possible
alignment values, see "alignment" on page 116. Note that fill is
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

CHAPTER 4: User-Interface Tools

Control objects

142

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

Control object functions
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
"Registering event listeners for windows or controls" on page 82.

capturePhase

Optional. When true, the handler is called only in the capturing phase of the event
propagation. Default is false, meaning that the handler is called in the bubbling
phase if this object is an ancestor of the target, or in the at-target phase if this
object is itself the target.

Registers an event handler for a particular type of event occurring in this control.
Returns undefined.

CHAPTER 4: User-Interface Tools

Control objects

143

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

CHAPTER 4: User-Interface Tools

Control objects

144

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

CHAPTER 4: User-Interface Tools

Control objects

145

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

CHAPTER 4: User-Interface Tools

Control objects

146

invokePlayerFunction()
flashPlayerObj.invokePlayerFunction(fnName, [arg1[,...argn]] )
fnName

String. The name of a Flash ActionScript function that has been registered with the
ExternalInterface object by the currently loaded SWF file; see "Calling ActionScript
functions from a ScriptUI script" on page 86.

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

CHAPTER 4: User-Interface Tools

Control objects

147

Control event-handling callbacks
The following events are signalled in certain types of controls. To handle the event, define a function with
the corresponding name in the control object. Handler functions take no arguments and have no
expected return values; see "Defining behavior with event callbacks and listeners" on page 80.
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

CHAPTER 4: User-Interface Tools

Control objects

148

onExpand

Called when the user expands (opens) a node in a TreeView control. The parameter
to this function is the ListItem node object that was expanded.

onShortcutKey

(In Windows only) Called when a shortcut-key sequence is typed that matches the
shortcutKey value for an element in the active window.

DrawState object
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

CHAPTER 4: User-Interface Tools

Event handling

149

Event handling
Several helper classes provide low-level event-handling capabilities.
Event objects are normally created by ScriptUI and passed to your event handler. However, you can
simulate a user action by constructing an event object using ScriptUI.events.events.createEvent(),
and sending it to a target object’s dispatchEvent() function.
A helper object, Keyboard state object, provides global access to the keyboard state during function
execution, outside the event-handling framework.

UIEvent base class
Encapsulates input event information for an event that propagates through a container and control
hierarchy. This is a base class for the more specialized KeyboardEvent object and MouseEvent object.

UIEvent object properties
Both keyboard and mouse events have these properties.
bubbles

Boolean When true, the event supports the bubbling phase.

cancelable

Boolean When true, the handler can call this object’s preventDefault() method to
cancel the default action of the event.

currentTarget

Object

eventPhase

Number Current event propagation phase. One of these constants:

The element object where the currently executing handler was registered.
This could be an ancestor of the target object, if the handler is invoked
during the capture or bubbling phase.

Event.NOT_DISPATCHING
Event.CAPTURING_PHASE
Event.AT_TARGET
Event.BUBBLING_PHASE

I

target

Object

The element object where the event occurred.

timeStamp

Object

Time the event was initiated. A JavaScript Date object.

type

String

The name of the event that occurred. Predefined events types are:
change
move
resize
show
focus

changing
moving
resizing
enterKey
blur

Additional type names apply specifically to keyboard and mouse events.
view

Object

The container or control object that dispatched the event.

CHAPTER 4: User-Interface Tools

Event handling

150

UIEvent object functions
initUIEvent()
eventObj.initUIEvent (eventName, bubble, isCancelable, view, detail)
eventName

The event name string.

bubble

When true, the event should be triggered in ancestors of the target object during
the bubbling phase.

isCancelable

When true, the event can be cancelled.

view

The container or control object that dispatched the event.

detail

Details of the event, which vary according to the event type. The value is 1 or 2 for
the click event, indicating a single or double click.

Modifies an event before it is dispatched to its targets. Takes effect only if UIEvent.eventPhase is

Event.NOT_DISPATCHING. Ignored at all other phases.

Returns undefined.
preventDefault()
eventObj.preventDefault ( )

Cancels the default action of this event, if this event is cancelable (that is, cancelable is true). For
example, the default click action of an OK button is to close the containing dialog; this call prevents
that behavior.
Returns undefined.
stopPropagation()
eventObj.stopPropagation ( )

Stops event propagation (bubbling and capturing) after executing the handler or handlers at the
current target.
Returns undefined.

CHAPTER 4: User-Interface Tools

Event handling

151

KeyboardEvent object
This type of object is passed to your registered event handler when a keyboard-input event occurs. The
properties reflect the keypress and key modifier state at the time the keyboard event was generated. All
properties are read-only.

KeyboardEvent object properties
In addition to the properties defined for UIEvent base class, a keyboard event has these properties. All
properties are read-only.
altKey

Boolean When true, the ALT key was active. Value is undefined if the
keyIdentifier is for a modifier key.

ctrlKey

Boolean When true, the CTRL key was active. Value is undefined if the
keyIdentifier is for a modifier key.

metaKey

Boolean When true, the META or COMMAND key was active. Value is undefined if the
keyIdentifier is for a modifier key.

shiftKey

Boolean When true, the SHIFT key was active. Value is undefined if the
keyIdentifier is for a modifier key.

keyIdentifier

String

keyLocation

Number A constant that identifies where on the keyboard the keypress occurred.
One of:

The key whose keypress generated the event, as a W3C identifier
contained in a string; for example, "U+0044". See
http://www.w3.org/TR/DOM-Level-3-Events/keyset.html#KeySet-Set.

DOM_KEY_LOCATION_STANDARD
DOM_KEY_LOCATION_LEFT
DOM_KEY_LOCATION_RIGHT
DOM_KEY_LOCATION_NUMPAD
keyName

String

The key whose keypress generated the event, as a simple key name; for
example "A".

type

String

The name of the event that occurred. Key events types are:
keyup
keydown

CHAPTER 4: User-Interface Tools

Event handling

152

KeyboardEvent object functions
In addition to the functions defined for UIEvent base class, a keyboard event has these functions.
getModifierState()
eventObj.getModifierState (keyIdentifier)
keyIdentifier

A string containing a modifier key identifier, one of:
Alt
CapsLock
Control
Meta
NumLock
Scroll
Shift

Returns true if the given modifier was active when the event occurred, false otherwise.
initKeyboardEvent()
eventObj.initKeyboardEvent (eventName, bubble, isCancelable, view, keyID,
keyLocation, modifiersList)
eventName

The event name string.

bubble

When true, the event should be triggered in ancestors of the target object
during the bubbling phase.

isCancelable

When true, the event can be cancelled.

view

The container or control object that dispatched the event.

keyID

Sets the keyIdentifier value.

keyLocation

Sets the keyLocation. value.

modifiersList

A whitespace-separated string of modifier key names, such as "Control Alt".

Reinitializes the object, allowing you to change the event properties after construction. Arguments
set the corresponding properties. Returns undefined.

CHAPTER 4: User-Interface Tools

Event handling

153

MouseEvent object
This type of object is passed to your registered event handler when a mouse-input event occurs. The
properties reflect the button and modifier-key state and pointer position at the time the event was
generated.
In the case of nested elements, mouse event types are always targeted at the most deeply nested element.
Ancestors of the targeted element can use bubbling to obtain notification of mouse events which occur
within its descendent elements.

MouseEvent object properties
In addition to the properties defined for UIEvent base class, a mouse event has these properties. All
properties are read-only.
altKey

Boolean When true, the ALT key was active. Value is undefined if the
keyIdentifier is for a modifier key.

button

Number Which mouse button changed state.
0-The left button of a two- or three-button mouse or the one button
on a one-button mouse, used to activate a UI button or select text.
1- The middle button of a three-button mouse, or the mouse wheel.
2-The right button, used to display a context menu, if present.
Some mice may provide or simulate more buttons, and values higher than
2 represent such buttons.

clientX
clientY

Number The horizontal and vertical coordinates at which the event occurred
relative to the target object. The origin is the top left of the control or
window, inside any border decorations.

ctrlKey

Boolean When true, the CTRL key was active. Value is undefined if the
keyIdentifier is for a modifier key.

detail

Number Details of the event, which vary according to the event type. For the
click, mousedown, and mouseup events, the value is 1 for a single click, or
2 for a double click.

metaKey

Boolean When true, the META or COMMAND key was active. Value is undefined if the
keyIdentifier is for a modifier key.

relatedTarget

Object

For a mouseover event, the UI element the pointer is leaving, if any.
For a mouseout event, the UI element the pointer is entering, if any.
Otherwise undefined.

screenX
screenY

Number The horizontal and vertical coordinates at which the event occurred
relative to the screen.

CHAPTER 4: User-Interface Tools

Event handling

shiftKey

Boolean When true, the SHIFT key was active. Value is undefined if the
keyIdentifier is for a modifier key.

type

String

154

The name of the event that occurred. Mouse events types are:
mousedown
mouseup
mousemove
mouseover
mouseout
click (detail = 1 for single, 2 for double)

The sequence of click events is: mousedown, mouseup, click.

MouseEvent object functions
In addition to the functions defined for UIEvent base class, a mouse event has these functions.
getModifierState()
eventObj.getModifierState (keyIdentifier)
keyIdentifier

A string containing a modifier key identifier, one of:
Alt
CapsLock
Control
Meta
NumLock
Scroll
Shift

Returns true if the given modifier was active when the event occurred, false otherwise.
initMouseEvent()
eventObj.initMouseEvent (eventName, bubble, isCancelable, view, detail,
screenX, screenY, clientX, clientY, ctrlKey, altKey, shiftKey, metaKey,
button, relatedTarget)
eventName

The event name string.

bubble

When true, the event should be triggered in ancestors of the target object
during the bubbling phase.

isCancelable

When true, the event can be cancelled.

view

The container or control object that dispatched the event.

detail

Sets the single-double click value for the click event.

screenX,
screenY

Sets the event coordinates relative to the screen.

clientX,
clientY

Sets the event coordinates relative to the target object. The origin is the top left
of the control or window, inside any border decorations.

ctrlKey,
altKey,
metaKey

Sets the modifier key states.

CHAPTER 4: User-Interface Tools

Graphic customization objects

button

Sets the mouse button.

relatedTarget

Optional. Sets the related target, if any, for a mouseover or mouseout event.

155

Reinitializes the object, allowing you to change the event properties after construction. Arguments
set the corresponding properties.
Returns undefined.

Keyboard state object
This JavaScript object reports the active state of the keyboard at any time; that is, the current key that is
down and any modifiers that are pressed. It is independent of the event-handling system, and is available
through the ScriptUI.environment object:
myKeyState = ScriptUI.environment.keyboardState;

The object has the following properties:
keyName

String

The name of the key currently pressed. This is the JavaScript name, a
string such as "A" or "a".

shiftKey
ctrlKey
altKey
metaKey

Boolean

True if the named modifier key is currently active.

Graphic customization objects
These objects provide the ability to customize the appearance of user-interface controls before they are
drawn:
ScriptUIGraphics object
ScriptUIBrush object
ScriptUIFont object
ScriptUIImage object
ScriptUIPath object
ScriptUIPen object
In addition, the Custom element class (if supported by the Adobe application you are using) allows you to
define completely customized UI elements that are rendered by the application in a manner you define.

ScriptUIGraphics object
Most types of user-interface elements have a graphics property which contains an object of this type,
which allows you to customize aspects of the element’s appearance, such as the color and font. Use an
onDraw callback function to set these properties or call the functions.
All measurements are in pixels.

CHAPTER 4: User-Interface Tools

Graphic customization objects

156

ScriptUIGraphics class properties
These static properties provide color type constants with which to create Pen and Brush objects.
BrushType

Object

Contains the enumerated constants for the type argument of
newBrush(). Types are:
SOLID_COLOR
THEME_COLOR

PenType

Object

Contains the enumerated constants for the type argument of newPen().
Types are:
SOLID_COLOR
THEME_COLOR

ScriptUIGraphics object properties
The object contains the following properties:
backgroundColor

Object The background color of a container, or the parent
background color for a control element. A ScriptUIBrush
object.

currentPath

Object The current drawing path for this object, a ScriptUIPath
object.

currentPoint

Object The current position in the drawing path for this object, a
Point object.

disabledBackgroundColor

Object The background color for the disabled state of a container, or
the parent background color for the disabled state of a
control element. A ScriptUIBrush object.

disabledForegroundColor

Object The foreground color for the disabled state of a container, or
the parent foreground color for the disabled state of a control
element. A ScriptUIPen object.

font

Object The default font to use in writing text, a ScriptUIFont object.

foregroundColor

Object The foreground color for a container, or the parent
foreground color of a control element. A ScriptUIPen object.

CHAPTER 4: User-Interface Tools

Graphic customization objects

157

ScriptUIGraphics object functions
These functions directly customize the appearance of the associated element by drawing on the screen, or
create the Pen and Brush objects used to populate the graphics object or pass to the drawing methods:
closePath()
controlObj.graphics.closePath ( )

Defines a line from the current position to the start point of the current path (the value of
currentPath), which closes the path.
Returns undefined.
drawFocusRing()
controlObj.graphics.drawFocusRing (left, top[, width, height])
left, top

Defines the top left corner of the region, in the coordinate system of the control
that contains this graphics object.

width, height

The width and height of the region in pixels.

Draws a focus ring within the given rectangular region. This is a visual indicator showing that a given
control has the keyboard focus (accepts keyboard input). In Mac OS, this is typically a light blue ring
around the control. In Windows, it is typically a dashed-line rectangle around some part of the
control.
Returns undefined.
drawImage()
controlObj.graphics.drawImage (image, left, top[, width, height])
image

The ScriptUIImage object containing the images to be drawn.

left, top

Defines the top left corner of the drawing region, in the coordinate system of the
control that contains this graphics object.

width, height

Optional. The width and height of the drawing region in pixels. If specified, the
image is stretched or shrunk to fit into the given rectangular area. If omitted, the
image’s original width or height is used.

Draws an image within the given rectangular region, using the image file from the given image
object that is appropriate to the control’s current state.
Returns undefined.
drawOSControl()
controlObj.graphics.drawOSControl ( )

Draws the platform-specific control associated with this element.
Returns undefined.

CHAPTER 4: User-Interface Tools

Graphic customization objects

drawString()
controlObj.graphics.drawString (text, pen, x, y, font)
text

The text string.

pen

The ScriptUIPen object for the drawing pen to use.

x, y

The origin point of the drawn text, in the coordinate system of the control that
contains this graphics object.

font

Optional. The ScriptUIFont object for the font to use. Default is the font value in
this object.

Draws a string of text starting at a given point, using the given pen and font.
Returns undefined.
ellipsePath()
controlObj.graphics.ellipsePath (left, top[, width, height])
left, top

Defines the top left corner of the region, in the coordinate system of the control
that contains this graphics object.

width, height

The width and height of the region in pixels.

Defines an elliptical path within a given rectangular area in the currentPath object, which can be
filled using fillPath() or stroked using strokePath().
Returns a Point object for the upper left corner of the area, which is the new currentPoint.
fillPath()
controlObj.graphics.fillPath (brush[, path])
brush

The ScriptUIBrush object that defines the fill color.

path

Optional, the ScriptUIPath object for the path. If not supplied, operates on the
currentPath.

Fills a path using a given painting brush.
Returns undefined.
lineto()
controlObj.graphics.lineto (x, y)
x, y

The destination point of the line, in the coordinate system of the control that
contains this graphics object.

Adds a path segment to the currentPath, from the currentPoint to the specified point.
Returns a Point object for the given destination point, which is the new current position.

158

CHAPTER 4: User-Interface Tools

Graphic customization objects

159

measureString()
controlObj.graphics.measureString (text, font[, boundingWidth])
text

The text string to measure.

font

Optional. The ScriptUIFont object for the font to use. Default is the font value in
this object.

boundingWidth Optional. A number that specifies the maximum width in pixels of the area in

which the text might be placed. Use when wrapping a long string of text across
multiple lines.

Calculates the size needed to draw a text string in a given font.
Returns a Dimension object containing the height and width of the string in pixels.
moveto()
controlObj.graphics.moveto (x, y)
x, y

The new coordinates, in the coordinate system of the control that contains this
graphics object.

Adds a given point to the currentPath, and makes it the currentPoint.
Returns a Point object for the given destination point, which is the new current position.
newBrush()
controlObj.graphics.newBrush( type, color );
type

The brush type, one of these constants:
ScriptUIGraphics.BrushType.SOLID_COLOR
ScriptUIGraphics.BrushType.THEME_COLOR

color

The brush color.
If type is SOLID_COLOR, the color expressed as an array of three or four values,
in the form [R, B, G, A] specifying the red, green, and blue values of the
color and, optionally, the opacity (alpha channel). All values are numbers in
the range [0.0...1.0]. An opacity of 0 is fully transparent, and an opacity of 1 is
fully opaque.
If the type is THEME_COLOR, the name string of the theme. Theme colors are
defined by the host application.

Creates a new painting brush.
Returns a ScriptUIBrush object.
newPath()
controlObj.graphics.newPath( );

Creates a new, empty drawing path in currentPath, replacing any existing path.
Returns a ScriptUIPath object.

CHAPTER 4: User-Interface Tools

Graphic customization objects

160

newPen()
controlObj.graphics.newPen( type, color, lineWidth);
type

The pen type, one of these constants:
ScriptUIGraphics.PenType.SOLID_COLOR
ScriptUIGraphics.PenType.THEME_COLOR

color

The pen color.
If type is SOLID_COLOR, the color expressed as an array of three or four values,
in the form [R, B, G, A] specifying the red, green, and blue values of the
color and, optionally, the opacity (alpha channel). All values are numbers in
the range [0.0...1.0]. An opacity of 0 is fully transparent, and an opacity of 1 is
fully opaque.
If the type is THEME_COLOR, the name string of the theme. Theme colors are
defined by the host application.

lineWidth

The width in pixels of the line this pen will draw. The line is centered around the
current point. For example, if lineWidth is 2, drawing a line from (0, 10) to (5, 10)
paints the two rows of pixels directly above and below y-position 10.

Creates a new drawing pen.
Returns a ScriptUIPen object.
rectPath()
controlObj.graphics.rectPath (left, top[, width, height])
left, top

Defines the top left corner of the region, in the coordinate system of the control
that contains this graphics object.

width, height

The width and height of the region in pixels.

Defines a rectangular path in the currentPath object, which can be filled using fillPath() or stroked
using strokePath().
Returns a Point object for the upper left corner of the rectangle, which is the new currentPoint.
strokePath()
controlObj.graphics.fillPath (pen[, path])
pen

The ScriptUIPen object that defines the color and line width.

path

Optional, the ScriptUIPath object for the path. If not supplied, operates on the
currentPath.

Strokes the path segments of a path with a given drawing pen.
Returns undefined.

CHAPTER 4: User-Interface Tools

Graphic customization objects

161

ScriptUIBrush object
A helper object that encapsulates the qualities of a brush used to paint fill into a path in a control. Create
with the newBrush() method of the ScriptUIGraphics object.
Used as a value of backgroundColor and disabledBackgroundColor.
Passed as an argument to fillPath().

ScriptUIBrush object properties
The object contains the following properties:
color

Array of Number

The paint color to use when the type is SOLID_COLOR. An array in the
form [R, B, G, A] specifying the red, green, blue values of the color
and the opacity (alpha channel) value as numbers in the range
[0.0...1.0].
An opacity of 0 is fully transparent, and an opacity of 1 is fully opaque.

theme

String

The name of a color theme to use as a painting texture when the type is
THEME_COLOR. Theme colors are defined by the host application.

type

Number

The brush type, one of these constants:
ScriptUIGraphics.BrushType.SOLID_COLOR
ScriptUIGraphics.BrushType.THEME_COLOR

ScriptUIFont object
A helper object that encapsulates the qualities of a font used to draw text into a control. Create with the
newFont() method of the ScriptUI class.
Used as a value of font.
Passed as an argument to drawString() and measureString().

ScriptUIFont object properties
The object contains the following properties:
family

String

The font family name.

name

String

The complete font name, consisting of the family and style, if specified.

size

Number

The font point size.

CHAPTER 4: User-Interface Tools

style

Graphic customization objects

Object

162

The font style. One of these constants:
ScriptUI.FontStyle.REGULAR
ScriptUI.FontStyle.BOLD
ScriptUI.FontStyle.ITALIC
ScriptUI.FontStyle.BOLDITALIC

substitute

String

The name of a substitution font, a fallback font to substitute for this font
if the requested font family or style is not available.

ScriptUIImage object
A helper object that encapsulates a set of images that can be drawn into a control. Alternate versions of an
image can reflect the state, such as a dimmed version for a disabled control.
An object of this type is created automatically when a script uses a pathname or File object to set the
image property of an Image, IconButton, or ListItem object; the new object becomes the value of that
property.
You can create this object explicitly using the newImage() method of the ScriptUI class. When you do this,
you can specify alternate versions of the image to be used for different control states, such as enabled,
disabled, and rollover.
This object is passed as an argument to drawImage().

ScriptUIImage object properties
The object contains the following read-only properties:
format

String

The image format. Scripts can define images in JPEG and PNG format.
Applications can define images in the resource format.

name

String

The image name, either a file name or resource name.

pathname

String

The full path to the file that contains the image.

size

Dimension

A Dimension object that defines the size of the image in pixels.

I

ScriptUIPath object
A helper object that encapsulates a drawing path for a figure to be drawn into a control. Create the object
the newPath() method and define path segments with the moveto(), lineto(), rectPath(), and ellipsePath()
methods of the ScriptUIGraphics object.
Used as a value of currentPath, where it is acted upon by closePath() and other methods.
Can be passed as an optional argument to fillPath() and strokePath() (which otherwise act upon the
currentPath).
The class defines no properties or methods.

CHAPTER 4: User-Interface Tools

Graphic customization objects

163

ScriptUIPen object
A helper object that encapsulates the qualities of a pen used to stroke path segments in a control. Create
with the newPen() method of the ScriptUIGraphics object.
Used as a value of foregroundColor and disabledForegroundColor.
Passed as an argument to drawString() and strokePath().

ScriptUIPen object properties
The object contains the following properties:
color

Array of
Number

The paint color to use when the type is SOLID_COLOR. An array in the form
[R, B, G, A] specifying the red, green, blue values of the color and the
opacity (alpha channel) value as numbers in the range [0.0...1.0].
An opacity of 0 is fully transparent, and an opacity of 1 is fully opaque.

lineWidth

Number

The pixel width of the drawing line.

theme

String

The name of a color theme to use for drawing when the type is
THEME_COLOR. Theme colors are defined by the host application.

type

Number

The pen type, one of these constants:
ScriptUIGraphics.PenType.SOLID_COLOR
ScriptUIGraphics.PenType.THEME_COLOR

Custom element class
Elements of the Custom class differ from typical UI elements in that they have no default appearance; the
script which creates a custom element is responsible for drawing it by defining the element's onDraw
event handler function. This allows scripts to create any appearance for custom elements that can be
rendered via the drawing functions defined for a UI element's graphics object.
Custom elements have the same common properties that other types of control elements have (see
"Common properties" on page 108). The different types of custom elements have additional properties.
The Custom element class has the following types of elements:

CHAPTER 4: User-Interface Tools

customBoundedValue

Graphic customization objects

164

Can be used to implement controls whose 'value' can vary within minimum
and maximum bounds, like the Progressbar, Slider, and Scrollbar. Has the
same additional properties as those controls:
value
minvalue
maxvalue
shortcutKey

If the value property is changed, the control receives an onChange event
notification, followed by an onDraw event notification, so the element can
redraw itself with the changed state.
customButton

Can be used to implement various types of button controls, like the Button,
IconButton with text, Checkbox, and so on. Additional properties are:
image
shortcutKey
text
value

customView

Has an image property that allows a script to define an image to display.
If no onDraw function is defined and the image property is set, the default
appearance is simply the specified image, rendered centered in the bounds of
the element.

A custom element's onDraw event handler function is not called when the mouse enters or leaves the
screen region occupied by the element. If you need to force a drawing update in such cases, you must call
notify("onDraw") for the element, in response to a mouseOver or mouseout event for the element.
In the following example, the script forces a visual update for a customButton element when the mouse
enters or leaves the button, by handling mouseover or mouseout events for the custom button:
var res =
"""palette {
text:’Custom elements demo’,
properties:{ closeOnKey:’OSCmnd+W’, resizeable:true },
customBtn: Custom {
type:’customButton’,
text:’Redraw original image’
},
customImageViewer: Custom {
type:’customView’,
alignment:[’fill’,’fill’]
}
}""";
var w = new Window (res);
w.customBtn.onDraw = drawButton;
w.customBtn.addEventListener (’mouseover’, btnMouseEventHandler, false);
w.customBtn.addEventListener (’mouseout’, btnMouseEventHandler, false);
...
function btnMouseEventHandler (event) {
try {
//
Redraw the button on mouseover and mouseout
event.target.notify("onDraw");
}
catch (e) {

CHAPTER 4: User-Interface Tools

LayoutManager object

165

}
}
function drawButton (drawingState) {
...
}

LayoutManager object
Controls the automatic layout behavior for a window or container. The subclass AutoLayoutManager
implements the default automatic layout behavior.

AutoLayoutManager object constructor
Create an instance of the AutoLayoutManager class with the new operator:
myWin.layout = new AutoLayoutManager(myWin);

An instance is automatically created when you create a Window or container (group or panel) object, and
referenced by the container’s layout property. This instance implements the default layout behavior unless
you override it.

AutoLayoutManager object properties
The default object has no predefined properties, but a script can assign arbitrary properties to an object it
creates, to store data needed by the script-defined layout algorithm.

AutoLayoutManager object functions
layout()
windowObj.layout.layout (recalculate)
recalculate

Optional. When true, forces the layout manager to recalculate the container size for
this and any child containers. Default is false.

Invokes the automatic layout behavior for the managed container. Adjusts sizes and positions of the
child elements of this window or container according to the placement and alignment property
values in the parent and children.
Invoked automatically the first time the window is displayed. Thereafter, the script must invoke it
explicitly to change the layout in case of changes in the size or position of the parent or children.
Returns undefined
resize()
windowObj.layout.resize ()

Resizes and moves the child elements of the managed container, according to the alignment values
for each child of the container, after the container has been resized by the user or by a script.
See "Automatic layout" on page 86 for details of how alignment affects an element’s size and
location.
Returns undefined.
