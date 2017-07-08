.. _xml-object-reference:

XML Object Reference
====================
This section provides reference details for the properties and methods of the XML object itself, and for the
related utility objects and global functions that you use to work with namespaces:

- :ref:`xml-object`
- :ref:`namespace-object`
- :ref:`qname-object`
- :ref:`xml-global-functions`

--------------------------------------------------------------------------------

.. _xml-object:

XML object
----------

The ``XML`` object provides both static properties and functions, available through the ``XML`` class,
and dynamic properties and functions available through each instance.

XML object constructor
**********************

The constructor returns the XML object representing the root node of an XML tree, which contains
additional XML objects for all contained elements.

``[new] XML (xmlCode);``

.. _xmlCode:

xmlCode
+++++++
String or XML

A string containing valid XML code, or an existing XML object.

- If a valid string is supplied, returns a new XML object
  encapsulating the XML code. If the XML code cannot be parsed,
  throws a JavaScript error.
- If an existing object is supplied and the ``new`` operator is used,
  returns a copy of the object; otherwise, returns the object itself.

--------------------------------------------------------------------------------

.. _xml-class-properties:

XML class properties
********************

These static properties are available through the XML class. They control how XML is parsed and generated:

================================  =========  =======================================================
**ignoreComments**                Boolean    When true, comments are stripped from the XML
                                             during parsing. Default is false.
**ignoreProcessingInstructions**  Boolean    When true, processing instructions (``<?xxx?>``
                                             elements) are stripped from the XML during
                                             parsing. Default is false.
**ignoreWhitespace**              Boolean    When true, white-space characters are stripped
                                             from the XML during parsing. Default is true.
**prettyIndent**                  Number     The number of spaces to use for indenting when
                                             pretty-printing. Default is 2.
**prettyPrinting**                Boolean    When true, ``toXMLString()`` uses indenting and
                                             line feeds to create the XML string. Default is true.
================================  =========  =======================================================

--------------------------------------------------------------------------------

.. _xml-class-functions:

XML class functions
*******************

These static functions are available through the XML class, and provide information about the global
settings of the XML parser.

.. _xml-defaultSettings:

defaultSettings()
+++++++++++++++++
``XML.defaultSettings ();``

Retrieves the default global option settings that control how XML is parsed and generated.

Returns a JavaScript object containing five properties, which correspond to the five :ref:`xml-class-properties`.

--------------------------------------------------------------------------------

.. _xml-settings:

settings()
++++++++++
``XML.settings ();``

Retrieves the current global option settings that control how XML is parsed and generated.

Returns a JavaScript object containing five properties, which correspond to the five :ref:`xml-class-properties`

--------------------------------------------------------------------------------

.. _xml-setSettings:

setSettings()
+++++++++++++
``XML.setSettings (object);``

======  ======================================================================================
object  A JavaScript object containing five properties, which correspond to the five :ref:`xml-class-properties`
======  ======================================================================================

Sets the global option settings that control how XML is parsed and generated. You can use this to
restore settings retrieved with :ref:`xml-settings` or :ref:`xml-defaultSettings`.

Returns ``undefined``.

--------------------------------------------------------------------------------

.. _xml-object-properties:

XML object properties
*********************

The properties of the XML object are named for and contain the values of the child elements and attributes
of the element that the object represents.

==================  =================  =====================================================================================
*childElementName*  :ref:`xml-object`  Child-element properties are named with the child element name.
**@attributeName**  :ref:`xml-object`  Attribute properties are named with the attribute name prefixed with the at-sign, @.
==================  =================  =====================================================================================

--------------------------------------------------------------------------------

.. _xml-object-functions:

XML object functions
********************

addNamespace()
++++++++++++++
``xmlObj.addNamespace (ns);``

==  =========================================
ns  A :ref:`namespace-object`.
==  =========================================

Adds a namespace declaration to this node.

Returns this :ref:`xml-object`.

--------------------------------------------------------------------------------

.. _xml-object-appendChild:

appendChild()
+++++++++++++
``xmlObj.appendChild (child);``

===== ============================================================================
child An :ref:`xml-object` or any value that can be converted to a String with ``toString()``.
===== ============================================================================

