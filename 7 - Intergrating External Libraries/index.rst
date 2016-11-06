Integrating External Libraries
You can extend the JavaScript DOM for an application by writing a C or C++ shared library, compiling it for
the platform you are using, and loading it into JavaScript as an ExternalObject object. A shared library is
implemented by a DLL in Windows, a bundle or framework in Mac OS, or a SharedObject in UNIX.
You can access the library functions directly through the ExternalObject instance, or you can define an
interface that allows your C/C++ code to create and access JavaScript classes and objects.
All Adobe Creative Suite 4 applications support this feature.
Example code
The sample code distributed with the Adobe ExtendScript SDK includes an example that demonstrates
how write a C/C++ shared library to be integrated with JavaScript. It is in the directory:
sdkInstall/sdksamples/cpp/

The sample shows how to write a plug-in for Adobe Bridge in C/C++, using the ExternalObject
mechanism, which enables the C/C++ code to be called from the JavaScript context. Project files for
Microsoft Visual Studio 2005 and XCode 2.4 are included in subfolders of
sdkInstall/sdksamples/cpp/build.

Loading and using shared libraries
To load an external shared library into JavaScript, create a new ExternalObject object. The instance acts as
a container and manager for the JavaScript interface to the library. It provides a logging facility that prints
status information to the JavaScript Console in the ExtendScript Toolkit, to help you debug your external
library use.
Once the library has been loaded, its exported symbols become available to JavaScript. In your JavaScript
code, you can call the functions defined in the library directly in the ExternalObject instance, or indirectly
through library-defined object types.
Direct access to library calls through the ExternalObject instance - Use the direct-access style
for C-language libraries. For each function defined in the C library, there is a corresponding method in
the ExternalObject object. You can pass data to these methods and receive the return value directly.
For example:
mylib = new ExternalObject ("lib:" + samplelib); // load the library
alert(mylib.version) ;
// access functions directly from ExternalObject instance
var a = mylib.method_abc(1,2.0,true, "this is data") ;
alert(a) ;
mylib.unload() ;

For details of how to define functions for direct access through the ExternalObject object, see
"Defining entry points for direct access" on page 203.
Indirect access to library calls through JavaScript classes - Use the indirect style to access classes
defined in a C++ library. For each C++ class defined in the library, a corresponding JavaScript class is

200

CHAPTER 7: Integrating External Libraries

ExternalObject object

201

automatically defined, and you can access the properties and methods through an instance of that
class. For example:
anotherlib= new ExternalObject ("lib:" + filespec); // load the library
alert(anotherlib.version) ;
// instantiate library-defined class
var myObject = new MyNewClass() ;
// access functions from instance
var a = myObject.method_abc(1,2.0,true,"this is data") ;
alert(a) ;
anotherlib.unload() ;

For details of how to define functions for direct access through the ExternalObject object, see
"Defining entry points for indirect access" on page 206.

ExternalObject object
You specify the name of the library in the constructor. The constructor searches for the named library
using the paths defined in the static property ExternalObject.searchFolders.
If you are having difficulty loading your library as an ExternalObject, set the property
ExternalObject.log to true, then call ExternalObject.search('lib:myLibrary'). This function
performs the search, and the log reports the paths that have been searched to the ExtendScript Toolkit
Console.
Before loading the library, the current folder is temporarily switched to the location of the found
executable file.
In Mac OS, the current directory is set to the bundle or framework folder for the library.
In Windows and UNIX, the current directory is set to the folder that contains the library.

ExternalObject constructor
obj = new ExternalObject ("lib:" + filespec, arg1, ...argn);
filespec

The specifier "lib:" is case sensitive, and serves as the marker for dynamic libraries.
Concatenate this to the base name of the shared library, with or without an extension.
ExtendScript appends a file extension if necessary, according to the operating system:
.dll in Windows
.bundle or .framework in Mac OS (only Mach-O bundles are supported)
.so in UNIX (except for HP/UX, where the extension is .sl )

