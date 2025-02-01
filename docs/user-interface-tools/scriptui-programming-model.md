# ScriptUI programming model

ScriptUI defines `Window` objects that represent platform-specific windows, and various control elements
such as `Button` and `StaticText`, that represent user-interface controls. These objects share a common set
of properties and methods that allow you to query the type, move the element around, set the title,
caption or content, and so on. Many element types also have properties unique to that class of elements.

---

## Creating a window

ScriptUI defines the following types of windows:

- Modal dialog box: Holds focus when shown, does not allow activity in other application windows until
  dismissed.
- Floating palette: Also called modeless dialog, allows activity in other application windows. (Adobe
  Photoshop® does not support script creation of palette windows.)
- Main window: Suitable for use as an application’s main window. (Main windows are not normally
  created by script developers for Adobe applications. Photoshop does not support script creation of
  main windows.)

To create a new window, use the `Window` constructor function. The constructor takes the desired type of
the window. The type is `"dialog"` for a modal dialog, or `"palette"` for a modeless dialog or floating
palette. You can supply optional arguments to specify an initial window title and bounds; or you can set
the location and size separately.

The following example creates an empty dialog with the variable name dlg, which is used in subsequent
examples:

```default
// Create an empty dialog window near the upper left of the screen
var dlg = new Window( "dialog", "Alert Box Builder" );
dlg.frameLocation = [ 100, 100 ];
```

Initially, new windows are hidden. The show method makes them visible and responsive to user
interaction; for example:

```default
dlg.show();
```

---

## Container elements

All Windows are containers-that is, they contain other elements within their bounds. Within a Window, you
can create other types of container elements: Panels and Groups. These can contain control elements,
and can also contain other Panel and Group containers. However, a Window cannot be added to any
container.

- A `Group` is the simplest container used to visually organize related controls. You would typically define
  a group and populate it with related elements, for instance an edittext box and its descriptive
  statictext label.
- A `Panel` is a frame object, also typically used to visually organize related controls. It has a text property
  to specify a title, and can have a border to visually separate the collection of elements from other
  elements of a dialog.
- A `TabbedPanel` is a frame that contains only Tab elements. Each Tab is a frame with a localizable title
  in the selection tab, which contains a set of controls. When a tab is active, the Tab object is the value of
  the TabbedPanel.selection property.

You might create a `Panel` and populate it with several `Groups`, each with their own elements. You can
create nested containers, with different layout properties for different containers, in order to define a
relatively complex layout without any explicit placement.