Appends a child element to this node, after any existing children. If the argument is not XML,
creates a new XML element that contains the string as its text value, using the same element name
as the last element currently contained in this object's node.

Returns this :ref:`xml-object`.

--------------------------------------------------------------------------------

.. _xml-object-attributes:

attributes()
++++++++++++
``xmlObj.attributes (name);``

====  ==============================
name  A String, the attribute name.
====  ==============================

Retrieves a list of the named attribute elements contained in this node.

Returns an :ref:`xml-object` containing all values of the named attribute.

--------------------------------------------------------------------------------

.. _xml-object-child:

child()
+++++++
``xmlObj.child (which);``

=====  ======================================================================================
which  A String, the element name, or a Number, a 0-based index into this node's child array.
=====  ======================================================================================

Retrieves a list of all child elements of this node of a given type.

Returns an :ref:`xml-object` containing all child elements of the given type.

--------------------------------------------------------------------------------

.. _xml-object-childIndex:

childIndex()
++++++++++++
``xmlObj.childIndex ();``

Retrieves the 0-based position index of this node within its parent node.

Returns a Number.

--------------------------------------------------------------------------------

.. _xml-object-children:

children()
++++++++++
``xmlObj.children();``

Retrieves all of the immediate child elements of this node, including text elements.

Returns an :ref:`xml-object` containing the child elements.

--------------------------------------------------------------------------------

.. _xml-object-comments:

comments()
++++++++++
``xmlObj.comments();``

Retrieves all XML comment elements from this node.

Returns an :ref:`xml-object` containing the comments.

--------------------------------------------------------------------------------

.. _xml-object-contains:

contains()
++++++++++
``xmlObj.contains (element);``

=======  ======================
element  An :ref:`xml-object`.
=======  ======================

Reports whether an element is contained in this node at any level of nesting.

Returns ``true`` if the element is contained in this XML tree.

--------------------------------------------------------------------------------

.. _xml-object-copy:

copy()
++++++
``xmlObj.copy();``

Creates a copy of this node.

Returns the new XML object.

--------------------------------------------------------------------------------

.. _xml-object-descendants:

descendants()
+++++++++++++
``xmlObj.descendants ([name]);``

====  ==============================================================================
name  Optional. A String, the element name to match. If not provided, matches all
      elements.
====  ==============================================================================

Retrieves all descendent elements of this node of a given element type, or all XML-valued
descendants, at any level of nesting. Includes text elements.

Returns an :ref:`xml-object` containing properties for each descendant element.

--------------------------------------------------------------------------------

.. _xml-object-elements:

elements()
++++++++++
``xmlObj.elements (name);``

====  ==============================================================================
name  Optional. A String, the element name to match. If not provided, matches all
      elements.
====  ==============================================================================

Retrieves all of the immediate child elements of this node of the given type, or of all types. Does not
include text elements.

Returns an :ref:`xml-object` containing properties for each child element.

--------------------------------------------------------------------------------

.. _xml-object-hasComplexContent:

hasComplexContent()
+++++++++++++++++++
``xmlObj.hasComplexContent ();``

Reports whether this node has complex content; that is, whether it contains child elements.
Disregards contents of other kinds, including attributes, comments, processing instructions and
text nodes.

Returns ``true`` if this node contains child elements.

--------------------------------------------------------------------------------

.. _xml-object-hasSimpleContent:

hasSimpleContent()
++++++++++++++++++
``xmlObj.hasSimpleContent ();``

Reports whether this node has simple content; that is, whether it represents a text node, an
attribute node, or an element without child elements (regardless of whether it also contains
attributes, comments, processing instructions or text).

Object representing comments and processing instructions do not have simple content.

Returns ``true`` if this node contains no child elements.

--------------------------------------------------------------------------------

.. _xml-object-inScopeNamespaces:

inScopeNamespaces()
+++++++++++++++++++
``xmlObj.inScopeNamespaces ();``

Retrieves the current list of valid namespaces in this element.

Returns an Array of :ref:`namespace-object`, in which the last member is the default namespace.

--------------------------------------------------------------------------------

.. _xml-object-insertChildAfter:

insertChildAfter()
++++++++++++++++++
``xmlObj.insertChildAfter (child1, child2);``