The name of the library is case sensitive in UNIX.
arg1...argn

Optional. Any number of arguments to pass to the library’s initialization routine.

For example:
var mylib = new ExternalObject( "lib:myLibrary" );

CHAPTER 7: Integrating External Libraries

ExternalObject object

202

ExternalObject class properties
The ExternalObject class provides these static properties:
log

Boolean

Set to true to write status information to standard output (the
JavaScript Console in the ExtendScript Toolkit). Set to false to turn
logging off. Default is false.

searchFolders

String

A set of alternate paths in which to search for the shared library files, a
single string with multiple path specifications delimited by semicolons
(;). Paths can be absolute or relative to the Folder.startup location.
Default value is:
In Windows, "Plugins;Plug-Ins;."
In Mac OS,
"Plugins;Plug-Ins;Frameworks;.;../../../Plugins;
../../../Plug-ins;../../../Frameworks;../../..;"

In UNIX, "Plugins;Plug-Ins;plugins;."
version

Number

The version of the library, as returned by ESGetVersion().

ExternalObject class function
The ExternalObject class provides this static function to help debug problems with loading libraries as
external objects:
search()
ExternalObject.search (spec)
spec

String. The file specification for the compiled library, with or without path information.

Reports whether a compiled C/C++ library can be found, but does not load it. If logging is on, the
paths searched are reported to the JavaScript Console in the ExtendScript Toolkit.
Returns true if the library is found, false otherwise.

ExternalObject instance function
terminate()
ExternalObject_obj.terminate ()

Explicitly shuts down the ExternalObject dynamic library wrapped by this instance.
It can be helpful to force a shutdown of the external library if termination of external libraries during
the shutdown of the hosting application does not occur in the correct order.
Returns undefined.

CHAPTER 7: Integrating External Libraries

Defining entry points for direct access

Defining entry points for direct access
A library to be loaded and accessed directly through an ExternalObject instance must publish the
following entry points. These must be exported as C functions, not C++ functions:
ESInitialize()
char* ESInitialize (TaggedData* argv, long argc);
argv, argc

The pointer to and number of arguments passed to the constructor, in the form of
TaggedData.

Called when your library is loaded into memory.
Returns a string of function signatures; see "Library initialization" on page 204.
ESGetVersion()
long ESGetVersion (void );

Takes no arguments, and returns a version number for the library as a long integer. The result is
available in JavaScript as ExternalObject.version.
ESFreeMem()
void ESFreeMem (void* p);
p

A pointer to the string.

Called to free memory allocated for a null-terminated string passed to or from library functions.
Returns nothing.
ESTerminate()
void ESTerminate (void );

Called when your library is being unloaded. See "Library termination" on page 205.
Takes no arguments, and returns nothing.

Additional functions
The shared library can contain any number of additional functions. Each function corresponds to a
JavaScript method in the ExternalObject instance. If a function is undefined, ExtendScript throws a
run-time error.
Each function must accept the following arguments:
An array of TaggedData.
An argument count.
A variant data structure that takes the return value.
The variant data does not support JavaScript objects. The following data types are allowed:
undefined
Boolean
double

203

CHAPTER 7: Integrating External Libraries

Defining entry points for direct access

204

string - Must be UTF-8 encoded.

The library must define an entry point ESFreeMem(), which ExtendScript calls to release a returned
string pointer. If this entry point is missing, ExtendScript does not attempt to release any returned
string data.
Script - A string to be evaluated by ExtendScript. Use to return small JavaScript scripts that define

arbitrarily complex data.

If, when a function is invoked, a supplied parameter is undefined, ExtendScript sets the data type to
undefined and does not attempt to convert the data to the requested type.
NOTE: The data type of a return value cannot be predefined; JavaScript functions can return any data type.
The called function is free to return any of the listed data types.

