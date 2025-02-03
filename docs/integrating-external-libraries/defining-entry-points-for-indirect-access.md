# Defining entry points for indirect access

The C-client object interface for external libraries allows your C or C++ shared-library code to define, create, use, and manage JavaScript objects.

---

## Entry Points

The following entry points are required if you wish to use the object interface:

### ESClientInterface()

`int ESClientInterface (SoCClient_e kReason, SoServerInterface* pServer, SoHServer hServer)`

#### Description

Your library must define this global function in order to use the object interface to JavaScript. The function is called twice in each session, immediately upon loading the library, and again when unloading it.

#### Parameters

+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter |                                                                                                                              Description                                                                                                                               |
+===========+========================================================================================================================================================================================================================================================================+
| `kReason` | The reason for this call, one of these constants:                                                                                                                                                                                                                      |
|           |                                                                                                                                                                                                                                                                        |
|           | - `kSoCClient_init`: The function is being called for initialization upon load.                                                                                                                                                                                        |
|           | - `kSoCClient_term`.: The function is being called for termination upon unload.                                                                                                                                                                                        |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pServer` | A pointer to an [SoServerInterface](#shared-library-soserverinterface) containing function pointers for the entry points, which enable the shared-library code to call into JavaScript to create and access JavaScript classes and objects.                            |
|           |                                                                                                                                                                                                                                                                        |
|           | The shared-library code is responsible for storing this structure between the initialization and termination call, and retrieving it to access the functions.                                                                                                          |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `hServer` | An [Support structures](#sohserver) reference for this shared library. The server is an object factory that creates and manages [Support structures](#sohobject) objects.                                                                                              |
|           |                                                                                                                                                                                                                                                                        |
|           | The shared-library code is responsible for storing this structure between the initialization and termination calls. You must pass it to [taggedDataInit()](#externalobject-functions-taggeddatainit) and [taggedDataFree()](#externalobject-functions-taggeddatafree). |
+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### Returns

Returns an error code, `kESErrOK` on success.

---

### ESMallocMem()

`void * ESMallocMem (size_t nbytes)`

#### Description

Provides a memory allocation routine to be used by JavaScript for managing memory associated with the library's objects.

#### Parameters

| Parameter |           Description            |
| --------- | -------------------------------- |
| `nbytes`  | The number of bytes to allocate. |

#### Returns

A pointer to the allocated block of memory.

---

## Shared-library function API

Your shared-library C/C++ code defines its interface to JavaScript in two sets of functions, collected in [SoServerInterface](#shared-library-soserverinterface) and [SoObjectInterface](#shared-library-soobjectinterface) function-pointer structures.

Return values from most functions are integer constants. The error code `kESErrOK == 0` indicates success.

### SoServerInterface

`SoServerInterface` is a structure of function pointers which enable the shared-library code to call

JavaScript objects. It is passed to the global ESClientInterface() function for initialization when the library is loaded, and again for cleanup when the library is unloaded. Between these calls, your shared-library code must store the structure and use it to access the communication functions.

You can store information for every object and class in your C code. The recommended method is to create a data structure during the initialize() and free it during finalize(). You can then access that data with setClientData() and getClientData().

The SoServerInterface structure contains these function pointers:

```cpp
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

These functions allow your C/C++ shared library code to create, modify, and access JavaScript classes and objects. The functions must conform to the following type definitions.

#### dumpServer()

`ESerror_t dumpServer (SoHServer hServer);`

##### Description

Prints the contents of this server to the JavaScript Console in the ExtendScript Toolkit, for debugging.

##### Parameters