======  ====================================================================================
child1  An :ref:`xml-object`, the existing child element after which to place the new child,
        or null to insert the new child at the beginning.
child2  An :ref:`xml-object`, the new child element, or any value that can be converted to a String
        with ``toString()``.
======  ====================================================================================

Inserts a new child element or text node into this node, after another existing child element. If the
relative element is not currently in this node, does not insert the new child.

Returns this :ref:`xml-object`.

--------------------------------------------------------------------------------

.. _xml-object-insertChildBefore:

insertChildBefore()
+++++++++++++++++++
``xmlObj.insertChildBefore (child1, child2);``

======  ====================================================================================
child1  An :ref:`xml-object`, the existing child element before which to place the new child,
        or null to insert the new child at the end.
child2  An :ref:`xml-object`, the new child element, or any value that can be converted to a String
        with ``toString()``.
======  ====================================================================================

Inserts a new child element or text node into this node, before another existing child element. If the
relative element is not currently in this node, does not insert the new child.

Returns this :ref:`xml-object`.

--------------------------------------------------------------------------------

.. _xml-object-length:

length()
++++++++
``xmlObj.length ();``

Reports the number of child elements contained in this node. The minimum number is 1, the
element that this object represents.

Returns a Number.

--------------------------------------------------------------------------------

.. _xml-object-localName:

localName()
+++++++++++
``xmlObj.localName ();``

Retrieves the local name of this element; that is, the element name, without any namespace prefix.

Returns a String.

--------------------------------------------------------------------------------

.. _xml-object-name:

name()
++++++
``xmlObj.name ();``

Retrieves the full name of this element, with the namespace information.

Returns a :ref:`qname-object` containing the element name and namespace URI.

--------------------------------------------------------------------------------

.. _xml-object-namespace:

namespace()
+++++++++++
``xmlObj.namespace ();``

Retrieves the namespace URI of this element.

Returns a String.

--------------------------------------------------------------------------------

.. _xml-object-nodeKind:

nodeKind()
++++++++++
``xmlObj.nodeKind ();``

Reports the type of this node.

Returns a String, one of:

- ``element``
- ``attribute``
- ``comment``
- ``processing-instruction``
- ``text``

--------------------------------------------------------------------------------

.. _xml-object-namespaceDeclarations:

namespaceDeclarations()
+++++++++++++++++++++++
``xmlObj.namespaceDeclarations ();``

Retrieves all of the namespace declarations contained in this node.

Returns an Array of :ref:`namespace-object`.

--------------------------------------------------------------------------------

.. _xml-object-normalize:

normalize()
+++++++++++
``xmlObj.normalize ();``

Puts all text nodes in this and all descendant XML objects into a normal form by merging adjacent
text nodes and eliminating empty text nodes.

Returns this :ref:`xml-object`.

--------------------------------------------------------------------------------

.. _xml-object-parent:

parent()
++++++++
``xmlObj.parent ();``

Retrieves the parent node of this node.

Returns an :ref:`xml-object`, or ``null`` for the root element.

--------------------------------------------------------------------------------

.. _xml-object-prependChild:

prependChild()
++++++++++++++
``xmlObj.prependChild (child);``

=====  ===============================
child  An :ref:`xml-object` or string.
=====  ===============================

Prepends a child element to this node, before any existing children. If you prepend a string to a text
element, the result is two text elements; call :ref:`xml-object-normalize` to concatenate them into a single text
string.

Returns this :ref:`xml-object`.

--------------------------------------------------------------------------------

.. _xml-object-processingInstructions:

processingInstructions()
++++++++++++++++++++++++
``xmlObj.processingInstructions ([name]);``
name

A String, the name of a processing instruction, or null to get all processing
instructions.

Retrieves processing instructions contained in this node.

Returns an :ref:`xml-object` containing the children of this object that are processing instructions,
matching the name if supplied.

--------------------------------------------------------------------------------

.. _xml-object-replace:

replace()
+++++++++
``xmlObj.replace (name, value);``

=====  ======================================================================================
name   An element or attribute name, with or without the 0-based position index of a
       specific element, or the wildcard string ``"*"``.

       - If no position index is supplied, replaces the value of all matching elements.
       - If the wildcard is supplied, replaces the value of all contained elements. When an
         element contain subelements, those are removed, and only the replacement
         value remains.

