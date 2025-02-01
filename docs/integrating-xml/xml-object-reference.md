# XML Object Reference

This section provides reference details for the properties and methods of the XML object itself, and for the
related utility objects and global functions that you use to work with namespaces:

- [XML object](#xml-object)
- [Namespace object](#namespace-object)
- [QName object](#qname-object)
- [Global functions](#xml-global-functions)

---

## XML object

The `XML` object provides both static properties and functions, available through the `XML` class,
and dynamic properties and functions available through each instance.

### XML object constructor

The constructor returns the XML object representing the root node of an XML tree, which contains
additional XML objects for all contained elements.

`[new] XML (xmlCode);`

| xmlCode   | String or XML   | A string containing valid XML code, or an existing XML object.<br/><br/>> - If a valid string is supplied, returns a new XML object<br/>>   encapsulating the XML code. If the XML code cannot be parsed,<br/>>   throws a JavaScript error.<br/>> - If an existing object is supplied and the `new` operator is used,<br/>>   returns a copy of the object; otherwise, returns the object itself.   |
|-----------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

---

### XML class properties

These static properties are available through the XML class. They control how XML is parsed and generated:

| **ignoreComments**               | Boolean   | When true, comments are stripped from the XML<br/>during parsing. Default is false.                                         |
|----------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------|
| **ignoreProcessingInstructions** | Boolean   | When true, processing instructions (`<?xxx?>`<br/>elements) are stripped from the XML during<br/>parsing. Default is false. |
| **ignoreWhitespace**             | Boolean   | When true, white-space characters are stripped<br/>from the XML during parsing. Default is true.                            |
| **prettyIndent**                 | Number    | The number of spaces to use for indenting when<br/>pretty-printing. Default is 2.                                           |
| **prettyPrinting**               | Boolean   | When true, `toXMLString()` uses indenting and<br/>line feeds to create the XML string. Default is true.                     |

---

### XML class functions

These static functions are available through the XML class, and provide information about the global
settings of the XML parser.

#### defaultSettings()

`XML.defaultSettings ();`

Retrieves the default global option settings that control how XML is parsed and generated.

Returns a JavaScript object containing five properties, which correspond to the five [XML class properties](#xml-class-properties).

---

#### settings()

`XML.settings ();`

Retrieves the current global option settings that control how XML is parsed and generated.

Returns a JavaScript object containing five properties, which correspond to the five [XML class properties](#xml-class-properties)

---

#### setSettings()

`XML.setSettings (object);`

| object   | A JavaScript object containing five properties, which correspond to the five [XML class properties](#xml-class-properties)   |
|----------|------------------------------------------------------------------------------------------------------------------------------|

Sets the global option settings that control how XML is parsed and generated. You can use this to
restore settings retrieved with [settings()](#xml-settings) or [defaultSettings()](#xml-defaultsettings).

Returns `undefined`.

---

### XML object properties

The properties of the XML object are named for and contain the values of the child elements and attributes
of the element that the object represents.

| *childElementName*   | [XML object](#xml-object)   | Child-element properties are named with the child element name.                      |
|----------------------|-----------------------------|--------------------------------------------------------------------------------------|
| **@attributeName**   | [XML object](#xml-object)   | Attribute properties are named with the attribute name prefixed with the at-sign, @. |

---

### XML object functions

#### addNamespace()

`xmlObj.addNamespace (ns);`

| ns   | A [Namespace object](#namespace-object).   |
|------|--------------------------------------------|

Adds a namespace declaration to this node.

Returns this [XML object](#xml-object).

---

#### appendChild()

`xmlObj.appendChild (child);`

| child   | An [XML object](#xml-object) or any value that can be converted to a String with `toString()`.   |
|---------|--------------------------------------------------------------------------------------------------|

Appends a child element to this node, after any existing children. If the argument is not XML,
creates a new XML element that contains the string as its text value, using the same element name
as the last element currently contained in this object's node.

Returns this [XML object](#xml-object).

---

#### attributes()

`xmlObj.attributes (name);`

| name   | A String, the attribute name.   |
|--------|---------------------------------|

Retrieves a list of the named attribute elements contained in this node.

Returns an [XML object](#xml-object) containing all values of the named attribute.

---

#### child()

`xmlObj.child (which);`

| which   | A String, the element name, or a Number, a 0-based index into this node's child array.   |
|---------|------------------------------------------------------------------------------------------|

Retrieves a list of all child elements of this node of a given type.

Returns an [XML object](#xml-object) containing all child elements of the given type.

---

#### childIndex()

`xmlObj.childIndex ();`

Retrieves the 0-based position index of this node within its parent node.

Returns a Number.

---

#### children()

`xmlObj.children();`

Retrieves all of the immediate child elements of this node, including text elements.

Returns an [XML object](#xml-object) containing the child elements.

---

#### comments()

`xmlObj.comments();`

Retrieves all XML comment elements from this node.

Returns an [XML object](#xml-object) containing the comments.

---

#### contains()

`xmlObj.contains (element);`

| element   | An [XML object](#xml-object).   |
|-----------|---------------------------------|

Reports whether an element is contained in this node at any level of nesting.

Returns `true` if the element is contained in this XML tree.

---

#### copy()

`xmlObj.copy();`

Creates a copy of this node.

Returns the new XML object.

---

#### descendants()

`xmlObj.descendants ([name]);`

| name   | Optional. A String, the element name to match. If not provided, matches all<br/>elements.   |
|--------|---------------------------------------------------------------------------------------------|

Retrieves all descendent elements of this node of a given element type, or all XML-valued
descendants, at any level of nesting. Includes text elements.

Returns an [XML object](#xml-object) containing properties for each descendant element.

---

#### elements()

`xmlObj.elements (name);`

| name   | Optional. A String, the element name to match. If not provided, matches all<br/>elements.   |
|--------|---------------------------------------------------------------------------------------------|

Retrieves all of the immediate child elements of this node of the given type, or of all types. Does not
include text elements.

Returns an [XML object](#xml-object) containing properties for each child element.

---

#### hasComplexContent()

`xmlObj.hasComplexContent ();`

Reports whether this node has complex content; that is, whether it contains child elements.
Disregards contents of other kinds, including attributes, comments, processing instructions and
text nodes.

Returns `true` if this node contains child elements.

---

#### hasSimpleContent()

`xmlObj.hasSimpleContent ();`

Reports whether this node has simple content; that is, whether it represents a text node, an
attribute node, or an element without child elements (regardless of whether it also contains
attributes, comments, processing instructions or text).

Object representing comments and processing instructions do not have simple content.

Returns `true` if this node contains no child elements.

---

#### inScopeNamespaces()

`xmlObj.inScopeNamespaces ();`

Retrieves the current list of valid namespaces in this element.

Returns an Array of [Namespace object](#namespace-object), in which the last member is the default namespace.

---

#### insertChildAfter()

`xmlObj.insertChildAfter (child1, child2);`

| child1   | An [XML object](#xml-object), the existing child element after which to place the new child,<br/>or null to insert the new child at the beginning.   |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| child2   | An [XML object](#xml-object), the new child element, or any value that can be converted to a String<br/>with `toString()`.                           |

Inserts a new child element or text node into this node, after another existing child element. If the
relative element is not currently in this node, does not insert the new child.

Returns this [XML object](#xml-object).

---

#### insertChildBefore()

`xmlObj.insertChildBefore (child1, child2);`

| child1   | An [XML object](#xml-object), the existing child element before which to place the new child,<br/>or null to insert the new child at the end.   |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| child2   | An [XML object](#xml-object), the new child element, or any value that can be converted to a String<br/>with `toString()`.                      |

Inserts a new child element or text node into this node, before another existing child element. If the
relative element is not currently in this node, does not insert the new child.

Returns this [XML object](#xml-object).

---

#### length()

`xmlObj.length ();`

Reports the number of child elements contained in this node. The minimum number is 1, the
element that this object represents.

Returns a Number.

---

#### localName()

`xmlObj.localName ();`

Retrieves the local name of this element; that is, the element name, without any namespace prefix.

Returns a String.

---

#### name()

`xmlObj.name ();`

Retrieves the full name of this element, with the namespace information.

Returns a [QName object](#qname-object) containing the element name and namespace URI.

---

#### namespace()

`xmlObj.namespace ();`

Retrieves the namespace URI of this element.

Returns a String.

---

#### nodeKind()

`xmlObj.nodeKind ();`

Reports the type of this node.

Returns a String, one of:

- `element`
- `attribute`
- `comment`
- `processing-instruction`
- `text`

---

#### namespaceDeclarations()

`xmlObj.namespaceDeclarations ();`

Retrieves all of the namespace declarations contained in this node.

Returns an Array of [Namespace object](#namespace-object).

---

#### normalize()

`xmlObj.normalize ();`

Puts all text nodes in this and all descendant XML objects into a normal form by merging adjacent
text nodes and eliminating empty text nodes.

Returns this [XML object](#xml-object).

---

#### parent()

`xmlObj.parent ();`

Retrieves the parent node of this node.

Returns an [XML object](#xml-object), or `null` for the root element.

---

#### prependChild()

`xmlObj.prependChild (child);`

| child   | An [XML object](#xml-object) or string.   |
|---------|-------------------------------------------|

Prepends a child element to this node, before any existing children. If you prepend a string to a text
element, the result is two text elements; call [normalize()](#xml-object-normalize) to concatenate them into a single text
string.

Returns this [XML object](#xml-object).

---

#### processingInstructions()

`xmlObj.processingInstructions ([name]);`
name

A String, the name of a processing instruction, or null to get all processing
instructions.

Retrieves processing instructions contained in this node.

Returns an [XML object](#xml-object) containing the children of this object that are processing instructions,
matching the name if supplied.

---

#### replace()

`xmlObj.replace (name, value);`

| name   | An element or attribute name, with or without the 0-based position index of a<br/>specific element, or the wildcard string `"*"`.<br/><br/>- If no position index is supplied, replaces the value of all matching elements.<br/>- If the wildcard is supplied, replaces the value of all contained elements. When an<br/>  element contain subelements, those are removed, and only the replacement<br/>  value remains.   |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| value  | An [XML object](#xml-object) or any value that can be converted to a String with `toString()`.                                                                                                                                                                                                                                                                                                                             |

Replaces one or more property values in this node.

If the named element does not exist, appends the given value as a text element.

Returns this [XML object](#xml-object).

---

#### setChildren()

`xmlObj.setChildren (value);`

| value   | An [XML object](#xml-object) or any value that can be converted to a String with `toString()`.   |
|---------|--------------------------------------------------------------------------------------------------|

Replaces all of the XML-valued properties in this object with a new value, which can be a simple text
element, or can contain another set of XML properties.

Returns this [XML object](#xml-object).

---

#### setLocalName()

`xmlObj.setLocalName(name);`

| name   | A String, the new name.   |
|--------|---------------------------|

Replaces the local name of this object; that is, the element name without any namespace prefix.

Returns this [XML object](#xml-object).

---

#### setName()

`xmlObj.setName(name);`

| name   | A String, the new name.   |
|--------|---------------------------|

Replaces the full name of this object; that is, the element name and its namespace prefix.

Returns this [XML object](#xml-object).

---

#### setNamespace()

`xmlObj.setNamespace(ns);`

| ns   | A Namespace object for a namespace that has been declared in the tree above this element.   |
|------|---------------------------------------------------------------------------------------------|

Sets the namespace for this XML element. If the namespace has not been declared in the tree above
this element, add a namespace declaration instead.

Returns this [XML object](#xml-object).

---

#### text()

`xmlObj.text();`

Retrieves text nodes from this element.

Returns an [XML object](#xml-object) containing all properties of this object that represent XML text nodes.

---

#### toString()

`xmlObj.toString();`

Creates a string representation of this object.

- For text and attribute nodes, this is the textual value of the node.
- For other elements, it is the result of [toXMLString()](#xml-object-toxmlstring).
- If this XML object is a list, concatenates the result of calling the function on each contained element.

Returns a String.

---

#### toXMLString()

`xmlObj.toXMLString();`

Creates an XML-encoded string representation of this [XML object](#xml-object).

This result includes the start tag, attributes and end tag of the XML object, regardless of its content. Formats the string as specified by the global settings [XML.prettyPrinting](#xml-class-properties) and [XML.prettyIndent](#xml-class-properties).

Returns a String.

---

#### xpath()

`xmlObj.xpath (expression[, variables]);`

| expression   | A String containing an XPath expression.<br/><br/>#### NOTE<br/>In this context, include the actual top level element. For example, an<br/>expression for the example XML must start with "/bookstore". This is unlike<br/>JavaScript property access, where the top level element is implied.   |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| variables    | Optional. A JavaScript object containing variable definitions. The properties are used<br/>to look up XPath variables contained in the expression. For example, if the<br/>expression contains the variable `$abc`, the value is in the object's `abc` property.                                 |

Evaluates an XPath expression in accordance with the W3C XPath recommendation, using this XML
object as the context node. The context position and size are set to 1, and all variables are initially
unbound. If this XML object is a list, evaluates all contained XML element nodes (not comments or
other node types) and return the results in a list in the order of execution.

If the XPath expression does not evaluate to a node list, throws a JavaScript exception.

Returns an [XML object](#xml-object), the result of evaluation.

---

## Global functions

These functions are available in the JavaScript global namespace.

### isXMLName()

`isXMLName (String name)`

| name   | A string.   |
|--------|-------------|

Reports whether a string contains a name that conforms to valid XML syntax.

!!! note
    This implementation uses the same rules as for a JavaScript name, except for the '$' character,
which is disallowed, and the '-' character, which as added. It does not follow the W3C definition of an
XML name, which adds more Unicode characters to the valid set of characters.

Returns `true` if the name is a valid XML name, `false` otherwise.

---

### setDefaultXMLNamespace()

`setDefaultXMLNamespace (Namespace ns)`

| ns   | A Namespace object. Any prefix is ignored.   |
|------|----------------------------------------------|

Sets the default namespace for XML objects. You can also set the default namespace using this
syntax:

```default
default xml namespace = Namespace object
default xml namespace = URL_string
```

Returns `undefined`.

---

## QName object

This object encapsulates a fully qualified XML name, the combination of a local XML name and its
namespace URI.

---

### QName object constructors

The constructor takes several forms:

```default
new QName ()
new QName (name)
new QName (ns)
new QName (uri, name)
```

When no arguments are supplies, creates a `QName` object with an empty local name and no URI.

| name      | String    | Creates a `QName` object with the given local name and the URI of the default<br/>namespace. Can be the wildcard character, "\*".                                                                                                   |
|-----------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| name      | QName     | Creates a copy of an existing [QName object](#qname-object).                                                                                                                                                                        |
| ns        | Namespace | Creates a `QName` object with an empty local name and the URI of the [Namespace object](#namespace-object).                                                                                                                         |
| uri, name | String    | Create a `QName` object with the given namespace URI and local name.<br/><br/>If the local name is supplied as the wildcard character, "\*", the `uri` argument<br/>is ignored, and the URI value is that of the default namespace. |

---

### QName object properties

| name   | String   | The local element name portion of the XML element's fully qualified XML name.   |
|--------|----------|---------------------------------------------------------------------------------|
| uri    | String   | The namespace prefix of the XML element's fully qualified XML name.             |

---

## Namespace object

This object encapsulates the definition of an XML namespace. A namespace associates an XML-name
prefix with a complete URI. The prefix is a string that precedes the local name of an XML element or
attribute and identifies the namespace, while the URI points to the actual location where the definition of
the namespace is found.

For example, this XML definition contains a namespace declaration:

```default
.. code-block::xml

  <?xml xmlns:adobe=http://www.adobe.com/test?>
```

In the corresponding namespace, the prefix is `adobe`, and the URI is `http://www.adobe.com/test`.

---

### Namespace object constructors

The Namespace constructor takes several forms:

```default
new Namespace()
new Namespace (String uri)
new Namespace (QName prefix)
new Namespace (Namespace ns)
new Namespace (String prefix, String uri)
```

When no argument is supplied, creates a namespace with an empty prefix and URI.

| uri         | String    | Creates a Namespace object with an empty prefix and the given URI.                                                                                                                                                                                                           |
|-------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| prefix      | QName     | Creates a namespace with an empty prefix and the URI set to the URI of the<br/>[QName object](#qname-object) (if the QName object contains a URI).                                                                                                                           |
| ns          | Namespace | Creates a copy of the given [Namespace object](#namespace-object).<br/><br/>If the `Namespace()` function is called without the `new` operator, and the only<br/>argument is a `Namespace` object, the function simply returns that object,<br/>rather than creating a copy. |
| prefix, uri | String    | Creates a `Namespace` object with the given prefix and the given URI.                                                                                                                                                                                                        |

---

### Namespace object properties

| prefix   | String   | The element-name prefix associated with the namespace URI.<br/><br/>The prefix value can be `undefined`, as when a specified prefix is not a valid XML<br/>name. Namespaces with an undefined prefix are completely ignored; they are not<br/>added to an XML namespace declaration.   |
|----------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| uri      | String   | The location of the namespace definition, a URI.                                                                                                                                                                                                                                       |