| Parameter |                                                                                           Description                                                                                           |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `hServer` | The [Support structures](#sohserver) reference for this shared library, as passed to your global [ESClientInterface()](#externalobject-functions-esclientinterface) function on initialization. |


##### Returns

Returns an error code, `kESErrOK` on success.

---

#### dumpObject()

`ESerror_t dumpObject (SoHObject hObject);`

##### Description

Prints the contents of this object to the JavaScript Console in the ExtendScript Toolkit, for debugging.

##### Parameters

| Parameter |                                  Description                                  |
| --------- | ----------------------------------------------------------------------------- |
| `hObject` | The [Support structures](#sohobject) reference for an instance of this class. |


##### Returns

Returns an error code, `kESErrOK` on success.

---

#### addClass()

`ESerror_t addClass (SoHServer hServer, char* name, SoObjectInterface_p pObjectInterface);`

##### Description

Creates a new JavaScript class.

##### Parameters

|     Parameter      |                                                                                           Description                                                                                           |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `hServer`          | The [Support structures](#sohserver) reference for this shared library, as passed to your global [ESClientInterface()](#externalobject-functions-esclientinterface) function on initialization. |
| `name`             | String. The unique name of the new class. The name must begin with an uppercase alphabetic character.                                                                                           |
| `pObjectInterface` | A pointer to an [SoObjectInterface](#shared-library-soobjectinterface). A structure containing pointers to the object interface methods for instances of this class.                            |

##### Returns

Returns an error code, `kESErrOK` on success.

---

#### addMethod()

`ESerror_t addMethod (SoHObject hObject, const char* name, int id, char* desc);`

##### Description

Adds new method to an instance.

##### Parameters

| Parameter |                                  Description                                  |
| --------- | ----------------------------------------------------------------------------- |
| `hObject` | The [Support structures](#sohobject) reference for an instance of this class. |
| `name`    | String. The unique name of the new method.                                    |
| `id`      | Number. The unique identifier for the new method.                             |
| `desc`    | String. A descriptive string for the new method.                              |

##### Returns

Returns an error code, `kESErrOK` on success.

---

#### addMethods()

`ESerror_t addMethods (SoHObject hObject, SoCClientName_p pNames);`

##### Description

Adds a set of new methods to an instance.

##### Parameters

| Parameter  |                                                Description                                                |
| ---------- | --------------------------------------------------------------------------------------------------------- |
| `hObject`  | The [Support structures](#sohobject) reference for an instance of this class.                             |
| `pNames[]` | [SoCClientName](#socclientname). A structure containing the names and identifiers of methods to be added. |

##### Returns

Returns an error code, `kESErrOK` on success.

---

#### addProperty()

`ESerror_t addProperty (SoHObject hObject, const char* name, int id, char* desc);`

##### Description

Adds new property to an instance.

##### Parameters

| Parameter |                                  Description                                  |
| --------- | ----------------------------------------------------------------------------- |
| `hObject` | The [Support structures](#sohobject) reference for an instance of this class. |
| `name`    | String. The unique name of the new property.                                  |
| `id`      | Number. The unique identifier for the new property.                           |
| `desc`    | String. Optional. A descriptive string for the new property, or null.         |

##### Returns

Returns an error code, `kESErrOK` on success.

---

#### addProperties()

`ESerror_t addProperties (SoHObject hObject, SoCClientName_p pNames);`

##### Description

Adds a set of new properties to an instance.

##### Parameters

| Parameter  |                                                 Description                                                  |
| ---------- | ------------------------------------------------------------------------------------------------------------ |
| `hObject`  | The [Support structures](#sohobject) reference for an instance of this class.                                |
| `pNames[]` | [SoCClientName](#socclientname). A structure containing the names and identifiers of properties to be added. |

##### Returns

Returns an error code, `kESErrOK` on success.

---

#### getClass()

`ESerror_t getClass (SoHObject hObject, char* name, int name_l);`

##### Description

Retrieves this object's parent class name.

##### Parameters

| Parameter |                                  Description                                  |
| --------- | ----------------------------------------------------------------------------- |
| `hObject` | The [Support structures](#sohobject) reference for an instance of this class. |
| `name`    | String. A buffer in which to return the unique name of the class.             |
| `name_1`  | Number. The size of the name buffer.                                          |

##### Returns

Returns an error code, `kESErrOK` on success.

---

#### getServer()

`ESerror_t getServer (SoHObject hObject, SoHServer* phServer, SoServerInterface_p* ppServerInterface);`

##### Description

Retrieves the interface methods for this object, and the server object that manages it.

##### Parameters

|      Parameter      |                                                    Description                                                    |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `hObject`           | The [Support structures](#sohobject) reference for an instance of this class.                                     |
| `phServer`          | A buffer in which to return the [Support structures](#sohserver) reference for this object.                       |
| `ppServerInterface` | A buffer in which to return the [SoObjectInterface](#shared-library-soobjectinterface) reference for this object. |

##### Returns

Returns an error code, `kESErrOK` on success.

---

#### setClientData()

`ESerror_t setClientData (SoHObject hObject, void* pData);`

##### Description

Sets your own data to be stored with an object.

##### Parameters

| Parameter |                                  Description                                  |
| --------- | ----------------------------------------------------------------------------- |
| `hObject` | The [Support structures](#sohobject) reference for an instance of this class. |
| `pData`   | A pointer to the library-defined data.                                        |

##### Returns

Returns an error code, `kESErrOK` on success.

---

#### getClientData()

`ESerror_t setClientData (SoHObject hObject, void** pData);`

##### Description

Retrieves data that was stored with [setClientData()](#externalobject-functions-setclientdata).

##### Parameters

| Parameter |                                  Description                                  |
| --------- | ----------------------------------------------------------------------------- |
| `hObject` | The [Support structures](#sohobject) reference for an instance of this class. |
| `pData`   | A buffer in which to return a pointer to the library-defined data.            |

##### Returns

Returns an error code, `kESErrOK` on success.

---

#### eval()

`ESerror_t eval (SohServer hServer, char* string, TaggedData* pTaggedData);`

##### Description

Calls the JavaScript interpreter to evaluate a JavaScript expression.

##### Parameters

|   Parameter   |                                                                                           Description                                                                                           |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `hServer`     | The [Support structures](#sohserver) reference for this shared library, as passed to your global [ESClientInterface()](#externalobject-functions-esclientinterface) function on initialization. |
| String        | A string containing the JavaScript expression to evaluate.                                                                                                                                      |
| `pTaggedData` | A pointer to a [TaggedData](#taggeddata) object in which to return the result of evaluation.                                                                                                    |


##### Returns

Returns an error code, `kESErrOK` on success.

---

#### taggedDataInit()

`ESerror_t taggedDataInit (SoHSever hServer, TaggedData* pTaggedData);`

##### Description

Initializes a TaggedData structure.

##### Parameters

|   Parameter   |                                                                                           Description                                                                                           |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `hServer`     | The [Support structures](#sohserver) reference for this shared library, as passed to your global [ESClientInterface()](#externalobject-functions-esclientinterface) function on initialization. |
| `pTaggedData` | A pointer to a [TaggedData](#taggeddata).                                                                                                                                                       |

##### Returns

Returns an error code, `kESErrOK` on success.

---

#### taggedDataFree()

`ESerror_t setClientData (SoHServer hServer, TaggedData* pTaggedData);`

##### Description

Frees memory being used by a TaggedData structure.

##### Parameters

|   Parameter   |                                                                                           Description                                                                                           |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `hServer`     | The [Support structures](#sohserver) reference for this shared library, as passed to your global [ESClientInterface()](#externalobject-functions-esclientinterface) function on initialization. |
| `pTaggedData` | A pointer to a [TaggedData](#taggeddata).                                                                                                                                                       |

##### Returns

Returns an error code, `kESErrOK` on success.

---

### SoObjectInterface

When you add a JavaScript class with SoServerInterface.addClass(), you must provide this interface. JavaScript calls the provided functions to interact with objects of the new class.

The SoObjectInterface is an array of function pointers defined as follows:

```cpp
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

All `SoObjectInterface` members must be valid function pointers, or NULL. You must implement `initialize()` and `finalize()`. The functions must conform to the following type definitions.

#### initialize()

`ESerror_t initialize (SoHObject hObject, int argc, TaggedData* argv);`

##### Description

Required. Called when JavaScript code instantiates this class with the new operator:

```javascript
var xx = New MyClass(arg1, ...)
```

The initialization function typically adds properties and methods to the object. Objects of the same class can offer different properties and methods, which you can add with the [addMethod()](#externalobject-functions-addmethod) and [addProperty()](#externalobject-functions-addproperty) functions in the stored SoServerInterface.

##### Parameters

|  Parameter   |                                                 Description                                                 |
| ------------ | ----------------------------------------------------------------------------------------------------------- |
| `hObject`    | The [Support structures](#sohobject) reference for an instance of this class.                               |
| `argc, argv` | The number of and pointer to arguments passed to the constructor, in the form of [TaggedData](#taggeddata). |

##### Returns

Returns an error code, `kESErrOK` on success.

---

#### put()

`ESerror_t put (SoHObject hObject, SoCClientName* name, TaggedData* pValue);`

##### Description

Called when JavaScript code sets a property of this class:

```javascript
xx.myproperty = "abc" ;
```

If you provide `NULL` for this function, the JavaScript object is read-only.

##### Parameters

| Parameter |                                  Description                                  |
| --------- | ----------------------------------------------------------------------------- |
| `hObject` | The [Support structures](#sohobject) reference for an instance of this class. |
| `name`    | The name of the property, a pointer to an [SoCClientName](#socclientname).    |
| `pValue`  | The new value, a pointer to a [TaggedData](#taggeddata).                      |

##### Returns

Returns an error code, `kESErrOK` on success.

---

#### get()

`ESerror_t get (SoHObject hObject, SoCClientName* name, TaggedData* pValue);`

##### Description

Called when JavaScript code accesses a property of this class:

```javascript
alert(xx.myproperty);
```

##### Parameters

| Parameter |                                  Description                                  |
| --------- | ----------------------------------------------------------------------------- |
| `hObject` | The [Support structures](#sohobject) reference for an instance of this class. |
| `name`    | The name of the property, a pointer to an [SoCClientName](#socclientname).    |
| `pValue`  | A buffer in which to return the property value, a [TaggedData](#taggeddata).  |

##### Returns

Returns an error code, `kESErrOK` on success.

---

#### call()

`ESerror_t call (SoHObject hObject, SoCClientName* name, int argc, TaggedData* argv, TaggedData* pResult);`

##### Description

Called when JavaScript code calls a method of this class:

```javascript
xx.mymethod()
```

Required in order for JavaScript to call any methods of this class.

##### Parameters

|  Parameter   |                                           Description                                            |
| ------------ | ------------------------------------------------------------------------------------------------ |
| `hObject`    | The [Support structures](#sohobject) reference for an instance of this class.                    |
| `name`       | The name of the property, a pointer to an [SoCClientName](#socclientname).                       |
| `argc, argv` | The number and pointer to arguments passed to the call, in the form of [TaggedData](#taggeddata) |
| `pResult`    | A buffer in which to return the result of the call, in the form of [TaggedData](#taggeddata)     |

##### Returns

Returns an error code, `kESErrOK` on success.

---

#### valueOf()

`ESerror_t valueOf (SoHObject hObject, TaggedData* pResult);`

##### Description

Creates and returns the value of the object, with no type conversion.

##### Parameters

| Parameter |                                          Description                                          |
| --------- | --------------------------------------------------------------------------------------------- |
| `hObject` | The [Support structures](#sohobject) reference for an instance of this class.                 |
| `pResult` | A buffer in which to return the result of the value, in the form of [TaggedData](#taggeddata) |

##### Returns

Returns an error code, `kESErrOK` on success.

---

#### toString()

`ESerror_t toString (SoHObject hObject, TaggedData* pResult);`

##### Description

Creates and returns a string representing the value of this object.

##### Parameters

| Parameter |                                          Description                                           |
| --------- | ---------------------------------------------------------------------------------------------- |
| `hObject` | The [Support structures](#sohobject) reference for an instance of this class.                  |
| `pResult` | A buffer in which to return the result of the string, in the form of [TaggedData](#taggeddata) |


##### Returns

Returns an error code, `kESErrOK` on success.

---

#### finalize()

`ESerror_t finalize (SoHObject hObject);`

##### Description

Required. Called when JavaScript deletes an instance of this class.

Use this function to free any memory you have allocated.

##### Parameters

| Parameter |                                  Description                                  |
| --------- | ----------------------------------------------------------------------------- |
| `hObject` | The [Support structures](#sohobject) reference for an instance of this class. |

##### Returns

Returns an error code, `kESErrOK` on success.

---

## Support structures

These support structures are passed to functions that you define for your JavaScript interface:

#### Parameters

|    Parameter    |                                                 Description                                                 |
| --------------- | ----------------------------------------------------------------------------------------------------------- |
| `SoHObject`     | An opaque pointer `(long *)` to the C/C++ representation of a JavaScript object.                            |
| `SoHServer`     | An opaque pointer `(long *)` to the server object, which acts as an object factory for the shared library.  |
| `SoCClientName` | A structure that uniquely identifies methods and properties.                                                |
| `TaggedData`    | A structure that encapsulates data values with type information, to be passed between C/C++ and JavaScript. |

### SoCClientName

The SoCClientName data structure stores identifying information for methods and properties of JavaScript objects created by shared-library C/C++ code. It is defined as follows:

```cpp
SoCClientName {
    char* name_sig ;
    uint32_t id ;
    char* desc ;
}
```

#### Parameters

| Parameter  |                                                                                                                                                        Description                                                                                                                                                         |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name_sig` | The name of the property or method, unique within the class. Optionally contains a signature following an underscore, which identifies the types of arguments to methods; see Function signatures. When names are passed back to your SoObjectInterface functions, the signature portion is omitted.                       |
| `id`       | A unique identifying number for the property or method, or 0 to assign a generated UID. If you assign the UID, your C/C++ code can use it to avoid string comparisons when identifying JavaScript properties and methods. It is recommended that you either assign all UIDs explicitly, or allow them all to be generated. |
| `desc`     | A descriptive string or `NULL`.                                                                                                                                                                                                                                                                                            |

---

### TaggedData

The TaggedData structure is used to communicate data values between JavaScript and shared-library C/C++ code. Types are automatically converted as appropriate:

```cpp
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

#### Parameters

+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter |                                                                                                                                               Description                                                                                                                                                |
+===========+==========================================================================================================================================================================================================================================================================================================+
| `intval`  | Integer and boolean data values. Type is `kTypeInteger`, `kTypeUInteger`, or `kTypeBool`.                                                                                                                                                                                                                |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `fltval`  | Floating-point numeric data values. Type is `kTypeDouble`.                                                                                                                                                                                                                                               |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| String    | String data values. All strings are UTF-8 encoded and null-terminated. Type is `kTypeString` or `kTypeScript`.                                                                                                                                                                                           |
|           |                                                                                                                                                                                                                                                                                                          |
|           | - The library must define an entry point [ESFreeMem()](defining-entry-points-for-direct-access.md#externalobject-functions-esfreemem), which ExtendScript calls to release a returned string pointer. If this entry point is missing, ExtendScript does not attempt to release any returned string data. |
|           | - When a function returns a string of type kTypeScript, ExtendScript evaluates the script and returns the result of evaluation as the result of the function call.                                                                                                                                       |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `hObject` | A C/C++ representation of a JavaScript object data value. Type is `kTypeLiveObject` or `kTypeLiveObjectRelease`.                                                                                                                                                                                         |
|           |                                                                                                                                                                                                                                                                                                          |
|           | - When a function returns an object of type kTypeLiveObject, ExtendScript does not release the object.                                                                                                                                                                                                   |
|           | - When a function returns an object of type kTypeLiveObjectRelease, ExtendScript releases the object.                                                                                                                                                                                                    |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `type`    | The data type tag. One of:                                                                                                                                                                                                                                                                               |
|           |                                                                                                                                                                                                                                                                                                          |
|           | - `kTypeUndefined`: a null value, equivalent of JavaScript `undefined`. The return value for a function is always set to this by default.                                                                                                                                                                |
|           | - `kTypeBool`: a boolean value, 0 for false, 1 for true.                                                                                                                                                                                                                                                 |
|           | - `kTypeDouble`: a 64-bit floating-point number.                                                                                                                                                                                                                                                         |
|           | - `kTypeString`: a character string.                                                                                                                                                                                                                                                                     |
|           | - `kTypeLiveObject`: a pointer to an internal representation of an object (SoHObject).                                                                                                                                                                                                                   |
|           | - `kTypeLiveObjectRelease`: a pointer to an internal representation of an object (SoHObject).                                                                                                                                                                                                            |
|           | - `kTypeInteger`: a 32-bit signed integer value.                                                                                                                                                                                                                                                         |
|           | - `kTypeUInteger`: a 32-bit unsigned integer value.                                                                                                                                                                                                                                                      |
|           | - `kTypeScript`: a string containing an executable JavaScript script.                                                                                                                                                                                                                                    |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `filler`  | A 4-byte filler for 8-byte alignment.                                                                                                                                                                                                                                                                    |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
