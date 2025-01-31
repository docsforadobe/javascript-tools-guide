<a id="extendscript-reflection-interface"></a>

# ExtendScript reflection interface

ExtendScript provides a reflection interface that allows you to find out everything about an object,
including its name, a description, the expected data type for properties, the arguments and return value
for methods, and any default values or limitations to the input values.

<a id="reflection-object"></a>

## Reflection object

Every object has a reflect property that returns a reflection object that reports the contents of the
object. You can, for example, show the values of all the properties of an object with code like this:

```default
var f = new File ("myfile");
var props = f.reflect.properties;
for (var i = 0; i < props.length; i++) {
  $.writeln('this property ' + props[i].name + ' is ' + f[props[i].name]);
}
```

---

<a id="reflection-object-properties"></a>

### Reflection object properties

All properties are read only.

| description   | String                  | Short text describing the reflected object, or undefined if no<br/>description is available.                                                                                                                                                                                                                                                                                                                                                              |
|---------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| help          | String                  | Longer text describing the reflected object more completely, or<br/>`undefined` if no description is available.                                                                                                                                                                                                                                                                                                                                           |
| methods       | Array of ReflectionInfo | An Array of [ReflectionInfo object](#reflectioninfo-object) containing all methods of the<br/>reflected object, defined in the class or in the specific instance.                                                                                                                                                                                                                                                                                         |
| name          | String                  | The class name of the reflected object.                                                                                                                                                                                                                                                                                                                                                                                                                   |
| properties    | Array of ReflectionInfo | An Array of [ReflectionInfo object](#reflectioninfo-object) containing all properties of the<br/>reflected object, defined in the class or in the specific instance. For<br/>objects with dynamic properties (defined at runtime) the list contains<br/>only those dynamic properties that have already been accessed by<br/>the script. For example, in an object wrapping an HTML tag, the<br/>names of the HTML attributes are determined at run time. |

---

<a id="reflection-object-functions"></a>

### Reflection object functions

<a id="reflection-object-find"></a>

#### find()

`reflectionObj.find (name)`

| name   | The property for which to retrieve information.   |
|--------|---------------------------------------------------|

Returns the [ReflectionInfo object](#reflectioninfo-object) for the named property of the reflected object, or null if no such
property exists.

Use this method to get information about dynamic properties that have not yet been accessed, but
that are known to exist.

#### Examples

This code determines the class name of an object:

```default
obj = new String ("hi");
obj.reflect.name; // => String
```

This code gets a list of all methods:

```default
obj = new String ("hi");
obj.reflect.methods; //=> indexOf,slice,...
obj.reflect.find ("indexOf"); // => the method info
```

This code gets a list of properties:

```default
Math.reflect.properties; //=> PI,LOG10,...
```

This code gets the data type of a property:

```default
Math.reflect.find ("PI").type; // => number
```

---

<a id="reflectioninfo-object"></a>

## ReflectionInfo object

This object contains information about a property, a method, or a method argument.
You can access ReflectionInfo objects in a Reflection object’s properties and methods arrays, by
name or index:

```default
obj = new String ("hi");
obj.reflect.methods[0];
obj.reflect.methods["indexOf"];
```

You can access the ReflectionInfo objects for the arguments of a method in the arguments array of
the ReflectionInfo object for the method, by index:

```default
obj.reflect.methods["indexOf"].arguments[0];
obj.reflect.methods.indexOf.arguments[0];
```

---

<a id="reflectioninfo-object-properties"></a>

## ReflectionInfo object properties

| arguments    | Array of<br/>ReflectionInfo   | For a reflected method, an array of ReflectionInfo objects describing<br/>each method argument.                                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dataType     | String                        | The data type of the reflected element. One of:<br/><br/>- `boolean`<br/>- `number`<br/>- `string`<br/>- `Classname`: The class name of an object.<br/><br/>  #### NOTE<br/>  Class names start with a capital letter. Thus, the value<br/>  `string` stands for a JavaScript string, while `String` is a<br/>  JavaScript `String` wrapper object.<br/>- `*`: Any type. This is the default.<br/>- `null`<br/>- `undefined`: Return data type for a function that does not return<br/>  any value.<br/>- `unknown` |
| defaultValue | any                           | The default value for a reflected property or method argument, or<br/>`undefined` if there is no default value, if the property is undefined, or<br/>if the element is a method.                                                                                                                                                                                                                                                                                                                                    |
| description  | String                        | Short text describing the reflected object, or `undefined` if no<br/>description is available.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| help         | String                        | Longer text describing the reflected object more completely, or<br/>`undefined` if no description is available.                                                                                                                                                                                                                                                                                                                                                                                                     |
| isCollection | Boolean                       | When `true`, the reflected property or method returns a collection;<br/>otherwise, `false`.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| max          | Number                        | The maximum numeric value for the reflected element, or<br/>`undefined` if there is no maximum or if the element is a method.                                                                                                                                                                                                                                                                                                                                                                                       |
| min          | Number                        | The minimum numeric value for the reflected element, or `undefined`<br/>if there is no minimum or if the element is a method.                                                                                                                                                                                                                                                                                                                                                                                       |
| name         | String<br/>Number             | The name of the reflected element. A string, or a number for an array<br/>index.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| type         | String                        | The type of the reflected element. One of:<br/><br/>- `readonly`: A Read only property.<br/>- `readwrite`: A read-write property.<br/>- `createonly`: A property that is valid only during creation of an<br/>  object.<br/>- `method`: A method.                                                                                                                                                                                                                                                                   |
