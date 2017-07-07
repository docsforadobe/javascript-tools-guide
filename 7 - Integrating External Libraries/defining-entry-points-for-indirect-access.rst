.. _defining-entry-points-for-indirect-access:

Defining entry points for indirect access
=========================================
The C-client object interface for external libraries allows your C or C++ shared-library code to define,
create, use, and manage JavaScript objects.
The following entry points are required if you wish to use the object interface:

--------------------------------------------------------------------------------

.. _externalobject-functions-ESClientInterface:

ESClientInterface()
*******************
``int ESClientInterface (SoCClient_e kReason, SoServerInterface* pServer, SoHServer hServer)``

===========  ===================================================================================
``kReason``  The reason for this call, one of these constants:
             - ``kSoCClient_init``: The function is being called for initialization upon load.
             - ``kSoCClient_term``.: The function is being called for termination upon unload.
``pServer``  A pointer to an :ref:`shared-library-SoServerInterface` containing function pointers for the entry points,
             which enable the shared-library code to call into JavaScript to create and access
             JavaScript classes and objects.

             The shared-library code is responsible for storing this structure between the
             initialization and termination call, and retrieving it to access the functions.
``hServer``  An :ref:`SoHServer` reference for this shared library. The server is an object factory that
             creates and manages :ref:`SoHObject` objects.

             The shared-library code is responsible for storing this structure between the
             initialization and termination calls. You must pass it to :ref:`taggedDataInit() <externalobject-functions-taggedDataInit>` and
             :ref:`taggedDataFree() <externalobject-functions-taggedDataFree>`.
===========  ===================================================================================

Your library must define this global function in order to use the object interface to JavaScript. The
function is called twice in each session, immediately upon loading the library, and again when
unloading it.

Returns an error code, ``kESErrOK`` on success.

--------------------------------------------------------------------------------

.. _externalobject-functions-ESMallocMem:

ESMallocMem()
*************
``void * ESMallocMem ( size_t nbytes)``

==========  ===================================================================================
``nbytes``  The number of bytes to allocate.
==========  ===================================================================================

Provides a memory allocation routine to be used by JavaScript for managing memory associated
with the library's objects.

Returns a pointer to the allocated block of memory.

--------------------------------------------------------------------------------

.. _shared-library-function-api:

Shared-library function API
---------------------------
Your shared-library C/C++ code defines its interface to JavaScript in two sets of functions, collected in
:ref:`shared-library-SoServerInterface` and :ref:`shared-library-SoObjectInterface` function-pointer structures.
Return values from most functions are integer constants. The error code ``kESErrOK == 0`` indicates success.

.. _shared-library-SoServerInterface:

SoServerInterface
*****************

``SoServerInterface`` is a structure of function pointers which enable the shared-library code to call

JavaScript objects. It is passed to the global ESClientInterface() function for initialization when the library is
loaded, and again for cleanup when the library is unloaded. Between these calls, your shared-library code
must store the structure and use it to access the communication functions.
You can store information for every object and class in your C code. The recommended method is to create
a data structure during the initialize() and free it during finalize(). You can then access that data with
setClientData() and getClientData().

The SoServerInterface structure contains these function pointers::

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

--------------------------------------------------------------------------------

.. _externalobject-functions-dumpServer:

dumpServer()
************
``ESerror_t dumpServer (SoHServer hServer);``

===========  ===================================================================================
``hServer``  The :ref:`SoHServer` reference for this shared library, as passed to your global
             :ref:`ESClientInterface() <externalobject-functions-ESClientInterface>` function on initialization.
===========  ===================================================================================

Prints the contents of this server to the JavaScript Console in the ExtendScript Toolkit, for
debugging.

Returns an error code, ``kESErrOK`` on success.

--------------------------------------------------------------------------------

.. _externalobject-functions-dumpObject:

dumpObject()
************
``ESerror_t dumpObject (SoHObject hObject);``

===========  ===================================================================================
``hObject``  The :ref:`SoHObject` reference for an instance of this class.
===========  ===================================================================================