Library initialization
ExtendScript calls ESInitialize() to initialize the library.
The function receives an argument vector containing the additional arguments passed in to the
ExternalObject constructor.
The function can return an array of function name-signature strings, which are used to support the
ExtendScript reflection interface, and to cast function arguments to specific types. You do not need to
define a signature for a function in order to make it callable in JavaScript.

Function signatures
If you choose to return a set of function name-signature strings, each string associates a function name
with that function’s parameter types, if any. For example:
["functionName1_argtypes", "functionName2_argtypes", "functionName3"]

For each function, the string begins with the function name, followed by an underscore character and a list
of argument data types, represented as a single character for each argument. If the function does not have
arguments, you can omit the trailing underscore character (unless there is an underscore in the function
name).
The characters that indicate data types are:
a

Any type. The argument is not converted. This is the default, if no type is supplied or if a type
code is unrecognized.

b

Boolean

d

signed 32 bit integer

u

unsigned 32 bit integer

f

64 bit floating point

s

String

CHAPTER 7: Integrating External Libraries

Defining entry points for direct access

205

For example, suppose your library defines these two entry points:
One (Integer a, String b);
Two ();

The signature strings for these two functions would be "One_ds", "Two".
NOTE: You cannot define function overloading by returning multiple different signatures for one function.
Attempting to do so produces undefined results.

Library termination
Define the entry point ESTerminate() to free any memory you have allocated when your library is
unloaded.
Whenever a JavaScript function makes a call to a library function, it increments a reference count for that
library. When the reference count for a library reaches 0, the library is automatically unloaded; your
termination function is called, and the ExternalObject instance is deleted. Note that deleting the
ExternalObject instance does not unload the library if there are remaining references.

CHAPTER 7: Integrating External Libraries

Defining entry points for indirect access

206

Defining entry points for indirect access
The C-client object interface for external libraries allows your C or C++ shared-library code to define,
create, use, and manage JavaScript objects.
The following entry points are required if you wish to use the object interface:
ESClientInterface()
int ESClientInterface (SoCClient_e kReason, SoServerInterface* pServer,
SoHServer hServer)
kReason

The reason for this call, one of these constants:
kSoCClient_init: The function is being called for initialization upon load.
kSoCClient_term.: The function is being called for termination upon unload.

pServer

A pointer to an SoServerInterface containing function pointers for the entry points,
which enable the shared-library code to call into JavaScript to create and access
JavaScript classes and objects.
The shared-library code is responsible for storing this structure between the
initialization and termination call, and retrieving it to access the functions.

hServer

An SoHServer reference for this shared library. The server is an object factory that
creates and manages SoHObject objects.
The shared-library code is responsible for storing this structure between the
initialization and termination calls. You must pass it to taggedDataInit() and
taggedDataFree().

Your library must define this global function in order to use the object interface to JavaScript. The
function is called twice in each session, immediately upon loading the library, and again when
unloading it.
Returns an error code, kESErrOK on success.
ESMallocMem()
void * ESMallocMem ( size_t nbytes)
nbytes

The number of bytes to allocate.

Provides a memory allocation routine to be used by JavaScript for managing memory associated
with the library’s objects.
Returns a pointer to the allocated block of memory.

Shared-library function API
Your shared-library C/C++ code defines its interface to JavaScript in two sets of functions, collected in
SoServerInterface and SoObjectInterface function-pointer structures.
Return values from most functions are integer constants. The error code kESErrOK == 0 indicates success.

CHAPTER 7: Integrating External Libraries

Defining entry points for indirect access

207

SoServerInterface
SoServerInterface is a structure of function pointers which enable the shared-library code to call

JavaScript objects. It is passed to the global ESClientInterface() function for initialization when the library is
loaded, and again for cleanup when the library is unloaded. Between these calls, your shared-library code
must store the structure and use it to access the communication functions.
You can store information for every object and class in your C code. The recommended method is to create
a data structure during the initialize() and free it during finalize(). You can then access that data with
setClientData() and getClientData().
The SoServerInterface structure contains these function pointers:
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

