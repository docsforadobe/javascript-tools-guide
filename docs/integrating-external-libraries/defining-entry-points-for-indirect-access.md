<a id="defining-entry-points-for-indirect-access"></a>

# Defining entry points for indirect access

The C-client object interface for external libraries allows your C or C++ shared-library code to define,
create, use, and manage JavaScript objects.

---

<a id="indirect-access-entry-points"></a>

## Entry Points

The following entry points are required if you wish to use the object interface:

<a id="externalobject-functions-esclientinterface"></a>

### ESClientInterface()

`int ESClientInterface (SoCClient_e kReason, SoServerInterface* pServer, SoHServer hServer)`

| `kReason`   | The reason for this call, one of these constants:<br/>- `kSoCClient_init`: The function is being called for initialization upon load.<br/>- `kSoCClient_term`.: The function is being called for termination upon unload.                                                                                                                                                                                                                                             |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `pServer`   | A pointer to an [SoServerInterface](#shared-library-soserverinterface) containing function pointers for the entry points,<br/>which enable the shared-library code to call into JavaScript to create and access<br/>JavaScript classes and objects.<br/><br/>The shared-library code is responsible for storing this structure between the<br/>initialization and termination call, and retrieving it to access the functions.                                        |
| `hServer`   | An [Support structures](#sohserver) reference for this shared library. The server is an object factory that<br/>creates and manages [Support structures](#sohobject) objects.<br/><br/>The shared-library code is responsible for storing this structure between the<br/>initialization and termination calls. You must pass it to [taggedDataInit()](#externalobject-functions-taggeddatainit) and<br/>[taggedDataFree()](#externalobject-functions-taggeddatafree). |

Your library must define this global function in order to use the object interface to JavaScript. The
function is called twice in each session, immediately upon loading the library, and again when
unloading it.

Returns an error code, `kESErrOK` on success.

---

<a id="externalobject-functions-esmallocmem"></a>

### ESMallocMem()

`void * ESMallocMem ( size_t nbytes)`

| `nbytes`   | The number of bytes to allocate.   |
|------------|------------------------------------|

Provides a memory allocation routine to be used by JavaScript for managing memory associated
with the library’s objects.

Returns a pointer to the allocated block of memory.

---

<a id="shared-library-function-api"></a>

## Shared-library function API

Your shared-library C/C++ code defines its interface to JavaScript in two sets of functions, collected in
[SoServerInterface](#shared-library-soserverinterface) and [SoObjectInterface](#shared-library-soobjectinterface) function-pointer structures.
Return values from most functions are integer constants. The error code `kESErrOK == 0` indicates success.

<a id="shared-library-soserverinterface"></a>

### SoServerInterface

`SoServerInterface` is a structure of function pointers which enable the shared-library code to call

JavaScript objects. It is passed to the global ESClientInterface() function for initialization when the library is
loaded, and again for cleanup when the library is unloaded. Between these calls, your shared-library code
must store the structure and use it to access the communication functions.
You can store information for every object and class in your C code. The recommended method is to create
a data structure during the initialize() and free it during finalize(). You can then access that data with
setClientData() and getClientData().

The SoServerInterface structure contains these function pointers:

```default
SoServerInterface {
    SoServerDumpServer_f
    SoServerDumpObject_f

    dumpServer; //debugging, show server in console
    dumpObject; //debugging, show object in console

    SoServerAddClass_f

    addClass; //define a JS class

    SoServerAddMethod_f
    SoServerAddMethods_f
    SoServerAddProperty_f
    SoServerAddProperties_f

    addMethod; // define a method
    addMethods; // define a set of methods
    addProperty; // define a property
    addProperties; // define a set of properties

    SoServerGetClass_f
    SoServerGetServer_f

    getClass; // get class for an instance
    getServer; // get server for an instance

    SoServerSetClientData_f
    SoServerGetClientData_f

    setClientData; //set data in instance
    getClientData; //get data from instance

    SoServerEval_f
    eval; // call JavaScript interpreter
    SoServerTaggedDataInit_f taggedDataInit; // init tagged data
    SoServerTaggedDataFree_f taggedDataFree; // free tagged data
}
```

These functions allow your C/C++ shared library code to create, modify, and access JavaScript classes and
objects. The functions must conform to the following type definitions.

---

<a id="externalobject-functions-dumpserver"></a>

#### dumpServer()

`ESerror_t dumpServer (SoHServer hServer);`

| `hServer`   | The [Support structures](#sohserver) reference for this shared library, as passed to your global<br/>[ESClientInterface()](#externalobject-functions-esclientinterface) function on initialization.   |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Prints the contents of this server to the JavaScript Console in the ExtendScript Toolkit, for
debugging.

Returns an error code, `kESErrOK` on success.

---

<a id="externalobject-functions-dumpobject"></a>

#### dumpObject()

`ESerror_t dumpObject (SoHObject hObject);`

| `hObject`   | The [Support structures](#sohobject) reference for an instance of this class.   |
|-------------|---------------------------------------------------------------------------------|

Prints the contents of this object to the JavaScript Console in the ExtendScript Toolkit, for
debugging.

Returns an error code, `kESErrOK` on success.

---

<a id="externalobject-functions-addclass"></a>

#### addClass()

`ESerror_t addClass (SoHServer hServer, char* name, SoObjectInterface_p pObjectInterface);`

| `hServer`          | The [Support structures](#sohserver) reference for this shared library, as passed to your global<br/>[ESClientInterface()](#externalobject-functions-esclientinterface) function on initialization.   |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`             | String. The unique name of the new class. The name must begin with an<br/>uppercase alphabetic character.                                                                                             |
| `pObjectInterface` | A pointer to an [SoObjectInterface](#shared-library-soobjectinterface). A structure containing pointers to the<br/>object interface methods for instances of this class.                              |

Creates a new JavaScript class.

Returns an error code, `kESErrOK` on success.

---

<a id="externalobject-functions-addmethod"></a>

#### addMethod()

`ESerror_t addMethod (SoHObject hObject, const char* name, int id, char* desc);`

| `hObject`   | The [Support structures](#sohobject) reference for an instance of this class.   |
|-------------|---------------------------------------------------------------------------------|
| `name`      | String. The unique name of the new method.                                      |
| `id`        | Number. The unique identifier for the new method.                               |
| `desc`      | String. A descriptive string for the new method.                                |

Adds new method to an instance.

Returns an error code, `kESErrOK` on success.

---

<a id="externalobject-functions-addmethods"></a>

#### addMethods()

`ESerror_t addMethods (SoHObject hObject, SoCClientName_p pNames);`

| `hObject`   | The [Support structures](#sohobject) reference for an instance of this class.                                 |
|-------------|---------------------------------------------------------------------------------------------------------------|
| `pNames[]`  | [SoCClientName](#socclientname). A structure containing the names and identifiers of<br/>methods to be added. |

Adds a set of new methods to an instance.

Returns an error code, `kESErrOK` on success.

---

<a id="externalobject-functions-addproperty"></a>

#### addProperty()

`ESerror_t addProperty (SoHObject hObject, const char* name, int id, char* desc);`

| `hObject`   | The [Support structures](#sohobject) reference for an instance of this class.   |
|-------------|---------------------------------------------------------------------------------|
| `name`      | String. The unique name of the new property.                                    |
| `id`        | Number. The unique identifier for the new property.                             |
| `desc`      | String. Optional. A descriptive string for the new property, or null.           |

Adds new property to an instance.

Returns an error code, `kESErrOK` on success.

---

<a id="externalobject-functions-addproperties"></a>

#### addProperties()

`ESerror_t addProperties (SoHObject hObject, SoCClientName_p pNames);`

| `hObject`   | The [Support structures](#sohobject) reference for an instance of this class.                                    |
|-------------|------------------------------------------------------------------------------------------------------------------|
| `pNames[]`  | [SoCClientName](#socclientname). A structure containing the names and identifiers of<br/>properties to be added. |

Adds a set of new properties to an instance.

Returns an error code, `kESErrOK` on success.

---

<a id="externalobject-functions-getclass"></a>

#### getClass()

`ESerror_t getClass (SoHObject hObject, char* name, int name_l);`

| `hObject`   | The [Support structures](#sohobject) reference for an instance of this class.   |
|-------------|---------------------------------------------------------------------------------|
| `name`      | String. A buffer in which to return the unique name of the class.               |
| `name_1`    | Number. The size of the name buffer.                                            |

Retrieves this object’s parent class name.

Returns an error code, `kESErrOK` on success.

---

<a id="externalobject-functions-getserver"></a>

#### getServer()

`ESerror_t getServer (SoHObject hObject, SoHServer* phServer, SoServerInterface_p* ppServerInterface);`

| `hObject`           | The [Support structures](#sohobject) reference for an instance of this class.                                     |
|---------------------|-------------------------------------------------------------------------------------------------------------------|
| `phServer`          | A buffer in which to return the [Support structures](#sohserver) reference for this object.                       |
| `ppServerInterface` | A buffer in which to return the [SoObjectInterface](#shared-library-soobjectinterface) reference for this object. |

Retrieves the interface methods for this object, and the server object that manages it.

Returns an error code, `kESErrOK` on success.

---

<a id="externalobject-functions-setclientdata"></a>

#### setClientData()

`ESerror_t setClientData (SoHObject hObject, void* pData);`

| `hObject`   | The [Support structures](#sohobject) reference for an instance of this class.   |
|-------------|---------------------------------------------------------------------------------|
| `pData`     | A pointer to the library-defined data.                                          |

Sets your own data to be stored with an object.

Returns an error code, `kESErrOK` on success.

---

<a id="externalobject-functions-getclientdata"></a>

#### getClientData()

`ESerror_t setClientData (SoHObject hObject, void** pData);`

| `hObject`   | The [Support structures](#sohobject) reference for an instance of this class.   |
|-------------|---------------------------------------------------------------------------------|
| `pData`     | A buffer in which to return a pointer to the library-defined data.              |

Retrieves data that was stored with [setClientData()](#externalobject-functions-setclientdata).

Returns an error code, `kESErrOK` on success.

---

<a id="externalobject-functions-eval"></a>

#### eval()

`ESerror_t eval (SohServer hServer, char* string, TaggedData* pTaggedData);`

| `hServer`     | The [Support structures](#sohserver) reference for this shared library, as passed to your global<br/>[ESClientInterface()](#externalobject-functions-esclientinterface) function on initialization.   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `string`      | A string containing the JavaScript expression to evaluate.                                                                                                                                            |
| `pTaggedData` | A pointer to a [TaggedData](#taggeddata) object in which to return the result of evaluation.                                                                                                          |

Calls the JavaScript interpreter to evaluate a JavaScript expression.

Returns an error code, `kESErrOK` on success.

---

<a id="externalobject-functions-taggeddatainit"></a>

#### taggedDataInit()

`ESerror_t taggedDataInit (SoHSever hServer, TaggedData* pTaggedData);`

| `hServer`     | The [Support structures](#sohserver) reference for this shared library, as passed to your global<br/>[ESClientInterface()](#externalobject-functions-esclientinterface) function on initialization.   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `pTaggedData` | A pointer to a [TaggedData](#taggeddata).                                                                                                                                                             |

Initializes a TaggedData structure.

Returns an error code, `kESErrOK` on success.

---

<a id="externalobject-functions-taggeddatafree"></a>

#### taggedDataFree()

`ESerror_t setClientData (SoHServer hServer, TaggedData* pTaggedData);`

| `hServer`     | The [Support structures](#sohserver) reference for this shared library, as passed to your global<br/>[ESClientInterface()](#externalobject-functions-esclientinterface) function on initialization.   |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `pTaggedData` | A pointer to a [TaggedData](#taggeddata).                                                                                                                                                             |

Frees memory being used by a TaggedData structure.

Returns an error code, `kESErrOK` on success.

---

<a id="shared-library-soobjectinterface"></a>

### SoObjectInterface

When you add a JavaScript class with SoServerInterface.addClass(), you must provide this interface.
JavaScript calls the provided functions to interact with objects of the new class.
The SoObjectInterface is an array of function pointers defined as follows:

```default
SoObjectInterface {
    SoObjectInitialize_f initialize;
    SoObjectPut_f        put;
    SoObjectGet_f        get;
    SoObjectCall_f       call;
    SoObjectValueOf_f    valueOf;
    SoObjectToString_f   toString;
    SoObjectFinalize_f   finalize;
}
```

All `SoObjectInterface` members must be valid function pointers, or NULL. You must implement
`initialize()` and `finalize()`. The functions must conform to the following type definitions.

---

<a id="externalobject-functions-initialize"></a>

#### initialize()

`ESerror_t initialize (SoHObject hObject, int argc, TaggedData* argv);`

| `hObject`    | The [Support structures](#sohobject) reference for an instance of this class.                               |
|--------------|-------------------------------------------------------------------------------------------------------------|
| `argc, argv` | The number of and pointer to arguments passed to the constructor, in the form of [TaggedData](#taggeddata). |

Required. Called when JavaScript code instantiates this class with the new operator:

```default
var xx = New MyClass(arg1, ...)
```

The initialization function typically adds properties and methods to the object. Objects of the same
class can offer different properties and methods, which you can add with the [addMethod()](#externalobject-functions-addmethod) and
[addProperty()](#externalobject-functions-addproperty) functions in the stored SoServerInterface.

Returns an error code, `kESErrOK` on success.

---

<a id="externalobject-functions-put"></a>

#### put()

`ESerror_t put (SoHObject hObject, SoCClientName* name, TaggedData* pValue);`

| `hObject`   | The [Support structures](#sohobject) reference for an instance of this class.   |
|-------------|---------------------------------------------------------------------------------|
| `name`      | The name of the property, a pointer to an [SoCClientName](#socclientname).      |
| `pValue`    | The new value, a pointer to a [TaggedData](#taggeddata).                        |

Called when JavaScript code sets a property of this class:

```default
xx.myproperty = "abc" ;
```

If you provide `NULL` for this function, the JavaScript object is read-only.

Returns an error code, `kESErrOK` on success.

---

<a id="externalobject-functions-get"></a>

#### get()

`ESerror_t get (SoHObject hObject, SoCClientName* name, TaggedData* pValue);`

| `hObject`   | The [Support structures](#sohobject) reference for an instance of this class.   |
|-------------|---------------------------------------------------------------------------------|
| `name`      | The name of the property, a pointer to an [SoCClientName](#socclientname).      |
| `pValue`    | A buffer in which to return the property value, a [TaggedData](#taggeddata).    |

Called when JavaScript code accesses a property of this class:

```default
alert(xx.myproperty);
```

Returns an error code, `kESErrOK` on success.

---

<a id="externalobject-functions-call"></a>

#### call()

`ESerror_t call (SoHObject hObject, SoCClientName* name, int argc, TaggedData* argv, TaggedData* pResult);`

| `hObject`    | The [Support structures](#sohobject) reference for an instance of this class.                    |
|--------------|--------------------------------------------------------------------------------------------------|
| `name`       | The name of the property, a pointer to an [SoCClientName](#socclientname).                       |
| `argc, argv` | The number and pointer to arguments passed to the call, in the form of [TaggedData](#taggeddata) |
| `pResult`    | A buffer in which to return the result of the call, in the form of [TaggedData](#taggeddata)     |

Called when JavaScript code calls a method of this class:

```default
xx.mymethod()
```

Required in order for JavaScript to call any methods of this class.

Returns an error code, `kESErrOK` on success.

---

<a id="externalobject-functions-valueof"></a>

#### valueOf()

`ESerror_t valueOf (SoHObject hObject, TaggedData* pResult);`

| `hObject`   | The [Support structures](#sohobject) reference for an instance of this class.                 |
|-------------|-----------------------------------------------------------------------------------------------|
| `pResult`   | A buffer in which to return the result of the value, in the form of [TaggedData](#taggeddata) |

Creates and returns the value of the object, with no type conversion.

Returns an error code, `kESErrOK` on success.

---

<a id="externalobject-functions-tostring"></a>

#### toString()

`ESerror_t toString (SoHObject hObject, TaggedData* pResult);`

| `hObject`   | The [Support structures](#sohobject) reference for an instance of this class.                  |
|-------------|------------------------------------------------------------------------------------------------|
| `pResult`   | A buffer in which to return the result of the string, in the form of [TaggedData](#taggeddata) |

Creates and returns a string representing the value of this object.

Returns an error code, `kESErrOK` on success.

---

<a id="externalobject-functions-finalize"></a>

#### finalize()

`ESerror_t finalize (SoHObject hObject);`

| `hObject`   | The [Support structures](#sohobject) reference for an instance of this class.   |
|-------------|---------------------------------------------------------------------------------|

Required. Called when JavaScript deletes an instance of this class.
Use this function to free any memory you have allocated.

Returns an error code, `kESErrOK` on success.

---

<a id="sohobject"></a>

<a id="sohserver"></a>

<a id="support-structures"></a>

## Support structures

These support structures are passed to functions that you define for your JavaScript interface:

| `SoHObject`     | An opaque pointer `(long *)` to the C/C++ representation of a JavaScript object.                                |
|-----------------|-----------------------------------------------------------------------------------------------------------------|
| `SoHServer`     | An opaque pointer `(long *)` to the server object, which acts as an object factory for<br/>the shared library.  |
| `SoCClientName` | A structure that uniquely identifies methods and properties.                                                    |
| `TaggedData`    | A structure that encapsulates data values with type information, to be passed<br/>between C/C++ and JavaScript. |

<a id="socclientname"></a>

### SoCClientName

The SoCClientName data structure stores identifying information for methods and properties of
JavaScript objects created by shared-library C/C++ code. It is defined as follows:

```default
SoCClientName {
    char* name_sig ;
    uint32_t id ;
    char* desc ;
}
```

| `name_sig`   | The name of the property or method, unique within the class.<br/>Optionally contains a signature following an underscore, which identifies the types of<br/>arguments to methods; see Function signatures. When names are passed back to your<br/>SoObjectInterface functions, the signature portion is omitted.                       |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`         | A unique identifying number for the property or method, or 0 to assign a generated UID.<br/>If you assign the UID, your C/C++ code can use it to avoid string comparisons when<br/>identifying JavaScript properties and methods. It is recommended that you either assign all<br/>UIDs explicitly, or allow them all to be generated. |
| `desc`       | A descriptive string or `NULL`.                                                                                                                                                                                                                                                                                                        |

<a id="taggeddata"></a>

### TaggedData

The TaggedData structure is used to communicate data values between JavaScript and shared-library
C/C++ code. Types are automatically converted as appropriate:

```default
typedef struct {
    union {
        long intval;
        double fltval;
        char* string;
        SoHObject* hObject;
    } data;
    long type;
    long filler;
} TaggedData;
```

| `intval`   | Integer and boolean data values. Type is kTypeInteger, kTypeUInteger, or kTypeBool.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `fltval`   | Floating-point numeric data values. Type is kTypeDouble.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `string`   | String data values. All strings are UTF-8 encoded and null-terminated. Type is<br/>kTypeString or kTypeScript.<br/><br/>- The library must define an entry point [ESFreeMem()](defining-entry-points-for-direct-access.md#externalobject-functions-esfreemem),<br/>  which ExtendScript calls to release a returned string pointer.<br/>  If this entry point is missing, ExtendScript does not attempt to release any returned string data.<br/>- When a function returns a string of type kTypeScript, ExtendScript evaluates the<br/>  script and returns the result of evaluation as the result of the function call.                                                                                                          |
| `hObject`  | A C/C++ representation of a JavaScript object data value. Type is kTypeLiveObject or<br/>kTypeLiveObjectRelease.<br/><br/>- When a function returns an object of type kTypeLiveObject, ExtendScript does not<br/>  release the object.<br/>- When a function returns an object of type kTypeLiveObjectRelease, ExtendScript<br/>  releases the object.                                                                                                                                                                                                                                                                                                                                                                             |
| `type`     | The data type tag. One of:<br/><br/>- `kTypeUndefined`: a null value, equivalent of JavaScript `undefined`. The return value<br/>  for a function is always set to this by default.<br/>- `kTypeBool`: a boolean value, 0 for false, 1 for true.<br/>- `kTypeDouble`: a 64-bit floating-point number.<br/>- `kTypeString`: a character string.<br/>- `kTypeLiveObject`: a pointer to an internal representation of an object (SoHObject).<br/>- `kTypeLiveObjectRelease`: a pointer to an internal representation of an object (SoHObject).<br/>- `kTypeInteger`: a 32-bit signed integer value.<br/>- `kTypeUInteger`: a 32-bit unsigned integer value.<br/>- `kTypeScript`: a string containing an executable JavaScript script. |
| `filler`   | A 4-byte filler for 8-byte alignment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