Prints the contents of this object to the JavaScript Console in the ExtendScript Toolkit, for
debugging.

Returns an error code, ``kESErrOK`` on success.

--------------------------------------------------------------------------------

.. _externalobject-functions-addClass:

addClass()
**********
``ESerror_t addClass (SoHServer hServer, char* name, SoObjectInterface_p pObjectInterface);``

====================  ===================================================================================
``hServer``           The :ref:`SoHServer` reference for this shared library, as passed to your global
                      :ref:`ESClientInterface() <externalobject-functions-ESClientInterface>` function on initialization.
``name``              String. The unique name of the new class. The name must begin with an
                      uppercase alphabetic character.
``pObjectInterface``  A pointer to an :ref:`SoObjectInterface <mising link>`. A structure containing pointers to the
                      object interface methods for instances of this class.
====================  ===================================================================================

Creates a new JavaScript class.

Returns an error code, ``kESErrOK`` on success.

--------------------------------------------------------------------------------

.. _externalobject-functions-addMethod:

addMethod()
***********
``ESerror_t addMethod (SoHObject hObject, const char* name, int id, char* desc);``

===========  ===================================================================================
``hObject``  The :ref:`SoHObject` reference for an instance of this class.
``name``     String. The unique name of the new method.
``id``       Number. The unique identifier for the new method.
``desc``     String. A descriptive string for the new method.
===========  ===================================================================================

Adds new method to an instance.

Returns an error code, ``kESErrOK`` on success.

--------------------------------------------------------------------------------

.. _externalobject-functions-addMethods:

addMethods()
************
``ESerror_t addMethods (SoHObject hObject, SoCClientName_p pNames);``

============  ===================================================================================
``hObject``   The :ref:`SoHObject` reference for an instance of this class.
``pNames[]``  :ref:`SoCClientName`. A structure containing the names and identifiers of
              methods to be added.
============  ===================================================================================

Adds a set of new methods to an instance.

Returns an error code, ``kESErrOK`` on success.

--------------------------------------------------------------------------------

.. _externalobject-functions-addProperty:

addProperty()
*************
``ESerror_t addProperty (SoHObject hObject, const char* name, int id, char* desc);``

===========  ===================================================================================
``hObject``  The :ref:`SoHObject` reference for an instance of this class.
``name``     String. The unique name of the new property.
``id``       Number. The unique identifier for the new property.
``desc``     String. Optional. A descriptive string for the new property, or null.
===========  ===================================================================================

Adds new property to an instance.

Returns an error code, ``kESErrOK`` on success.

--------------------------------------------------------------------------------

.. _externalobject-functions-addProperties:

addProperties()
***************
``ESerror_t addProperties (SoHObject hObject, SoCClientName_p pNames);``

============  ===================================================================================
``hObject``   The :ref:`SoHObject` reference for an instance of this class.
``pNames[]``  :ref:`SoCClientName`. A structure containing the names and identifiers of
              properties to be added.
============  ===================================================================================

Adds a set of new properties to an instance.

Returns an error code, ``kESErrOK`` on success.

--------------------------------------------------------------------------------

.. _externalobject-functions-getClass:

getClass()
**********
``ESerror_t getClass (SoHObject hObject, char* name, int name_l);``

===========  ===================================================================================
``hObject``  The :ref:`SoHObject` reference for an instance of this class.
``name``     String. A buffer in which to return the unique name of the class.
``name_1``   Number. The size of the name buffer.
===========  ===================================================================================

Retrieves this object's parent class name.

Returns an error code, ``kESErrOK`` on success.

--------------------------------------------------------------------------------

.. _externalobject-functions-getServer:

getServer()
***********
``ESerror_t getServer (SoHObject hObject, SoHServer* phServer, SoServerInterface_p* ppServerInterface);``

