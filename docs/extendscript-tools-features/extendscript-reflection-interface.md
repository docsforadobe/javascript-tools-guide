# ExtendScript Reflection Interface

ExtendScript provides a reflection interface that allows you to find out everything about an object, including its name, a description, the expected data type for properties, the arguments and return value for methods, and any default values or limitations to the input values.

---

## ReflectionObject

Every object has a reflect property that returns a Reflection Object that reports the contents of the object. You can, for example, show the values of all the properties of an object with code like this:

```javascript
var f = new File ("myfile");
var props = f.reflect.properties;
for (var i = 0; i < props.length; i++) {
  $.writeln('this property ' + props[i].name + ' is ' + f[props[i].name]);
}
```

### ReflectionObject Attributes

All properties are read only.

#### description

`reflect.description`

##### Description

Short text describing the reflected object, or undefined if no description is available.

##### Type

String

---

#### help

`reflect.help`

##### Description

Longer text describing the reflected object more completely, or `undefined` if no description is available.

##### Type

String

---

#### methods

`reflect.methods`

##### Description

An Array of [ReflectionInfo object](#reflectioninfo-object) containing all methods of the reflected object, defined in the class or in the specific instance.

##### Type

Array of [ReflectionInfo objects](#reflection-object)

---

#### name

`reflect.name`

##### Description

The class name of the reflected object.

##### Type

String

---

#### properties

`reflect.properties`

##### Description

An Array of [ReflectionInfo object](#reflectioninfo-object) containing all properties of the reflected object, defined in the class or in the specific instance. For objects with dynamic properties (defined at runtime) the list contains only those dynamic properties that have already been accessed by the script.

For example, in an object wrapping an HTML tag, the names of the HTML attributes are determined at run time.

##### Type

Array of [ReflectionInfo objects](#reflection-object)

---

### ReflectionObject Methods

#### find()

`reflectionObj.find(name)`

##### Description

Returns the [ReflectionInfo object](#reflectioninfo-object) for the named property of the reflected object, or null if no such property exists.

Use this method to get information about dynamic properties that have not yet been accessed, but that are known to exist.

##### Parameters

| Parameter |  Type  |                   Description                   |
| --------- | ------ | ----------------------------------------------- |
| name      | String | The property for which to retrieve information. |

#### Examples

This code determines the class name of an object:

```javascript
obj = new String ("hi");
obj.reflect.name; // => String
```

This code gets a list of all methods:

```javascript
obj = new String ("hi");
obj.reflect.methods; //=> indexOf,slice,...
obj.reflect.find ("indexOf"); // => the method info
```

This code gets a list of properties:

```javascript
Math.reflect.properties; //=> PI,LOG10,...
```

This code gets the data type of a property:

```javascript
Math.reflect.find ("PI").type; // => number
```

---

## ReflectionInfo Object

This object contains information about a property, a method, or a method argument.

You can access ReflectionInfo objects in a Reflection object's properties and methods arrays, by name or index:

```javascript
obj = new String ("hi");
obj.reflect.methods[0];
obj.reflect.methods["indexOf"];
```

You can access the ReflectionInfo objects for the arguments of a method in the arguments array of the ReflectionInfo object for the method, by index:

```javascript
obj.reflect.methods["indexOf"].arguments[0];
obj.reflect.methods.indexOf.arguments[0];
```

---

### ReflectionInfo Attributes

#### arguments

`obj.reflect.methods[0].arguments`

##### Description

For a reflected method, an array of [ReflectionInfo objects](#reflectioninfo-object) describing each method argument.

##### Type

Array of [ReflectionInfo objects](#reflectioninfo-object)

---

#### dataType

`obj.reflect.methods[0].dataType`

##### Description

The data type of the reflected element.

##### Type

String. One of:

- `"boolean"`
- `"number"`
- `"string"`
- `"Classname"`: The class name of an object.
    !!! note
        Class names start with a capital letter. Thus, the value `String` stands for a JavaScript string, while String is a JavaScript String wrapper object.
- `*`: Any type. This is the default.
- `null`
- `undefined`: Return data type for a function that does not return any value.
- `unknown`

---

#### defaultValue

`obj.reflect.methods[0].defaultValue`

##### Description

The default value for a reflected property or method argument, or `undefined` if there is no default value, if the property is undefined, or if the element is a method.

##### Type

Any

---

#### description

`obj.reflect.methods[0].description`

##### Description

Short text describing the reflected object, or `undefined` if no description is available.

##### Type

String

---

#### help

`obj.reflect.methods[0].help`

##### Description

Longer text describing the reflected object more completely, or `undefined` if no description is available.

##### Type

String

---

#### isCollection

`obj.reflect.methods[0].isCollection`

##### Description

When `true`, the reflected property or method returns a collection; otherwise, `false`.

##### Type

Boolean

---

#### max

`obj.reflect.methods[0].max`

##### Description

The maximum numeric value for the reflected element, or `undefined` if there is no maximum or if the element is a method.

##### Type

Number

---

#### min

`obj.reflect.methods[0].min`

##### Description

The minimum numeric value for the reflected element, or `undefined` if there is no minimum or if the element is a method.

##### Type

Number

---

#### name

`obj.reflect.methods[0].name`

##### Description

The name of the reflected element. A string, or a number for an array index.

##### Type

String or Number

---

#### type

`obj.reflect.methods[0].type`

##### Description

The type of the reflected element.

##### Type

String. One of:

- `readonly`: A Read only property.
- `readwrite`: A read-write property.
- `createonly`: A property that is valid only during creation of an object.
- `method`: A method.

---
