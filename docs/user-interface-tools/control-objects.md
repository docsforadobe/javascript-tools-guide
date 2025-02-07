# Control objects

UI elements that belong to windows can be containers or controls. Containers share some aspects of top-level windows, and some aspects of controls, and so are described here with controls.

---

## Control object constructors

Use the `add` method to create new containers and controls. The `add` method is available on `window` and container (`panel` and `group`) objects. (See also [add()](#add) for [DropDownList](#dropdownlist) and [ListBox](#listbox) controls.)

### add()

`containerObj.(type[, bounds, text, {creation_props}]);`

#### Description

Creates and returns a new control or container object and adds it to the children of this window or container.

#### Parameters

|    Parameter     |                         Type                         |                                                                                                                                    Description                                                                                                                                     |
| ---------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`           | String                                               | The control type. See [Control types and creation parameters](#control-types-and-creation-parameters).                                                                                                                                                                             |
| `bounds`         | [Bounds object](size-and-location-objects.md#bounds) | Optional. A bounds specification that describes the size and position of the new control or container, relative to its parent. If supplied, this value creates a new [Bounds](size-and-location-objects.md#bounds) object which is assigned to the new object's `bounds` property. |
| `text`           | String                                               | Optional. Initial text to be displayed in the control as the title, label, or contents, depending on the control type. If supplied, this value is assigned to the new object's `text` property.                                                                                    |
| `creation_props` | Object                                               | Optional. The properties of this object specify creation parameters, which are specific to each object type. See [Control types and creation parameters](#control-types-and-creation-parameters).                                                                                  |

#### Returns

Returns the new object, or `null` if unable to create the object.

---

## Control types and creation parameters

The following keywords can be used in string literals as the type specifier for the `add` method, available on `Window` and container (`Panel` and `Group`) objects. The class names can be used in resource specifications to define controls within a container element (`Window`, `Panel`, or `Group`).

All types of controls, including containers, have an optional creation parameter `name` that allows you to give the object a unique name.

---

### button

Class Name: `Button`

#### Description

A pushbutton containing a mouse-sensitive text string. Calls the [onClick](#onclick) callback if the control is clicked or if its [notify()](#notify) method is called.

#### Parameters

|       Parameter       |                         Type                         |                          Description                           |
| --------------------- | ---------------------------------------------------- | -------------------------------------------------------------- |
| `bounds`              | [Bounds object](size-and-location-objects.md#bounds) | Optional. The control's position and size.                     |
| `text`                | String                                               | Optional. The text displayed in the control.                   |
| `creation_properties` | Object                                               | Optional. An object that contains any of the properties below. |

#### Creation Properties

| Property |  Type  |                                                                                                                        Description                                                                                                                        |
| -------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`   | String | A unique name for the control. For a modal dialog, the special name "ok" makes this [defaultElement](window-object.md#defaultelement), and the special name "cancel" makes this the [cancelElement](window-object.md#cancelelement) of the parent dialog. |

#### Example

To add to a window `w`:

```javascript
w.add("button"[, bounds, text, {creation_properties}]);
```

---

### checkbox

Class Name: `Checkbox`

#### Description

A dual-state control showing a box with a checkmark when value is `true`, empty when `value` is `false`.

Calls the [onClick](#onclick) callback if the control is clicked or if its [notify()](#notify) method is called.

#### Parameters

|       Parameter       |                         Type                         |                          Description                           |
| --------------------- | ---------------------------------------------------- | -------------------------------------------------------------- |
| `bounds`              | [Bounds object](size-and-location-objects.md#bounds) | Optional. The control's position and size.                     |
| `text`                | String                                               | Optional. The text displayed in the control.                   |
| `creation_properties` | Object                                               | Optional. An object that contains any of the properties below. |

#### Creation Properties

| Property |  Type  |          Description           |
| -------- | ------ | ------------------------------ |
| `name`   | String | A unique name for the control. |

#### Example

To add to a window `w`:

```javascript
w.add("checkbox"[, bounds, text, {creation_properties}]);
```

---

### dropdownlist

Class Name: `DropDownList`

#### Description

A drop-down list with zero or more items. Calls the [onChange](#onchange) callback if the item selection is changed by a script or the user, or if the object's [notify()](#notify) method is called.

#### Parameters

|       Parameter       |                         Type                         |                                                                                                      Description                                                                                                       |
| --------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bounds`              | [Bounds object](size-and-location-objects.md#bounds) | Optional. The control's position and size.                                                                                                                                                                             |
| `items`               | Array of strings                                     | Optional. Supply this argument or the `creation_properties` argument, not both. The text of each list item. A `ListItem` object is created for each item. An item with the text string `"-"` creates a separator item. |
| `creation_properties` | Object                                               | Optional. An object that contains any of the properties below.                                                                                                                                                         |

#### Creation Properties

| Property |       Type       |                             Description                             |
| -------- | ---------------- | ------------------------------------------------------------------- |
| `name`   | String           | A unique name for the control.                                      |
| `items`  | Array of strings | The text of each list item. See the Parameters table for more info. |

#### Example

To add to a window `w`:

```javascript
w.add( "dropdownlist", bounds[, items, {creation_properties}] );
```

---

### editnumber

Class Name: `EditNumber`

!!! note
    This functionality was added in Photoshop 20.0 (CC 2019), and may not exist in other hosts.

#### Description

An editable text field the user can enter decimal numbers into. Fractions are allowed.

Calls the [onChange](#onchange) callback if the text is changed and the user types `ENTER` or the control loses focus, or if its [notify()](#notify) method is called.

Calls the [onChanging](#onchanging) callback when any change is made to the text.

The `textselection` property contains currently selected text.

#### Parameters

|       Parameter       |                         Type                         |                          Description                           |
| --------------------- | ---------------------------------------------------- | -------------------------------------------------------------- |
| `bounds`              | [Bounds object](size-and-location-objects.md#bounds) | Optional. The control's position and size.                     |
| `text`                | String                                               | Optional. The text displayed in the control.                   |
| `minValue`            | Number                                               | Optional. Minimum accepted value of number to be entered.      |
| `maxValue`            | Number                                               | Optional. Maximum accepted value of number to be entered.      |
| `creation_properties` | Object                                               | Optional. An object that contains any of the properties below. |

#### Creation Properties

|         Property          |  Type   |                                                                                                                                                                                                                     Description                                                                                                                                                                                                                     |
| ------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                    | String  | A unique name for the control.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `readonly`                | Boolean | Optional. When `false` (the default), the control accepts text input. When `true`, the control does not accept input but only displays the contents of the `text` property.                                                                                                                                                                                                                                                                         |
| `noecho`                  | Boolean | Optional. When `false` (the default), the control displays input text. When `true`, the control does not display input text (used for password input fields).                                                                                                                                                                                                                                                                                       |
| `enterKeySignalsOnChange` | Boolean | Optional. When `false` (the default), the control signals an [onChange](#onchange) event when the editable text is changed and the control loses the keyboard focus (that is, the user tabs to another control, clicks outside the control, or types `ENTER`). When `true`, the control only signals an `onChange` event when the editable text is changed and the user types `ENTER`; other changes to the keyboard focus do not signal the event. |
| `borderless`              | Boolean | Optional. When `true`, the control is drawn with no border. Default is `false`.                                                                                                                                                                                                                                                                                                                                                                     |

#### Example

To add to a window `w`:

```javascript
w.add("editnumber"[, bounds, text, minValue, maxValue, {creation_properties}]);
```

---

### edittext

Class Name: `EditText`

#### Description

An editable text field that the user can change. Calls the [onChange](#onchange) callback if the text is changed and the user types `ENTER` or the control loses focus, or if its [notify()](#notify) method is called. Calls the [onChanging](#onchanging) callback when any change is made to the text.

The `textselection` property contains currently selected text.

#### Parameters

|       Parameter       |                         Type                         |                          Description                           |
| --------------------- | ---------------------------------------------------- | -------------------------------------------------------------- |
| `bounds`              | [Bounds object](size-and-location-objects.md#bounds) | Optional. The control's position and size.                     |
| `text`                | String                                               | Optional. The text displayed in the control.                   |
| `creation_properties` | Object                                               | Optional. An object that contains any of the properties below. |

#### Creation Properties

|         Property          |  Type   |                                                                                                                                                                                                                Description                                                                                                                                                                                                                |
| ------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                    | String  | A unique name for the control.                                                                                                                                                                                                                                                                                                                                                                                                            |
| `readonly`                | Boolean | When `false` (the default), the control accepts text input. When `true`, the control does not accept input but only displays the contents of the `text` property.                                                                                                                                                                                                                                                                         |
| `noecho`                  | Boolean | When `false` (the default), the control displays input text. When `true`, the control does not display input text (used for password input fields).                                                                                                                                                                                                                                                                                       |
| `enterKeySignalsOnChange` | Boolean | When `false` (the default), the control signals an [onChange](#onchange) event when the editable text is changed and the control loses the keyboard focus (that is, the user tabs to another control, clicks outside the control, or types `ENTER`). When `true`, the control only signals an `onChange` event when the editable text is changed and the user types `ENTER`; other changes to the keyboard focus do not signal the event. |
| `borderless`              | Boolean | When `true`, the control is drawn with no border. Default is `false`.                                                                                                                                                                                                                                                                                                                                                                     |
| `multiline`               | Boolean | When `false` (the default), the control accepts a single line of text. When `true`, the control accepts multiple lines, in which case the text wraps within the width of the control.                                                                                                                                                                                                                                                     |
| `scrollable`              | Boolean | (For multiline elements only) When `true` (the default), the text field has a vertical scrollbar that is enabled when the element contains more text than fits in the visible area. When `false`, no vertical scrollbar appears; if the element contains more text than fits in the visible area, the arrow keys can be used to scroll the text up and down.                                                                              |

#### Example

To add to a window `w`:

```javascript
w.add("edittext"[, bounds, text, {creation_properties}]);
```

---

### flashplayer

Class Name: `FlashPlayer`

#### Description

A control that contains a Flash Player, which can load and play Flash movies stored in SWF files.

The ScriptUI FlashPlayer element runs the Flash application within an Adobe application. The Flash application runs ActionScript, a different implementation of JavaScript from the ExtendScript version of JavaScript that Adobe applications run.

A control object of this type contains functions that allow your script to load SWF files, control movie playback, and communicate with the ActionScript environment. See [FlashPlayer control functions](#flashplayer-control-functions).

#### Parameters

|       Parameter       |                             Type                              |                                   Description                                    |
| --------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `bounds`              | [Bounds object](size-and-location-objects.md#bounds)          | Optional. The control's position and size.                                       |
| `moveToLoad`          | String or [File object](../file-system-access/file-object.md) | Optional. A path or URL string or File for the SWF file to load into the player. |
| `creation_properties` | Object                                                        | Optional. An object that contains any of the properties below.                   |

#### Creation Properties

| Property |  Type  |          Description           |
| -------- | ------ | ------------------------------ |
| `name`   | String | A unique name for the control. |

#### Example

To add to a window `w`:

```javascript
w.add("flashplayer"[, bounds, movieToLoad, {creation_properties}]);
```

---

### group

Class Name: `Group`

#### Description

A container for other controls. Containers have additional properties that control the children; see [Container Attributes](window-object.md#container-attributes).

Hiding a group hides all its children. Making it visible makes visible those children that are not individually hidden.

#### Parameters

|       Parameter       |                         Type                         |                          Description                           |
| --------------------- | ---------------------------------------------------- | -------------------------------------------------------------- |
| `bounds`              | [Bounds object](size-and-location-objects.md#bounds) | Optional. The control's position and size.                     |
| `creation_properties` | Object                                               | Optional. An object that contains any of the properties below. |

#### Creation Properties

| Property |  Type  |          Description           |
| -------- | ------ | ------------------------------ |
| `name`   | String | A unique name for the control. |

#### Example

To add to a window `w`:

```javascript
w.add("group"[, bounds, {creation_properties}]);
```

---

### iconbutton

Class Name: `IconButton`

#### Description

A mouse-sensitive pushbutton containing an icon. Calls the [onClick](#onclick) callback if the control is clicked or if its [notify()](#notify) method is called.

#### Parameters

|       Parameter       |                                       Type                                       |                                                                             Description                                                                              |
| --------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bounds`              | [Bounds object](size-and-location-objects.md#bounds)                             | Optional. The control's position and size.                                                                                                                           |
| `icon`                | Named resource, pathname, or [File object](../file-system-access/file-object.md) | Optional. The named resource for the icon or family of icons displayed in the button control, or a pathname or File for an image file. Images must be in PNG format. |
| `creation_properties` | Object                                                                           | Optional. An object that contains any of the properties below.                                                                                                       |

#### Creation Properties

+----------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property |  Type   |                                                                                                                          Description                                                                                                                           |
+==========+=========+================================================================================================================================================================================================================================================================+
| `name`   | String  | A unique name for the control.                                                                                                                                                                                                                                 |
+----------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `style`  | String  | A string for the visual style, one of:                                                                                                                                                                                                                         |
|          |         |                                                                                                                                                                                                                                                                |
|          |         | - `button`: Has a visible border with a raised or 3D appearance.                                                                                                                                                                                               |
|          |         | - `toolbutton`: Has a flat appearance, appropriate for inclusion in a toolbar                                                                                                                                                                                  |
+----------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `toggle` | Boolean | For a button-style control, a value of `true` causes it to get a button-pressed appearance the first time it is clicked, and alternate with the unpressed appearance each time it is clicked. The toggle state is reflected in the control's `value` property. |
+----------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### Example

To add to a window `w`:

```javascript
w.add("iconbutton"[, bounds, icon, {creation_properties}]);
```

---

### image

Class Name: `Image`

#### Description

Displays an icon or image.

#### Parameters

|       Parameter       |                                       Type                                       |                                                                             Description                                                                              |
| --------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `bounds`              | [Bounds object](size-and-location-objects.md#bounds)                             | Optional. The control's position and size.                                                                                                                           |
| `icon`                | Named resource, pathname, or [File object](../file-system-access/file-object.md) | Optional. The named resource for the icon or family of icons displayed in the button control, or a pathname or File for an image file. Images must be in PNG format. |
| `creation_properties` | Object                                                                           | Optional. An object that contains any of the properties below.                                                                                                       |

#### Creation Properties

| Property |  Type  |          Description           |
| -------- | ------ | ------------------------------ |
| `name`   | String | A unique name for the control. |

#### Example

To add to a window `w`:

```javascript
w.add("image"[, bounds, icon, {creation_properties}]);
```

---

### item

Class Name: `Array of ListItem`

#### Description

The choice items in a list box or drop-down list. The objects are created when items are specified on creation of the parent list object, or afterward using the list control's [add()](#add) method.

Items in a drop-down list can be of type `separator`, in which case they cannot be selected, and are shown as a horizontal line.

Item objects have these properties which are not found in other controls:

- [checked](#checked)
- [expanded](#expanded)
- [image](#image)
- [index](#index)
- [selected](#selected)

---

### listbox

Class Name: `ListBox`

#### Description

A list box with zero or more items. Calls the [onChange](#onchange) callback if the item selection is changed by a script or the user, or if the object's [notify()](#notify) method is called. A double click on an item selects that item and calls the [onDoubleClick](#ondoubleclick) callback.

#### Parameters

|       Parameter       |                         Type                         |                                                                                                                                                                 Description                                                                                                                                                                  |     |
| --------------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| `bounds`              | [Bounds object](size-and-location-objects.md#bounds) | Optional. The control's position and size.                                                                                                                                                                                                                                                                                                   |     |
| `items`               | Array of Strings                                     | Optional. The text of each list item. A [ListItem](types-of-controls.md#listitem) object is created for each item. Supply this argument, or the items property in `creation_properties`, not both. A [ListItem](types-of-controls.md#listitem) object is created for each item. An item with the text string `"-"` creates a separator item. |     |
| `creation_properties` | Object                                               | Optional. An object that contains any of the properties below.                                                                                                                                                                                                                                                                               |     |

#### Creation Properties

|     Property      |       Type       |                                                                                                                                                                     Description                                                                                                                                                                      |
| ----------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`            | String           | A unique name for the control.                                                                                                                                                                                                                                                                                                                       |
| `multiselect`     | Boolean          | When `false` (the default), only one item can be selected. When `true`, multiple items can be selected.                                                                                                                                                                                                                                              |
| `items`           | Array of Strings | The text of each list item. Supply this property, or the `items` argument, not both. This form is most useful for elements defined using [Resource specifications](resource-specifications.md).                                                                                                                                                      |
| `numberOfColumns` | Number           | A number of columns in which to display the items; default is 1. When there are multiple columns, each [ListItem](types-of-controls.md#listitem) object represents a single selectable row. Its [text](#text) and [image](#image) values supply the label for the first column, and the `subitems` property specifies labels for additional columns. |
| `showHeaders`     | Boolean          | `true` to display column titles.                                                                                                                                                                                                                                                                                                                     |
| `columnWidths`    | Array of Numbers | An array of numbers for the preferred width in pixels of each column.                                                                                                                                                                                                                                                                                |
| `columnTitles`    | Array of Strings | A corresponding array of strings for the title of each column, to be shown if `showHeaders` is `true`.                                                                                                                                                                                                                                               |

#### Example

To add to a window `w`:

```javascript
w.add("listbox", bounds[, items, {creation_properties}]);
```

---

### panel

Class Name: `Panel`

#### Description

A container for other types of controls, with an optional frame.

Containers have additional properties that control the children; see [Container Attributes](window-object.md#container-attributes). Hiding a panel hides all its children. Making it visible makes visible those children that are not individually hidden.

#### Parameters

|       Parameter       |                         Type                         |                          Description                           |
| --------------------- | ---------------------------------------------------- | -------------------------------------------------------------- |
| `bounds`              | [Bounds object](size-and-location-objects.md#bounds) | Optional. The control's position and size.                     |
| `text`                | String                                               | Optional. The text displayed in the border of the panel.       |
| `creation_properties` | Object                                               | Optional. An object that contains any of the properties below. |

#### Creation Properties

+-----------------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|       Property        |  Type   |                                                                                                                              Description                                                                                                                               |
+=======================+=========+========================================================================================================================================================================================================================================================================+
| `name`                | String  | A unique name for the control.                                                                                                                                                                                                                                         |
+-----------------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `borderStyle`         | String  | A string that specifies the appearance of the border drawn around the panel. Default is `etched`. One of:                                                                                                                                                              |
|                       |         |                                                                                                                                                                                                                                                                        |
|                       |         | - `black`                                                                                                                                                                                                                                                              |
|                       |         | - `etched`                                                                                                                                                                                                                                                             |
|                       |         | - `gray`                                                                                                                                                                                                                                                               |
|                       |         | - `raised`                                                                                                                                                                                                                                                             |
|                       |         | - `sunken`                                                                                                                                                                                                                                                             |
|                       |         | - `topDivider`: draws a horizonal line at the top of the panel only.                                                                                                                                                                                                   |
|                       |         |                                                                                                                                                                                                                                                                        |
|                       |         | !!! warning                                                                                                                                                                                                                                                            |
|                       |         | The `topDivider` property is officially undocumented and was found via research. Please contribute if you have more information on it!                                                                                                                                 |
+-----------------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `subPanelCoordinates` | Boolean | When `true`, this panel automatically adjusts the positions of its children for compatability with Photoshop CS. Default is `false`, meaning that the panel does not adjust the positions of its children, even if the parent window has automatic adjustment enabled. |
+-----------------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### Example

To add to a window `w`:

```javascript
w.add("panel"[, bounds, text, {creation_properties}]);
```

---

### progressbar

Class Name: `Progressbar`

#### Description

A horizontal rectangle that shows progress of an operation.

All `progressbar` controls have a horizontal orientation. The `value` property contains the current position of the progress indicator; the default is 0. There is a `minvalue` property, but it is always 0; attempts to set it to a different value are silently ignored.

#### Parameters

|       Parameter       |                         Type                         |                                                            Description                                                            |
| --------------------- | ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `bounds`              | [Bounds object](size-and-location-objects.md#bounds) | Optional. The control's position and size.                                                                                        |
| `value`               | Number                                               | Optional. The initial position of the progress indicator. Default is 0.                                                           |
| `minvalue`            | Number                                               | Optional. The minimum value that the `value` property can be set to. Default is 0. Together with `maxvalue`, defines the range.   |
| `maxvalue`            | Number                                               | Optional. The maximum value that the `value` property can be set to. Default is 100. Together with `minvalue`, defines the range. |
| `creation_properties` | Object                                               | Optional. An object that contains any of the properties below.                                                                    |

#### Creation Properties

| Property |  Type  |          Description           |
| -------- | ------ | ------------------------------ |
| `name`   | String | A unique name for the control. |

#### Example

To add to a window `w`:

```javascript
w.add("progressbar"[, bounds, value, minvalue, maxvalue, creation_properties}]);
```

---

### radiobutton

Class Name: `RadioButton`

#### Description

A dual-state control, grouped with other radiobuttons, of which only one can be in the selected state. Shows the selected state when `value` is `true`, empty when value is `false`. Calls the [onClick](#onclick) callback if the control is clicked or if its [notify()](#notify) method is called.

All radiobuttons in a group must be created sequentially, with no intervening creation of other element types. Only one `radiobutton` in a group can be set at a time; setting a different `radiobutton` unsets the original one.

#### Parameters

|       Parameter       |                         Type                         |                          Description                           |
| --------------------- | ---------------------------------------------------- | -------------------------------------------------------------- |
| `bounds`              | [Bounds object](size-and-location-objects.md#bounds) | Optional. The control's position and size.                     |
| `text`                | String                                               | Optional. The text displayed in the control.                   |
| `creation_properties` | Object                                               | Optional. An object that contains any of the properties below. |

#### Creation Properties

| Property |  Type  |          Description           |
| -------- | ------ | ------------------------------ |
| `name`   | String | A unique name for the control. |

#### Example

To add to a window `w`:

```javascript
w.add("radiobutton"[, bounds, text, {creation_properties}]);
```

---

### scrollbar

Class Name: `Scrollbar`

#### Description

A scrollbar with a draggable scroll indicator and stepper buttons to move the indicator. The `scrollbar` control has a horizontal orientation if the `width` is greater than the `height` at creation time, or vertical if its `height` is greater than its `width`.

Calls the [onChange](#onchange) callback after the position of the indicator is changed or if its [notify()](#notify) method is called. Calls the [onChanging](#onchanging) callback repeatedly while the user is moving the indicator.

#### Properties

|  Property   |  Type  |                                                                              Description                                                                              |
| ----------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `value`     | Number | Contains the current position of the scrollbar's indicator within the scrolling area, within the range of `minvalue` and `maxvalue`.                                  |
| `stepdelta` | Number | Determines the scrolling unit for the up or down arrow. Default is `1`.                                                                                               |
| `jumpdelta` | Number | Determines the scrolling unit for a jump (as when the bar is clicked outside the indicator or arrows); default is 20% of the range between `minvalue` and `maxvalue`. |

#### Parameters

|       Parameter       |                         Type                         |                                                                 Description                                                                 |
| --------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `bounds`              | [Bounds object](size-and-location-objects.md#bounds) | Optional. The control's position and size.                                                                                                  |
| `value`               | Number                                               | Optional. The initial position of the scroll indicator. Default is 0.                                                                       |
| `minvalue`            | Number                                               | Optional. The minimum value that the `value` property can be set to. Default is 0. Together with `maxvalue`, defines the scrolling range.   |
| `maxvalue`            | Number                                               | Optional. The maximum value that the `value` property can be set to. Default is 100. Together with `minvalue`, defines the scrolling range. |
| `creation_properties` | Object                                               | Optional. An object that contains any of the properties below.                                                                              |

#### Creation Properties

| Property |  Type  |          Description           |
| -------- | ------ | ------------------------------ |
| `name`   | String | A unique name for the control. |

#### Example

To add to a window `w`:

```javascript
w.add("scrollbar"[, bounds, value, minvalue, maxvalue, {creation_properties}]);
```

---

### slider

Class Name: `Slider`

#### Description

A slider with a moveable position indicator. All `slider` controls have a horizontal orientation. Calls the [onChange](#onchange) callback after the position of the indicator is changed or if its [notify()](#notify) method is called.

Calls the `onChanging` callback repeatedly while the user is moving the indicator.

The `value` property contains the current position of the indicator within the range of `minvalue` and `maxvalue`.

#### Parameters

|       Parameter       |                         Type                         |                                                            Description                                                            |
| --------------------- | ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `bounds`              | [Bounds object](size-and-location-objects.md#bounds) | Optional. The control's position and size.                                                                                        |
| `value`               | Number                                               | Optional. The initial position of the scroll indicator. Default is 0.                                                             |
| `minvalue`            | Number                                               | Optional. The minimum value that the `value` property can be set to. Default is 0. Together with `maxvalue`, defines the range.   |
| `maxvalue`            | Number                                               | Optional. The maximum value that the `value` property can be set to. Default is 100. Together with `minvalue`, defines the range. |
| `creation_properties` | Object                                               | Optional. An object that contains any of the properties below.                                                                    |

#### Creation Properties

| Property |  Type  |          Description           |
| -------- | ------ | ------------------------------ |
| `name`   | String | A unique name for the control. |

#### Example

To add to a window `w`:

```javascript
w.add("slider"[, bounds, value, minvalue, maxvalue, {creation_properties}]);
```

---

### statictext

Class Name: `StaticText`

#### Description

A text field that the user cannot change.

#### Parameters

|       Parameter       |                         Type                         |                          Description                           |
| --------------------- | ---------------------------------------------------- | -------------------------------------------------------------- |
| `bounds`              | [Bounds object](size-and-location-objects.md#bounds) | Optional. The control's position and size.                     |
| `text`                | String                                               | Optional. The text displayed in the control.                   |
| `creation_properties` | Object                                               | Optional. An object that contains any of the properties below. |

#### Creation Properties

+-------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  Property   |  Type   |                                                                                       Description                                                                                        |
+=============+=========+==========================================================================================================================================================================================+
| `name`      | String  | A unique name for the control.                                                                                                                                                           |
+-------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `multiline` | Boolean | When `false` (the default), the control displays a single line of text. When `true`, the control displays multiple lines, in which case the text wraps within the width of the control.  |
+-------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `scrolling` | Boolean | When `false` (the default), the displayed text cannot be scrolled. When `true`, the displayed text can be vertically scrolled using scrollbars; this case implies `multiline` is `true`. |
| `truncate`  | String  | Truncate behaviour, one of:                                                                                                                                                              |
|             |         |                                                                                                                                                                                          |
|             |         | - `middle`                                                                                                                                                                               |
|             |         | - `end`                                                                                                                                                                                  |
|             |         | - `none`                                                                                                                                                                                 |
|             |         |                                                                                                                                                                                          |
|             |         | If `middle` or `end`, defines where to remove characters from the text and replace them with an ellipsis if the specified title does not fit within the space reserved for it.           |
|             |         | If `none`, and the text does not fit, characters are removed from the end, without any replacement ellipsis character.                                                                   |
+-------------+---------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### Example

To add to a window `w`:

```javascript
w.add("statictext"[, bounds, text, {creation_properties}]);
```

---

### tab

Class Name: `Tab`

#### Description

A container for other types of controls. Differs from a [panel](#panel) element in that is must be a direct child of a [tabbedpanel](#tabbedpanel) element, the title is shown in the selection tab, and it does not have a script-definable border. The currently active tab is the value of the parent's `selection` property.

Containers have additional properties that control the children; see [Container Attributes](window-object.md#container-attributes). Hiding a panel hides all its children. Making it visible makes visible those children that are not individually hidden.

#### Parameters

|       Parameter       |                         Type                         |                          Description                           |
| --------------------- | ---------------------------------------------------- | -------------------------------------------------------------- |
| `bounds`              | [Bounds object](size-and-location-objects.md#bounds) | Optional. The control's position and size.                     |
| `text`                | String                                               | Optional. The text displayed in the control.                   |
| `creation_properties` | Object                                               | Optional. An object that contains any of the properties below. |

#### Creation Properties

| Property |  Type  |          Description           |
| -------- | ------ | ------------------------------ |
| `name`   | String | A unique name for the control. |

#### Example

To add a tab to a tabbed panel `t` in window `w`:

```javascript
w.t.add("tab"[, bounds, text, {creation_properties}]);
```

---

### tabbedpanel

Class Name: `TabbedPanel`

#### Description

A container for selectable [tab](#tab) containers. Differs from a [panel](#panel) element in that it can contain only [tab](#tab) elements as direct children.

Containers have additional properties that control the children; see [Container Attributes](window-object.md#container-attributes). Hiding a panel hides all its children. Making it visible makes visible those children that are not individually hidden.

The selected tab child is the value of the parent's `selection` property. One and only one of the `tab` children must be selected; selecting one deselects the others. When the value of the `selection` property changes, either by a user selecting a different tab, or by a script setting the property, the `tabbedpanel` receives an [onChange](#onchange) notification.

#### Parameters

|       Parameter       |                         Type                         |                          Description                           |
| --------------------- | ---------------------------------------------------- | -------------------------------------------------------------- |
| `bounds`              | [Bounds object](size-and-location-objects.md#bounds) | Optional. The control's position and size.                     |
| `text`                | String                                               | Optional. The text displayed in the control.                   |
| `creation_properties` | Object                                               | Optional. An object that contains any of the properties below. |

#### Creation Properties

| Property |  Type  |          Description           |
| -------- | ------ | ------------------------------ |
| `name`   | String | A unique name for the control. |

#### Example

To add to a window `w`:

```javascript
w.add("tabbedpanel"[, bounds, text, {creation_properties}]);
```

---

### treeview

Class Name: `TreeView`

#### Description

A hierarchical list whose items can contain child items. Items at any level of the tree can be individually selected. Calls the [onChange](#onchange) callback if the item selection is changed by a script or the user, or if the object's [notify()](#notify) method is called.

#### Parameters

|       Parameter       |                         Type                         |                                                                                                                            Description                                                                                                                             |
| --------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `bounds`              | [Bounds object](size-and-location-objects.md#bounds) | Optional. The control's position and size.                                                                                                                                                                                                                         |
| `items`               | Array of Strings                                     | Optional. The text of each top-level list item. A [ListItem](types-of-controls.md#listitem) object is created for each item. An item with the type node can contain child items. Supply this argument, or the `items` property in `creation_properties`, not both. |
| `creation_properties` | Object                                               | Optional. An object that contains any of the properties below.                                                                                                                                                                                                     |

#### Creation Properties

| Property |       Type       |                                                                                                                                                                 Description                                                                                                                                                                  |
| -------- | ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`   | String           | A unique name for the control.                                                                                                                                                                                                                                                                                                               |
| `items`  | Array of Strings | The text of each top-level list item. A [ListItem](types-of-controls.md#listitem) object is created for each item. An item with the type `node` can contain child items. Supply this property, or the `items` argument, not both. This form is most useful for elements defined using [Resource specifications](resource-specifications.md). |

#### Example

To add to a window `w`:

```javascript
w.add("treeview"[, bounds, items, {creation_properties}])
```

---

## Control object properties

The following table shows the properties of ScriptUI control elements. Some values apply only to controls of particular types, as indicated.

See [Container Attributes](./window-object.md#container-attributes) for properties that apply to container elements (controls of type panel, tabbedpanel, tab, and group).

### active

`controlObj.active`

#### Description

When `true`, the object is active, `false` otherwise. Set to `true` to make a given control or dialog active.

- A modal dialog that is visible is by definition the active dialog.
- An active palette is the front-most window.
- An active control is the one with focus-that is, the one that accepts keystrokes, or in the case of a [Button](types-of-controls.md#button), be selected when the user types ENTER in Windows, or presses the spacebar in Mac OS.

#### Type

Boolean

---

### alignment

`controlObj.alignment`

#### Description

Applies to child elements of a container. If defined, this value overrides the `alignChildren` setting for the parent container.

For a single string value, allowed values depend on the `orientation` value in the parent container.

+---------------------+------------------------+
| `orientation` Value |     Allowed values     |
+=====================+========================+
| `"row"`             | - `"bottom"`           |
|                     | - `"center"` (default) |
|                     | - `"fill"`             |
|                     | - `"top"`              |
+---------------------+------------------------+
| `"column"`          | - `"center"` (default) |
|                     | - `"fill"`             |
|                     | - `"left"`             |
|                     | - `"right"`            |
+---------------------+------------------------+
| `"stack"`           | - `"bottom"`           |
|                     | - `"center"` (default) |
|                     | - `"fill"`             |
|                     | - `"left"`             |
|                     | - `"right"`            |
|                     | - `"top"`              |
+---------------------+------------------------+

For an array value, the first string element defines the horizontal alignment and the second element defines the vertical alignment.

The horizontal alignment value must be one of `"left"`, `"right"`, `"center"` or `"fill"`.

The vertical alignment value must be one of `"top"`, `"bottom"`, `"center"`, or `"fill"`.

!!! note
    Values are not case sensitive.

#### Type

String or Array of 2 Strings

---

### bounds

`controlObj.bounds`

#### Description

A [Bounds](size-and-location-objects.md#bounds) object describing the boundaries of the element, in screen coordinates for Window elements, and parent-relative coordinates for child elements (compare [windowBounds](#windowbounds)). For windows, the bounds refer only to the window's content region.

!!! warning
    Setting an element's [`size`](#size) or [`location`](#location) changes its [`bounds`](#bounds) property, and vice-versa.

#### Type

[Bounds](size-and-location-objects.md#bounds)

---

### characters

`controlObj.characters`

#### Description

Used by the [LayoutManager object](layoutmanager-object.md) to determine the default [preferredSize](#preferredsize) for a [StaticText](types-of-controls.md#statictext) or [EditText](types-of-controls.md#edittext) control.

The control will be made wide enough to display the given number of `X` characters in the font used by the control. Setting this property is the best way to reserve space in a control for a maximum number of characters to display.

#### Type

Number

---

### checked

`controlObj.checked`

#### Description

!!! info
    For [ListItem](types-of-controls.md#listitem) objects only.

- When `true`, the item is marked with the platform-appropriate checkmark.
- When `false`, no checkmark is drawn, but space is reserved for it in the left margin, so that the item lines up with other checkable items.
- When `undefined`, no space is reserved for a checkmark.

#### Type

Boolean

---

### columns

`controlObj.columns`

#### Description

!!! info
    For [ListBox](#listbox) objects only.

A JavaScript object with two read-only properties whose values are set by the creation parameters.

#### Properties

|     Property      |       Type       |                                             Description                                             |
| ----------------- | ---------------- | --------------------------------------------------------------------------------------------------- |
| `titles`          | Array of Strings | An array of column title strings, whose length matches the number of columns specified at creation. |
| `preferredWidths` | Array of Numbers | An array of column widths, whose length matches the number of columns specified at creation.        |

#### Type

Object

---

### enabled

`controlObj.enabled`

#### Description

- When `true`, the control is enabled, meaning that it accepts input.
- When `false`, control elements do not accept input, and all types of elements have a dimmed appearance.

!!! note
    A disabled [ListItem](types-of-controls.md#listitem) is not selectable in a [ListBox](#listbox), [DropDownList](#dropdownlist), or [TreeView](#treeview) object.

#### Type

Boolean

---

### expanded

`controlObj.expanded`

#### Description

For [ListItem](types-of-controls.md#listitem) objects of type `node` in [TreeView](#treeview) list controls. When `true`, the item is in the expanded state and its children are shown, when `false`, it is collapsed and children are hidden.

#### Type

Boolean

---

### graphics

`controlObj.graphics`

#### Description

A [ScriptUIGraphics object](graphic-customization-objects.md#scriptuigraphics-object) that can be used to customize the control's appearance, in response to the [onDraw](#ondraw) event.

#### Type

[ScriptUIGraphics object](graphic-customization-objects.md#scriptuigraphics-object)

---

### helpTip

`controlObj.helpTip`

#### Description

A brief help message (also called a *tool tip*) that is displayed in a small floating window when the mouse cursor hovers over a user-interface control element.

Set to an empty string or `null` to remove help text.

#### Type

String

---

### icon

`controlObj.icon`

#### Description

!!! danger
    Deprecated. Use [Image](types-of-controls.md#image) instead.

#### Type

String or [File](../file-system-access/file-object.md) object

---

### image

`controlObj.image`

#### Description

A [ScriptUIImage object](graphic-customization-objects.md#scriptuiimage-object), or the name of an icon resource, or the pathname or [File object](../file-system-access/file-object.md) for a file that contains a platform-specific image in PNG or JPEG format, or for a shortcut or alias to such a file.

- For an [IconButton](types-of-controls.md#iconbutton), the icon appears as the content of the button.
- For an [Image](types-of-controls.md#image), the image is the entire content of the image element.
- For a [ListItem](types-of-controls.md#listitem), the image is displayed to the left of the text.
    - If the parent is a multi-column [ListBox](#listbox), this is the display image for the label in the first column, and labels for further columns are specified in the [subitems](#subitems) array.
    - See [Creating multi-column lists](types-of-controls.md#creating-multi-column-lists).

#### Type

[ScriptUIImage object](graphic-customization-objects.md#scriptuiimage-object)

---

### indent

`controlObj.indent`

#### Description

A number of pixels by which to indent the element during automatic layout. Applies for `column` orientation and `left` alignment, or `row` orientation and `top` alignment.

#### Type

Number

---

### index

`controlObj.index`

#### Description

!!! info
    For [ListItem](types-of-controls.md#listitem) objects only.

The index of this item in the `items` collection of its parent list control.

#### Type

Number. Read only.

---

### items

`controlObj.items`

#### Description

!!! info
    For [ListBox](#listbox), [DropDownList](#dropdownlist), or [TreeView](#treeview) objects only.

A collection of [ListItem](types-of-controls.md#listitem) objects for the items in the list. Access by 0-based index.

!!! tip
    To obtain the number of items in the list, use `items.length`.

#### Type

Array of Objects. Read only.

---

### itemSize

`controlObj.itemSize`

#### Description

!!! info
    For [ListBox](#listbox), [DropDownList](#dropdownlist), or [TreeView](#treeview) objects only.

A [Dimension](./size-and-location-objects.md#dimension) object describing the width and height in pixels of each item in the list.

Used by auto-layout to determine the [`preferredSize`](#preferredsize) of the list, if not otherwise specified.

If not set explicitly, the size of each item is set to match the largest height and width among all items in the list.

#### Type

[Dimension](./size-and-location-objects.md#dimension) object

---

### jumpdelta

`controlObj.jumpdelta`

#### Description

!!! info
    For [Scrollbar](types-of-controls.md#scrollbar) objects only.

The amount to increment or decrement a [Scrollbar](types-of-controls.md#scrollbar) indicator's position when the user clicks ahead or behind the moveable element.

Default is 20% of the range between the [`maxvalue`](#maxvalue) and [`minvalue`](#minvalue) property values.

#### Type

Number

---

### justify

`controlObj.justify`

#### Description

The justification of text in [StaticText](#statictext) and [EditText](#edittext) controls.

One of:

- `"left"` (default)
- `"center"`
- `"right"`

!!! note
    Justification only works if the value is set on creation, using a resource specification or creation parameters.

#### Type

String

---

### location

`controlObj.location`

#### Description

A [Point](size-and-location-objects.md#point) object describing the location of the element as an array, `[x, y]`, representing the coordinates of the upper left corner of the element. These are screen coordinates for `Window` elements, and parent-relative coordinates for other elements.

The `location` is defined as `[bounds.x, bounds.y]`.

By default, `location` is `undefined` until the parent container's layout manager is invoked.

!!! warning
    Setting an element's [`size`](#size) or [`location`](#location) changes its [`bounds`](#bounds) property, and vice-versa.

#### Type

[Point object](size-and-location-objects.md#point)

---

### maximumSize

`controlObj.maximumSize`

#### Description

A [Dimension](size-and-location-objects.md#dimension) object that specifies the maximum height and width for an element.

The default is 50 pixels less than the screen size in each dimension. In Windows, this can occupy the entire screen; you must define a `maximumSize` to be large enough for your intended usage.

#### Type

[Dimension object](size-and-location-objects.md#dimension)

---

### minimumSize

`controlObj.minimumSize`

#### Description

A [Dimension](size-and-location-objects.md#dimension) object that specifies the minimum height and width for an element. Default is `[0,0]`.

#### Type

[Dimension object](size-and-location-objects.md#dimension)

---

### maxvalue

`controlObj.maxvalue`

#### Description

The maximum value that the [`value`](#value) property can have.

- If `maxvalue` is reset less than `value`, `value` is reset to `maxvalue`.
- If `maxvalue` is reset less than [`minvalue`](#minvalue), `minvalue` is reset to `maxvalue`.

#### Type

Number

---

### minvalue

`controlObj.minvalue`

#### Description

The minimum value that the [`value`](#value) property can have.

- If `minvalue` is reset greater than `value`, `value` is reset to `minvalue`.
- If `minvalue` is reset greater than [`maxvalue`](#maxvalue), `maxvalue` is reset to `minvalue`.

#### Type

Number

---

### parent

`controlObj.parent`

#### Description

The immediate parent object of this element.

#### Type

[Control Object](#). Read only.

---

### preferredSize

`controlObj.preferredSize`

#### Description

A [Dimension](size-and-location-objects.md#dimension) object used by layout managers to determine the best size for each element. If not explicitly set by a script, value is established by the user-interface framework in which ScriptUI is employed, and is based on such attributes of the element as its text, font, font size, icon size, and other user-interface framework-specific attributes.

A script can explicitly set `preferredSize` before the layout manager is invoked in order to establish an element size other than the default. To set a specific value for only one dimension, specify the other dimension as `-1`.

#### Type

[Dimension object](size-and-location-objects.md#dimension)

---

### properties

`controlObj.properties`

#### Description

An object that contains one or more creation properties of the element (properties used only when the element is created).

#### Type

Object

---

### selected

`controlObj.selected`

#### Description

!!! info
    For [ListItem](types-of-controls.md#listitem) objects only.

- When `true`, the item is part of the [`selection`](#selection) for its parent list.
- When `false`, the item is not selected.

Set to `true` to select this item in a single-selection list, or to add it to the selection array for a multi-selection list.

#### Type

Boolean

---

### selection

`controlObj.selection`

#### Description

!!! info
    For [ListBox](#listbox) objects only.

For a [ListBox](#listbox), an array of [ListItem](types-of-controls.md#listitem) objects for the current selection in a multi-selection list. Setting this value causes the selected item to be highlighted and to be scrolled into view if necessary. If no items are selected, the value is `null`. Set to `null` to deselect all items.

The value can also change because the user clicked or double-clicked an item, or because an item was removed with [remove()](#remove) or [removeAll()](#removeall). Whenever the value changes, the [onChange](#onchange) callback is called. If the value is changed by a double click, calls the [onDoubleClick](#ondoubleclick) callback.

You can set the value using the index of an item or an array of indices, rather than object references. If set to an index value that is out of range, the operation is ignored. When set with index values, the property still returns object references.

- If you set the value to an array for a single-selection list, only the first item in the array is selected.
- If you set the value to a single item for a multi-selection list, that item is added to the current selection.

#### Type

Array of [ListItem objects](./types-of-controls.md#listitem)

---

### selection

`controlObj.selection`

#### Description

!!! info
    For [DropDownList](#dropdownlist), or [TreeView](#treeview) objects only.

The currently selected [ListItem](types-of-controls.md#listitem) object.

Setting this value causes the selected item to be highlighted and to be scrolled into view if necessary. If no item is selected, the value is `null`. Set to `null` to deselect all items.

The value can also change because the user clicked on an item, or because an item was removed with [remove()](#remove) or [removeAll()](#removeall).

Whenever the value changes, the [onChange](#onchange) callback is called.

You can set the value using the index of an item or an array of indices, rather than object references. If set to an index value that is out of range, the operation is ignored. When set with an index value, the property still returns an object reference.

#### Type

`ListItem`

---

### shortcutKey

`controlObj.shortcutKey`

#### Description

The key sequence that invokes the [onShortcutKey](#onshortcutkey) callback for this element (in [Windows](./window-object.md) only).

#### Type

String

---

### size

`controlObj.size`

#### Description

A [Dimension](size-and-location-objects.md#dimension) object that defines the actual dimensions of an element.

Initially `undefined`, and unless explicitly set by a script, it is defined by a [LayoutManager object](./layoutmanager-object.md).

Although a script can explicitly set size before the layout manager is invoked to establish an element size other than the [`preferredSize`](#preferredsize) or the default size, this is not recommended.

Defined as `[bounds.width, bounds.height]`.

!!! warning
    Setting an element's [`size`](#size) or [`location`](#location) changes its [`bounds`](#bounds) property, and vice-versa.

#### Type

[Dimension](size-and-location-objects.md#dimension) object

---

### stepdelta

`controlObj.stepdelta`

#### Description

The amount by which to increment or decrement a [Scrollbar](types-of-controls.md#scrollbar) element's position when the user clicks a stepper button.

#### Type

Number

---

### subitems

`controlObj.subitems`

#### Description

!!! info
    For [ListItem](types-of-controls.md#listitem) objects only.

When the parent is a multi-column [ListBox](#listbox), the [ListItem.text](#text) and [ListItem.image](#image) values describe the label in the first column, and this specifies additional labels for that row in the remaining columns.

This contains an array of JavaScript objects, whose length is one less than the number of columns. Each member specifies a label in the corresponding column, with the first member (`subitems[0]`) describing the label in the second column.

#### Properties

Each object has two properties, of which one or both can be supplied:

| Property |  Type  |                 Description                  |
| -------- | ------ | -------------------------------------------- |
| `text`   | String | A localizable display string for this label. |
| `image`  | Image  | An Image object for this label.              |

#### Type

Array

---

### text

`controlObj.text`

#### Description

The title, label, or displayed text. Ignored for containers of type `group`.

For controls, the meaning depends on the control type. Buttons use the `text` as a label, for example, while edit fields use the text to access the content.

For [ListItem](types-of-controls.md#listitem) objects, this is the display string for the list choice. If the parent is a multi-column list box, this is the display string for the label in the first column, and labels for further columns are specified in the [subitems](#subitems) array. See [Creating multi-column lists](types-of-controls.md#creating-multi-column-lists).

This is a localizable string: see [Localization in ScriptUI objects](localization-in-scriptui-objects.md).

#### Type

String

---

### textselection

`controlObj.textselection`

#### Description

The currently selected text in a control that displays text, or the empty string if there is no text selected.

Setting the value replaces the current text selection and modifies the value of the [`text`](#text) property. If there is no current selection, inserts the new value into the `text` string at the current insertion point. The `textselection` value is reset to an empty string after it modifies the `text` value.

!!! note
    Setting the `textselection` property before the [EditText](types-of-controls.md#edittext) control's parent Window exists is an undefined operation.

#### Type

String

---

### title

`controlObj.title`

#### Description

!!! info
    For [DropDownList](#dropdownlist), [FlashPlayer](#flashplayer), [IconButton](#iconbutton), [Image](#image), or [TabbedPanel](#tabbedpanel) objects only.

A text label for the element. The title can appear to the left or right of the element, or above or below it, or you can superimpose the title over the center of the element. The placement is controlled by the [titleLayout](#titlelayout) value.

#### Type

String

---

### titleLayout

`controlObj.titleLayout`

#### Description

!!! info
    For [DropDownList](#dropdownlist), [FlashPlayer](#flashplayer), [IconButton](#iconbutton), [Image](#image), or [TabbedPanel](#tabbedpanel) objects only.

For a control with a title value, the way the text label is shown in relation to the element.

#### Properties

|   Property   |                      Type                      |                                                                                                                                                     Description                                                                                                                                                     |
| ------------ | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `alignment`  | Array or Numbers                               | The position of the title relative to the element, an array of [horizontal_alignment, vertical_alignment]. For possible alignment values, see [alignment](#alignment). Note that `fill` is not a valid alignment value for either horizontal or vertical alignment in this context.                                 |
| `characters` | Number                                         | If `1` or greater, reserves a title width wide enough to hold the specified number of "X" characters in the font for this element. If 0, the title width is calculated based on the value of the `title` property during layout operations.                                                                         |
| `spacing`    | Number                                         | `0` or greater. The number of pixels separating the title from the element.                                                                                                                                                                                                                                         |
| `margins`    | Array of Numbers, `[left, top, right, bottom]` | The number of pixels separating each edge of an element and the visible content within that element. This overrides the default margins.                                                                                                                                                                            |
| `justify`    | String                                         | One of `"left"`, `"center"`, or `"right"`, how to justify the text when the space allocated for the title width is greater than the actual width of the text.                                                                                                                                                       |
| `truncate`   | String                                         | If `"middle"` or `"end"`, defines where to remove characters from the text and replace them with an ellipsis ("...") if the specified title does not fit within the space reserved for it. If `"none"`, and the text does not fit, characters are removed from the end, without any replacement ellipsis character. |

#### Type

Object

---

### type

`controlObj.type`

#### Description

Contains the type name of the element, as specified on creation.

- For [`Window`](./window-object.md) objects, one of the type names window, palette, or dialog.
- For [`controls`](./control-objects.md), the type of the control, as specified in the add method that created it.

#### Type

String. Read only.

---

### value

`controlObj.value`

#### Description

!!! info
    For [Checkbox](types-of-controls.md#checkbox) or [RadioButton](types-of-controls.md#radiobutton) objects only.

`true` if the control is in the selected or set state, `false` if it is not.

#### Type

Boolean

---

### value

`controlObj.value`

#### Description

!!! info
    For [Scrollbar](types-of-controls.md#scrollbar) or [Slider](types-of-controls.md#slider) objects only.

The current position of the indicator. If set to a value outside the range specified by minvalue and maxvalue, it is automatically reset to the closest boundary.

#### Type

Number

---

### visible

`controlObj.visible`

#### Description

When `true`, the element is shown, when `false` it is hidden.

When a container is hidden, its children are also hidden, but they retain their own visibility values, and are shown or hidden accordingly when the parent is next shown.

#### Type

Boolean

---

### window

`controlObj.window`

#### Description

The Window that contains this control.

#### Type

[Window object](window-object.md). Read only.

---

### windowBounds

`controlObj.windowBounds`

#### Description

A [Bounds](size-and-location-objects.md#bounds) object that contains the bounds of this control in the containing window's coordinates. Compare to this control object's [`.bounds`](#bounds) property, in which coordinates are relative to the immediate parent container.

#### Type

[Bounds object](size-and-location-objects.md#bounds). Read only.

---

### function_name

`controlObj.function_name`

#### Description

For the [FlashPlayer](types-of-controls.md#flashplayer) control, a function definition for a callback from the Flash ActionScript environment.

There are no special naming requirements, but the function must take and return only the supported data types:

- Array
- Boolean
- Null
- Number
- Object
- String
- undefined

!!! note
    The ActionScript `class` and `date` objects are not supported as parameter values.

#### Type

Function

---

## Control object functions

The following table shows the methods defined for each element type, and for specific control types as indicated.

### addEventListener()

`controlObj.addEventListener(eventName, handler[, capturePhase=false]);`

#### Description

Registers an event handler for a particular type of event occurring in this control.

#### Parameter

+----------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   Parameter    |   Type   |                                                                                                                                                                                                                          Description                                                                                                                                                                                                                          |
+================+==========+===============================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| `eventName`    | String   | The event name string. Predefined event names include:                                                                                                                                                                                                                                                                                                                                                                                                        |
|                |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                |          | - `"change"`                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                |          | - `"changing"`                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                |          | - `"move"`                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                |          | - `"moving"`                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                |          | - `"resize"`                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                |          | - `"resizing"`                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                |          | - `"show"`                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                |          | - `"enterKey"`                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                |          | - `"focus"`                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                |          | - `"blur"`                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                |          | - `"mousedown"`                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                |          | - `"mouseup"`                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                |          | - `"mousemove"`                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                |          | - `"mouseover"`                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                |          | - `"mouseout"`                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                |          | - `"keyup"`                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                |          | - `"keydown"`                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                |          | - `"click"` (detail = 1 for single, 2 for double)                                                                                                                                                                                                                                                                                                                                                                                                             |
+----------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `handler`      | Function | The function to register for the specified event in this target. This can be the name of a function defined in the extension, or a locally defined handler function to be executed when the event occurs. A handler function takes one argument, an object of the UIEvent base class. See [Registering event listeners for windows or controls](defining-behavior-with-event-callbacks-and-listeners.md#registering-event-listeners-for-windows-or-controls). |
+----------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `capturePhase` | Boolean  | Optional. When `true`, the handler is called only in the capturing phase of the event propagation. Default is `false`, meaning that the handler is called in the bubbling phase if this object is an ancestor of the target, or in the at-target phase if this object is itself the target.                                                                                                                                                                   |
+----------------+----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### Returns

Nothing

---

### dispatchEvent()

`controlObj.dispatchEvent(eventObj)`

#### Description

Simulates the occurrence of an event in this target. A script can create an event object for a specific event, using [ScriptUI.events.createEvent()](scriptui-class.md#scriptuieventscreateevent), and pass it to this method to start the event propagation for the event.

#### Parameters

| Parameter  |  Type  |             Description              |
| ---------- | ------ | ------------------------------------ |
| `eventObj` | Object | An object of the UIEvent base class. |

#### Returns

Boolean. `false` if any of the registered listeners that handled the event called the event object's [preventDefault()](event-handling.md#preventdefault) method, `true` otherwise.

---

### hide()

`controlObj.hide()`

#### Description

Hides this container or control. When a window or container is hidden, its children are also hidden, but when it is shown again, the children retain their own visibility states.

#### Returns

Nothing

---

### notify()

`controlObj.notify([event])`

#### Description

Sends a notification message, simulating the specified user interaction event.

#### Parameters

+-----------+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter |  Type  |                                                                                    Description                                                                                     |
+===========+========+====================================================================================================================================================================================+
| `event`   | String | Optional. The name of the control event handler to call. One of:                                                                                                                   |
|           |        |                                                                                                                                                                                    |
|           |        | - `"onClick"`                                                                                                                                                                      |
|           |        | - `"onChange"`                                                                                                                                                                     |
|           |        | - `"onChanging"`                                                                                                                                                                   |
|           |        |                                                                                                                                                                                    |
|           |        | By default, simulates the [onChange](#onchange) event for an [EditText](types-of-controls.md#edittext) control, an [onClick](#onclick) event for controls that support that event. |
+-----------+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### Returns

Nothing

---

### removeEventListener()

`controlbj.removeEventListener(eventName, handler[, capturePhase]);`

#### Description

Unregisters an event handler for a particular type of event occurring in this control. All arguments must be identical to those that were used to register the event handler.

#### Parameters

|   Parameter    |   Type   |                               Description                               |
| -------------- | -------- | ----------------------------------------------------------------------- |
| `eventName`    | String   | The event name.                                                         |
| `handler`      | Function | The function that was registered to handle the event.                   |
| `capturePhase` | Boolean  | Optional. Whether the handler was to respond only in the capture phase. |

#### Returns

Nothing

---

### show()

`controlObj.show()`

#### Description

Shows this container or control.

When a window or container is hidden, its children are also hidden, but when it is shown again, the children retain their own visibility states.

#### Returns

Nothing

---

### toString()

`listItemObj.toString()`

#### Description

!!! info
    For [ListItem](types-of-controls.md#listitem) objects only.

Retrieves the value of this item's text property as a string.

#### Returns

String

---

### valueOf()

`listItemObj.valueOf()`

#### Description

!!! info
    For [ListItem](types-of-controls.md#listitem) objects only.

Retrieves the index number of this item in the parent list's items array.

#### Returns

Number

---

## List control object functions

The following table shows the methods defined for list objects only.

### add()

`listObj.add(type, text[, index=listObj.numItems])`

#### Description

!!! info
    For [ListBox](#listbox), [DropDownList](#dropdownlist), or [TreeView](#treeview) objects only.

Adds an `item` to the items array at the given index.

#### Parameters

+-----------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter |  Type  |                                                                                  Description                                                                                  |
+===========+========+===============================================================================================================================================================================+
| `type`    | String | The type of item to add. One of:                                                                                                                                              |
|           |        |                                                                                                                                                                               |
|           |        | - `item`: A basic, selectable item with a text label.                                                                                                                         |
|           |        | - `separator`: A separator. For [DropDownList](#dropdownlist) objects only. In this case, the text value is ignored, and the method returns `null`.                           |
+-----------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `text`    | String | The localizable text label for the item.                                                                                                                                      |
+-----------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `index`   | Number | Optional. The index into the current item list after which this item is inserted. If not supplied, or greater than the current list length, the new item is added at the end. |
+-----------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### Returns

[Item](#item) object for `type = "item"`, or `null` for `type = "separator"`.

---

### find()

`listObj.find(text)`

#### Description

!!! info
    For [ListBox](#listbox), [DropDownList](#dropdownlist), or [TreeView](#treeview) objects only.

Looks in this object's `items` array for an item object with the given `text` value.

#### Parameters

| Parameter |  Type  |          Description          |
| --------- | ------ | ----------------------------- |
| `text`    | String | The text of the item to find. |

#### Returns

The [ListItem](./types-of-controls.md#listitem) object if found; otherwise `null`.

---

### remove()

`containerObj.remove(index)`

`containerObj.remove(text)`

`containerObj.remove(child)`

#### Description

- For containers ([Panel](#panel), [Group](#group)): removes the specified child control from the container's `children` array.
- For [ListBox](#listbox), [DropDownList](#dropdownlist), or [TreeView](#treeview) objects: removes the specified item from this object's items array.

No error results if the item does not exist.

#### Parameters

|        Parameter         |                          Type                          |                                            Description                                             |
| ------------------------ | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| `index`, `text`, `child` | Number of String or [Control](#control-objects) object | The item or child to remove, specified by `0`-based index, `text` value, or as a `control` object. |

#### Returns

Nothing

---

### removeAll()

`listObj.removeAll()`

#### Description

!!! info
    For [ListBox](#listbox), [DropDownList](#dropdownlist), or [TreeView](#treeview) objects only.

Removes all items from the object's `items` array.

#### Returns

Nothing

---

### revealItem()

`listObj.revealItem(item)`

#### Description

!!! info
    For [ListBox](#listbox) objects only.

Scrolls the list to make the specified item visible, if necessary.

#### Parameters

| Parameter |                  Type                  |                  Description                   |
| --------- | -------------------------------------- | ---------------------------------------------- |
| `item`    | [Control](./control-objects.md) object | The item or child to reveal, a control object. |

#### Returns

Nothing

---

## FlashPlayer control functions

!!! info
    For [FlashPlayer](#flashplayer) objects only.

### Limitations

There are limitations on how these functions can be used to control playback of Flash movies:

- Do not use [stopMovie()](#stopmovie) and [playMovie()](#playmovie) to suspend and subsequently resume or restart an SWF file produced by Flex™.
- The [stopMovie()](#stopmovie) and [playMovie()](#playmovie) sequence does not make sense for some SWF files produced by Flash Authoring, depending on the exact details of how they were implemented. The sequence may not correctly reset the file to the initial state (when the `rewind` argument to [playMovie()](#playmovie) is `true`) nor suspend then resume the execution of the file (when `rewind` is `false`).
- Using [stopMovie()](#stopmovie) from the player's hosting environment has no effect on an SWF file playing in a ScriptUI Flash Player element. It is, however, possible to produce an SWF using Flash Authoring that can stop itself in response to user interaction.
- Do not call [playMovie()](#playmovie) when an SWF file is already playing.

---

### invokePlayerFunction()

`flashPlayerObj.invokePlayerFunction(fnName, [arg1[,...argN]] )`

#### Description

Invokes an ActionScript function defined in the Flash application.

#### Parameters

+-----------+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter |  Type  |                                                                                                                                              Description                                                                                                                                               |
+===========+========+========================================================================================================================================================================================================================================================================================================+
| `fnName`  | String | The name of a Flash ActionScript function that has been registered with the ExternalInterface object by the currently loaded SWF file; see [Calling ActionScript functions from a ScriptUI script](communicating-with-the-flash-application.md#calling-actionscript-functions-from-a-scriptui-script). |
+-----------+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `args`    | Any    | Optional. One or more arguments to pass through to the function, of these types:                                                                                                                                                                                                                       |
|           |        |                                                                                                                                                                                                                                                                                                        |
|           |        | - Array                                                                                                                                                                                                                                                                                                |
|           |        | - Boolean                                                                                                                                                                                                                                                                                              |
|           |        | - `null`                                                                                                                                                                                                                                                                                               |
|           |        | - Number                                                                                                                                                                                                                                                                                               |
|           |        | - Object                                                                                                                                                                                                                                                                                               |
|           |        | - String                                                                                                                                                                                                                                                                                               |
|           |        | - `undefined`                                                                                                                                                                                                                                                                                          |
+-----------+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### Returns

The result of the invoked function, which must be one of the allowed types. The ActionScript `class` and `date` objects are not supported as return values.

---

### loadMovie()

`flashPlayerObj.loadMovie(file)`

#### Description

Loads a movie into the Flash Player, and begins playing it. If you do not specify an associated movie file when creating the control, you must use this function to load one.

#### Parameters

| Parameter |                        Type                         |      Description      |
| --------- | --------------------------------------------------- | --------------------- |
| `file`    | [File object](../file-system-access/file-object.md) | The SWF file to load. |

#### Returns

Nothing

---

### playMovie()

`flashPlayerObj.playMovie(rewind)`

#### Description

Restarts a movie that has been stopped.

!!! warning
    Do not call when a movie is currently playing.

#### Parameters

| Parameter |  Type   |                                                    Description                                                     |
| --------- | ------- | ------------------------------------------------------------------------------------------------------------------ |
| `rewind`  | Boolean | When `true`, restarts the movie from the beginning; otherwise, starts playing from the point where it was stopped. |

#### Returns

Nothing

---

### stopMovie()

`flashPlayerObj.stopMovie()`

#### Description

Halts playback of the current movie.

!!! note
    Does not work when called from the player's hosting environment.

#### Returns

Nothing

---

## Control event-handling callbacks

The following events are signalled in certain types of controls. To handle the event, define a function with the corresponding name in the control object. Handler functions take no arguments and have no expected return values; see [Defining behavior with event callbacks and listeners](defining-behavior-with-event-callbacks-and-listeners.md).

---

### onActivate

Called when the user gives a control the keyboard focus by clicking it or tabbing into it.

---

### onClick

Called when the user clicks one of the following control types:

- [Button](types-of-controls.md#button)
- [Checkbox](types-of-controls.md#checkbox)
- [IconButton](types-of-controls.md#iconbutton)
- [RadioButton](types-of-controls.md#radiobutton)

---

### onChange

Called when the user finishes making a change in one of the following control types:

- [DropDownList](#dropdownlist)
- [EditNumber](types-of-controls.md#editnumber)
- [EditText](types-of-controls.md#edittext)
- [ListBox](#listbox)
- [Scrollbar](types-of-controls.md#scrollbar)
- [Slider](types-of-controls.md#slider)
- [TreeView](#treeview)

- For [EditNumber](types-of-controls.md#editnumber) and [EditText](types-of-controls.md#edittext) controls, called only when the change is complete-that is, when focus moves to another control, or the user types `ENTER`.
    - The exact behavior depends on the creation parameter `enterKeySignalsOnChange`; see the [EditText](#edittext) description.
- For a [Slider](types-of-controls.md#slider) or [Scrollbar](types-of-controls.md#scrollbar), called when the user has finished dragging the position marker or has clicked the control.
- For a [ListBox](#listbox), [DropDownList](#dropdownlist) or [TreeView](#treeview) control, called whenever the selection property changes.
    - This can happen when a script sets the property directly or removes a selected item from the list, or when the user changes the selection.

---

### onChanging

Called for each incremental change in one of the following control types:

- [EditNumber](types-of-controls.md#editnumber)
- [EditText](types-of-controls.md#edittext)
- [Scrollbar](types-of-controls.md#scrollbar)
- [Slider](types-of-controls.md#slider)

- For [EditNumber](types-of-controls.md#editnumber) and [EditText](types-of-controls.md#edittext) controls, called for each keypress while the control has focus.
- For a [Slider](types-of-controls.md#slider) or [Scrollbar](types-of-controls.md#scrollbar), called for any motion of the position marker.

---

### onCollapse

Called when the user collapses (closes) a node in a [TreeView](#treeview) control.

The parameter to this function is the [ListItem](types-of-controls.md#listitem) node object that was collapsed.

---

### onDeactivate

Called when the user removes keyboard focus from a previously active control by clicking outside it or tabbing out of it.

---

### onDoubleClick

Called when the user double clicks an item in a [ListBox](#listbox) control.

The list's [`selection`](#selection) property is set to the clicked item.

---

### onEnterKey

!!! warning
    This method/property is officially undocumented and was found via research. The information here may be inaccurate, and this whole method/property may disappear or stop working some point. Please contribute if you have more information on it!

Called when the user presses return or enter in a [EditText](#edittext) control.

---

### onDraw

Called when a container or control is about to be drawn. Allows the script to modify or control the appearance, using the control's associated [ScriptUIGraphics object](graphic-customization-objects.md#scriptuigraphics-object). Handler takes one argument, a [DrawState object](#drawstate-object).

---

### onExpand

Called when the user expands (opens) a node in a [TreeView](#treeview) control. The parameter to this function is the [ListItem](types-of-controls.md#listitem) node object that was expanded.

---

### onShortcutKey

!!! info
    For [Windows](./window-object.md) objects only.

Called when a shortcut-key sequence is typed that matches the [shortcutKey](#shortcutkey) value for an element in the active window.

---

## DrawState object

A helper object that describes an input state at the time of the triggering [onDraw](#ondraw) event. Contains properties that report whether the current control has the input focus, and the particular mouse button and key-press state.

There is no object constructor.

### DrawState object properties

The object contains the following read-only properties:

|       Property        |  Type   |                                           Behaviour                                           |
| --------------------- | ------- | --------------------------------------------------------------------------------------------- |
| `altKeyPressed`       | Boolean | When `true`, the ALT key was pressed. (In Windows OS only.)                                   |
| `capsLockKeyPressed`  | Boolean | When `true`, the CAPSLOCK key was pressed.                                                    |
| `cmdKeyPressed`       | Boolean | When `true`, the CMD key was pressed. (In Mac OS only.)                                       |
| `ctrlKeyPressed`      | Boolean | When `true`, the CTRL key was pressed.                                                        |
| `hasFocus`            | Boolean | When `true`, the control containing this object has the input focus.                          |
| `leftButtonPressed`   | Boolean | When `true`, the left mouse button was pressed.                                               |
| `middleButtonPressed` | Boolean | When `true`, the middle mouse button was pressed.                                             |
| `mouseOver`           | Boolean | When `true`, the cursor position was within the bounds of the control containing this object. |
| `numLockKeyPressed`   | Boolean | When `true`, the NUMLOCK key was pressed.                                                     |
| `optKeyPressed`       | Boolean | When `true`, the OPT key was pressed. (In Mac OS only.)                                       |
| `rightButtonPressed`  | Boolean | When `true`, the right mouse button was pressed.                                              |
| `shiftKeyPressed`     | Boolean | When `true`, the SHIFT key was pressed.                                                       |
