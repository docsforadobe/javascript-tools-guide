# LayoutManager object

Controls the automatic layout behavior for a window or container. The subclass AutoLayoutManager implements the default automatic layout behavior.

## AutoLayoutManager object constructor

Create an instance of the `AutoLayoutManager` class with the new operator:

```javascript
myWin.layout = new AutoLayoutManager( myWin );
```

An instance is automatically created when you create a `Window` or container (`group` or `panel`) object, and referenced by the container's [layout](window-object.md#container-properties-layout) property. This instance implements the default layout behavior unless you override it.

## AutoLayoutManager object properties

The default object has no predefined properties, but a script can assign arbitrary properties to an object it creates, to store data needed by the script-defined layout algorithm.

## AutoLayoutManager object functions

### layout()

`windowObj.layout.layout( recalculate )`

#### Description

Invokes the automatic layout behavior for the managed container. Adjusts sizes and positions of the child elements of this window or container according to the placement and alignment property values in the parent and children.

Invoked automatically the first time the window is displayed. Thereafter, the script must invoke it explicitly to change the layout in case of changes in the size or position of the parent or children.

#### Parameters

|   Parameter   |  Type   |                                                                Description                                                                |
| ------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `recalculate` | Boolean | Optional. When `true`, forces the layout manager to recalculate the container size for this and any child containers. Default is `false`. |

#### Returns

Nothing

---

### resize()

`windowObj.layout.resize()`

#### Description

Resizes and moves the child elements of the managed container, according to the alignment values for each child of the container, after the container has been resized by the user or by a script.

See [Automatic layout](automatic-layout.md) for details of how alignment affects an element's size and location.

#### Returns

Nothing
