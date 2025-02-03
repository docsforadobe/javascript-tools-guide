# Types of controls

The following sections introduce the types of controls you can add to a `Window` or other container element (`panel` or `group`). For details of the properties and functions, and of how to create each type of element, see [Control object constructors](control-objects.md#control-object-constructors).

---

## Containers

These are types of `Control` objects which are contained in windows, and which contain and group other controls.

| **Panel**       | Typically used to visually organize related controls.<br/><br/>- Set the text property to define a title that appears at the top of the panel.<br/>- An optional borderStyle creation property controls the appearance of the border<br/>  drawn around the panel.<br/><br/>You can use panels as separators: those with width of 0 appear as vertical lines and<br/>those with height of 0 appear as horizontal lines:<br/><br/>```javascript<br/>var dlg = new Window( "dialog", "Alert Box Builder" );<br/>dlg.msgPnl = dlg.add( "panel", [ 25, 15, 355, 130 ], "Messages" );<br/>```   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Group**       | Used to visually organize related controls. Unlike `Panels`, `Groups` have no title or<br/>visible border. You can use them to create hierarchies of controls, and for fine control<br/>over layout attributes of certain groups of controls within a larger panel. For examples,<br/>see [Creating more complex arrangements](automatic-layout.md#creating-more-complex-arrangements).                                                                                                                                                                                                 |
| **TabbedPanel** | A panel that contains only Tab objects as its immediate children. It has a selection<br/>property that contains the currently active Tab child. When the value of the selection<br/>property changes, either by a user selecting a different tab, or by a script setting the<br/>property, the TabbedPanel receives an onChange notification.<br/><br/>The title property provides an optional label; the titleLayout property places the<br/>label within the panel.                                                                                                                   |
| **Tab**         | A general container whose parent is a TabbedPanel, with a selectable tab showing a<br/>localizable text value. Its size and position are determined by the parent.                                                                                                                                                                                                                                                                                                                                                                                                                      |

---

## User-interface controls

These are types of `Control` objects that are contained in windows, panels, and groups, and that provide specific kinds of display and user interaction. Control instances are created by passing the corresponding `type` keyword to the `add()` method of a Window or container; see [Control types and creation parameters](control-objects.md#control-types-and-creation-parameters).

These examples do not set bounds explicitly on creation, because it is often more useful to set a preferred size, then allow the layout manager to set the bounds; see [Automatic layout](automatic-layout.md).

### Button

Typically used to initiate some action from a window when a user clicks the button; for example, accepting a dialog's current settings, canceling a dialog, bringing up a new dialog, and so on.

- Set the `text` property to assign a label to identify a Button's function.
- The `onClick` callback method provides behavior.

```javascript
var dlg = new Window( "dialog", "Alert Box Builder" );
dlg.btnPnl = dlg.add( "panel", undefined, "Build it" );
dlg.btnPnl.testBtn = dlg.btnPnl.add( "button", undefined, "Test" );
dlg.btnPnl.buildBtn = dlg.btnPnl.add( "button", undefined, "Build", { name: "ok" } );
dlg.btnPnl.cancelBtn = dlg.btnPnl.add( "button", undefined, "Cancel", { name: "cancel" } );
dlg.show();
```

### IconButton

A button that displays an icon, with or without a text label. Like a text button, typically initiates an action in response to a click.

- The `image` property identifies the icon image; see [Displaying images](#displaying-images).
- The `title` or `text` property provides an optional label; the [titleLayout](control-objects.md#controlobj-titlelayout) property places the label with respect to the image.
- The `onClick` callback method provides behavior.

### Image

Displays an iconic image.

- The `image` property identifies the icon image; see [Displaying images](#displaying-images).
- The `title` property provides an optional label; the [titleLayout](control-objects.md#controlobj-titlelayout) property places the label with respect to the image.

### StaticText

Typically used to display text strings that are not intended for direct manipulation by a user, such as informative messages or labels.

This example creates a Panel and adds several StaticText elements:

```javascript
var dlg = new Window( "dialog", "Alert Box Builder" );
dlg.msgPnl = dlg.add( "panel", undefined, "Messages" );
dlg.msgPnl.titleSt = dlg.msgPnl.add( "statictext", undefined, "Alert box title:" );
dlg.msgPnl.msgSt = dlg.msgPnl.add( "statictext", undefined, "Alert message:" );
dlg.show();
```

### EditText

Allows users to enter text, which is returned to the script when the dialog is dismissed. Text in EditText elements can be selected, copied, and pasted.

- Set the `text` property to assign the initial displayed text in the element, and read it to obtain the current text value, as entered or modified by the user.
- Set the `textselection` property to replace the current selection with new text, or to insert text at the cursor (insertion point). Read this property to obtain the current selection, if any.

This example adds some EditText elements, with initial values that a user can accept or replace:

```javascript
var dlg = new Window( "dialog", "Alert Box Builder" );
dlg.msgPnl = dlg.add( "panel", undefined, "Messages" );
dlg.msgPnl.titleSt = dlg.msgPnl.add( "statictext", undefined, "Alert box title:" );
dlg.msgPnl.titleEt = dlg.msgPnl.add( "edittext", undefined, "Sample Alert" );
dlg.msgPnl.msgSt = dlg.msgPnl.add( "statictext", undefined, "Alert message:" );
dlg.msgPnl.msgEt = dlg.msgPnl.add( "edittext", undefined, "<your message here>", { multiline: true } );
dlg.show();
```

!!! note
    the creation property on the second EditText field, where `multiline: true` indicates a field in which a long text string can be entered. The text wraps to appear as multiple lines.

### EditNumber

Allows users to enter a decimal number, which is returned to the script when the dialog is dismissed. The value entered is validated for being a localized number format and checked against a lower and upper boundary when the control loses focus. Text in EditNumber elements can be selected, copied, and pasted.

!!! note
    This functionality was added in Photoshop 20.0 (CC 2019), and may not exist in other hosts.

- Set the `text` property to assign the initial displayed number in the element, and read it to obtain the current number value, as entered or modified by the user.
- Set the `textselection` property to replace the current selection with new text, or to insert text at the cursor (insertion point). Read this property to obtain the current selection, if any.

This example adds some EditNumber elements, with initial values that a user can accept or replace:

```javascript
var dlg = new Window( "dialog", "Date Box" );
dlg.msgPnl = dlg.add( "panel", undefined, "Enter Date" );
dlg.msgPnl.titleSt = dlg.msgPnl.add( "statictext", undefined, "Month:" );
dlg.msgPnl.titleEt = dlg.msgPnl.add( "editnumber", undefined, 1, 1, 12 );
dlg.msgPnl.msgSt = dlg.msgPnl.add( "statictext", undefined, "Year:" );
dlg.msgPnl.msgEt = dlg.msgPnl.add( "editnumber", undefined, 2025, 2000, 2100 );
dlg.show();
```

!!! note
    Decimal numbers like `2.5` are accepted for minimum and maximum values.

### Checkbox

Allows the user to set a boolean state.

- Set the `text` property to assign an identifying text string that appears next to the clickable box.
- The user can click to select or deselect the box, which shows a checkmark when selected. The `value` is true when it is selected (checked) and false when it is not.

When you create a Checkbox, you can set its value property to specify its initial state and appearance.

```javascript
// Add a checkbox to control the buttons that dismiss an alert box
dlg.hasBtnsCb = dlg.add( "checkbox", undefined, "Should there be alert buttons?" );
dlg.hasBtnsCb.value = true;
```

### RadioButton

Allows the user to select one choice among several.

- Set the text property to assign an identifying text string that appears next to the clickable button.
- The `value` is true when the button is selected. The button shows the state in a platform-specific manner, with a filled or empty dot, for example.

You group a related set of radio buttons by creating all the related elements one after another. When any button's value becomes true, the value of all other buttons in the group becomes false. When you create a group of radio buttons, you should set the state of one of them true:

```javascript
var dlg = new Window( "dialog", "Alert Box Builder" );
dlg.alertBtnsPnl = dlg.add( "panel", undefined, "Button alignment" );
dlg.alertBtnsPnl.alignLeftRb = dlg.alertBtnsPnl.add( "radiobutton", undefined, "Left" );
dlg.alertBtnsPnl.alignCenterRb = dlg.alertBtnsPnl.add( "radiobutton", undefined, "Center" );
dlg.alertBtnsPnl.alignRightRb = dlg.alertBtnsPnl.add( "radiobutton", undefined, "Right" );
dlg.alertBtnsPnl.alignCenterRb.value = true;
dlg.show();
```

### Progressbar

Typically used to display the progress of a time-consuming operation. A colored bar covers a percentage of the area of the control, representing the percentage completion of the operation. The `value` property reflects and controls how much of the visible area is colored, relative to the maximum value (`maxvalue`). By default the range is 0 to 100, so the `value = 50` when the operation is half done.

### Slider

Typically used to select within a range of values. The slider is a horizontal bar with a draggable indicator, and you can click a point on the slider bar to jump the indicator to that location. The `value` property reflects and controls the position of the indicator, within the range determined by `minvalue` and `maxvalue`. By default the range is 0 to 100, so setting `value = 50` moves the indicator to the middle of the bar.

### Scrollbar

Like a slider, the scrollbar is a bar with a draggable indicator. It also has "stepper" buttons at each end, that you can click to jump the indicator by the amount in the `stepdelta` property. If you click a point on the bar outside the indicator, the indicator jumps by the amount in the jumpdelta property.

You can create scrollbars with horizontal or vertical orientation; if `width` is greater than `height`, it is horizontal, otherwise it is vertical. Arguments to the `add` method that creates the scrollbar define values for the `value`, `minvalue` and `maxvalue` properties.

Scrollbars are often created with an associated `EditText` field to display the current value of the scrollbar, and to allow setting the scrollbar's position to a specific value.

This example creates a scrollbar with associated `StaticText` and `EditText` elements within a panel:

```javascript
dlg.sizePnl = dlg.add( "panel", undefined, "Dimensions" );
dlg.sizePnl.widthSt = dlg.sizePnl.add( "statictext", undefined, "Width:" );
dlg.sizePnl.widthScrl = dlg.sizePnl.add( "scrollbar", undefined, 300, 300, 800 );
dlg.sizePnl.widthEt = dlg.sizePnl.add( "edittext" );
```

### ListBox, DropDownList and TreeView

These controls display lists of items, which are represented by `ListItem` objects in the `items` property. You can access the items in this array using a 0-based index.

- A `ListBox` control displays a list of choices. When you create the object, you specify whether it allows the user to select only one or multiple items. If a list contains more items than can be displayed in the available area, a scrollbar may appear that allows the user to scroll through all the list items. A list box can display items in multiple columns; see [Creating multi-column lists](#creating-multi-column-lists).
- A `DropDownList` control displays a single visible item. When you click the control, a list drops down and allows you to select one of the other items in the list. Drop-down lists can have nonselectable separator items for visually separating groups of related items, as in a menu.
- A `TreeView` control is similar to a ListBox, except that the items can have child items. Items with children can be expanded or collapsed to show or hide the child items. Child items can in turn contain children.
- The `title` property provides an optional label; the [titleLayout](control-objects.md#controlobj-titlelayout) property places the label with respect to the list.

You can specify the choice items on creation of the list object, or afterward using the list object's `add()` method. You can remove items programmatically with the list object's `remove()` and `removeAll()` methods.

### ListItem

Items added to or inserted into any type of list control are `ListItem` objects, with properties that can be manipulated from a script. ListItem elements can be of the following types:

| `item`      | The typical item in any type of list. It displays text or an image, and can be<br/>selected. To display an image, set the item object's image property; [Displaying images](#displaying-images).   |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `separator` | A separator is a nonselectable visual element in a drop-down list.<br/>Although it has a text property, the value is ignored, and the item is displayed as<br/>a horizontal line.                  |
| `node`      | A displayable and selectable item in a `TreeView` control which can contain<br/>other `ListItem` objects, including other items of type node.                                                      |

### FlashPlayer

Runs a Flash movie within a ScriptUI window. Its control's methods allow you to load a movie from an SWF file and control the playback. See [FlashPlayer control functions](control-objects.md#flashplayer-control-functions).

You can also use the control object to communicate with the Flash application, calling ActionScript methods, and making JavaScript methods defined in your Adobe application script available to the Flash ActionScript code. See [Calling ActionScript functions from a ScriptUI script](communicating-with-the-flash-application.md#calling-actionscript-functions-from-a-scriptui-script).

The `title` property provides an optional label; the [titleLayout](control-objects.md#controlobj-titlelayout) property places the label with respect to the player.

---

## Displaying images

You can display icon images in `Image` or `IconButton` controls, or display images in place of strings or in addition to strings as the selectable items in a `Listbox` or `DropdownList` control. In each case, the image is defined by setting the element's `image` property. You can set it to a [ScriptUIImage object](graphic-customization-objects.md#scriptuiimage-object); a named icon resource; a [File object](../file-system-access/file-object.md); or the pathname of a file containing the iconic image, or of an alias or shortcut to that file (see [Specifying paths](../file-system-access/using-file-and-folder-objects.md#specifying-paths)).

The image data for an icon can be in Portable Network Graphics (PNG) format, or in Joint Photographic Experts Group (JPEG) format. See [http://www.libpng.org](http://www.libpng.org) and [http://www.jpeg.org/](http://www.jpeg.org/) for detailed information on these formats.

You can set or reset the `image` property at any time to change the image displayed in the element.

The scripting environment can define icon *resources*, which are available to scripts by name. To specify an icon resource, set a control's `image` property to the resource's JavaScript name, or refer to the resource by name when creating the control. For example, to create a button with an application-defined icon resource:

```javascript
myWin.upBtn = myWin.add ( "iconbutton", undefined, "SourceFolderIcon" );
```

Photoshop CC, for example, defines these icon resources:

- `Step1Icon`
- `Step2Icon`
- `Step3Icon`
- `Step4Icon`
- `SourceFolderIcon`
- `DestinationFolderIcon`

If a script does not explicitly set the `preferredSize` or `size` property of an element that displays a icon image, the value of `preferredSize` is determined by the dimensions of the iconic image. If the size values are explicitly set to dimensions smaller than those of the actual image graphic, the displayed image is clipped. If they are set to dimensions larger than those of the image graphic, the displayed image is centered in the larger space. An image is never scaled to fit the available space.

---

## Creating multi-column lists

In list controls ([ListBox, DropDownList and TreeView](#listbox-dropdownlist-treeview)), a set of [ListItem](#listitem) objects represents the individual choices in the list. Each choice can be labeled with a localizable string, an image, or both, as specified by the [text](control-objects.md#controlobj-text) and [image](control-objects.md#controlobj-image) properties of the [ListItem](#listitem) (see [Displaying images](#displaying-images)).

You can define a [ListBox](control-objects.md#control-type-listbox) to have multiple columns, by specifying the `numberOfColumns` creation parameter. By default, the number of columns is 1. If you specify multiple columns, you can also use the creation parameters to specify whether headers are shown, and the header text for each column.

If you specify more than one column, each [ListItem]() object that you add to the box specifies one selectable row. The `text` and `image` of the [ListItem]() object specifies the label in the first column, and the [subitems](control-objects.md#controlobj-subitems) property specifies labels that appear in that row for the remaining columns.

The [subitems](control-objects.md#controlobj-subitems) value is an array, whose length is one less than the number of columns. That is, the first member, `ListItem.subitems[0]`, specifies the label in the second column. Each member specifies one label, as a JavaScript object with two properties:

```javascript
{ text : displayString , image : imageFileReference }
```

For example, the following fragment defines a list box with two columns, and specifies the labels in each column for the two choices:

```javascript
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
```

This creates a control that looks like this:

![Multi-Column Lists](user-interface-tools/_static/04_user-interface-tools_types-of-controls_multi-column-lists.jpg)

Notice that the columns have headers, and the label in the second column of the second row has both text and an image.

---

## Prompts and alerts

Static functions on the `Window` class are globally available to display short messages in standard dialogs.

The host application controls the appearance of these simple dialogs, so they are consistent with other alert and message boxes displayed by the application. You can often use these standard dialogs for simple interactions with your users, rather than designing special-purpose dialogs of your own.

Use the static functions `alert`, `confirm`, and `prompt` on the `Window` class to invoke these dialogs with your own messages. You do not need to create a Window object to call these functions.

---

## Modal dialogs

A modal dialog is initially invisible. Your script invokes it using the `show` method, which does not return until the dialog has been dismissed. The user can dismiss it by using a platform-specific window gesture, or by using one of the dialog controls that you supply, typically an **OK** or **Cancel** button. The `onClick` method of such a button must call the `close` or `hide` method to close the dialog. The `close` method allows you to pass a value to be returned by the show method.

For an example of how to define such buttons and their behavior, see [Defining behavior with event callbacks and listeners](defining-behavior-with-event-callbacks-and-listeners.md).

### Creating and using modal dialogs

A dialog typically contains some controls that the user must interact with, to make selections or enter values that your script will use. In some cases, the result of the user action is stored in the object, and you can retrieve it after the dialog has been dismissed. For example, if the user changes the state of a `Checkbox` or `RadioButton`, the new state is found in the control's `value` property.

However, if you need to respond to a user action while the dialog is still active, you must assign the control a callback function for the interaction event, either `onClick` or `onChange`. The callback function is the value of the `onClick` or `onChange` property of the control.

For example, if you need to validate a value that the user enters in a edittext control, you can do so in an `onChange` callback handler function for that control. The callback can perform the validation, and perhaps display an alert to inform the user of errors.

Sometimes, a modal dialog presents choices to the user that must be correct before your script allows the dialog to be dismissed. If your script needs to validate the state of a dialog after the user clicks OK, you can define an `onClose` event handler for the dialog. This callback function is invoked whenever a window is closed. If the function returns `true`, the window is closed, but if it returns `false`, the close operation is cancelled and the window remains open.

Your `onClose` handler can examine the states of any controls in the dialog to determine their correctness, and can show alert messages or use other modal dialogs to alert the user to any errors that must be corrected. It can then return `true` to allow the dialog to be dismissed, or `false` to allow the user to correct any errors.

### Dismissing a modal dialog

Every modal dialog should have at least one button that the user can click to dismiss the dialog. Typically modal dialogs have an OK and a Cancel button to close the dialog with or without accepting changes that were made in it.

You can define `onClick` callbacks for the buttons that close the parent dialog by calling its close method. You have the option of sending a value to the close method, which is in turn passed on to and returned from the show method that invoked the dialog. This return value allows your script to distinguish different closing events; for example, clicking OK can return 1, clicking Cancel can return 2. However, for this typical behavior, you do not need to define these callbacks explicitly; see [Default and cancel elements](#default-and-cancel-elements).

For some dialogs, such as a simple alert with only an OK button, you do not need to return any value. For more complex dialogs with several possible user actions, you might need to distinguish more outcomes. If you need to distinguish more than two closing states, you must define your own closing callbacks rather than relying on the default behavior.

If, by mistake, you create a modal dialog with no buttons to dismiss it, or if your dialog does have buttons, but their `onClick` handlers do not function properly, a user can still dismiss the dialog by typing ESC. In this case, the system will execute a call to the dialog's `close` method, passing a value of 2. This is not, of course, a recommended way to design your dialogs, but is provided as an escape hatch to prevent the application from hanging in case of an error in the operations of your dialog.

### Default and cancel elements

The user can typically dismiss a modal dialog by clicking an OK or Cancel button, or by typing certain keyboard shortcuts. By convention, typing ENTER is the same as clicking OK or the default button, and typing ESC is the same as clicking Cancel. The keyboard shortcut has the same effect as calling notify for the associated `button` control.

To determine which control is notified by which keyboard shortcut, set the `Dialog` object's `defaultElement` and `cancelElement` properties. The value is the control object that should be notified when the user types the associated keyboard shortcut.

- For buttons assigned as the `defaultElement`, if there is no `onClick` handler associated with the button, clicking the button or typing ENTER calls the parent dialog's `close` method, passing a value of 1 to be returned by the show call that opened the dialog.
- For buttons assigned as the `cancelElement`, if there is no `onClick` handler associated with the button, clicking the button or typing ESC calls the parent dialog's `close` method, passing a value of 2 to be returned by the show call that opened the dialog.

If you do not set the `defaultElement` and `cancelElement` properties explicitly, ScriptUI tries to choose reasonable defaults when the dialog is about to be shown for the first time. For the default element, it looks for a button whose `name` or `text` value is `"ok"` (disregarding case). For the cancel element, it looks for a button whose `name` or `text` value is `"cancel"` (disregarding case). Because it looks at the name value first, this works even if the text value is localized. If there is no suitable button in the dialog, the property value remains `null`, which means that the keyboard shortcut has no effect in that dialog.

To make this feature most useful, it is recommended that you always provide the `name` creation property for buttons meant to be used in this way.