=====================  =================================================================================================
``hObject``            The :ref:`SoHObject` reference for an instance of this class.
``phServer``           A buffer in which to return the :ref:`SoHServer` reference for this object.
``ppServerInterface``  A buffer in which to return the :ref:`shared-library-SoObjectInterface` reference for this object.
=====================  =================================================================================================

Retrieves the interface methods for this object, and the server object that manages it.

Returns an error code, ``kESErrOK`` on success.

--------------------------------------------------------------------------------

.. _externalobject-functions-setClientData:

setClientData()
***************
``ESerror_t setClientData (SoHObject hObject, void* pData);``

===========  =================================================================================================
``hObject``  The :ref:`SoHObject` reference for an instance of this class.
``pData``    A pointer to the library-defined data.
===========  =================================================================================================

Sets your own data to be stored with an object.

Returns an error code, ``kESErrOK`` on success.

--------------------------------------------------------------------------------

.. _externalobject-functions-getClientData:

getClientData()
***************
``ESerror_t setClientData (SoHObject hObject, void** pData);``

===========  =================================================================================================
``hObject``  The :ref:`SoHObject` reference for an instance of this class.
``pData``    A buffer in which to return a pointer to the library-defined data.
===========  =================================================================================================

Retrieves data that was stored with :ref:`setClientData() <externalobject-functions-setClientData>`.

Returns an error code, ``kESErrOK`` on success.

--------------------------------------------------------------------------------

.. _externalobject-functions-eval:

eval()
******
``ESerror_t eval (SohServer hServer, char* string, TaggedData* pTaggedData);``

===============  =================================================================================================
``hServer``      The :ref:`SoHServer` reference for this shared library, as passed to your global
                 :ref:`ESClientInterface() <externalobject-functions-ESClientInterface>` function on initialization.
``string``       A string containing the JavaScript expression to evaluate.
``pTaggedData``  A pointer to a :ref:`TaggedData` object in which to return the result of evaluation.
===============  =================================================================================================

Calls the JavaScript interpreter to evaluate a JavaScript expression.

Returns an error code, ``kESErrOK`` on success.

--------------------------------------------------------------------------------

.. _externalobject-functions-taggedDataInit:

taggedDataInit()
****************
``ESerror_t taggedDataInit (SoHSever hServer, TaggedData* pTaggedData);``

===============  =================================================================================================
``hServer``      The :ref:`SoHServer` reference for this shared library, as passed to your global
                 :ref:`ESClientInterface() <externalobject-functions-ESClientInterface>` function on initialization.
``pTaggedData``  A pointer to a :ref:`TaggedData`.
===============  =================================================================================================

Initializes a TaggedData structure.

Returns an error code, ``kESErrOK`` on success.

--------------------------------------------------------------------------------

.. _externalobject-functions-taggedDataFree:

taggedDataFree()
****************
``ESerror_t setClientData (SoHServer hServer, TaggedData* pTaggedData);``

===============  =================================================================================================
``hServer``      The :ref:`SoHServer` reference for this shared library, as passed to your global
                 :ref:`ESClientInterface() <externalobject-functions-ESClientInterface>` function on initialization.
``pTaggedData``  A pointer to a :ref:`TaggedData`.
===============  =================================================================================================

Frees memory being used by a TaggedData structure.

Returns an error code, ``kESErrOK`` on success.

--------------------------------------------------------------------------------

.. _shared-library-SoObjectInterface:

SoObjectInterface
*****************

When you add a JavaScript class with SoServerInterface.addClass(), you must provide this interface.
JavaScript calls the provided functions to interact with objects of the new class.
The SoObjectInterface is an array of function pointers defined as follows::

    SoObjectInterface {
        SoObjectInitialize_f initialize;
        SoObjectPut_f        put;
        SoObjectGet_f        get;
        SoObjectCall_f       call;
        SoObjectValueOf_f    valueOf;
        SoObjectToString_f   toString;
        SoObjectFinalize_f   finalize;
    }

All ``SoObjectInterface`` members must be valid function pointers, or NULL. You must implement
``initialize()`` and ``finalize()``. The functions must conform to the following type definitions.

