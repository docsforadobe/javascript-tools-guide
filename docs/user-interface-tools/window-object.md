# Window object

## Window Object constructor

The constructor creates and returns a new Window object, or null if window creation failed.

```javascript
new Window (type [, title, bounds, {creation_properties}]);
```

+-----------------------+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|       Parameter       |                          Type                           |                                                                            Description                                                                            |
+=======================+=========================================================+===================================================================================================================================================================+
| `type`                | String                                                  | The window type. One of:                                                                                                                                          |
|                       |                                                         |                                                                                                                                                                   |
|                       |                                                         | - `"dialog"` - Creates a modal dialog.                                                                                                                            |
|                       |                                                         | - `"palette"` - Creates a modeless dialog, also called a floating palette. (Not supported by Photoshop CC.)                                                       |
|                       |                                                         | - `"window"` - Creates a simple window that can be used as a main window for an application. (Not supported by Photoshop CC.)                                     |
|                       |                                                         |                                                                                                                                                                   |
|                       |                                                         | This argument can be a ScriptUI resource specification; in this case, all other arguments are ignored. See [Resource specifications](resource-specifications.md). |
+-----------------------+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `title`               | String                                                  | Optional. The window title. A localizable string.                                                                                                                 |
+-----------------------+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `bounds`              | [Bounds](./size-and-location-objects.md#bounds) object. | Optional. The window's position and size.                                                                                                                         |
+-----------------------+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `creation_properties` | Object                                                  | Optional. An object that contains any of the properties below.                                                                                                    |
+-----------------------+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### Creation Properties

+-----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|       Parameter       |  Type   |                                                                                                           Description                                                                                                            |
+=======================+=========+==================================================================================================================================================================================================================================+
| `resizeable`          | Boolean | When `true`, the window can be resized by the user.                                                                                                                                                                              |
|                       |         |                                                                                                                                                                                                                                  |
|                       |         | Default is `false`.                                                                                                                                                                                                              |
+-----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `su1PanelCoordinates` | Boolean | (Photoshop only) When `true`, the child panels of this window automatically adjust the positions of their children for compatability with Photoshop CS (in which the vertical coordinate was measured from outside the frame).   |
|                       |         | Individual panels can override the parent window's setting.                                                                                                                                                                      |
|                       |         |                                                                                                                                                                                                                                  |
|                       |         | Default is `false`.                                                                                                                                                                                                              |
+-----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `closeButton`         | Boolean | When `true`, the title bar includes a button to close the window, if the platform and window type allow it.                                                                                                                      |
|                       |         | When `false`, it does not. Not used for dialogs.                                                                                                                                                                                 |
|                       |         |                                                                                                                                                                                                                                  |
|                       |         | Default is `true`.                                                                                                                                                                                                               |
+-----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `maximizeButton`      | Boolean | When `true`, the title bar includes a button to expand the window to its maximum size (typically, the entire screen), if the platform and window type allow it. When `false`, it does not. Not used for dialogs.                 |
|                       |         |                                                                                                                                                                                                                                  |
|                       |         | Default is `false` for type palette, `true` for type window.                                                                                                                                                                     |
+-----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `minimizeButton`      | Boolean | When `true`, the title bar includes a button to minimize or iconify the window, if the platform and window type allow it. When `false`, it does not. Main windows cannot have a minimize button in Mac OS. Not used for dialogs. |
|                       |         |                                                                                                                                                                                                                                  |
|                       |         | Default is `false` for type palette, `true` for type window.                                                                                                                                                                     |
+-----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `independent`         | Boolean | When `true`, a window of type window is independent of other application windows, and can be hidden behind them in Windows. In Mac OS, has no effect.                                                                            |
|                       |         |                                                                                                                                                                                                                                  |
|                       |         | Default is `false`.                                                                                                                                                                                                              |
+-----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `borderless`          | Boolean | When `true`, the window has no title bar or borders. Properties that control those features are ignored.                                                                                                                         |
+-----------------------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

---

## Window Object Attributes

The following element properties apply specifically to Window elements:

### active

`windowOrContainerObj.active`

#### Description

When `true`, the object is active, `false` otherwise. Set to `true` to make a given control or dialog active.

- A modal dialog that is visible is by definition the active dialog.
- An active palette is the front-most window.
- An active control is the one with focus-that is, the one that accepts keystrokes, or in the case of a Button, be selected when the user types RETURN or ENTER.

#### Type

Boolean

---

### cancelElement

`windowOrContainerObj.cancelElement`

#### Description

For a window of type dialog, the control to notify when a user types the ESC key.

By default, looks for a button whose name or text is `"cancel"` (case disregarded).

#### Type

[Control object](./control-objects.md)

---

### defaultElement

`windowOrContainerObj.defaultElement`

#### Description

For a window of type dialog, the control to notify when a user types the ENTER key.

By default, looks for a button whose name or text is `"ok"` (case disregarded).

#### Type

[Control object](./control-objects.md)

---

### frameBounds

`windowOrContainerObj.frameBounds`

#### Description

A Bounds object for the boundaries of the Window's frame in screen coordinates.

The frame consists of the title bar and borders that enclose the content region of a window, depending on the windowing system.

#### Type

[Bounds](size-and-location-objects.md#bounds). Read only.

---

### frameLocation

`windowOrContainerObj.frameLocation`

#### Description

A Point object for the location of the top left corner of the Window's frame. The same as `[frameBounds.x, frameBounds.y]`.

Set this value to move the window frame to the specified location on the screen. The [`frameBounds`](#framebounds) value changes accordingly.

#### Type

[Point](size-and-location-objects.md#point)

---

### frameSize

`windowOrContainerObj.frameSize`

#### Description

A Dimension object for the size and location of the Window's frame in screen coordinates.

#### Type

[Dimension](size-and-location-objects.md#dimension). Read only.

---

### maximized

`windowOrContainerObj.maximized`

#### Description

When `true`, the window is expanded.

#### Type

Boolean

---

### minimized

`windowOrContainerObj.minimized`

#### Description

When `true`, the window is minimized or iconified.

#### Type

Boolean

---

### opacity

`windowOrContainerObj.opacity`

#### Description

The opacity of the window, in the range `[0..1]`.

A value of `1.0` (the default) makes the window completely opaque, a value of 0 makes it completely transparent.

Intermediate values make it partially transparent to any degree.

#### Type

Number

---

### shortcutKey

`windowOrContainerObj.shortcutKey`

#### Description

!!! note
    In [Windows](#) only.

The key sequence that invokes this window's [ControlEvent.onShortcutKey](./control-objects.md#onshortcutkey) callback.

#### Type

String

---

## Container Attributes

The following table shows properties that apply to Window objects and container objects (controls of type `panel`, `tabbedpanel`, `tab`, and `group`).

---

### alignChildren

`windowOrContainerObj.alignChildren`

#### Description

Tells the layout manager how unlike-sized children of a container should be aligned within a column or row. Order of creation determines which children are at the top of a column or the left of a row; the earlier a child is created, the closer it is to the top or left of its column or row.

If defined, alignment for a child element overrides the alignChildren setting for the parent container.

For a single string value, allowed values depend on the orientation value.

For `orientation=row`:

- `top`
- `bottom`
- `center` (default)
- `fill`

For `orientation=column`:

- `left`
- `right`
- `center` (default)
- `fill`

For `orientation=stack`:

- `top`
- `bottom`
- `left`
- `right`
- `center` (default)
- `fill`

For an array value, the first string element defines the horizontal alignment and the second element defines the vertical alignment. The horizontal alignment value must be one of left, right, center or fill. The vertical alignment value must be one of top, bottom, center, or fill.

Values are not case sensitive.

#### Type

String, or Array of 2 Strings

---

### alignment

`windowOrContainerObj.alignment`

#### Description

Applies to child elements of a container. If defined, this value overrides the alignChildren setting for the parent container.

For a single string value, allowed values depend on the `orientation` value.

For `orientation = row`:

- `top`
- `bottom`
- `center` (default)
- `fill`

For `orientation=column`:

- `left`
- `right`
- `center` (default)
- `fill`

For `orientation = stack`:

- `top`
- `bottom`
- `left`
- `right`
- `center` (default)
- `fill`

For an array value, the first string element defines the horizontal alignment and the second element defines the vertical alignment.

The horizontal alignment value must be one of `left`, `right`, `center` or `fill`. The vertical alignment value must be one of `top`, `bottom`, `center`, or `fill`.

Values are not case sensitive.

#### Type

String, or Array of 2 Strings

---

### bounds

`windowOrContainerObj.bounds`

#### Description

A Bounds object for the boundaries of the window's drawable area in screen coordinates. Compare [frameBounds](#framebounds).

Does not apply to containers of type tab, whose bounds are determined by the parent tabbedpanel container.

#### Type

[Bounds](size-and-location-objects.md#bounds). Read only.

---

### children

`windowOrContainerObj.children`

#### Description

The collection of user-interface elements that have been added to this window or container.

An array indexed by number or by a string containing an element's `name`. The `length` property of this array is the number of child elements for container elements, and is zero for controls.

#### Type

Array of Objects. Read only.

---

### graphics

`windowOrContainerObj.graphics`

#### Description

A ScriptUIGraphics object that can be used to customize the window's appearance, in response to the onDraw event.

#### Type

[ScriptUIGraphics object](graphic-customization-objects.md#scriptuigraphics-object)

---

### layout

`windowOrContainerObj.layout`

#### Description

A LayoutManager object for a window or container. The first time a container object is made visible, ScriptUI invokes this layout manager by calling its layout function.

Default is an instance of the LayoutManager class that is automatically created when the container element is created.

#### Type

[LayoutManager object](layoutmanager-object.md)

---

### location

`windowOrContainerObj.location`

#### Description

A Point object for the location of the top left corner of the Window's drawable area, or the top left corner of the frame for a panel.

The same as `[bounds.x, bounds.y]`.

#### Type

[Point](size-and-location-objects.md#point)

---

### margins

`windowOrContainerObj.margins`

#### Description

A Margins object describing the number of pixels between the edges of this container and the outermost child elements. You can specify different margins for each edge of the container.

The default value is based on the type of container, and is chosen to match the standard Adobe user-interface guidelines.

#### Type

[Margins](size-and-location-objects.md#margins)

---

### maximumSize

`windowOrContainerObj.maximumSize`

#### Description

[Dimension](size-and-location-objects.md#dimension)

A Dimension object for the largest rectangle to which the window can be resized, used in automatic layout and resizing.

#### Type

---

### minimumSize

`windowOrContainerObj.minimumSize`

#### Description

[Dimension](size-and-location-objects.md#dimension)

A Dimension object for the smallest rectangle to which the window can be resized, used in automatic layout and resizing.

#### Type

---

### orientation

`windowOrContainerObj.orientation`

#### Description

How elements are organized within this container.

Interpreted by the layout manager for the container.

The default LayoutManager object accepts the (case-insensitive) values:

- `row`
- `column`
- `stack`

The default orientation depends on the type of container. For `Window` and `Panel`, the default is `column`, and for `Group` the default is `row`.

The allowed values for the container's alignChildren and its children's alignment properties depend on the orientation.

#### Type

String

---

### parent

`windowOrContainerObj.parent`

#### Description

The immediate parent object of this element, a window or container element. The value is `null` for Window objects.

#### Type

Object. Read only.

---

### preferredSize

`windowOrContainerObj.preferredSize`

#### Description

A Dimension object for the preferred size of the window, used in automatic layout and resizing. To set a specific value for only one dimension, specify other dimension as `-1`.

#### Type

[Dimension](size-and-location-objects.md#dimension)

---

### properties

`windowOrContainerObj.properties`

#### Description

An object that contains one or more creation properties of the container (properties used only when the element is created).

#### Type

Object

---

### selection

`windowOrContainerObj.selection`

#### Description

!!! info
    For [TabbedPanel](./control-objects.md#tabbedpanel) objects only.

The currently active [Tab](control-objects.md#tab) child. Setting this property changes the active tab. The value can only be `null` when the panel has no children; setting it to `null` is an error.

When the value changes, either by a user selecting a different tab, or by a script setting the property, the [onChange](control-objects.md#onchange) callback for the panel is called.

#### Type

[tab](control-objects.md#tab)

---

### size

`windowOrContainerObj.size`

#### Description

A Dimension object for the current size and location of a group or panel element, or of the content area of a window.

#### Type

[Dimension](size-and-location-objects.md#dimension)

---

### spacing

`windowOrContainerObj.spacing`

#### Description

The number of pixels separating one child element from its adjacent sibling element. Because each container holds only a single row or column of children, only a single spacing value is needed for a container.

The default value is based on the type of container, and is chosen to match standard Adobe user-interface guidelines.

#### Type

Number

---

### text

`windowOrContainerObj.text`

#### Description

The title, label, or displayed text. Does not apply to containers of type `group` or `tabbedpanel`.

This is a localizable string: see [Localization in ScriptUI objects](localization-in-scriptui-objects.md).

#### Type

String

---

### visible

`windowOrContainerObj.visible`

#### Description

When `true`, the element is shown, when `false` it is hidden.

When a container is hidden, its children are also hidden, but they retain their own visibility values, and are shown or hidden accordingly when the parent is next shown.

#### Type

Boolean

---

### window

`windowOrContainerObj.window`

#### Description

The top-level parent window of this container, a [Window object](#window-object).

#### Type

[Window](#window-object)

---

### windowBounds

`windowOrContainerObj.windowBounds`

#### Description

A Bounds object for the size and location of this container relative to its top-level parent window.

#### Type

[Bounds](size-and-location-objects.md#bounds)

---

## Window Object Methods

These functions are defined for Window instances, and as indicated for container objects of type `Panel` and `Group`.

---

### add()

`windowOrContainerObj.add(type[, bounds, text, { creation_props } ]);`

#### Description

Creates and returns a new control or container object and adds it to the children of this window or container.

#### Parameters

|    Parameter     |                          Type                          |                                                                                                                                      Description                                                                                                                                       |
| ---------------- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`           | String                                                 | The control type. See [Control types and creation parameters](control-objects.md#control-types-and-creation-parameters).                                                                                                                                                               |
| `bounds`         | [Bounds object](./size-and-location-objects.md#bounds) | Optional. A bounds specification that describes the size and position of the new control or container, relative to its parent. See Bounds object for specification formats. If supplied, this value creates a new Bounds object which is assigned to the new object's bounds property. |
| `text`           | String                                                 | Optional. Initial text to be displayed in the control as the title, label, or contents, depending on the control type. If supplied, this value is assigned to the new object's text property.                                                                                          |
| `creation_props` | Object.                                                | Optional. The properties of this object specify creation parameters, which are specific to each object type. See [Control types and creation parameters](control-objects.md#control-types-and-creation-parameters).                                                                    |

#### Returns

The new object, or `null` if unable to create the object.

---

### addEventListener()

`windowObj.addEventListener(eventName, handler[, capturePhase=false]);`

#### Description

Registers an event handler for a particular type of event occurring in this window.

#### Parameters

+----------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|   Parameter    |   Type   |                                                                                                                                                                                                                   Description                                                                                                                                                                                                                    |
+================+==========+==================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| `eventName`    | String   | The event name string. Predefined event names include:                                                                                                                                                                                                                                                                                                                                                                                           |
|                |          |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                |          | - `"change"`                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                |          | - `"changing"`                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                |          | - `"move"`                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                |          | - `"moving"`                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                |          | - `"resize"`                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                |          | - `"resizing"`                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                |          | - `"show"`                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                |          | - `"enterKey"`                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                |          | - `"focus"`                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                |          | - `"blur"`                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                |          | - `"mousedown"`                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                |          | - `"mouseup"`                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                |          | - `"mousemove"`                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                |          | - `"mouseover"`                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                |          | - `"mouseout"`                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                |          | - `"click"` (detail = 1 for single, 2 for double)                                                                                                                                                                                                                                                                                                                                                                                                |
+----------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `handler`      | Function | The function to register for the specified event in this target. This can be the name of a function defined in the extension, or a locally defined handler function to be executed when the event occurs. A handler function takes one argument, the UIEvent base class. See [Registering event listeners for windows or controls](defining-behavior-with-event-callbacks-and-listeners.md#registering-event-listeners-for-windows-or-controls). |
+----------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `capturePhase` | Boolean  | Optional. When `true`, the handler is called only in the capturing phase of the event propagation. Default is `false`, meaning that the handler is called in the bubbling phase if this object is an ancestor of the target, or in the at-target phase if this object is itself the target.                                                                                                                                                      |
+----------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### Returns

Nothing

---

### center()

`windowObj.center([window])`

#### Description

Centers this window on the screen, or with respect to another specified window.

#### Parameters

| Parameter |                Type                 |        Description         |
| --------- | ----------------------------------- | -------------------------- |
| `window`  | [Window object](./window-object.md) | Optional. A Window object. |

#### Returns

Nothing

---

### close()

`windowObj.close([result])`

#### Description

Closes this window. If an `onClose` callback is defined for the window, calls that function before closing the window.

#### Parameters

| Parameter |  Type  |                                            Description                                             |
| --------- | ------ | -------------------------------------------------------------------------------------------------- |
| `result`  | Number | Optional. A number to be returned from the show method that invoked this window as a modal dialog. |

#### Returns

Nothing

---

### dispatchEvent()

`windowObj.dispatchEvent(eventObj)`

#### Description

Simulates the occurrence of an event in this target. A script can create a UIEvent base class for a specific event and pass it to this method to start the event propagation for the event.

#### Parameters

| Parameter  |                             Type                             |      Description      |
| ---------- | ------------------------------------------------------------ | --------------------- |
| `eventObj` | [UIEvent base class](./event-handling.md#uievent-base-class) | A UIEvent base class. |

#### Returns

Boolean. `false` if any of the registered listeners that handled the event called the event object's [preventDefault()](event-handling.md#preventdefault) method, `true` otherwise.

---

### findElement()

`windowOrContainerObj.findElement(name)`

#### Description

Searches for the named element among the children of this window or container, and returns the object if found.

#### Parameters

| Parameter |  Type  |                             Description                              |
| --------- | ------ | -------------------------------------------------------------------- |
| `name`    | String | The name of the element, as specified in the name creation property. |

#### Returns

The control object or `null`.

---

### hide()

`windowObj.hide()`

Hides this window. When a window is hidden, its children are also hidden, but when it is shown again, the children retain their own visibility states.

For a modal dialog, closes the dialog and sets its result to `0`.

#### Returns

Nothing

---

### notify()

`windowObj.notify([event])`

#### Description

Sends a notification message, simulating the specified user interaction event.

#### Parameters

+-----------+--------+-----------------------------------------------------------------+
| Parameter |  Type  |                           Description                           |
+===========+========+=================================================================+
| `event`   | String | Optional. The name of the window event handler to call. One of: |
|           |        |                                                                 |
|           |        | - `onClose`                                                     |
|           |        | - `onMove`                                                      |
|           |        | - `onMoving`                                                    |
|           |        | - `onResize`                                                    |
|           |        | - `onResizing`                                                  |
|           |        | - `onShow`                                                      |
+-----------+--------+-----------------------------------------------------------------+

#### Returns

Nothing

#### Example

To simulate a dialog being moved by a user:

```javascript
myDlg.notify("onMove")
```

---

### remove()

`windowOrContainerObj.remove(index)`

`windowOrContainerObj.remove(text)`

`windowOrContainerObj.remove(child)`

#### Description

Removes the specified child control from this window's or container's children array. No error results if the child does not exist.

#### Parameters

|       Parameter        |                           Type                            |                                                Description                                                 |
| ---------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `index`/`text`/`child` | Number, String, or [Control object](./control-objects.md) | The child control to remove, specified by 0-based index, the contained text value, or as a control object. |

#### Returns

Nothing

---

### removeEventListener()

`windowOrContainerObj.removeEventListener(eventName, handler[, capturePhase])`

#### Description

Unregisters an event handler for a particular type of event occurring in this window. All arguments must be identical to those that were used to register the event handler.

#### Parameters

|   Parameter    |   Type   |                               Description                               |
| -------------- | -------- | ----------------------------------------------------------------------- |
| `eventName`    | String   | The event name string.                                                  |
| `handler`      | Function | The function that was registered to handle the event.                   |
| `capturePhase` | Boolean  | Optional. Whether the handler was to respond only in the capture phase. |

#### Returns

Nothing

---

### show()

`windowOrContainerObj.show()`

Shows this window, container, or control. If an [onShow](#window-event-handling-callbacks) callback is defined for a window, calls that function before showing the window.

When a window or container is hidden, its children are also hidden, but when it is shown again, the children retain their own visibility states.

For a modal dialog, opens the dialog and does not return until the dialog is dismissed. If it is dismissed via the [close()](#close) method, this method returns any result value passed to that method. Otherwise, returns 0.

#### Returns

Nothing

---

### update()

`windowOrContainerObj.update()`

Allows a script to run a long operation (such as copying a large file) and update UI elements to show the status of the operation.

Normally, drawing updates to UI elements occur during idle periods, when the application is not doing anything and the OS event queue is being processed, but during a long scripted operation, the normal event loop is not running. Use this method to perform the necessary synchronous drawing updates, and also process certain mouse and keyboard events in order to allow a user to cancel the current operation (by clicking a Cancel button, for instance).

During the update() operation, the application is put into a modal state, so that it does not handle any events that would activate a different window, or give focus to a control outside the window being updated. The modal state allows drawing events for controls in other windows to occur (as is the case during a modal [show()](#show) operation), so that the script does not prevent the update of other parts of the application's UI while in the operation loop.

It is an error to call the update() method for a window that is not currently visible.

#### Returns

Nothing

---

## Window event-handling callbacks

The following callback functions can be defined to respond to events in windows. To respond to an event, define a function with the corresponding name in the `Window` instance. These callbacks are not available for other container types (controls of type `panel` or `group`).

### onActivate

Called when the user make the window active by clicking it or otherwise making it the keyboard focus.

---

### onClose

Called when a request is made to close the window, either by an explicit call to the [close()](#close) function or by a user action (clicking the OS-specific close icon in the title bar). The function is called before the window actually closes; it can return `false` to cancel the close operation.

---

### onDeactivate

Called when the user makes a previously active window inactive; for instance by closing it, or by clicking another window to change the keyboard focus.

---

### onDraw

Called when a container or control is about to be drawn. Allows the script to modify or control the appearance, using the control's associated [ScriptUIGraphics object](graphic-customization-objects.md#scriptuigraphics-object) object. Handler takes one argument, a [DrawState object](control-objects.md#drawstate-object) object.

---

### onMove

Called when the window has been moved.

---

### onMoving

Called while a window in being moved, each time the position changes. A handler can monitor the move operation.

---

### onResize

Called when the window has been resized.

---

### onResizing

Called while a window is being resized, each time the height or width changes. A handler can monitor the resize operation.

---

### onShortcutKey

(In [Windows](#) only)

Called when a shortcut-key sequence is typed that matches the shortcutKey value for this window.

---

### onShow

Called when a request is made to open the window using the [show()](#show) method, before the window is made visible, but after automatic layout is complete. A handler can modify the results of the automatic layout.