These functions allow your C/C++ shared library code to create, modify, and access JavaScript classes and
objects. The functions must conform to the following type definitions.
dumpServer()
ESerror_t dumpServer (SoHServer hServer);
hServer

The SoHServer reference for this shared library, as passed to your global
ESClientInterface() function on initialization.

Prints the contents of this server to the JavaScript Console in the ExtendScript Toolkit, for
debugging.
Returns an error code, kESErrOK on success.
dumpObject()
ESerror_t dumpObject (SoHObject hObject);
hObject

The SoHObject reference for an instance of this class.

Prints the contents of this object to the JavaScript Console in the ExtendScript Toolkit, for
debugging.
Returns an error code, kESErrOK on success.

CHAPTER 7: Integrating External Libraries

Defining entry points for indirect access

addClass()
ESerror_t addClass (SoHServer hServer, char* name,
SoObjectInterface_p pObjectInterface);
hServer

The SoHServer reference for this shared library, as passed to your global
ESClientInterface() function on initialization.

name

String. The unique name of the new class. The name must begin with an
uppercase alphabetic character.

pObjectInterface

A pointer to an SoObjectInterface. A structure containing pointers to the
object interface methods for instances of this class.

Creates a new JavaScript class.
Returns an error code, kESErrOK on success.
addMethod()
ESerror_t addMethod (SoHObject hObject, const char* name, int id, char* desc);
hObject

The SoHObject reference for an instance of this class.

name

String. The unique name of the new method.

id

Number. The unique identifier for the new method.

desc

String. A descriptive string for the new method.

Adds new method to an instance.
Returns an error code, kESErrOK on success.
addMethods()
ESerror_t addMethods (SoHObject hObject, SoCClientName_p pNames);
hObject

The SoHObject reference for an instance of this class.

pNames[]

SoCClientName. A structure containing the names and identifiers of
methods to be added.

Adds a set of new methods to an instance.
Returns an error code, kESErrOK on success.
addProperty()
ESerror_t addProperty (SoHObject hObject, const char* name, int id, char* desc);
hObject

The SoHObject reference for an instance of this class.

name

String. The unique name of the new property.

id

Number. The unique identifier for the new property.

desc

String. Optional. A descriptive string for the new property, or null.

Adds new property to an instance.
Returns an error code, kESErrOK on success.

208

CHAPTER 7: Integrating External Libraries

Defining entry points for indirect access

addProperties()
ESerror_t addProperties (SoHObject hObject, SoCClientName_p pNames);
hObject

The SoHObject reference for an instance of this class.

pNames[]

SoCClientName. A structure containing the names and identifiers of
properties to be added.

Adds a set of new properties to an instance.
Returns an error code, kESErrOK on success.
getClass()
ESerror_t getClass (SoHObject hObject, char* name, int name_l);
hObject

The SoHObject reference for an instance of the class.

name

String. A buffer in which to return the unique name of the class.

name_l

Number. The size of the name buffer.

Retrieves this object’s parent class name.
Returns an error code, kESErrOK on success.
getServer()
ESerror_t getServer (SoHObject hObject, SoHServer* phServer,
SoServerInterface_p* ppServerInterface);
hObject

The SoHObject reference for an instance of the class.

phServer

A buffer in which to return theSoHServer reference for this object.

ppServerInterface

A buffer in which to return the SoServerInterface reference for this object.

Retrieves the interface methods for this object, and the server object that manages it.
Returns an error code, kESErrOK on success.
setClientData()
ESerror_t setClientData (SoHObject hObject, void* pData);
hObject

The SoHObject reference for an instance of the class.

pData

A pointer to the library-defined data.

Sets your own data to be stored with an object.
Returns an error code, kESErrOK on success.
getClientData()
ESerror_t setClientData (SoHObject hObject, void** pData);
hObject

The SoHObject reference for an instance of the class.

pData

A buffer in which to return a pointer to the library-defined data.

Retrieves data that was stored with setClientData().
Returns an error code, kESErrOK on success.

209

CHAPTER 7: Integrating External Libraries