--------------------------------------------------------------------------------

.. _externalobject-functions-initialize:

initialize()
************
``ESerror_t initialize (SoHObject hObject, int argc, TaggedData* argv);``

===============  =================================================================================================
``hObject``      The :ref:`SoHObject` reference for an instance of this class.
``argc, argv``   The number of and pointer to arguments passed to the constructor, in the form of :ref:`TaggedData`.
===============  =================================================================================================

Required. Called when JavaScript code instantiates this class with the new operator::

    var xx = New MyClass(arg1, ...)

The initialization function typically adds properties and methods to the object. Objects of the same
class can offer different properties and methods, which you can add with the :ref:`addMethod() <externalobject-functions-addMethod>` and
:ref:`addProperty() <externalobject-functions-addProperty>` functions in the stored SoServerInterface.

Returns an error code, ``kESErrOK`` on success.

--------------------------------------------------------------------------------

.. _externalobject-functions-put:

put()
*****
``ESerror_t put (SoHObject hObject, SoCClientName* name, TaggedData* pValue);``

===============  =================================================================================================
``hObject``      The :ref:`SoHObject` reference for an instance of this class.
``name``         The name of the property, a pointer to an :ref:`SoCClientName`.
``pValue``       The new value, a pointer to a :ref:`TaggedData`.
===============  =================================================================================================

Called when JavaScript code sets a property of this class::

    xx.myproperty = "abc" ;

If you provide ``NULL`` for this function, the JavaScript object is read-only.

Returns an error code, ``kESErrOK`` on success.

--------------------------------------------------------------------------------

.. _externalobject-functions-get:

get()
*****
``ESerror_t get (SoHObject hObject, SoCClientName* name, TaggedData* pValue);``

===============  =================================================================================================
``hObject``      The :ref:`SoHObject` reference for an instance of this class.
``name``         The name of the property, a pointer to an :ref:`SoCClientName`.
``pValue``       A buffer in which to return the property value, a :ref:`TaggedData`.
===============  =================================================================================================

Called when JavaScript code accesses a property of this class::

    alert(xx.myproperty);

Returns an error code, ``kESErrOK`` on success.

--------------------------------------------------------------------------------

.. _externalobject-functions-call:

call()
******
``ESerror_t call (SoHObject hObject, SoCClientName* name, int argc, TaggedData* argv, TaggedData* pResult);``

===============  =================================================================================================
``hObject``      The :ref:`SoHObject` reference for an instance of this class.
``name``         The name of the property, a pointer to an :ref:`SoCClientName`.
``argc, argv``   The number and pointer to arguments passed to the call, in the form of :ref:`TaggedData`s.
``pResult``      A buffer in which to return the result of the call, in the form of :ref:`TaggedData`.
===============  =================================================================================================

Called when JavaScript code calls a method of this class::

    xx.mymethod()

Required in order for JavaScript to call any methods of this class.

Returns an error code, ``kESErrOK`` on success.

--------------------------------------------------------------------------------

.. _externalobject-functions-valueOf:

valueOf()
*********
``ESerror_t valueOf (SoHObject hObject, TaggedData* pResult);``

===============  =================================================================================================
``hObject``      The :ref:`SoHObject` reference for an instance of this class.
``pResult``      A buffer in which to return the result of the value, in the form of :ref:`TaggedData`.
===============  =================================================================================================

Creates and returns the value of the object, with no type conversion.

Returns an error code, ``kESErrOK`` on success.

--------------------------------------------------------------------------------

.. _externalobject-functions-toString:

toString()
**********
``ESerror_t toString (SoHObject hObject, TaggedData* pResult);``

===============  =================================================================================================
``hObject``      The :ref:`SoHObject` reference for an instance of this class.
``pResult``      A buffer in which to return the result of the string, in the form of :ref:`TaggedData`s.
===============  =================================================================================================

Creates and returns a string representing the value of this object.

Returns an error code, ``kESErrOK`` on success.

--------------------------------------------------------------------------------

