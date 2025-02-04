# Drawing objects

ScriptUI allows you to draw directly on controls to customize their appearance. You do this by calling methods of the [ScriptUIGraphics object](graphic-customization-objects.md#scriptuigraphics-object) in response to the [onDraw](control-objects.md#ondraw) event (see [Defining behavior with event callbacks and listeners](defining-behavior-with-event-callbacks-and-listeners.md)).

These methods take as parameters a number of helper objects that encapsulate drawing information, including the following:

|                                     Object                                     |                                                                Description                                                                |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| [ScriptUIGraphics](./graphic-customization-objects.md#scriptuigraphics-object) | Encapsulates the drawing methods. The graphics object is associated with each control is found in the control object's graphics property. |
| [ScriptUIBrush](./graphic-customization-objects.md#scriptuibrush-object)       | Describes the brush used to paint textures in a control.                                                                                  |
| [ScriptUIFont](./graphic-customization-objects.md#scriptuifont-object)         | Describes the font used to write text into a control.                                                                                     |
| [ScriptUIImage](./graphic-customization-objects.md#scriptuiimage-object)       | Describes an image to be drawn in a control.                                                                                              |
| [ScriptUIPath](./graphic-customization-objects.md#scriptuipath-object)         | Describes a drawing path for a figure to be drawn into a control.                                                                         |
| [ScriptUIPen](./graphic-customization-objects.md#scriptuipen-object)           | Describes the pen used to draw lines in a control.                                                                                        |

For details of these objects, see [Graphic customization objects](./graphic-customization-objects.md).

The `ScriptUIGraphics` object contains methods that create the other graphics objects; for example, `ScriptUIGraphics.newBrush()` creates a `ScriptUIBrush` instance with a specific color. These graphic objects are then used as property values in the `ScriptUIGraphics` object, which controls how a user-interface element is drawn on the screen. For example, if you put the new Brush object in the `backgroundColor` property, the element is drawn using that color for the background.

To make the background of a window light gray, you could use this code:

```javascript
g = myWindow.graphics;
myBrush = g.newBrush( g.BrushType.SOLID_COLOR, [ 0.75, 0.75, 0.75, 1 ] );
g.backgroundColor = myBrush;
```

These examples in the [Adobe ExtendScript SDK](https://github.com/Adobe-CEP/CEP-Resources/tree/master/ExtendScript-Toolkit) demonstrates how to use graphic customization objects:

|                                                                Example                                                                |                                                          Description                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| [ColorSelector.jsx](https://github.com/Adobe-CEP/CEP-Resources/blob/master/ExtendScript-Toolkit/Samples/javascript/ColorSelector.jsx) | Uses graphic objects to change the background color of a window as the user selects the color value with a slider.            |
| [ColorPicker.jsx](https://github.com/Adobe-CEP/CEP-Resources/blob/master/ExtendScript-Toolkit/Samples/javascript/ColorPicker.jsx)     | A more complex version of the color-selection dialog shows how to use additional graphics objects, including fonts and paths. |

In addition, the [Custom element class](./graphic-customization-objects.md#custom-element-class) allows you to define completely customized elements of several types (ranges, buttons, lists), whose appearance is rendered entirely by your [onDraw](control-objects.md#ondraw) implementation.