Defining entry points for indirect access

210

eval()
ESerror_t eval (SohServer hServer, char* string, TaggedData* pTaggedData);
hServer

The SoHServer reference for this shared library, as passed to your global
ESClientInterface() function on initialization.

string

A string containing the JavaScript expression to evaluate.

pTaggedData

A pointer to a TaggedData object in which to return the result of evaluation.

Calls the JavaScript interpreter to evaluate a JavaScript expression.
Returns an error code, kESErrOK on success.
taggedDataInit()
ESerror_t taggedDataInit (SoHSever hServer, TaggedData* pTaggedData);
hServer

The SoHServer reference for this shared library, as passed to your global
ESClientInterface() function on initialization.

pTaggedData

A pointer to the TaggedData.

Initializes a TaggedData structure.
Returns an error code, kESErrOK on success.
taggedDataFree()
ESerror_t setClientData (SoHServer hServer, TaggedData* pTaggedData);
hServer

The SoHServer reference for this shared library, as passed to your global
ESClientInterface() function on initialization.

pTaggedData

A pointer to the TaggedData.

Frees memory being used by a TaggedData structure.
Returns an error code, kESErrOK on success.

SoObjectInterface
When you add a JavaScript class with SoServerInterface.addClass(), you must provide this interface.
JavaScript calls the provided functions to interact with objects of the new class.
The SoObjectInterface is an array of function pointers defined as follows:
SoObjectInterface {
SoObjectInitialize_f
SoObjectPut_f
SoObjectGet_f
SoObjectCall_f
SoObjectValueOf_f
SoObjectToString_f
SoObjectFinalize_f
}

initialize;
put;
get;
call;
valueOf;
toString;
finalize;

CHAPTER 7: Integrating External Libraries

Defining entry points for indirect access

211

All SoObjectInterface members must be valid function pointers, or NULL. You must implement
initialize() and finalize(). The functions must conform to the following type definitions.
initialize()
ESerror_t initialize (SoHObject hObject, int argc, TaggedData* argv);
hObject

The SoHObject reference for this instance.

argc, argv

The number of and pointer to arguments passed to the constructor, in the form of
TaggedData.

Required. Called when JavaScript code instantiates this class with the new operator:
var xx = New MyClass(arg1, ...)

The initialization function typically adds properties and methods to the object. Objects of the same
class can offer different properties and methods, which you can add with the addMethod() and
addProperty() functions in the stored SoServerInterface.
Returns an error code, kESErrOK on success.
put()
ESerror_t put (SoHObject hObject, SoCClientName* name, TaggedData* pValue);
hObject

The SoHObject reference for this instance.

name

The name of the property, a pointer to an SoCClientName.

pValue

The new value, a pointer to a TaggedData.

Called when JavaScript code sets a property of this class:
xx.myproperty = "abc" ;

If you provide NULL for this function, the JavaScript object is read-only.
Returns an error code, kESErrOK on success.
get()
ESerror_t get (SoHObject hObject, SoCClientName* name, TaggedData* pValue);
hObject

The SoHObject reference for this instance.

name

The name of the property, a pointer to an SoCClientName.

pValue

A buffer in which to return the property value, a TaggedData.

Called when JavaScript code accesses a property of this class:
alert(xx.myproperty);

Returns an error code, kESErrOK on success.

CHAPTER 7: Integrating External Libraries

Defining entry points for indirect access

212

call()
ESerror_t call (SoHObject hObject, SoCClientName* name, int argc, TaggedData* argv,
TaggedData* pResult);
hObject

The SoHObject reference for this instance.

name

The name of the method, an SoCClientName.

argc, argv

The number and pointer to arguments passed to the call, in the form of TaggedDatas.

pResult

A buffer in which to return the result of the call, in the form of TaggedDatas.

Called when JavaScript code calls a method of this class:
xx.mymethod()

Required in order for JavaScript to call any methods of this class.
Returns an error code, kESErrOK on success.
valueOf()
ESerror_t valueOf (SoHObject hObject, TaggedData* pResult);
hObject