.. _externalobject-functions-finalize:

finalize()
**********
``ESerror_t finalize (SoHObject hObject);``

===============  =================================================================================================
``hObject``      The :ref:`SoHObject` reference for an instance of this class.
===============  =================================================================================================

Required. Called when JavaScript deletes an instance of this class.
Use this function to free any memory you have allocated.

Returns an error code, ``kESErrOK`` on success.

--------------------------------------------------------------------------------

.. _SoHObject:
.. _SoHServer:
.. _support-structures:

Support structures
------------------
These support structures are passed to functions that you define for your JavaScript interface:

=================  ====================================================================================
``SoHObject``      An opaque pointer (long *) to the C/C++ representation of a JavaScript object.
``SoHServer``      An opaque pointer (long *) to the server object, which acts as an object factory for
                   the shared library.
``SoCClientName``  A structure that uniquely identifies methods and properties.
``TaggedData``     A structure that encapsulates data values with type information, to be passed
                   between C/C++ and JavaScript.
=================  ====================================================================================

.. _SoCClientName:

**SoCClientName**

The SoCClientName data structure stores identifying information for methods and properties of
JavaScript objects created by shared-library C/C++ code. It is defined as follows::

    SoCClientName {
        char* name_sig ;
        uint32_t id ;
        char* desc ;
    }

============  ===========================================================================================
``name_sig``  The name of the property or method, unique within the class.
              Optionally contains a signature following an underscore, which identifies the types of
              arguments to methods; see Function signatures. When names are passed back to your
              SoObjectInterface functions, the signature portion is omitted.
``id``        A unique identifying number for the property or method, or 0 to assign a generated UID.
              If you assign the UID, your C/C++ code can use it to avoid string comparisons when
              identifying JavaScript properties and methods. It is recommended that you either assign all
              UIDs explicitly, or allow them all to be generated.
``desc``      A descriptive string or ``NULL``.
============  ===========================================================================================

.. _TaggedData:

**TaggedData**

The TaggedData structure is used to communicate data values between JavaScript and shared-library
C/C++ code. Types are automatically converted as appropriate::

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

===========  ==========================================================================================
``intval``   Integer and boolean data values. Type is kTypeInteger, kTypeUInteger, or kTypeBool.
``fltval``   Floating-point numeric data values. Type is kTypeDouble.
``string``   String data values. All strings are UTF-8 encoded and null-terminated. Type is
             kTypeString or kTypeScript.
             - The library must define an entry point :ref:`ESFreeMem() <externalobject-functions-ESFreeMem>`,
               which ExtendScript calls to release a returned string pointer.
               If this entry point is missing, ExtendScript does not attempt to release any returned string data.
             - When a function returns a string of type kTypeScript, ExtendScript evaluates the
               script and returns the result of evaluation as the result of the function call.
``hObject``  A C/C++ representation of a JavaScript object data value. Type is kTypeLiveObject or
             kTypeLiveObjectRelease.
             - When a function returns an object of type kTypeLiveObject, ExtendScript does not
               release the object.
             - When a function returns an object of type kTypeLiveObjectRelease, ExtendScript
               releases the object.
``type``     The data type tag. One of:
             - ``kTypeUndefined``: a null value, equivalent of JavaScript ``undefined``. The return value
               for a function is always set to this by default.
             - ``kTypeBool``: a boolean value, 0 for false, 1 for true.
             - ``kTypeDouble``: a 64-bit floating-point number.
             - ``kTypeString``: a character string.
             - ``kTypeLiveObject``: a pointer to an internal representation of an object (SoHObject).
             - ``kTypeLiveObjectRelease``: a pointer to an internal representation of an object (SoHObject).
             - ``kTypeInteger``: a 32-bit signed integer value.
             - ``kTypeUInteger``: a 32-bit unsigned integer value.
             - ``kTypeScript``: a string containing an executable JavaScript script.
``filler``   A 4-byte filler for 8-byte alignment.
===========  ==========================================================================================