value  An :ref:`xml-object` or any value that can be converted to a String with ``toString()``.
=====  ======================================================================================

Replaces one or more property values in this node.

If the named element does not exist, appends the given value as a text element.

Returns this :ref:`xml-object`.

--------------------------------------------------------------------------------

.. _xml-object-setChildren:

setChildren()
+++++++++++++
``xmlObj.setChildren (value);``

=====  ========================================================================================
value  An :ref:`xml-object` or any value that can be converted to a String with ``toString()``.
=====  ========================================================================================

Replaces all of the XML-valued properties in this object with a new value, which can be a simple text
element, or can contain another set of XML properties.

Returns this :ref:`xml-object`.

--------------------------------------------------------------------------------

.. _xml-object-setLocalName:

setLocalName()
++++++++++++++
``xmlObj.setLocalName(name);``

====  =======================
name  A String, the new name.
====  =======================

Replaces the local name of this object; that is, the element name without any namespace prefix.

Returns this :ref:`xml-object`.

--------------------------------------------------------------------------------

.. _xml-object-setName:

setName()
+++++++++
``xmlObj.setName(name);``

====  =======================
name  A String, the new name.
====  =======================

Replaces the full name of this object; that is, the element name and its namespace prefix.

Returns this :ref:`xml-object`.

--------------------------------------------------------------------------------

.. _xml-object-setNamespace:

setNamespace()
++++++++++++++
``xmlObj.setNamespace(ns);``

==  =========================================================================================
ns  A Namespace object for a namespace that has been declared in the tree above this element.
==  =========================================================================================

Sets the namespace for this XML element. If the namespace has not been declared in the tree above
this element, add a namespace declaration instead.

Returns this :ref:`xml-object`.

--------------------------------------------------------------------------------

.. _xml-object-text:

text()
++++++
``xmlObj.text();``

Retrieves text nodes from this element.

Returns an :ref:`xml-object` containing all properties of this object that represent XML text nodes.

--------------------------------------------------------------------------------

.. _xml-object-toString:

toString()
++++++++++
``xmlObj.toString();``

Creates a string representation of this object.

- For text and attribute nodes, this is the textual value of the node.
- For other elements, it is the result of :ref:`xml-object-toXMLString`.
- If this XML object is a list, concatenates the result of calling the function on each contained element.

Returns a String.

--------------------------------------------------------------------------------

.. _xml-object-toXMLString:

toXMLString()
+++++++++++++
``xmlObj.toXMLString();``

Creates an XML-encoded string representation of this :ref:`xml-object`. This result includes the start tag,
attributes and end tag of the XML object, regardless of its content. Formats the string as specified
by the global settings XML.:ref:`prettyPrinting <xml-class-properties>` and XML.:ref:`prettyIndent <xml-class-properties>`.

Returns a String.

--------------------------------------------------------------------------------

.. _xml-object-xpath:

xpath()
+++++++
``xmlObj.xpath (expression[, variables]);``

==========  ==========================================================================================
expression  A String containing an XPath expression.

            .. note:: In this context, include the actual top level element. For example, an
              expression for the example XML must start with "/bookstore". This is unlike
              JavaScript property access, where the top level element is implied.

variables   Optional. A JavaScript object containing variable definitions. The properties are used
            to look up XPath variables contained in the expression. For example, if the
            expression contains the variable ``$abc``, the value is in the object's ``abc`` property.
==========  ==========================================================================================

Evaluates an XPath expression in accordance with the W3C XPath recommendation, using this XML
object as the context node. The context position and size are set to 1, and all variables are initially
unbound. If this XML object is a list, evaluates all contained XML element nodes (not comments or
other node types) and return the results in a list in the order of execution.

If the XPath expression does not evaluate to a node list, throws a JavaScript exception.

Returns an :ref:`xml-object`, the result of evaluation.

--------------------------------------------------------------------------------

.. _xml-global-functions:

Global functions
----------------

These functions are available in the JavaScript global namespace.

.. _xml-isXMLName:

isXMLName()
***********
``isXMLName (String name)``

