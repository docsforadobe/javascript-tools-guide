.. _externalobject-object:

ExternalObject object
=====================

You specify the name of the library in the constructor. The constructor searches for the named library
using the paths defined in the static property :ref:`ExternalObject.searchFolders <externalobject-class-properties>`.

If you are having difficulty loading your library as an ExternalObject, set the property
``ExternalObject.log`` to ``true``, then call ``ExternalObject.search('lib:myLibrary')``. This function
performs the search, and the log reports the paths that have been searched to the ExtendScript Toolkit
Console.

Before loading the library, the current folder is temporarily switched to the location of the found
executable file.

- In Mac OS, the current directory is set to the bundle or framework folder for the library.
- In Windows and UNIX, the current directory is set to the folder that contains the library.

--------------------------------------------------------------------------------

.. _externalobject-constructor:

ExternalObject constructor
--------------------------

``obj = new ExternalObject ("lib:" + filespec, arg1, ...argn);``

===============  =======================================================================================
``filespec``     The specifier "lib:" is case sensitive, and serves as the marker for dynamic libraries.
                 Concatenate this to the base name of the shared library, with or without an extension.
                 ExtendScript appends a file extension if necessary, according to the operating system:

                 - ``.dll`` in Windows
                 - ``.bundle`` or ``.framework`` in Mac OS (only Mach-O bundles are supported)
                 - ``.so`` in UNIX (except for HP/UX, where the extension is .sl )

                 The name of the library is case sensitive in UNIX.
``arg1...argn``  Optional. Any number of arguments to pass to the library's initialization routine.
===============  =======================================================================================

For example::

    var mylib = new ExternalObject( "lib:myLibrary" );

--------------------------------------------------------------------------------

.. _externalobject-class-properties:

ExternalObject class properties
-------------------------------
The ExternalObject class provides these static properties:

=================  =======  ============================================================================
**log**            Boolean  Set to true to write status information to standard output (the
                            JavaScript Console in the ExtendScript Toolkit). Set to false to turn
                            logging off. Default is false.
**searchFolders**  String   A set of alternate paths in which to search for the shared library files, a
                            single string with multiple path specifications delimited by semicolons
                            (;). Paths can be absolute or relative to the :ref:`Folder.startup <folder-class-properties>` location.
                            Default value is:

                            - In Windows, ``"Plugins;Plug-Ins;."``
                            - In Mac OS,
                              ``"Plugins;Plug-Ins;Frameworks;.;../../../Plugins;
                              ../../../Plug-ins;../../../Frameworks;../../..;"``
                            - In UNIX, ``"Plugins;Plug-Ins;plugins;."``

**version**        Number   The version of the library, as returned by :ref:`ESGetVersion() <externalobject-functions-ESGetVersion>`.
=================  =======  ============================================================================

--------------------------------------------------------------------------------

.. _externalobject-class-function:

ExternalObject class function
-----------------------------
The ExternalObject class provides this static function to help debug problems with loading libraries as
external objects:

--------------------------------------------------------------------------------

.. _externalobject-functions-search:

search()
********
``ExternalObject.search (spec)``

========  ===================================================================================
``spec``  String. The file specification for the compiled library, with or without path information.
========  ===================================================================================

Reports whether a compiled C/C++ library can be found, but does not load it. If logging is on, the
paths searched are reported to the JavaScript Console in the ExtendScript Toolkit.

Returns ``true`` if the library is found, ``false`` otherwise.

--------------------------------------------------------------------------------

.. _externalobject-instance-function:

ExternalObject instance function
--------------------------------

.. _externalobject-functions-terminate:

terminate()
***********
``ExternalObject_obj.terminate ()``

Explicitly shuts down the ``ExternalObject`` dynamic library wrapped by this instance.

It can be helpful to force a shutdown of the external library if termination of external libraries during
the shutdown of the hosting application does not occur in the correct order.

Returns ``undefined``.
