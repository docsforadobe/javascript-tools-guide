<a id="size-and-location-objects"></a>

# Size and location objects

ScriptUI defines objects to represent the complex values of properties that place and size windows and
user-interface elements. These objects cannot be created directly, but are created when you set the
corresponding property. That property then returns that object. For example, the `bounds` property returns
a `Bounds` object.

You can set these properties as objects, strings, or arrays.

- `e.prop = Object` - The object must contain the set of properties defined for this type, as shown in
  the table below. The properties have integer values.
- `e.prop = String` - The string must be an executable JavaScript inline object declaration,
  conforming to the same object description.
- `e.prop = Array` - The array must have integer coordinate values in the order defined for this type,
  as shown in the table below. For example:

The following examples show equivalent ways of placing a 380 by 390 pixel window near the upper left
corner of the screen:

```default
var dlg = new Window( "dialog", "Alert Box Builder ");
dlg.bounds = { x:100, y:100, width:380, height:390 }; // Object
dlg.bounds = { left:100, top:100, right:480, bottom:490 }; // Object
dlg.bounds = "x:100, y:100, width:380, height:390"; // String
dlg.bounds = "left:100, top:100, right:480, bottom:490"; // String
dlg.bounds = [100, 100, 480, 490]; // Array
```

You can access the resulting object as an array with values in the order defined for the type, or as an object
with the properties supported for the type.

---

<a id="size-and-location-object-types"></a>

## Size and location object types

The following table shows the property-value object types, the element properties that create and contain
them, and their array and object-property formats.

<a id="bounds"></a>

### Bounds

Defines the boundaries of a window within the screen’s coordinate space, or of a
user-interface element within the container’s coordinate space. Contains an array, [left,
top, right, bottom], that defines the coordinates of the upper left and lower right
corners of the element.

A `Bounds` object is created when you set an element’s `bounds` property, and this property
returns a `Bounds` object.

- An object must contain properties named `left`, `top`, `right`, `bottom`,
  or `x`, `y`, `width`, `height`.
- An array must have values in the order [left, top, right, bottom].

<a id="dimension"></a>

### Dimension

Defines the size of a Window or user-interface element. Contains an array, `[ width, height ]`,
that defines the element’s size in pixels.

A `Dimension` object is created when you set an element’s size or `preferredSize`
property. (A `preferredSize` of -1 causes the size to be calculated automatically.)

- An object must contain properties named `width` and `height`.
- An array must have values in the order `[ width, height ]`.

<a id="margins"></a>

### Margins

Defines the number of pixels between the edges of a container and its outermost child
elements. Contains an array `[ left, top, right, bottom ]` whose elements define the
margins between the left edge of a container and its leftmost child element, and so on.

A `Margins` object is created when you set an element’s `margins` property.

- An object must contain properties named `left`, `top`, `right`, and `bottom`.
- An array must have values in the order [ `left`, `top`, `right`, `bottom` ].

You can also set the margins property to a number; all of the array values are then set to
this number.

<a id="point"></a>

### Point

Defines the location of a `Window` or user-interface element. Contains an array, `[ x, y ]`,
whose values represent the origin point of the element as horizontal and vertical pixel
offsets from the origin of the element’s coordinate space.

A `Point` object is created when you set an element’s location property.

- An object must contain properties named `x` and `y`.
- An array must have values in the order `[ x, y ]`.
