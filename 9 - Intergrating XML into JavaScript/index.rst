Integrating XML into JavaScript
ExtendScript defines the XML object, which allows you to process XML with your JavaScript scripts. This
feature offers a subset of the functionality specified by the ECMA-357 specification (E4X). For more
information on this standard, see:
http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-357.pdf

The XML Object
The XML object represents an XML element node in an XML tree. The topmost XML object for an XML file
represents the root node. It acts as a list, which contains additional XML objects for each element. These in
turn contain XML objects for their own member elements, and so on.
The child elements of an element tree are available as properties of the XML object for the parent. The
name of the property corresponds to the name of the element. Each property contains an array of XML
objects, each of which represents one element of the named type.
For example, suppose you have the following, minimal XML code:
<rootElement>
<elementA>
<elementB></elementB>
</elementA>
<elementA>
<elementB></elementB>
</elementA>
</rootElement>

In a JavaScript script, the XML object that you create from this XML code represents the root element:
var myRoot = new XML ( "<rootElement> <elementA> <elementB></elementB> </elementA>
<elementA> <elementB></elementB> </elementA>
</rootElement>");

You can assign a constant to an XML value directly. The following implicitly creates the XML object
assigned to myRoot:
var myRoot = <rootElement>
<elementA>
<elementB></elementB>
</elementA>
<elementA>
<elementB></elementB>
</elementA>
</rootElement> ;

The object myRoot contains a property named elementA, which contains two XML objects for the two
instances of that element. Each of these, in turn, contains an elementB property, which contains one
empty XML object:
var elemB1 = myRoot.elementA[0].elementB[0];

If an element is empty in the XML, the corresponding property exists and contains an empty XML object; it
is never null or undefined.

Accessing XML elements
This sample XML code is used for examples throughout this chapter:
<bookstore>
<book category="COOKING">
<title lang="en">The Boston Cooking-School Cookbook</title>
<author>Fannie Merrit Farmer</author>
<year>1896</year>
<price>49.99</price>
</book>
<book category="CHILDREN">
<title lang="en">The Wonderful Wizard of Oz</title>
<author>L. Frank Baum</author>
<year>1900</year>
<price>39.95</price>
</book>
<book category="CHILDREN">
<title lang="en">Alice’s Adventures in Wonderland</title>
<author>Charles "Lewis Carroll" Dodgeson</author>
<author>Charles Dodgeson</author>
<author>Lewis Carroll</author>
<year>1865</year>
<price>29.99</price>
</book>
<book category="MUSIC">
<title lang="en">Gilbert and Sullivan Opera; A History and a Comment</title>
<author>H. M. Walbrook</author>
<year>1922</year>
<price>30.00</price>
</book>
</bookstore>

To encapsulate this code in an XML object, serialize it into a string and pass that string to the constructor:
var bookXmlStr = "...";
var bookstoreXML = new XML (bookXmlStr);

Using this example, the root element <bookstore>, is represented by the XML object returned from the
constructor. Each of the <book> elements is available as a member of the book property of the XML object.
The Javascript statement bookstoreXML.book; returns the entire list of books.
The statement bookstoreXML.book[0]; returns the XML object for the first book.
The statement bookstoreXML.book[0].author; returns all authors of the first book.
For additional ways of accessing elements in the tree, see "Retrieving contained elements" on page 241,
and "Creating and accessing namespaces" on page 242.

Accessing XML attributes
Attribute are properties of their parent elements. In ExtendScript, access an attribute name by using a
preceding at-sign (@). An attribute property is a one-element list, which contains an XML object for the
value of the attribute. For example:
bookstoreXML.book [0].@category;

This returns the category attribute of the first book, whose value is the string "COOKING".
To access all category attributes of all books, use this statement:
bookstoreXML.book.@category

You can reference a set of elements with a particular attribute value, using a predicate in this form:
element.(@attribute == value)

For example, this statement returns only book elements that have a category attribute with the value
"CHILDREN":
bookstoreXML.book.(@category == "CHILDREN");

Viewing XML objects
The XML object, like all ExtendScript objects, has a toString() method that serializes the contents into a
string. In this case, the string contains only the text content of the element, not the tags. For example, for
the element <x>text</x>, the toString() method returns "text".
This method is called when you evaluate the object in the JavaScript Console of the ExtendScript Toolkit. It
recreates the XML text that the object encapsulates. Thus, if you evaluate the object
bookstoreXML.book[1] in the Console, you see the XML text for the encapsulated tree, formatted with
line feeds and spaces:
> bookstoreXML.book[1];
<book category="CHILDREN">
<title lang="en">The Wonderful Wizard of Oz</title>
<author>L. Frank Baum</author>
<year>1900</year>
<price>39.95</price>
</book>

If you evaluate an object with a text value, you see the text value. For example:
> bookstoreXML.book[1].@category;
CHILDREN

If you access multiple values, the values are concatenated:
> bookstoreXML.book.@category
COOKINGCHILDRENCHILDRENMUSIC

The toXMLString() method serializes the entire element, including the tags, into a string. For example, for
the element <x>text</x>, the method returns "<x>text</x>".

Modifying XML elements and attributes
You can change an element by assigning a value to the corresponding property.
If the value assigned is an XML element, the element is simply replaced. If there are multiple elements
of the same type, the first element is replaced, and all other elements are deleted.
If the value assigned is not XML, it is converted to a string, and the content of the element is replaced
with that string.
If no element of this type is present, a new element is appended to the XML.
You can change the values of attributes using the same technique.
Modification examples
In the sample XML, the third book has several <author> elements. This statement replaces all of them
with a single element, containing a new string:
bookstoreXML.book[2].author = "Charles ’Lewis Carroll’ Dodgeson";

The result is this XML:
<book category="CHILDREN">
<title lang="en">Alice’s Adventures in Wonderland</title>
<author>Charles ’Lewis Carroll’ Dodgeson</author>
<year>1865</year>
<price>29.99</price>
</book>

To replace just the first author, leaving all the other authors in place, use this statement:
bookstoreXML.book[2].author[0] = "Charles Dodgeson, aka Lewis Carroll";

This statement changes the content of the <year> element in the second book. ExtendScript
automatically converts the numeric value to a string:
bookstoreXML.book[1].year = 1901;

This following statement adds a new <rating> element to the second book:
bookstoreXML.book[1].rating = "*****";

The result is this XML:
<book category="CHILDREN">
<title lang="en">The Wonderful Wizard of Oz</title>
<author>L. Frank Baum</author>
<year>1900</year>
<price>39.95</price>
<rating>*****</rating>
</book>

This statement changes the value of the category attribute of the second book:
bookstoreXML.book[1].@category = "LITERATURE, FANTASY"

The result is this XML:
<book category="LITERATURE, FANTASY">
<title lang="en">The Wonderful Wizard of Oz</title>
...

Deleting elements and attributes
To delete an element or attribute in the XML, use the JavaScript delete operator to delete the
corresponding element or attribute property. If there are multiple instances of an element, you can delete
all, or refer to a single one by its index.
Deletion examples
This statement deletes all authors from the third book:
delete bookstoreXML.book[2].author;

This statement deletes only the second author from the third book:
delete bookstoreXML.book[2].author[1];

This statement deletes the category attribute from the third book:
delete bookstoreXML.book[2].@category;

Retrieving contained elements
The XML object provides methods that allow you to retrieve elements contained at various levels of the
tree:
XML.children() gets the direct child elements, including text elements.
XML.elements() gets the direct child elements that are XML tags, but does not get text.
XML.descendants() allows you to match a specific tag, and gets all matching elements at any level of

nesting. You can also use a "double dot" notation to access descendants of an element. For example,
these statements are equivalent:

xml..title
xml.descendants("title")

For example, consider this XML code loaded into a top-level XML object named x:
<top>
<one>one text</one>
<two>
two text
<inside>inside text</inside>
</two>
top text
</top>

Here are the results of the different calls.

The result of XML.children() contains 3 elements, the direct child tags <one> and <two>, and the
directly contained text of the <top> tag:
> x.children()
<one>one text</one>
<two>
two text
<inside>inside text</inside>
</two>
top text
> x.children().length()
3

The result of XML.elements() contains 2 elements, the direct child tags <one> and <two>:
> x.elements()
<one>one text</one>
<two>
two text
<inside>inside text</inside>
</two>
> x.elements().length()
2

The result of XML.descendants() contains 7 elements, the direct child tags <one> and <two>, the
<inside> tag one level down, and the text contents of all the tags:
> x.descendants()
<one>one text</one>
one text
<two>
two text
<inside>inside text</inside>
</two>
two text
<inside>inside text</inside>
inside text
top text
> x.descendants().length()
7

Creating and accessing namespaces
Simple access statements access elements in the default namespace. If you need to define elements in
more than one namespace, you must use a Namespace object to access any elements that are NOT in the
default namespace.

Defining a namespace within the tree
You can define a namespace within an XML element using the xmlns attribute, and define elements within
the schema as belonging to that namespace. For example, these additions to the example XML add a
namespace that maps the prefix "kids" to the namespace "http://kids.mybookstore.com", and then
uses the prefix to place a particular book element in that namespace:
<bookstore xmlns:kids="http://kids.mybookstore.com">

<book category="COOKING">
<title lang="en">The Boston Cooking-School Cookbook</title>
<author>Fannie Merrit Farmer</author>
<year>1896</year>
<price>49.99</price>
</book>
<kids:book category="CHILDREN">
<title lang="en">The Wonderful Wizard of Oz</title>
<author>L. Frank Baum</author>
<year>1900</year>
<price>39.95</price>
</kids:book>
...

When this namespace is defined, the simple statement bookstoreXML.book no longer returns "The
Wonderful Wizard of Oz", because that book is no longer in the default namespace. To access that book,
you must define a Namespace object for the namespace, and use it to access the element.
For example, this JavaScript code creates a Namespace object for the namespace defined in the
<bookstore> element, and accesses the books in the namespace through that object:
var ns = new Namespace ("http://kids.mybookstore.com");
bookstoreXML.ns::book;

Setting a default namespace
By default, the default namespace is a namespace whose URI is the empty string. It is possible to set the
default namespace; in this case, simple accessors access elements that are in that namespace.
To set the default namespace, use the global function setDefaultXMLNamespace(), or this syntax:
default xml namespace = namespace_specifier;

The namespace specifier can be either a Namespace object, or a URL string. For example:
default xml namespace = "http://books.mybookstore.com";

Once you have set the default namespace:
Elements that are meant to be in the default namespace (and thus accessible with simple accessors)
must use the namespace prefix.
All elements that do not have a specific namespace assignment are in the empty namespace, rather
than the default namespace. In order to access them, you must use a Namespace object with the
empty string as the URI.

Accessing elements in namespaces
You can access elements that are in the default namespace directly, without using a Namespace
object.
If you have not set a default, you can use direct access for elements with no namespace specifier.
If you have set a default, you can use direct access for elements in that namespace.

If you have assigned an element to a namespace, and have not made it the default, you must use a
Namespace object to access those elements. For example:
var ns = new Namespace ("http://kids.mybookstore.com");
bookstoreXML.ns::book;

This returns all books that have been assigned to the "kids" namespace.
If you have set a default namespace, you can still access all objects that do not have any specific
namespace assignment by using a Namespace object for the empty string, which is the default
creation case:
var emptyNS = new Namespace ();
bookstoreXML.emptyNS::book;

This returns all books that have not been assigned to any namespace.
To access all elements, regardless of the namespace assignment, you can use an asterisk (*) wild-card
character or null as the namespace name:
bookstoreXML.*::book;

or
var nullNS = null;
bookstoreXML.nullNS::book;

Mixing XML and JavaScript
You can enclose JavaScript statements in curly brackets, and embed them into XML. The JavaScript part is
evaluated during the construction of the XML.
For example, this function returns an XML value, in which embedded JavaScript variables will be evaluated
and included:
function makeXML (first, last) {
return <person first={first} last={last}>{first + " " + last}</person>;
}

Calling this function:
makeXML ( "Jane", "Doe" );

results in this XML:
<person first="Jane" last="Doe">Jane Doe</person>

You can also use these operators on XML elements:
Use the plus operator, +, to combine XML elements into a list.
Use the == operator to make an in-depth comparison of two XML trees.

XML lists
ExtendScript defines an XMLList object, which is identical to the XML object except that you can create it
by passing it an XML list, and it creates an XML list rather than an XML tag.

All XML statements and functions that collect XML return the result as an XMLList, which can be empty if
there is no match. For example, the following statement returns an empty list:
bookstoreXML.magazine;

XML Object Reference
This section provides reference details for the properties and methods of the XML object itself, and for the
related utility objects and global functions that you use to work with namespaces:
"XML object" on page 246
"Namespace object" on page 255
"QName object" on page 255
"Global functions" on page 254

XML object
The XML object provides both static properties and functions, available through the XML class, and dynamic
properties and functions available through each instance.

XML object constructor
The constructor returns the XML object representing the root node of an XML tree, which contains
additional XML objects for all contained elements.
[new] XML (xmlCode);
xmlCode

String or XML

A string containing valid XML code, or an existing XML object.
If a valid string is supplied, returns a new XML object
encapsulating the XML code. If the XML code cannot be parsed,
throws a JavaScript error.
If an existing object is supplied and the new operator is used,
returns a copy of the object; otherwise, returns the object itself.

XML class properties
These static properties are available through the XML class. They control how XML is parsed and generated:
ignoreComments

Boolean

When true, comments are stripped from the XML
during parsing. Default is false.

ignoreProcessingInstructions

Boolean

When true, processing instructions (<?xxx?>
elements) are stripped from the XML during
parsing. Default is false.

ignoreWhitespace

Boolean

When true, white-space characters are stripped
from the XML during parsing. Default is true.


prettyIndent

Number

The number of spaces to use for indenting when
pretty-printing. Default is 2.

prettyPrinting

Boolean

When true, toXMLString() uses indenting and
line feeds to create the XML string. Default is true.

XML class functions
These static functions are available through the XML class, and provide information about the global
settings of the XML parser.
defaultSettings()
XML.defaultSettings ();

Retrieves the default global option settings that control how XML is parsed and generated.
Returns a JavaScript object containing five properties, which correspond to the five XML class
properties.
settings()
XML.settings ();

Retrieves the current global option settings that control how XML is parsed and generated.
Returns a JavaScript object containing five properties, which correspond to the five XML class
properties.
setSettings()
XML.setSettings (object);
object

A JavaScript object containing five properties, which correspond to the five XML class
properties.

Sets the global option settings that control how XML is parsed and generated. You can use this to
restore settings retrieved with settings() or defaultSettings().
Returns undefined.

XML object properties
The properties of the XML object are named for and contain the values of the child elements and attributes
of the element that the object represents.
childElementName

XML object Child-element properties are named with the child element
name.

@attributeName

XML object Attribute properties are named with the attribute name prefixed
with the at-sign, @.

XML object functions
addNamespace()
xmlObj.addNamespace (ns);
ns

A Namespace object.

Adds a namespace declaration to this node.
Returns this XML object.
appendChild()
xmlObj.appendChild (child);
child

An XML object or any value that can be converted to a String with toString().

Appends a child element to this node, after any existing children. If the argument is not XML,
creates a new XML element that contains the string as its text value, using the same element name
as the last element currently contained in this object’s node.
Returns this XML object.
attributes()
xmlObj.attributes (name);
name

A String, the attribute name.

Retrieves a list of the named attribute elements contained in this node.
Returns an XML object containing all values of the named attribute.
child()
xmlObj.child (which);
which

A String, the element name, or a Number, a 0-based index into this node’s child array.

Retrieves a list of all child elements of this node of a given type.
Returns an XML object containing all child elements of the given type.
childIndex()
xmlObj.childIndex ();

Retrieves the 0-based position index of this node within its parent node.
Returns a Number.
children()
xmlObj.children();

Retrieves all of the immediate child elements of this node, including text elements.
Returns an XML object containing the child elements.
comments()
xmlObj.comments();

Retrieves all XML comment elements from this node.
Returns an XML object containing the comments.

contains()
xmlObj.contains (element);
element

An XML object.

Reports whether an element is contained in this node at any level of nesting.
Returns true if the element is contained in this XML tree.
copy()
xmlObj.copy();

Creates a copy of this node.
Returns the new XML object.
descendants()
xmlObj.descendants ([name]);
name

Optional. A String, the element name to match. If not provided, matches all
elements.

Retrieves all descendent elements of this node of a given element type, or all XML-valued
descendants, at any level of nesting. Includes text elements.
Returns an XML object containing properties for each descendant element.
elements()
xmlObj.elements (name);
name

Optional. A String, the element name to match. If not provided, matches all
elements.

Retrieves all of the immediate child elements of this node of the given type, or of all types. Does not
include text elements.
Returns an XML object containing properties for each child element.
hasComplexContent()
xmlObj.hasComplexContent ();

Reports whether this node has complex content; that is, whether it contains child elements.
Disregards contents of other kinds, including attributes, comments, processing instructions and
text nodes.
Returns true if this node contains child elements.
hasSimpleContent()
xmlObj.hasSimpleContent ();

Reports whether this node has simple content; that is, whether it represents a text node, an
attribute node, or an element without child elements (regardless of whether it also contains
attributes, comments, processing instructions or text).
Object representing comments and processing instructions do not have simple content.
Returns true if this node contains no child elements.

inScopeNamespaces()
xmlObj.inScopeNamespaces ();

Retrieves the current list of valid namespaces in this element.
Returns an Array of Namespace objects, in which the last member is the default namespace.
insertChildAfter()
xmlObj.insertChildAfter (child1, child2);
child1

An XML object, the existing child element after which to place the new child, or null
to insert the new child at the beginning.

child2

An XML object, the new child element, or any value that can be converted to a String
with toString().

Inserts a new child element or text node into this node, after another existing child element. If the
relative element is not currently in this node, does not insert the new child.
Returns this XML object.
insertChildBefore()
xmlObj.insertChildBefore (child1, child2);
child1

An XML object, the existing child element before which to place the new child, or
null to insert the new child at the end.

child2

An XML object, the new child element, or any value that can be converted to a String
with toString().

Inserts a new child element or text node into this node, before another existing child element. If the
relative element is not currently in this node, does not insert the new child.
Returns this XML object.
length()
xmlObj.length ();

Reports the number of child elements contained in this node. The minimum number is 1, the
element that this object represents.
Returns a Number.
localName()
xmlObj.localName ();

Retrieves the local name of this element; that is, the element name, without any namespace prefix.
Returns a String.
name()
xmlObj.name ();

Retrieves the full name of this element, with the namespace information.
Returns a QName object containing the element name and namespace URI.

namespace()
xmlObj.namespace ();

Retrieves the namespace URI of this element.
Returns a String.
nodeKind()
xmlObj.nodeKind ();

Reports the type of this node.
Returns a String, one of:
element
attribute
comment
processing-instruction
text
namespaceDeclarations()
xmlObj.namespaceDeclarations ();

Retrieves all of the namespace declarations contained in this node.
Returns an Array of Namespace objects.
normalize()
xmlObj.normalize ();

Puts all text nodes in this and all descendant XML objects into a normal form by merging adjacent
text nodes and eliminating empty text nodes.
Returns this XML object.
parent()
xmlObj.parent ();

Retrieves the parent node of this node.
Returns an XML object, or null for the root element.
prependChild()
xmlObj.prependChild (child);
child

An XML object or string.

Prepends a child element to this node, before any existing children. If you prepend a string to a text
element, the result is two text elements; call normalize() to concatenate them into a single text
string.
Returns this XML object.

processingInstructions()
xmlObj.processingInstructions ([name]);
name

A String, the name of a processing instruction, or null to get all processing
instructions.

Retrieves processing instructions contained in this node.
Returns an XML object containing the children of this object that are processing instructions,
matching the name if supplied.
replace()
xmlObj.replace (name, value);
name

An element or attribute name, with or without the 0-based position index of a
specific element, or the wildcard string "*".
If no position index is supplied, replaces the value of all matching elements.
If the wildcard is supplied, replaces the value of all contained elements. When an
element contain subelements, those are removed, and only the replacement
value remains.

value

An XML object or any value that can be converted to a String with toString().

Replaces one or more property values in this node.
If the named element does not exist, appends the given value as a text element.
Returns this XML object.
setChildren()
xmlObj.setChildren (value);
value

An XML object or any value that can be converted to a String with toString().

Replaces all of the XML-valued properties in this object with a new value, which can be a simple text
element, or can contain another set of XML properties.
Returns this XML object.
setLocalName()
xmlObj.setLocalName(name);
name

A String, the new name.

Replaces the local name of this object; that is, the element name without any namespace prefix.
Returns this XML object.
setName()
xmlObj.setName(name);
name

A String, the new name.

Replaces the full name of this object; that is, the element name and its namespace prefix.
Returns this XML object.

setNamespace()
xmlObj.setNamespace(ns);

A Namespace object for a namespace that has been declared in the tree above this
element.

ns

Sets the namespace for this XML element. If the namespace has not been declared in the tree above
this element, add a namespace declaration instead.
Returns this XML object.
text()
xmlObj.text();

Retrieves text nodes from this element.
Returns an XML object containing all properties of this object that represent XML text nodes.
toString()
xmlObj.toString();

Creates a string representation of this object.
For text and attribute nodes, this is the textual value of the node.
For other elements, it is the result of toXMLString().
If this XML object is a list, concatenates the result of calling the function on each contained
element.
Returns a String.
toXMLString()
xmlObj.toXMLString();

Creates an XML-encoded string representation of this XML object. This result includes the start tag,
attributes and end tag of the XML object, regardless of its content. Formats the string as specified
by the global settings XML.prettyPrinting and XML.prettyIndent.
Returns a String.

xpath()
xmlObj.xpath (expression[, variables]);
expression

A String containing an XPath expression.
NOTE: In this context, include the actual top level element. For example, an
expression for the example XML must start with "/bookstore". This is unlike
JavaScript property access, where the top level element is implied.

variables

Optional. A JavaScript object containing variable definitions. The properties are used
to look up XPath variables contained in the expression. For example, if the
expression contains the variable $abc, the value is in the object’s abc property.

Evaluates an XPath expression in accordance with the W3C XPath recommendation, using this XML
object as the context node. The context position and size are set to 1, and all variables are initially
unbound. If this XML object is a list, evaluates all contained XML element nodes (not comments or
other node types) and return the results in a list in the order of execution.

If the XPath expression does not evaluate to a node list, throws a JavaScript exception.
Returns an XML object, the result of evaluation.

Global functions
These functions are available in the JavaScript global namespace.
isXMLName()
isXMLName (String name)
name

A string.

Reports whether a string contains a name that conforms to valid XML syntax.
NOTE: This implementation uses the same rules as for a JavaScript name, except for the '$' character,
which is disallowed, and the '-' character, which as added. It does not follow the W3C definition of an
XML name, which adds more Unicode characters to the valid set of characters.
Returns true if the name is a valid XML name, false otherwise.
setDefaultXMLNamespace()
setDefaultXMLNamespace (Namespace ns)
ns

A Namespace object. Any prefix is ignored.

Sets the default namespace for XML objects. You can also set the default namespace using this
syntax:
default xml namespace = Namespace object
default xml namespace = URL_string

Returns undefined.

QName object
This object encapsulates a fully qualified XML name, the combination of a local XML name and its
namespace URI.

QName object constructors
The constructor takes several forms:
new
new
new
new

QName
QName
QName
QName

()
(name)
(ns)
(uri, name)

When no arguments are supplies, creates a QName object with an empty local name and no URI.
name

String

Creates a QName object with the given local name and the URI of the default
namespace. Can be the wildcard character, "*".

name

QName

Creates a copy of an existing QName object.

ns

Namespace Creates a QName object with an empty local name and the URI of the
Namespace object.

uri, name String

Create a QName object with the given namespace URI and local name.
If the local name is supplied as the wildcard character, "*", the uri argument
is ignored, and the URI value is that of the default namespace.

QName object properties
name

String

The local element name portion of the XML element’s fully qualified XML name.

uri

String

The namespace prefix of the XML element’s fully qualified XML name.

Namespace object
This object encapsulates the definition of an XML namespace. A namespace associates an XML-name
prefix with a complete URI. The prefix is a string that precedes the local name of an XML element or
attribute and identifies the namespace, while the URI points to the actual location where the definition of
the namespace is found.
For example, this XML definition contains a namespace declaration:
<?xml xmlns:adobe=http://www.adobe.com/test?>

In the corresponding namespace, the prefix is adobe, and the URI is http://www.adobe.com/test.

Namespace object constructors
The Namespace constructor takes several forms:
new
new
new
new
new

Namespace()
Namespace (String uri)
Namespace (QName prefix)
Namespace (Namespace ns)
Namespace (String prefix, String uri)

When no argument is supplied, creates a namespace with an empty prefix and URI.
uri

String

Creates a Namespace object with an empty prefix and the given URI.

prefix

QName

Creates a namespace with an empty prefix and the URI set to the URI of the
QName object (if the QName object contains a URI).

ns

Namespace

Creates a copy of the given Namespace object.
If the Namespace() function is called without the new operator, and the only
argument is a Namespace object, the function simply returns that object,
rather than creating a copy.

prefix,
uri

String

Creates a Namespace object with the given prefix and the given URI.

Namespace object properties
prefix

String

The element-name prefix associated with the namespace URI.
The prefix value can be undefined, as when a specified prefix is not a valid XML
name. Namespaces with an undefined prefix are completely ignored; they are not
added to an XML namespace declaration.

uri

String

The location of the namespace definition, a URI.
