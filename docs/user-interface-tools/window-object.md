<a id="window-object"></a>

# Window object

<a id="window-object-constructor"></a>

## Window object constructor

The constructor creates and returns a new Window object, or null if window creation failed.

```default
new Window (type [, title, bounds, {creation_properties}]);
```

| `type`                | The window type. The value is:<br/><br/>> - `dialog` - Creates a modal dialog.<br/>> - `palette` - Creates a modeless dialog, also called a floating palette.<br/>>   (Not supported by Photoshop CC.)<br/>> - `window` - Creates a simple window that can be used as a main window for<br/>>   an application. (Not supported by Photoshop CC.)<br/><br/>This argument can be a ScriptUI resource specification; in this case, all other<br/>arguments are ignored. See [Resource specifications](resource-specifications.md#resource-specifications).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `title`               | Optional. The window title. A localizable string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `bounds`              | Optional. The window’s position and size.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `creation_properties` | Optional. An object that can contain any of these properties:<br/><br/>> - `resizeable` - When true, the window can be resized by the user. Default<br/>>   is false.<br/>> - `su1PanelCoordinates` - Photoshop only. When true, the child panels of<br/>>   this window automatically adjust the positions of their children for<br/>>   compatability with Photoshop CS (in which the vertical coordinate was<br/>>   measured from outside the frame). Default is false. Individual panels can<br/>>   override the parent window’s setting.<br/>> - `closeButton` - When true, the title bar includes a button to close the<br/>>   window, if the platform and window type allow it. When false, it does not.<br/>>   Default is true. Not used for dialogs.<br/>> - `maximizeButton` - When true, the title bar includes a button to expand<br/>>   the window to its maximum size (typically, the entire screen), if the<br/>>   platform and window type allow it. When false, it does not. Default is false<br/>>   for type palette, true for type window. Not used for dialogs.<br/>> - `minimizeButton` - When true, the title bar includes a button to minimize<br/>>   or iconify the window, if the platform and window type allow it. When<br/>>   false, it does not. Default is false for type palette, true for type window.<br/>>   Main windows cannot have a minimize button in Mac OS. Not used for<br/>>   dialogs.<br/>> - `independent` - When true, a window of type window is independent of<br/>>   other application windows, and can be hidden behind them in Windows.<br/>>   In Mac OS, has no effect. Default is false.<br/>> - `borderless` - When true, the window has no title bar or borders.<br/>>   Properties that control those features are ignored. |

---

<a id="window-object-properties"></a>

## Window object properties

The following element properties apply specifically to Window elements:

<a id="window-active"></a>

### active

Type: Boolean

When true, the object is active, false otherwise. Set to true to make a
given control or dialog active.

- A modal dialog that is visible is by definition the active dialog.
- An active palette is the front-most window.
- An active control is the one with focus-that is, the one that
  accepts keystrokes, or in the case of a Button, be selected when
  the user types RETURN or ENTER.

---

<a id="window-cancelelement"></a>

### cancelElement

Type: Object

For a window of type dialog, the control to notify when a user types
the ESC key. By default, looks for a button whose name or text is
`"cancel"` (case disregarded).

---

<a id="window-defaultelement"></a>

### defaultElement

Type: Object

For a window of type dialog, the control to notify when a user types
the ENTER key. By default, looks for a button whose name or text is
`"ok"` (case disregarded).

---

<a id="window-framebounds"></a>

### frameBounds

Type: [Bounds](size-and-location-objects.md#bounds)

A Bounds object for the boundaries of the Window’s frame in screen
coordinates. The frame consists of the title bar and borders that
enclose the content region of a window, depending on the
windowing system. Read only.

---

<a id="window-framelocation"></a>

### frameLocation

Type: [Point](size-and-location-objects.md#point)

A Point object for the location of the top left corner of the Window’s
frame. The same as [frameBounds.x, frameBounds.y]. Set this
value to move the window frame to the specified location on the
screen. The frameBounds value changes accordingly.

---

<a id="window-framesize"></a>

### frameSize

Type: [Dimension](size-and-location-objects.md#dimension)

A Dimension object for the size and location of the Window’s frame
in screen coordinates. Read only.

---

<a id="window-maximized"></a>

### maximized

Type: Boolean

When true, the window is expanded.

---

<a id="window-minimized"></a>

### minimized

Type: Boolean

When true, the window is minimized or iconified.

---

<a id="window-opacity"></a>

### opacity

Type: Number

The opacity of the window, in the range [0..1]. A value of 1.0 (the
default) makes the window completely opaque, a value of 0 makes it
completely transparent. Intermediate values make it partially
transparent to any degree.

---

<a id="window-shortcutkey"></a>

### shortcutKey

Type: String

The key sequence that invokes this window’s ref:control-event-onshortcutkey callback
(in Windows only).

---

<a id="container-properties"></a>

## Container properties

The following table shows properties that apply to Window objects and container objects (controls of type
panel, tabbedpanel, tab, and group).

---

<a id="container-properties-alignchildren"></a>

### alignChildren

Type: String, or Array of 2 Strings

Tells the layout manager how unlike-sized children of a container
should be aligned within a column or row. Order of creation
determines which children are at the top of a column or the left of
a row; the earlier a child is created, the closer it is to the top or left
of its column or row.

If defined, alignment for a child element overrides the alignChildren setting for the parent container.

For a single string value, allowed values depend on the orientation value.

For `orientation=row`:

> - `top`
> - `bottom`
> - `center` (default)
> - `fill`

For `orientation=column`:

> - `left`
> - `right`
> - `center` (default)
> - `fill`

For `orientation=stack`:

> - `top`
> - `bottom`
> - `left`
> - `right`
> - `center` (default)
> - `fill`

For an array value, the first string element defines the horizontal
alignment and the second element defines the vertical
alignment. The horizontal alignment value must be one of left,
right, center or fill. The vertical alignment value must be one
of top, bottom, center, or fill.
Values are not case sensitive.

---

<a id="container-properties-alignment"></a>

### alignment

Type: String, or Array of 2 Strings

Applies to child elements of a container. If defined, this value
overrides the alignChildren setting for the parent container.
For a single string value, allowed values depend on the
`orientation` value.

For `orientation = row`:

> - `top`
> - `bottom`
> - `center` (default)
> - `fill`

For `orientation=column`:

> - `left`
> - `right`
> - `center` (default)
> - `fill`

For `orientation = stack`:

> - `top`
> - `bottom`
> - `left`
> - `right`
> - `center` (default)
> - `fill`

For an array value, the first string element defines the horizontal
alignment and the second element defines the vertical
alignment. The horizontal alignment value must be one of left,
right, center or fill. The vertical alignment value must be one
of top, bottom, center, or fill.

Values are not case sensitive.

---

<a id="container-properties-bounds"></a>

### bounds

Type: [Bounds](size-and-location-objects.md#bounds)

A Bounds object for the boundaries of the window’s drawable
area in screen coordinates. Compare [frameBounds](). Does not
apply to containers of type tab, whose bounds are determined
by the parent tabbedpanel container.

Read only.

---

<a id="container-properties-children"></a>

### children

Type: Array of Object

The collection of user-interface elements that have been added
to this window or container. An array indexed by number or by a
string containing an element’s `name`. The `length` property of this
array is the number of child elements for container elements, and
is zero for controls.

Read only.

---

<a id="container-properties-graphics"></a>

### graphics

Type: [ScriptUIGraphics object](graphic-customization-objects.md#scriptuigraphics-object)

A ScriptUIGraphics object that can be used to customize the
window’s appearance, in response to the onDraw event.

---

<a id="container-properties-layout"></a>

### layout

Type: [LayoutManager object](layoutmanager-object.md#layoutmanager-object)

A LayoutManager object for a window or container. The first time
a container object is made visible, ScriptUI invokes this layout
manager by calling its layout function. Default is an instance of
the LayoutManager class that is automatically created when the
container element is created.

---

<a id="container-properties-location"></a>

### location

Type: [Point](size-and-location-objects.md#point)

A Point object for the location of the top left corner of the
Window’s drawable area, or the top left corner of the frame for a
panel. The same as [bounds.x, bounds.y].

---

<a id="container-properties-margins"></a>

### margins

Type: [Margins](size-and-location-objects.md#margins)

A Margins object describing the number of pixels between the
edges of this container and the outermost child elements. You
can specify different margins for each edge of the container. The
default value is based on the type of container, and is chosen to
match the standard Adobe user-interface guidelines.

---

<a id="container-properties-maximumsize"></a>

### maximumSize

Type: [Dimension](size-and-location-objects.md#dimension)

A Dimension object for the largest rectangle to which the
window can be resized, used in automatic layout and resizing.

---

<a id="container-properties-minimumsize"></a>

### minimumSize

Type: [Dimension](size-and-location-objects.md#dimension)

A Dimension object for the smallest rectangle to which the
window can be resized, used in automatic layout and resizing.

---

<a id="container-properties-orientation"></a>

### orientation

Type: String

How elements are organized within this container. Interpreted by
the layout manager for the container. The default LayoutManager
object accepts the (case-insensitive) values:

> - `row`
> - `column`
> - `stack`

The default orientation depends on the type of container. For
`Window` and `Panel`, the default is `column`, and for `Group` the
default is `row`.

The allowed values for the container’s alignChildren and its
children’s alignment properties depend on the orientation.

---

<a id="container-properties-parent"></a>

### parent

Type: Object

The immediate parent object of this element, a window or
container element. The value is `null` for Window objects.

Read only.

---

<a id="container-properties-preferredsize"></a>

### preferredSize

Type: [Dimension](size-and-location-objects.md#dimension)

A Dimension object for the preferred size of the window, used in
automatic layout and resizing. To set a specific value for only one
dimension, specify other dimension as `-1`.

---

<a id="container-properties-properties-properties"></a>

### properties

Type: Object

An object that contains one or more creation properties of the
container (properties used only when the element is created).

---

<a id="container-properties-selection"></a>

### selection

Type: [tab](control-objects.md#control-type-tab)

For a [tabbedpanel](control-objects.md#control-type-tabbedpanel) only, the currently active [tab](control-objects.md#control-type-tab) child. Setting
this property changes the active tab. The value can only be `null`
when the panel has no children; setting it to `null` is an error.
When the value changes, either by a user selecting a different tab,
or by a script setting the property, the [onChange](control-objects.md#control-event-onchange) callback for the
panel is called.

---

<a id="container-properties-size"></a>

### size

Type: [Dimension](size-and-location-objects.md#dimension)

A Dimension object for the current size and location of a group or
panel element, or of the content area of a window.

---

<a id="container-properties-spacing"></a>

### spacing

Type: Number

The number of pixels separating one child element from its
adjacent sibling element. Because each container holds only a
single row or column of children, only a single spacing value is
needed for a container. The default value is based on the type of
container, and is chosen to match standard Adobe user-interface
guidelines.

---

<a id="container-properties-text"></a>

### text

Type: String

The title, label, or displayed text. Does not apply to containers of
type group or tabbedpanel. This is a localizable string: see
[Localization in ScriptUI objects](localization-in-scriptui-objects.md#localization-in-scriptui-objects).

---

<a id="container-properties-visible"></a>

### visible

Type: Boolean

When true, the element is shown, when false it is hidden.

When a container is hidden, its children are also hidden, but they
retain their own visibility values, and are shown or hidden
accordingly when the parent is next shown.

---

<a id="container-properties-window"></a>

### window

Type: [Window](#window-object)

The top-level parent window of this container, a [Window object](#window-object).

---

<a id="container-properties-windowbounds"></a>

### windowBounds

Type: [Bounds](size-and-location-objects.md#bounds)

A Bounds object for the size and location of this container relative
to its top-level parent window.

---

<a id="window-object-functions"></a>

## Window object functions

These functions are defined for Window instances, and as indicated for container objects of type Panel and
Group.

---

<a id="window-object-functions-add"></a>

### add()

`windowOrContainerObj.add (type [, bounds, text, { creation_props> } ]);`

| `type`           | The control type. See [Control types and creation parameters](control-objects.md#control-types-and-creation-parameters).                                                                                                                                                                                    |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `bounds`         | Optional. A bounds specification that describes the size and position of the new<br/>control or container, relative to its parent. See Bounds object for specification<br/>formats.<br/><br/>If supplied, this value creates a new Bounds object which is assigned to the new<br/>object’s bounds property. |
| `text`           | Optional. String. Initial text to be displayed in the control as the title, label, or<br/>contents, depending on the control type. If supplied, this value is assigned to<br/>the new object’s text property.                                                                                               |
| `creation_props` | Optional. Object. The properties of this object specify creation parameters,<br/>which are specific to each object type. See [Control types and creation parameters](control-objects.md#control-types-and-creation-parameters).                                                                             |

Creates and returns a new control or container object and adds it to the children of this window or
container.

Returns the new object, or `null` if unable to create the object.

---

<a id="window-object-functions-addeventlistener"></a>

### addEventListener()

`windowObj.addEventListener (eventName, handler[, capturePhase]);`

| `eventName`    | The event name string. Predefined event names include:<br/><br/>> - `change`<br/>> - `changing`<br/>> - `move`<br/>> - `moving`<br/>> - `resize`<br/>> - `resizing`<br/>> - `show`<br/>> - `enterKey`<br/>> - `focus`<br/>> - `blur`<br/>> - `mousedown`<br/>> - `mouseup`<br/>> - `mousemove`<br/>> - `mouseover`<br/>> - `mouseout`<br/>> - `click` (detail = 1 for single, 2 for double)                                                                  |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `handler`      | The function to register for the specified event in this target. This can be the<br/>name of a function defined in the extension, or a locally defined handler<br/>function to be executed when the event occurs. A handler function takes one<br/>argument, the UIEvent base class. See [Registering event listeners for windows or controls](defining-behavior-with-event-callbacks-and-listeners.md#registering-event-listeners-for-windows-or-controls). |
| `capturePhase` | Optional. When true, the handler is called only in the capturing phase of the<br/>event propagation. Default is false, meaning that the handler is called in the<br/>bubbling phase if this object is an ancestor of the target, or in the at-target<br/>phase if this object is itself the target.                                                                                                                                                          |

Registers an event handler for a particular type of event occurring in this window.

Returns `undefined`.

---

<a id="window-object-functions-center"></a>

### center()

`windowObj.center ([window])`

| `window`   | Optional. A Window object.   |
|------------|------------------------------|

Centers this window on the screen, or with respect to another specified window.

Returns `undefined`.

---

<a id="window-object-functions-close"></a>

### close()

`windowObj.close ([result])`

| `result`   | Optional. A number to be returned from the show method that invoked this<br/>window as a modal dialog.   |
|------------|----------------------------------------------------------------------------------------------------------|

Closes this window. If an onClose callback is defined for the window, calls that function before
closing the window.

Returns undefined.

---

<a id="window-object-functions-dispatchevent"></a>

### dispatchEvent()

`windowObj.dispatchEvent(eventObj)`

| `eventObj`   | A UIEvent base class.   |
|--------------|-------------------------|

Simulates the occurrence of an event in this target. A script can create a UIEvent base class for a
specific event and pass it to this method to start the event propagation for the event.

Returns `false` if any of the registered listeners that handled the event called the event object’s
[preventDefault()](event-handling.md#eventobj-preventdefault) method, `true` otherwise.

---

<a id="window-object-functions-findelement"></a>

### findElement()

`windowOrContainerObj.findElement(name)`

| `name`   | The name of the element, as specified in the name creation property.   |
|----------|------------------------------------------------------------------------|

Searches for the named element among the children of this window or container, and returns the
object if found.

Returns the control object or `null`.

---

<a id="window-object-functions-hide"></a>

### hide()

`windowObj.hide()`

Hides this window. When a window is hidden, its children are also hidden, but when it is shown
again, the children retain their own visibility states.

For a modal dialog, closes the dialog and sets its result to 0.

Returns `undefined`.

---

<a id="window-object-functions-notify"></a>

### notify()

`windowObj.notify([event])`

| `event`   | Optional. The name of the window event handler to call. One of:<br/><br/>> - `onClose`<br/>> - `onMove`<br/>> - `onMoving`<br/>> - `onResize`<br/>> - `onResizing`<br/>> - `onShow`   |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Sends a notification message, simulating the specified user interaction event. For example, to
simulate a dialog being moved by a user:

```default
myDlg.notify("onMove")
```

Returns `undefined`.

---

<a id="window-object-functions-remove"></a>

### remove()

`windowOrContainerObj.remove(index)`
`windowOrContainerObj.remove(text)`
`windowOrContainerObj.remove(child)`

| `index`/`text`/`child`   | The child control to remove, specified by 0-based index, the contained text<br/>value, or as a control object.   |
|--------------------------|------------------------------------------------------------------------------------------------------------------|

Removes the specified child control from this window’s or container’s children array. No error
results if the child does not exist.

Returns `undefined`.

---

<a id="window-object-functions-removeeventlistener"></a>

### removeEventListener()

`windowObj.removeEventListener(eventName, handler[, capturePhase])`

| `eventName`    | The event name string.                                                  |
|----------------|-------------------------------------------------------------------------|
| `handler`      | The function that was registered to handle the event.                   |
| `capturePhase` | Optional. Whether the handler was to respond only in the capture phase. |

Unregisters an event handler for a particular type of event occurring in this window. All arguments
must be identical to those that were used to register the event handler.

Returns `undefined`.

---

<a id="window-object-functions-show"></a>

### show()

`windowObj.show()`

Shows this window, container, or control. If an [onShow](#window-event-handling-callbacks) callback is defined for a window, calls that
function before showing the window.

When a window or container is hidden, its children are also hidden, but when it is shown again, the
children retain their own visibility states.

For a modal dialog, opens the dialog and does not return until the dialog is dismissed. If it is
dismissed via the [close()](#window-object-functions-close) method, this method returns any result value passed to that method.
Otherwise, returns 0.

---

<a id="window-object-functions-update"></a>

### update()

`windowObj.update()`

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
the case during a modal [show()](#window-object-functions-show) operation), so that the script does not prevent the update of other
parts of the application’s UI while in the operation loop.

It is an error to call the update() method for a window that is not currently visible.

---

<a id="window-event-handling-callbacks"></a>

## Window event-handling callbacks

The following callback functions can be defined to respond to events in windows. To respond to an event,
define a function with the corresponding name in the `Window` instance. These callbacks are not available
for other container types (controls of type `panel` or `group`).

| Callback          | Description                                                                                                                                                                                                                                                                                                                                           |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **onActivate**    | Called when the user make the window active by clicking it or otherwise making it<br/>the keyboard focus.                                                                                                                                                                                                                                             |
| **onClose**       | Called when a request is made to close the window, either by an explicit call to the<br/>[close()](#window-object-functions-close) function or by a user action<br/>(clicking the OS-specific close icon in the title bar).<br/><br/>The function is called before the window actually closes; it can return false to cancel<br/>the close operation. |
| **onDeactivate**  | Called when the user makes a previously active window inactive; for instance by<br/>closing it, or by clicking another window to change the keyboard focus.                                                                                                                                                                                           |
| **onDraw**        | Called when a container or control is about to be drawn. Allows the script to modify<br/>or control the appearance, using the control’s associated [ScriptUIGraphics object](graphic-customization-objects.md#scriptuigraphics-object) object.<br/>Handler takes one argument, a [DrawState object](control-objects.md#drawstate-object) object.      |
| **onMove**        | Called when the window has been moved.                                                                                                                                                                                                                                                                                                                |
| **onMoving**      | Called while a window in being moved, each time the position changes. A handler<br/>can monitor the move operation.                                                                                                                                                                                                                                   |
| **onResize**      | Called when the window has been resized.                                                                                                                                                                                                                                                                                                              |
| **onResizing**    | Called while a window is being resized, each time the height or width changes. A<br/>handler can monitor the resize operation.                                                                                                                                                                                                                        |
| **onShortcutKey** | (In Windows only) Called when a shortcut-key sequence is typed that matches the<br/>shortcutKey value for this window.                                                                                                                                                                                                                                |
| **onShow**        | Called when a request is made to open the window using the [show()](#window-object-functions-show) method, before<br/>the window is made visible, but after automatic layout is complete. A handler can<br/>modify the results of the automatic layout.                                                                                               |
