# Defining entry points for direct access

A library to be loaded and accessed directly through an [ExternalObject instance](./externalobject-object.md) must publish the following entry points.

!!! note
    These must be exported as C functions, not C++ functions

---

## Entry Points

The following entry points are required if you wish to use an [ExternalObject instance](./externalobject-object.md):

### ESInitialize()

`char* ESInitialize (TaggedData* argv, long argc);`

#### Description

Called when your library is loaded into memory.

#### Parameters

|  Parameter   |                                         Description                                          |
| ------------ | -------------------------------------------------------------------------------------------- |
| `argv, argc` | The pointer to and number of arguments passed to the constructor, in the form of TaggedData. |

#### Returns

A string of function signatures; see [Library initialization](#library-initialization).

---

### ESGetVersion()

`long ESGetVersion (void );`

#### Description

Takes no arguments, and returns a version number for the library as a long integer.

The result is available in JavaScript as ExternalObject.version.

#### Returns

Long integer

---

### ESFreeMem()

`void ESFreeMem (void* p);`

#### Description

Called to free memory allocated for a null-terminated string passed to or from library functions.

| Parameter |       Description        |
| --------- | ------------------------ |
| `p`       | A pointer to the string. |

#### Returns

Nothing

---

### ESTerminate()

`void ESTerminate (void );`

#### Description

Called when your library is being unloaded. See [Library termination](#library-termination).

#### Returns

Nothing

---

## Additional functions

The shared library can contain any number of additional functions. Each function corresponds to a JavaScript method in the [ExternalObject instance](./externalobject-object.md). If a function is undefined, ExtendScript throws a run-time error.

Each function must accept the following arguments:

- An array of [TaggedData](defining-entry-points-for-indirect-access.md#taggeddata).
- An argument count.
- A variant data structure that takes the return value.

The variant data does not support JavaScript objects. The following data types are allowed:

- `undefined`
- Boolean
- `double`
- String - Must be UTF-8 encoded. The library must define an entry point [ESFreeMem()](#esfreemem), which ExtendScript calls to release a returned string pointer. If this entry point is missing, ExtendScript does not attempt to release any returned string data.
- `Script` - A string to be evaluated by ExtendScript. Use to return small JavaScript scripts that define arbitrarily complex data.

If, when a function is invoked, a supplied parameter is undefined, ExtendScript sets the data type to `undefined` and does not attempt to convert the data to the requested type.

!!! note
    The data type of a return value cannot be predefined; JavaScript functions can return any data type.

    The called function is free to return any of the listed data types.

---

## Library initialization

ExtendScript calls [ESInitialize()](#esinitialize) to initialize the library.

The function receives an argument vector containing the additional arguments passed in to the ExternalObject constructor.

The function can return an array of function name-signature strings, which are used to support the ExtendScript reflection interface, and to cast function arguments to specific types. You do not need to define a signature for a function in order to make it callable in JavaScript.

### Function signatures

If you choose to return a set of function name-signature strings, each string associates a function name with that function's parameter types, if any. For example:

```javascript
["functionName1_argtypes", "functionName2_argtypes", "functionName3"]
```

For each function, the string begins with the function name, followed by an underscore character and a list of argument data types, represented as a single character for each argument. If the function does not have arguments, you can omit the trailing underscore character (unless there is an underscore in the function name).

The characters that indicate data types are:

| Characeter |                                                       Description                                                       |
| ---------- | ----------------------------------------------------------------------------------------------------------------------- |
| `a`        | Any type. The argument is not converted. This is the default, if no type is supplied or if a type code is unrecognized. |
| `b`        | Boolean                                                                                                                 |
| `d`        | signed 32 bit integer                                                                                                   |
| `u`        | unsigned 32 bit integer                                                                                                 |
| `f`        | 64 bit floating point                                                                                                   |
| `s`        | String                                                                                                                  |

For example, suppose your library defines these two entry points:

```javascript
One (Integer a, String b);
Two ();
```

The signature strings for these two functions would be `"One_ds"`, `"Two"`.

!!! warning
    You cannot define function overloading by returning multiple different signatures for one function.

    Attempting to do so produces undefined results.

---

## Library termination

Define the entry point [ESInitialize()](#esinitialize) to free any memory you have allocated when your library is unloaded.

Whenever a JavaScript function makes a call to a library function, it increments a reference count for that library. When the reference count for a library reaches 0, the library is automatically unloaded; your termination function is called, and the `ExternalObject` instance is deleted. Note that deleting the `ExternalObject` instance does not unload the library if there are remaining references.