====  =========
name  A string.
====  =========

Reports whether a string contains a name that conforms to valid XML syntax.

.. note:: This implementation uses the same rules as for a JavaScript name, except for the '$' character,
  which is disallowed, and the '-' character, which as added. It does not follow the W3C definition of an
  XML name, which adds more Unicode characters to the valid set of characters.

Returns ``true`` if the name is a valid XML name, ``false`` otherwise.

--------------------------------------------------------------------------------

.. _xml-setDefaultXMLNamespace:

setDefaultXMLNamespace()
************************
``setDefaultXMLNamespace (Namespace ns)``

==  ==========================================
ns  A Namespace object. Any prefix is ignored.
==  ==========================================

Sets the default namespace for XML objects. You can also set the default namespace using this
syntax::

  default xml namespace = Namespace object
  default xml namespace = URL_string

Returns ``undefined``.

--------------------------------------------------------------------------------

.. _qname-object:

QName object
------------

This object encapsulates a fully qualified XML name, the combination of a local XML name and its
namespace URI.

--------------------------------------------------------------------------------

QName object constructors
*************************

The constructor takes several forms::

  new QName ()
  new QName (name)
  new QName (ns)
  new QName (uri, name)

When no arguments are supplies, creates a ``QName`` object with an empty local name and no URI.

=========  =========  ================================================================================
name       String     Creates a ``QName`` object with the given local name and the URI of the default
                      namespace. Can be the wildcard character, "*".
name       QName      Creates a copy of an existing :ref:`qname-object`.
ns         Namespace  Creates a ``QName`` object with an empty local name and the URI of the :ref:`namespace-object`.
uri, name  String     Create a ``QName`` object with the given namespace URI and local name.

                      If the local name is supplied as the wildcard character, "*", the ``uri`` argument
                      is ignored, and the URI value is that of the default namespace.
=========  =========  ================================================================================

--------------------------------------------------------------------------------

QName object properties
***********************

======  =======  ==============================================================================
name    String   The local element name portion of the XML element's fully qualified XML name.
uri     String   The namespace prefix of the XML element's fully qualified XML name.
======  =======  ==============================================================================

--------------------------------------------------------------------------------

.. _namespace-object:

Namespace object
----------------
This object encapsulates the definition of an XML namespace. A namespace associates an XML-name
prefix with a complete URI. The prefix is a string that precedes the local name of an XML element or
attribute and identifies the namespace, while the URI points to the actual location where the definition of
the namespace is found.

For example, this XML definition contains a namespace declaration::

  .. code-block::xml

    <?xml xmlns:adobe=http://www.adobe.com/test?>

In the corresponding namespace, the prefix is ``adobe``, and the URI is ``http://www.adobe.com/test``.

--------------------------------------------------------------------------------

.. _namespace-object-constructors:

Namespace object constructors
*****************************

The Namespace constructor takes several forms::

  new Namespace()
  new Namespace (String uri)
  new Namespace (QName prefix)
  new Namespace (Namespace ns)
  new Namespace (String prefix, String uri)

When no argument is supplied, creates a namespace with an empty prefix and URI.

===========  =========  ========================================================================
uri          String     Creates a Namespace object with an empty prefix and the given URI.
prefix       QName      Creates a namespace with an empty prefix and the URI set to the URI of the
                        :ref:`qname-object` (if the QName object contains a URI).
ns           Namespace  Creates a copy of the given :ref:`namespace-object`.

                        If the ``Namespace()`` function is called without the ``new`` operator, and the only
                        argument is a ``Namespace`` object, the function simply returns that object,
                        rather than creating a copy.
prefix, uri  String     Creates a ``Namespace`` object with the given prefix and the given URI.
===========  =========  ========================================================================

--------------------------------------------------------------------------------

.. _namespace-object-properties:

Namespace object properties
***************************

======  ======  ======================================================================================
prefix  String  The element-name prefix associated with the namespace URI.

                The prefix value can be ``undefined``, as when a specified prefix is not a valid XML
                name. Namespaces with an undefined prefix are completely ignored; they are not
                added to an XML namespace declaration.
uri     String  The location of the namespace definition, a URI.
======  ======  ======================================================================================
