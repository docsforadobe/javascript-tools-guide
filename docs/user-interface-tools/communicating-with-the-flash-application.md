# Communicating with the Flash application

ScriptUI supports a Flash Player, which runs the Flash application within a window in an Adobe
application. The Flash application runs ActionScript, a different implementation of JavaScript from the
ExtendScript version of JavaScript that Adobe applications run.

To open a Flash Player, add a control of type [FlashPlayer](types-of-controls.md#flashplayer) to your ScriptUI window. A control object of this
type contains functions that allow your script to load SWF files and control movie playback. It also contains
functions that allow your Adobe application script to communicate with the ActionScript environment of
the Flash application. See [FlashPlayer control functions](control-objects.md#flashplayer-control-functions).

A limited set of data types can be passed between the two scripting environments:

- `Number`
- `String`
- `Boolean`
- `Null`
- `undefined`
- `Object`
- `Array`

The ActionScript `class` and `date` objects are not supported as parameter values.

In the ActionScript script for your Flash application, you must prepare for two-way communication by
providing access to the External API. Do this by importing the `ExternalInterface` class into your Flash
application:

```default
import flash.external.ExternalInterface;
```

---

## Calling ExtendScript functions from ActionScript

The ActionScript `ExternalInterface` class allows you to call an ExtendScript function that has been
defined in the `FlashPlayer` element in the Adobe application script, and run it in the ActionScript
environment. You must define the method in your [FlashPlayer](types-of-controls.md#flashplayer) element with a matching function name.

For example, in order for the SWF code to call an ExtendScript function named `myExtendScriptFunction`,
define a function with the name `myExtendScriptFunction` as a method of your `FlashPlayer` control
object. There are no special requirements for function names, but the function must take and return only
data of the supported types.

You do not need to register the ExtendScript function in the ActionScript environment. Your ActionScript
script can simply call the external function using the `ExternalInterface.call()` method:

```default
var res = ExternalInterface.call( "myJavaScriptFunction" );
```

When the Flash Player executes the ExternalInterface call, ScriptUI looks for a function with the same
name as a method of the FlashPlayer element, and invokes it with the specified arguments. In the
context of the function, the JavaScript this object refers to the `FlashPlayer` object.

---

## Calling ActionScript functions from a ScriptUI script

From the ExtendScript side, use the `FlashPlayer` method [invokePlayerFunction()](control-objects.md#flashplayerobj-invokeplayerfunction) to call ActionScript
methods that have been defined within the Flash application:

```default
var result = flashElement.invokePlayerFunction( "ActionScript_function_name", [ arg1, ..., argN ] );
```

You can use the optional arguments to pass data (of supported types) to the ActionScript method.

Before you can call any ActionScript function from your Adobe application script, your Flash application
must register that function with the `ExternalInterface` object, as a callback from the Flash container. To
register a function, use the `ExternalInterface.addCallback()` method:

```default
public static addCallback(methodName:String, instance:Object, method:Function);
```

This registers a function defined in your Adobe application script named `getActionScriptArray()`:

```default
ExternalInterface.addCallback( "getActionScriptArray", this, getActionScriptArray );
```

---

## Flash Examples

These examples in the [Adobe ExtendScript SDK](https://github.com/Adobe-CEP/CEP-Resources/tree/master/ExtendScript-Toolkit) demonstrate how to use the Flash Player:

| [UsingFlashPlayer.jsx](https://github.com/Adobe-CEP/CEP-Resources/blob/master/ExtendScript-Toolkit/Samples/javascript/UsingFlashPlayer.jsx)   | Shows how to create a Flash® Player, and use it to load a play back a movie defined in an SWF file.                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| [ActionScriptDemo.jsx](https://github.com/Adobe-CEP/CEP-Resources/blob/master/ExtendScript-Toolkit/Samples/javascript/ActionScriptDemo.jsx)   | Shows how to communicate between the Adobe application scripting environment and the ActionScript™ scripting environment of the Flash Player. |
