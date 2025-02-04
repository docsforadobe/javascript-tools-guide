# XML Object Reference

This section provides reference details for the properties and methods of the XML object itself, and for the related utility objects and global functions that you use to work with namespaces:

- [XML object](#xml-object)
- [Namespace object](#namespace-object)
- [QName object](#qname-object)
- [Global functions](#global-functions)

## XML Object

The `XML` object provides both static properties and functions, available through the `XML` class, and dynamic properties and functions available through each instance.

### XML object constructor

The constructor returns the XML object representing the root node of an XML tree, which contains additional XML objects for all contained elements.

`[new] XML (xmlCode);`

+-----------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Property  |     Type      |                                                                    Description                                                                     |
+===========+===============+====================================================================================================================================================+
| `xmlCode` | String or XML | A string containing valid XML code, or an existing XML object.                                                                                     |
|           |               |                                                                                                                                                    |
|           |               | - If a valid string is supplied, returns a new XML object encapsulating the XML code. If the XML code cannot be parsed, throws a JavaScript error. |
|           |               | - If an existing object is supplied and the `new` operator is used, returns a copy of the object; otherwise, returns the object itself.            |
+-----------+---------------+----------------------------------------------------------------------------------------------------------------------------------------------------+


---

## XML Settings

These static properties are available through the XML class. They control how XML is parsed and generated:

|            Property            |  Type   |                                                             Description                                                             |
| ------------------------------ | ------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `ignoreComments`               | Boolean | Description When `true`, comments are stripped from the XML during parsing. Default is `false`.                                     |
| `ignoreProcessingInstructions` | Boolean | Description When `true`, processing instructions (`<?xxx?>` elements) are stripped from the XML during parsing. Default is `false`. |
| `ignoreWhitespace`             | Boolean | Description When `true`, white-space characters are stripped from the XML during parsing. Default is `true`.                        |
| `prettyIndent`                 | Number  | Description The number of spaces to use for indenting when pretty-printing. Default is 2.                                           |
| `prettyPrinting`               | Boolean | Description When `true`, `toXMLString()` uses indenting and line feeds to create the XML string. Default is `true`.                 |

---

## XML Class Methods

These static functions are available through the XML class, and provide information about the global settings of the XML parser.

### XML.defaultSettings()

`XML.defaultSettings();`

#### Description

Retrieves the default global option settings that control how XML is parsed and generated.

#### Returns

Returns a JavaScript object containing five properties, which correspond to the five [XML Settings](#xml-settings).

---

### XML.settings()

`XML.settings();`

#### Description

Retrieves the current global option settings that control how XML is parsed and generated.

#### Returns

Returns a JavaScript object containing five properties, which correspond to the five [XML Settings](#xml-settings)

---

### XML.setSettings()

`XML.setSettings(object);`

#### Description

Sets the global option settings that control how XML is parsed and generated. You can use this to restore settings retrieved with [settings()](#xml-settings) or [defaultSettings()](#xmldefaultsettings).

#### Parameters

| Parameter |  Type  |                                                Description                                                 |
| --------- | ------ | ---------------------------------------------------------------------------------------------------------- |
| `object`  | Object | A JavaScript object containing five properties, which correspond to the five [XML Settings](#xml-settings) |

#### Returns

Nothing

---

## XML Object Attributes

The properties of the XML object are named for and contain the values of the child elements and attributes of the element that the object represents.

### xmlObj.childElementName

`xmlObj.childElementName`

#### Description

Child-element properties are named with the child element name.

#### Type

[XML object](#xml-object)

---

### xmlObj.@attributeName

`xmlObj.@attributeName`

#### Description

Attribute properties are named with the attribute name prefixed with the at-sign, `@`.

#### Type

[XML object](#xml-object)

---

## XML Object Methods

### XML.addNamespace()

`xmlObj.addNamespace(ns);`

#### Description

Adds a namespace declaration to this node.

#### Parameters

| Parameter |                 Type                  |         Description          |
| --------- | ------------------------------------- | ---------------------------- |
| `ns`      | [Namespace object](#namespace-object) | Namespace declaration to add |

#### Returns

This [XML object](#xml-object).

---

### XML.appendChild()

`xmlObj.appendChild(child);`

#### Description

Appends a child element to this node, after any existing children. If the argument is not XML, creates a new XML element that contains the string as its text value, using the same element name as the last element currently contained in this object's node.

#### Parameters

| Parameter |                                            Type                                             |       Description       |
| --------- | ------------------------------------------------------------------------------------------- | ----------------------- |
| `child`   | [XML object](#xml-object), or any value that can be converted to a String with `toString()` | Child element to append |

#### Returns

This [XML object](#xml-object).

---

### XML.attributes()

`xmlObj.attributes(name);`

#### Description

Retrieves a list of the named attribute elements contained in this node.

#### Parameters

| Parameter |  Type  |     Description     |
| --------- | ------ | ------------------- |
| `name`    | String | Ahe attribute name. |

#### Returns

An [XML object](#xml-object) containing all values of the named attribute.

---

### XML.child()

`xmlObj.child(which);`

#### Description

Retrieves a list of all child elements of this node of a given type.

#### Parameters

| Parameter |       Type       |                                 Description                                  |
| --------- | ---------------- | ---------------------------------------------------------------------------- |
| `which`   | String or Number | The element name, or a Number, a 0-based index into this node's child array. |

#### Returns

An [XML object](#xml-object) containing all child elements of the given type.

---

### XML.childIndex()

`xmlObj.childIndex ();`

#### Description

Retrieves the 0-based position index of this node within its parent node.

#### Returns

Number

---

### XML.children()

`xmlObj.children();`

#### Description

Retrieves all of the immediate child elements of this node, including text elements.

#### Returns

An [XML object](#xml-object) containing the child elements.

---

### XML.comments()

`xmlObj.comments();`

#### Description

Retrieves all XML comment elements from this node.

#### Returns

An [XML object](#xml-object) containing the comments.

---

### XML.contains()

`xmlObj.contains(element);`

#### Description

Reports whether an element is contained in this node at any level of nesting.

#### Parameters

| Parameter |           Type            |   Description    |
| --------- | ------------------------- | ---------------- |
| `element` | [XML object](#xml-object) | Element to check |

#### Returns

Boolean. `true` if the element is contained in this XML tree.

---

### XML.copy()

`xmlObj.copy();`

#### Description

Creates a copy of this node.

#### Returns

The new XML object.

---

### XML.descendants()

`xmlObj.descendants([name]);`

#### Description

Retrieves all descendent elements of this node of a given element type, or all XML-valued descendants, at any level of nesting. Includes text elements.

#### Parameters

| Parameter |  Type  |                                 Description                                 |
| --------- | ------ | --------------------------------------------------------------------------- |
| `name`    | String | Optional. The element name to match. If not provided, matches all elements. |

#### Returns

An [XML object](#xml-object) containing properties for each descendant element.

---

### XML.elements()

`xmlObj.elements(name);`

#### Description

Retrieves all of the immediate child elements of this node of the given type, or of all types. Does not include text elements.

#### Parameters

| Parameter |  Type  |                                 Description                                 |
| --------- | ------ | --------------------------------------------------------------------------- |
| `name`    | String | Optional. The element name to match. If not provided, matches all elements. |

#### Returns

An [XML object](#xml-object) containing properties for each child element.

---

### XML.hasComplexContent()

`xmlObj.hasComplexContent();`

#### Description

Reports whether this node has complex content; that is, whether it contains child elements. Disregards contents of other kinds, including attributes, comments, processing instructions and text nodes.

#### Returns

Boolean. `true` if this node contains child elements.

---

### XML.hasSimpleContent()

`xmlObj.hasSimpleContent();`

#### Description

Reports whether this node has simple content; that is, whether it represents a text node, an attribute node, or an element without child elements (regardless of whether it also contains attributes, comments, processing instructions or text).

Object representing comments and processing instructions do not have simple content.

#### Returns

Boolean. `true` if this node contains no child elements.

---

### XML.inScopeNamespaces()

`xmlObj.inScopeNamespaces();`

#### Description

Retrieves the current list of valid namespaces in this element.

#### Returns

An Array of [Namespace object](#namespace-object), in which the last member is the default namespace.

---

### XML.insertChildAfter()

`xmlObj.insertChildAfter(child1, child2);`

#### Description

Inserts a new child element or text node into this node, after another existing child element. If the relative element is not currently in this node, does not insert the new child.

#### Parameters

| Parameter |           Type            |                                                    Description                                                     |
| --------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `child1`  | [XML object](#xml-object) | The existing child element after which to place the new child, or `null` to insert the new child at the beginning. |
| `child2`  | [XML object](#xml-object) | The new child element, or any value that can be converted to a String with `toString()`.                           |

#### Returns

This [XML object](#xml-object).

---

### XML.insertChildBefore()

`xmlObj.insertChildBefore(child1, child2);`

#### Description

Inserts a new child element or text node into this node, before another existing child element. If the relative element is not currently in this node, does not insert the new child.

#### Parameters

| Parameter |                                                                 Type                                                                  | Description |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `child1`  | [XML object](#xml-object) The existing child element before which to place the new child, or null to insert the new child at the end. |             |
| `child2`  | [XML object](#xml-object) The new child element, or any value that can be converted to a String with `toString()`.                    |             |

#### Returns

This [XML object](#xml-object).

---

### XML.length()

`xmlObj.length();`

#### Description

Reports the number of child elements contained in this node. The minimum number is 1, the element that this object represents.

#### Returns

Number

---

### XML.localName()

`xmlObj.localName();`

#### Description

Retrieves the local name of this element; that is, the element name, without any namespace prefix.

#### Returns

String

---

### XML.name()

`xmlObj.name();`

#### Description

Retrieves the full name of this element, with the namespace information.

#### Returns

A [QName object](#qname-object) containing the element name and namespace URI.

---

### XML.namespace()

`xmlObj.namespace();`

#### Description

Retrieves the namespace URI of this element.

#### Returns

String

---

### XML.nodeKind()

`xmlObj.nodeKind();`

#### Description

Reports the type of this node.

#### Returns

A String, one of:

- `element`
- `attribute`
- `comment`
- `processing-instruction`
- `text`

---

### XML.namespaceDeclarations()

`xmlObj.namespaceDeclarations();`

#### Description

Retrieves all of the namespace declarations contained in this node.

#### Returns

An Array of [Namespace object](#namespace-object).

---

### XML.normalize()

`xmlObj.normalize();`

#### Description

Puts all text nodes in this and all descendant XML objects into a normal form by merging adjacent text nodes and eliminating empty text nodes.

#### Returns

This [XML object](#xml-object).

---

### XML.parent()

`xmlObj.parent();`

#### Description

Retrieves the parent node of this node.

#### Returns

An [XML object](#xml-object), or `null` for the root element.

---

### XML.prependChild()

`xmlObj.prependChild(child);`

#### Description

Prepends a child element to this node, before any existing children. If you prepend a string to a text element, the result is two text elements; call [normalize()](#xmlnormalize) to concatenate them into a single text string.

#### Parameters

| Parameter |                Type                 |       Description        |
| --------- | ----------------------------------- | ------------------------ |
| `child`   | [XML object](#xml-object) or String | Child element to prepend |

#### Returns

This [XML object](#xml-object).

---

### XML.processingInstructions()

`xmlObj.processingInstructions ([name]);`

#### Description

A String, the name of a processing instruction, or null to get all processing instructions.

Retrieves processing instructions contained in this node.

#### Returns

An [XML object](#xml-object) containing the children of this object that are processing instructions, matching the name if supplied.

---

### XML.replace()

`xmlObj.replace(name, value);`

#### Description

Replaces one or more property values in this node.

If the named element does not exist, appends the given value as a text element.

#### Parameters

+-----------+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter |                                            Type                                            |                                                                                 Description                                                                                  |
+===========+============================================================================================+==============================================================================================================================================================================+
| `name`    | String                                                                                     | An element or attribute name, with or without the 0-based position index of a specific element, or the wildcard string `"*"`.                                                |
|           |                                                                                            |                                                                                                                                                                              |
|           |                                                                                            | - If no position index is supplied, replaces the value of all matching elements.                                                                                             |
|           |                                                                                            | - If the wildcard is supplied, replaces the value of all contained elements. When an element contain subelements, those are removed, and only the replacement value remains. |
+-----------+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `value`   | [XML object](#xml-object) or any value that can be converted to a String with `toString()` | Value to replace with                                                                                                                                                        |
+-----------+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### Returns

This [XML object](#xml-object).

---

### XML.setChildren()

`xmlObj.setChildren(value);`

#### Description

Replaces all of the XML-valued properties in this object with a new value, which can be a simple text element, or can contain another set of XML properties.

#### Parameters

| Parameter |                                            Type                                             |      Description      |
| --------- | ------------------------------------------------------------------------------------------- | --------------------- |
| `value`   | [XML object](#xml-object) or any value that can be converted to a String with `toString()`. | Value to replace with |

#### Returns

This [XML object](#xml-object).

---

### XML.setLocalName()

`xmlObj.setLocalName(name);`

#### Description

Replaces the local name of this object; that is, the element name without any namespace prefix.

#### Parameters

| Parameter |  Type  |  Description  |
| --------- | ------ | ------------- |
| `name`    | String | The new name. |

#### Returns

This [XML object](#xml-object).

---

### XML.setName()

`xmlObj.setName(name);`

#### Description

Replaces the full name of this object; that is, the element name and its namespace prefix.

#### Parameters

| Parameter |  Type  |  Description  |
| --------- | ------ | ------------- |
| `name`    | String | The new name. |

#### Returns

This [XML object](#xml-object).

---

### XML.setNamespace()

`xmlObj.setNamespace(ns);`

#### Description

Sets the namespace for this XML element. If the namespace has not been declared in the tree above this element, add a namespace declaration instead.

#### Parameters

| Parameter |       Type       |                           Description                            |
| --------- | ---------------- | ---------------------------------------------------------------- |
| `ns`      | Namespace object | Namespace that has been declared in the tree above this element. |

#### Returns

This [XML object](#xml-object).

---

### XML.text()

`xmlObj.text();`

#### Description

Retrieves text nodes from this element.

An [XML object](#xml-object) containing all properties of this object that represent XML text nodes.

---

### XML.toString()

`xmlObj.toString();`

#### Description

Creates a string representation of this object.

- For text and attribute nodes, this is the textual value of the node.
- For other elements, it is the result of [toXMLString()](#xmltoxmlstring).
- If this XML object is a list, concatenates the result of calling the function on each contained element.

#### Returns

String

---

### XML.toXMLString()

`xmlObj.toXMLString();`

#### Description

Creates an XML-encoded string representation of this [XML object](#xml-object).

This result includes the start tag, attributes and end tag of the XML object, regardless of its content. Formats the string as specified by the global settings [XML.prettyPrinting](#xml-settings) and [XML.prettyIndent](#xml-settings).

#### Returns

String

---

### XML.xpath()

`xmlObj.xpath(expression[, variables]);`

#### Description

Evaluates an XPath expression in accordance with the W3C XPath recommendation, using this XML object as the context node. The context position and size are set to 1, and all variables are initially unbound. If this XML object is a list, evaluates all contained XML element nodes (not comments or other node types) and return the results in a list in the order of execution.

If the XPath expression does not evaluate to a node list, throws a JavaScript exception.

#### Parameters

|  Parameter   |  Type  |                                                                                                                                          Description                                                                                                                                           |
| ------------ | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `expression` | String | A String containing an XPath expression.<br/><br/>#### NOTE<br/>In this context, include the actual top level element. For example, an<br/>expression for the example XML must start with "/bookstore". This is unlike<br/>JavaScript property access, where the top level element is implied. |
| `variables`  | Object | Optional. A JavaScript object containing variable definitions. The properties are used to look up XPath variables contained in the expression. For example, if the expression contains the variable `$abc`, the value is in the object's `abc` property.                                       |

#### Returns

An [XML object](#xml-object), the result of evaluation.

---

## Global functions

These functions are available in the JavaScript global namespace.

### isXMLName()

`isXMLName(String name)`

#### Description

Reports whether a string contains a name that conforms to valid XML syntax.

!!! note
    This implementation uses the same rules as for a JavaScript name, except for the '$' character, which is disallowed, and the '-' character, which as added.

    It does not follow the W3C definition of an XML name, which adds more Unicode characters to the valid set of characters.

#### Parameters

| Parameter |  Type  |            Description            |
| --------- | ------ | --------------------------------- |
| `name`    | String | Whether the string is an XML Name |

#### Returns

Boolean. `true` if the name is a valid XML name, `false` otherwise.

---

### setDefaultXMLNamespace()

`setDefaultXMLNamespace(Namespace ns)`

#### Description

Sets the default namespace for XML objects. You can also set the default namespace using this syntax:

```javascript
default xml namespace = Namespace object
default xml namespace = URL_string
```

#### Parameters

| Parameter |       Type       |                   Description                    |
| --------- | ---------------- | ------------------------------------------------ |
| `ns`      | Namespace object | Object to set as default. Any prefix is ignored. |

#### Returns

Nothing

---

## QName Object

This object encapsulates a fully qualified XML name, the combination of a local XML name and its namespace URI.

### QName object constructor

The constructor takes several forms:

```javascript
new QName ()
new QName (name)
new QName (ns)
new QName (uri, name)
```

When no arguments are supplies, creates a `QName` object with an empty local name and no URI.

| Parameter |   Type    |                                                                                                      Description                                                                                                       |
| --------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name      | String    | Creates a `QName` object with the given local name and the URI of the default namespace. Can be the wildcard character, "\*".                                                                                          |
| name      | QName     | Creates a copy of an existing [QName object](#qname-object).                                                                                                                                                           |
| ns        | Namespace | Creates a `QName` object with an empty local name and the URI of the [Namespace object](#namespace-object).                                                                                                            |
| uri, name | String    | Create a `QName` object with the given namespace URI and local name. If the local name is supplied as the wildcard character, "\*", the `uri` argument is ignored, and the URI value is that of the default namespace. |

---

## QName Object Attributes

### QName.name

`QName.name`

#### Description

The local element name portion of the XML element's fully qualified XML name.

#### Type

String

---

### QName.uri

`QName.uri`

#### Description

The namespace prefix of the XML element's fully qualified XML name.

#### Type

String

---

## Namespace object

This object encapsulates the definition of an XML namespace. A namespace associates an XML-name prefix with a complete URI. The prefix is a string that precedes the local name of an XML element or attribute and identifies the namespace, while the URI points to the actual location where the definition of the namespace is found.

For example, this XML definition contains a namespace declaration:

```xml
<?xml xmlns:adobe=http://www.adobe.com/test?>
```

In the corresponding namespace, the prefix is `adobe`, and the URI is `http://www.adobe.com/test`.

---

### Namespace object constructor

The Namespace constructor takes several forms:

```javascript
new Namespace()
new Namespace (String uri)
new Namespace (QName prefix)
new Namespace (Namespace ns)
new Namespace (String prefix, String uri)
```

When no argument is supplied, creates a namespace with an empty prefix and URI.

#### Parameters

|   Parameter   |   Type    |                                                                                                                         Description                                                                                                                         |
| ------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `uri`         | String    | Creates a Namespace object with an empty prefix and the given URI.                                                                                                                                                                                          |
| `prefix`      | QName     | Creates a namespace with an empty prefix and the URI set to the URI of the [QName object](#qname-object) (if the QName object contains a URI).                                                                                                              |
| `ns`          | Namespace | Creates a copy of the given [Namespace object](#namespace-object). If the `Namespace()` function is called without the `new` operator, and the only argument is a `Namespace` object, the function simply returns that object, rather than creating a copy. |
| `prefix, uri` | String    | Creates a `Namespace` object with the given prefix and the given URI.                                                                                                                                                                                       |

---

## Namespace Object Attributes

### Namespace.prefix

`namespace.prefix`

#### Description

The element-name prefix associated with the namespace URI. The prefix value can be `undefined`, as when a specified prefix is not a valid XML name.

Namespaces with an undefined prefix are completely ignored; they are not added to an XML namespace declaration.

#### Type

String

---

### Namespace.uri

`namespace.uri`

#### Description

The location of the namespace definition, a URI.

#### Type

String
