# Loading and using shared libraries

To load an external shared library into JavaScript, create a new [ExternalObject object](externalobject-object.md). The instance acts as a container and manager for the JavaScript interface to the library. It provides a logging facility that prints status information to the JavaScript Console in the ExtendScript Toolkit, to help you debug your external library use.

Once the library has been loaded, its exported symbols become available to JavaScript. In your JavaScript code, you can call the functions defined in the library directly in the `ExternalObject` instance, or indirectly through library-defined object types.

---

## Direct access to library calls through the ExternalObject instance

Use the direct-access style for C-language libraries. For each function defined in the C library, there is a corresponding method in the ExternalObject object. You can pass data to these methods and receive the return value directly.

For example:

```javascript
mylib = new ExternalObject ("lib:" + samplelib); // load the library
alert(mylib.version) ;
// access functions directly from ExternalObject instance
var a = mylib.method_abc(1,2.0,true, "this is data") ;
alert(a) ;
mylib.unload() ;
```

For details of how to define functions for direct access through the ExternalObject object, see [Defining entry points for direct access](./defining-entry-points-for-direct-access.md)

---

## Indirect access to library calls through JavaScript classes

Use the indirect style to access classes defined in a C++ library. For each C++ class defined in the library, a corresponding JavaScript class is automatically defined, and you can access the properties and methods through an instance of that class.

For example:

```javascript
anotherlib= new ExternalObject ("lib:" + filespec); // load the library
alert(anotherlib.version) ;
// instantiate library-defined class
var myObject = new MyNewClass() ;
// access functions from instance
var a = myObject.method_abc(1,2.0,true,"this is data") ;
alert(a) ;
anotherlib.unload() ;
```

For details of how to define functions for direct access through the ExternalObject object, see [Defining entry points for indirect access](./defining-entry-points-for-indirect-access.md).