You can add elements to any container using the add method (see [Adding elements to containers](#adding-elements-to-containers)). An element added to a container is considered a child of that container. Certain operations on a
container apply to its children; for example, when you hide a container, its children are also hidden.

---

## Window layout

When a script creates a `Window` and adds various user-interface elements to it, the locations and sizes of
elements and spacing between elements is known as the *layout* of the window. Each user-interface
element has properties which define its location and dimensions: `location`, `size`, and `bounds`. These
properties are initially undefined, and a script that employs [Automatic layout](automatic-layout.md#automatic-layout) should leave them
undefined for the main window as well as its contained elements, allowing the automatic layout
mechanism to set their values.

Your script can access these values, and (if not using auto-layout) set them as follows:

- The `location` of a window is defined by a `Point` object containing a pair of coordinates (`x` and `y`) for
  the top left corner (the origin), specified in the screen coordinate system. The location of an element
  within a window or other container is defined as the origin point specified in the container’s
  coordinate system. That is, the x and y values are relative to the origin of the container.
  The following examples show equivalent ways of placing the content region of an existing window at
  screen coordinates [10, 50]:
  ```default
  win.location = [ 10, 50 ];
  win.location = { x: 10, y: 50 };
  win.location = "x:10, y:50";
  ```
- The `size` of an element’s region is defined by a `Dimension` object containing a `width` and `height` in pixels.
  The following examples show equivalent ways of changing an existing window’s width and height to 200 and 100:
  ```default
  win.size = [ 200, 100 ];
  win.size = { width: 200, height: 100 };
  win.size = "width:200, height:100";
  ```

  This example shows how to change a window’s height to 100, leaving its location and width
  unchanged:
  ```default
  win.size.height = 100;
  ```
- The `bounds` of an element are defined by a `Bounds` object containing both the origin point (`x`, `y`) and
  size (`width`, `height`) To define the size and location of windows and controls in one step, use the
  bounds property.

  The value of the `bounds` property can be a string with appropriate contents, an inline JavaScript
  `Bounds` object, or a four-element array. The following examples show equivalent ways of placing a 380
  by 390 pixel window near the upper left corner of the screen:
  ```default
  var dlg = new Window( "dialog", "Alert Box Builder", [ 100, 100, 480, 490] );
  dlg.bounds = [ 100, 100, 480, 490 ];
  dlg.bounds = { x: 100, y: 100, width: 380, height: 390 };
  dlg.bounds = { left: 100, top: 100, right: 480, bottom: 490 };
  dlg.bounds = "left:100, top:100, right:480, bottom:490";
  ```

The `window` dimensions define the size of the *content region* of the window, or that portion of the window
that a script can directly control. The actual window size is typically larger, because the host platform’s
window system typically adds title bars and borders. The `bounds` property for a `Window` refers only to its
content region. To determine the bounds of the frame surrounding the content region of a window, use
the `Window.frameBounds` property.

---

## Adding elements to containers

To add elements to a `window`, `panel`, or `group`, use the container’s `add` method. This method accepts the
type of the element to be created and some optional parameters, depending on the element type. It
creates and returns an object of the specified type.

In additions to windows, ScriptUI defines the following user-interface elements and controls:

- Panels (frames) and groups, to collect and organize other control types
- Push buttons with text or icons, radio buttons, checkbox buttons
- Static text or images, edit text
- Progress bars, scrollbars, sliders
- Lists, which include list boxes, drop-down (also called popup) lists, and tree views. Each item in a list is
  a control of type `item`, and the parent list’s `items` property contains an array of child items. Tree views
  can also have collapsible `node`-type items, which contain child items. You can add list items with the
  parent’s `add` method.

You can specify the initial size and position of any new element relative to the working area of the parent
container, in an optional `bounds` parameter. Different types of elements have different additional
parameters. For elements which display text, for example, you can specify the initial text. See the ScriptUI
Classes dictionary in the ExtendScript Toolkit’s Object Model Viewer for details.

The order of optional parameters must be maintained. Use the value `undefined` for a parameter you do
not wish to set. For example, if you want to use automatic layout to determine the bounds, but still set the
title and text in a panel and button, the following creates `Panel` and `Button` elements with an initial `text`
value, but no `bounds` value:

```default
dlg.btnPnl = dlg.add('panel', undefined, 'Build it');
dlg.btnPnl.testBtn = dlg.btnPnl.add('button', undefined, 'Test');
```

A new element is initially set to be visible, but is not shown unless its parent object is shown.

---

### Creation properties

Some element types have attributes that can only be specified when the element is created. These are not
normal properties of the element, in that they cannot be changed during the element’s lifetime, and they
are only needed once. For these element types, you can supply an optional creation-properties
argument to the add method. This argument is an object with one or more properties that control aspects
of the element’s appearance, or special functions such as whether an edit text element is editable or Read
only. See [Control object constructors](control-objects.md#control-object-constructors) for details.

You can also specify the creation properties for new objects using the resource specification format; for
details, see [Resource specifications](resource-specifications.md#resource-specifications).

All user-interface elements have an optional creation property called name, which assigns a name for
identifying that element. For example, the following creates a new Button element with the name ok:

```default
dlg.btnPnl.buildBtn = dlg.btnPnl.add('button', undefined, 'Build', {name:'ok'});
```

!!! note
    In Photoshop CS, panel coordinates were measured from outside the frame (including the title bar),
but in Photoshop CS2, panel coordinates are measured from the inside the frame (the content area). This
means that if you use the same values to set the vertical positions of child controls in a panel, the positions
are slightly different in the two versions. When you add a panel to a window, you can choose to set a
creation property (su1PanelCoordinates), which causes that panel to automatically adjust the positions
of its children; see the add method for panel. When automatic adjustment is enabled, you provide
position values that were correct for Photoshop CS, and the result is the same in Photoshop CS2, CS3, CS4,
CS5, or CC. You can also set automatic adjustment for a window; in this case, it applies to all child panels of
that window unless it is explicitly disabled in the child panel. See Window object constructor.

---

### Accessing child elements

A reference to each element added to a container is appended to the container’s `children` property. You
can access the child elements through this array, using a 0-based index. For controls that are not
containers, the `children` collection is empty.

In this example, the `msgPnl` panel was the first element created in dlg, so the script can access the panel
object at index 0 of the parent’s `children` property to set the text for the title:

```default
var dlg = new Window( "dialog", "Alert Box Builder" );
dlg.msgPnl = dlg.add( "panel" );
dlg.children[ 0 ].text = "Messages";
```

If you use a creation property to assign a name to a newly created element, you can access that child by its
name, either in the `children` array of its parent, or directly as a property of its parent. For example, the
`Button` in a previous example was named **ok**, so it can be referenced as follows:

```default
dlg.btnPnl.children[ "ok" ].text = "Build";
dlg.btnPnl.ok.text = "Build";
```

You can also access named elements through the parent window’s `findElement()` method:

```default
var myOkButton = dlg.findElement( "ok" );
```

For list controls (type `list` and `dropdown`), you can access the child list-item objects through the `items`
array.

---

## Removing elements

To remove elements from a `Window`, `Panel`, or `Group`, use the container’s `remove` method. This method
accepts an object representing the element to be removed, or the name of the element, or the index of the
element in the container’s `children` collection (see [Accessing child elements](#accessing-child-elements)).

The specified element is removed from view if it was currently visible, and it is no longer accessible from
the container or window. The results of any further references by a script to the object representing the
element are undefined.

To remove list items from a list, use the parent list control’s remove method in the same way. It removes the
item from the parent’s `items` list, hides it from view, and deletes the item object.