The SoHObject reference for this instance.

pResult

A buffer in which to return the result of the value, in the form of TaggedDatas.

Creates and returns the value of the object, with no type conversion.
Returns an error code, kESErrOK on success.
toString()
ESerror_t toString (SoHObject hObject, TaggedData* pResult);
hObject

The SoHObject reference for this instance.

pResult

A buffer in which to return the result of the string, in the form of TaggedDatas.

Creates and returns a string representing the value of this object.
Returns an error code, kESErrOK on success.
finalize()
ESerror_t finalize (SoHObject hObject);
hObject

The SoHObject reference for this instance.

Required. Called when JavaScript deletes an instance of this class. Use this function to free any
memory you have allocated.
Returns an error code, kESErrOK on success.

CHAPTER 7: Integrating External Libraries

Defining entry points for indirect access

213

Support structures
These support structures are passed to functions that you define for your JavaScript interface:
SoHObject

An opaque pointer (long *) to the C/C++ representation of a JavaScript object.

SoHServer

An opaque pointer (long *) to the server object, which acts as an object factory for
the shared library.

SoCClientName

A structure that uniquely identifies methods and properties.

TaggedData

A structure that encapsulates data values with type information, to be passed
between C/C++ and JavaScript.

SoCClientName
The SoCClientName data structure stores identifying information for methods and properties of
JavaScript objects created by shared-library C/C++ code. It is defined as follows:
SoCClientName {
char* name_sig ;
uint32_t id ;
char* desc ;
}
name_sig

The name of the property or method, unique within the class.
Optionally contains a signature following an underscore, which identifies the types of
arguments to methods; see Function signatures. When names are passed back to your
SoObjectInterface functions, the signature portion is omitted.

id

A unique identifying number for the property or method, or 0 to assign a generated UID.
If you assign the UID, your C/C++ code can use it to avoid string comparisons when
identifying JavaScript properties and methods. It is recommended that you either assign all
UIDs explicitly, or allow them all to be generated.

desc

A descriptive string or NULL.

CHAPTER 7: Integrating External Libraries

Defining entry points for indirect access

214

TaggedData
The TaggedData structure is used to communicate data values between JavaScript and shared-library
C/C++ code. Types are automatically converted as appropriate.
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
intval

Integer and boolean data values. Type is kTypeInteger, kTypeUInteger, or kTypeBool.

fltval

Floating-point numeric data values. Type is kTypeDouble.

string

String data values. All strings are UTF-8 encoded and null-terminated. Type is
kTypeString or kTypeScript.
The library must define an entry point ESFreeMem(), which ExtendScript calls to
release a returned string pointer. If this entry point is missing, ExtendScript does not
attempt to release any returned string data.
When a function returns a string of type kTypeScript, ExtendScript evaluates the
script and returns the result of evaluation as the result of the function call.

hObject

A C/C++ representation of a JavaScript object data value. Type is kTypeLiveObject or
kTypeLiveObjectRelease.
When a function returns an object of type kTypeLiveObject, ExtendScript does not
release the object.
When a function returns an object of type kTypeLiveObjectRelease, ExtendScript
releases the object.

CHAPTER 7: Integrating External Libraries

type

Defining entry points for indirect access

215

The data type tag. One of:
kTypeUndefined: a null value, equivalent of JavaScript undefined. The return value
for a function is always set to this by default.
kTypeBool: a boolean value, 0 for false, 1 for true.
kTypeDouble: a 64-bit floating-point number.
kTypeString: a character string.
kTypeLiveObject: a pointer to an internal representation of an object (SoHObject).
kTypeLiveObjectRelease: a pointer to an internal representation of an object

(SoHObject).

kTypeInteger: a 32-bit signed integer value.
kTypeUInteger: a 32-bit unsigned integer value.
kTypeScript: a string containing an executable JavaScript script.
filler

A 4-byte filler for 8-byte alignment.
