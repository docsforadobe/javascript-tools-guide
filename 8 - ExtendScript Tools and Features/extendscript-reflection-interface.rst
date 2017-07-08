.. _extendscript-reflection-interface:

ExtendScript reflection interface
=================================
ExtendScript provides a reflection interface that allows you to find out everything about an object,
including its name, a description, the expected data type for properties, the arguments and return value
for methods, and any default values or limitations to the input values.

.. _reflection-object:

Reflection object
-----------------
Every object has a reflect property that returns a reflection object that reports the contents of the
object. You can, for example, show the values of all the properties of an object with code like this::

  var f = new File ("myfile");
  var props = f.reflect.properties;
  for (var i = 0; i < props.length; i++) {
    $.writeln('this property ' + props[i].name + ' is ' + f[props[i].name]);
  }

--------------------------------------------------------------------------------

.. _reflection-object-properties:

Reflection object properties
****************************

All properties are read only.

===========  ==============  =======================================================================
description  String          Short text describing the reflected object, or undefined if no
                             description is available.
help         String          Longer text describing the reflected object more completely, or
                             ``undefined`` if no description is available.
methods      Array of        An Array of :ref:`reflectioninfo-object`s containing all methods of the
             ReflectionInfo  reflected object, defined in the class or in the specific instance.
name         String          The class name of the reflected object.
properties   Array of        An Array of :ref:`reflectioninfo-object`s containing all properties of the
             ReflectionInfo  reflected object, defined in the class or in the specific instance. For
                             objects with dynamic properties (defined at runtime) the list contains
                             only those dynamic properties that have already been accessed by
                             the script. For example, in an object wrapping an HTML tag, the
                             names of the HTML attributes are determined at run time.
===========  ==============  =======================================================================

--------------------------------------------------------------------------------

.. _reflection-object-functions

Reflection object functions
****************************

.. _reflection-object-find:

find()
++++++
``reflectionObj.find (name)``

====  ===============================================
name  The property for which to retrieve information.
====  ===============================================

Returns the :ref:`reflectioninfo-object` for the named property of the reflected object, or null if no such
property exists.

Use this method to get information about dynamic properties that have not yet been accessed, but
that are known to exist.

Examples
++++++++

This code determines the class name of an object::

  obj = new String ("hi");
  obj.reflect.name; // => String

This code gets a list of all methods::

  obj = new String ("hi");
  obj.reflect.methods; //=> indexOf,slice,...
  obj.reflect.find ("indexOf"); // => the method info

This code gets a list of properties::

  Math.reflect.properties; //=> PI,LOG10,...

This code gets the data type of a property::

  Math.reflect.find ("PI").type; // => number

--------------------------------------------------------------------------------

.. _reflectioninfo-object:

ReflectionInfo object
---------------------

This object contains information about a property, a method, or a method argument.
You can access ReflectionInfo objects in a Reflection object's properties and methods arrays, by
name or index::

  obj = new String ("hi");
  obj.reflect.methods[0];
  obj.reflect.methods["indexOf"];

You can access the ReflectionInfo objects for the arguments of a method in the arguments array of
the ReflectionInfo object for the method, by index::

  obj.reflect.methods["indexOf"].arguments[0];
  obj.reflect.methods.indexOf.arguments[0];

--------------------------------------------------------------------------------

.. _reflectioninfo-object-properties:

ReflectionInfo object properties
--------------------------------

============  ==============  ===========================================================================
arguments     Array of        For a reflected method, an array of ReflectionInfo objects describing
              ReflectionInfo  each method argument.
dataType      String          The data type of the reflected element. One of:
                              - ``boolean``
                              - ``number``
                              - ``string``
                              - ``Classname``: The class name of an object.

                              .. note:: Class names start with a capital letter. Thus, the value
                                ``string`` stands for a JavaScript string, while ``String`` is a
                                JavaScript ``String`` wrapper object.

                              - *: Any type. This is the default.
                              - ``null``
                              - ``undefined``: Return data type for a function that does not return
                                any value.
                              - ``unknown``
defaultValue  any             The default value for a reflected property or method argument, or
                              ``undefined`` if there is no default value, if the property is undefined, or
                              if the element is a method.
description   String          Short text describing the reflected object, or ``undefined`` if no
                              description is available.
help          String          Longer text describing the reflected object more completely, or
                              ``undefined`` if no description is available.
isCollection  Boolean         When ``true``, the reflected property or method returns a collection;
                              otherwise, ``false``.
max           Number          The maximum numeric value for the reflected element, or
                              ``undefined`` if there is no maximum or if the element is a method.
min           Number          The minimum numeric value for the reflected element, or ``undefined``
                              if there is no minimum or if the element is a method.
name          String          The name of the reflected element. A string, or a number for an array
              Number          index.
type          String          The type of the reflected element. One of:
                              - ``readonly``: A Read only property.
                              - ``readwrite``: A read-write property.
                              - ``createonly``: A property that is valid only during creation of an
                                object.
                              - ``method``: A method.
============  ==============  ===========================================================================
