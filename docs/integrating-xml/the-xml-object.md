# The XML Object

The XML object represents an XML element node in an XML tree. The topmost `XML` object for an XML file
represents the root node. It acts as a list, which contains additional `XML` objects for each element. These in
turn contain XML objects for their own member elements, and so on.

The child elements of an element tree are available as properties of the `XML` object for the parent. The
name of the property corresponds to the name of the element. Each property contains an array of `XML`
objects, each of which represents one element of the named type.

For example, suppose you have the following, minimal XML code:

```xml
<rootElement>
    <elementA>
        <elementB></elementB>
    </elementA>
    <elementA>
        <elementB></elementB>
    </elementA>
</rootElement>
```

In a JavaScript script, the XML object that you create from this XML code represents the root element:

```default
var myRoot = new XML( "<rootElement> <elementA> <elementB></elementB> </elementA> <elementA> <elementB></elementB> </elementA> </rootElement>");
```

You can assign a constant to an XML value directly. The following implicitly creates the XML object
assigned to `myRoot`:

```default
var myRoot = <rootElement>
    <elementA>
        <elementB></elementB>
    </elementA>
    <elementA>
        <elementB></elementB>
    </elementA>
</rootElement>;
```

The object `myRoot` contains a property named `elementA`, which contains two `XML` objects for the two
instances of that element. Each of these, in turn, contains an `elementB` property, which contains one
empty `XML` object:

```default
var elemB1 = myRoot.elementA[0].elementB[0];
```

If an element is empty in the XML, the corresponding property exists and contains an empty XML object; it
is never `null` or `undefined`.

---

## Accessing XML elements

This sample XML code is used for examples throughout this chapter:

```xml
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
        <title lang="en">Alice's Adventures in Wonderland</title>
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
```

To encapsulate this code in an XML object, serialize it into a string and pass that string to the constructor:

```default
var bookXmlStr = "...";
var bookstoreXML = new XML (bookXmlStr);
```

Using this example, the root element `<bookstore>`, is represented by the XML object returned from the
constructor. Each of the `<book>` elements is available as a member of the book property of the XML object.

- The Javascript statement `bookstoreXML.book;` returns the entire list of books.
- The statement `bookstoreXML.book[0];` returns the `XML` object for the first book.
- The statement `bookstoreXML.book[0].author;` returns all authors of the first book.

For additional ways of accessing elements in the tree, see [Retrieving contained elements](#retrieving-contained-elements),
and [Creating and accessing namespaces](#creating-and-accessing-namespaces)

---

## Accessing XML attributes

Attribute are properties of their parent elements. In ExtendScript, access an attribute name by using a
preceding at-sign (`@`). An attribute property is a one-element list, which contains an XML object for the
value of the attribute. For example:

```default
bookstoreXML.book [0].@category;
```

This returns the category attribute of the first book, whose value is the string `"COOKING"`.
To access all category attributes of all books, use this statement:

```default
bookstoreXML.book.@category
```

You can reference a set of elements with a particular attribute value, using a predicate in this form:

```default
element.(@attribute == value)
```

For example, this statement returns only book elements that have a category attribute with the value
`"CHILDREN"`:

```default
bookstoreXML.book.(@category == "CHILDREN");
```

---

## Viewing XML objects

The XML object, like all ExtendScript objects, has a ref:controlobj-toString method that serializes the contents into a
string. In this case, the string contains only the text content of the element, not the tags. For example, for
the element `<x>text</x>`, the `toString()` method returns `"text"`.

This method is called when you evaluate the object in the JavaScript Console of the ExtendScript Toolkit. It
recreates the XML text that the object encapsulates. Thus, if you evaluate the object
`bookstoreXML.book[1]` in the Console, you see the XML text for the encapsulated tree, formatted with
line feeds and spaces:

```default
> bookstoreXML.book[1];
    <book category="CHILDREN">
        <title lang="en">The Wonderful Wizard of Oz</title>
        <author>L. Frank Baum</author>
        <year>1900</year>
        <price>39.95</price>
    </book>
```

If you evaluate an object with a text value, you see the text value. For example:

```default
> bookstoreXML.book[1].@category;
    CHILDREN
```

If you access multiple values, the values are concatenated:

```default
> bookstoreXML.book.@category
    COOKINGCHILDRENCHILDRENMUSIC
```

The [toXMLString()](xml-object-reference.md#xml-object-toxmlstring) method serializes the entire element, including the tags, into a string.
For example, for the element `<x>text</x>`, the method returns `"<x>text</x>"`.

---

## Modifying XML elements and attributes

You can change an element by assigning a value to the corresponding property.

- If the value assigned is an XML element, the element is simply replaced. If there are multiple elements
  of the same type, the first element is replaced, and all other elements are deleted.
- If the value assigned is not XML, it is converted to a string, and the content of the element is replaced
  with that string.
- If no element of this type is present, a new element is appended to the XML.

You can change the values of attributes using the same technique.

### Modification examples

- In the sample XML, the third book has several <author> elements. This statement replaces all of them
  with a single element, containing a new string:
  ```default
  bookstoreXML.book[2].author = "Charles 'Lewis Carroll' Dodgeson";
  ```

  The result is this XML:
  ```xml
  <book category="CHILDREN">
      <title lang="en">Alice's Adventures in Wonderland</title>
      <author>Charles 'Lewis Carroll' Dodgeson</author>
      <year>1865</year>
      <price>29.99</price>
  </book>
  ```
- To replace just the first author, leaving all the other authors in place, use this statement:
  ```default
  bookstoreXML.book[2].author[0] = "Charles Dodgeson, aka Lewis Carroll";
  ```
- This statement changes the content of the <year> element in the second book. ExtendScript
  automatically converts the numeric value to a string:
  ```default
  bookstoreXML.book[1].year = 1901;
  ```
- This following statement adds a new <rating> element to the second book:
  > bookstoreXML.book[1].rating = “**\***”;

  The result is this XML:
  ```xml
  <book category="CHILDREN">
      <title lang="en">The Wonderful Wizard of Oz</title>
      <author>L. Frank Baum</author>
      <year>1900</year>
      <price>39.95</price>
      <rating>*****</rating>
  </book>
  ```
- This statement changes the value of the category attribute of the second book:
  ```default
  bookstoreXML.book[1].@category = "LITERATURE, FANTASY"
  ```

  The result is this XML:
  ```xml
  <book category="LITERATURE, FANTASY">
  <title lang="en">The Wonderful Wizard of Oz</title>
  ...
  ```

---

## Deleting elements and attributes

To delete an element or attribute in the XML, use the JavaScript `delete` operator to delete the
corresponding element or attribute property. If there are multiple instances of an element, you can delete
all, or refer to a single one by its index.

### Deletion examples

This statement deletes all authors from the third book:

```default
delete bookstoreXML.book[2].author;
```

This statement deletes only the second author from the third book:

```default
delete bookstoreXML.book[2].author[1];
```

This statement deletes the category attribute from the third book:

```default
delete bookstoreXML.book[2].@category;
```

---

## Retrieving contained elements

The `XML` object provides methods that allow you to retrieve elements contained at various levels of the
tree:

- `XML.`[children()](xml-object-reference.md#xml-object-children) gets the direct child elements, including text elements.
- `XML.`[elements()](xml-object-reference.md#xml-object-elements) gets the direct child elements that are XML tags, but does not get text.
- `XML.`[descendants()](xml-object-reference.md#xml-object-descendants) allows you to match a specific tag, and gets all matching elements at any level of
  nesting. You can also use a “double dot” notation to access descendants of an element. For example,
  these statements are equivalent:
  ```default
  xml..title
  xml.descendants("title")
  ```

For example, consider this XML code loaded into a top-level `XML` object named `x`:

> ```xml
> <top>
>     <one>one text</one>
>     <two>
>         two text
>         <inside>inside text</inside>
>     </two>
>     top text
> </top>
> ```

Here are the results of the different calls.

- The result of `XML.`[children()](xml-object-reference.md#xml-object-children) contains 3 elements, the direct child tags `<one>` and `<two>`, and the
  directly contained text of the `<top>` tag:
  ```xml
  **> x.children()**
      <one>one text</one>
      <two>
      two text
      <inside>inside text</inside>
      </two>
      top text

  **> x.children().length()**
      3
  ```
- The result of `XML.`[elements()](xml-object-reference.md#xml-object-elements) contains 2 elements, the direct child tags `<one>` and `<two>`:
  ```xml
  **> x.elements()**
      <one>one text</one>
      <two>
          two text
          <inside>inside text</inside>
      </two>
  **> x.elements().length()**
      2
  ```
- The result of `XML.`[descendants()](xml-object-reference.md#xml-object-descendants) contains 7 elements, the direct child tags `<one>` and `<two>`, the
  `<inside>` tag one level down, and the text contents of all the tags:
  ```xml
  **> x.descendants()**
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
  **> x.descendants().length()**
      7
  ```

---

## Creating and accessing namespaces

Simple access statements access elements in the default namespace. If you need to define elements in
more than one namespace, you must use a [Namespace object](xml-object-reference.md#namespace-object) to access any elements that are NOT in the
default namespace.

### Defining a namespace within the tree

You can define a namespace within an XML element using the xmlns attribute, and define elements within
the schema as belonging to that namespace. For example, these additions to the example XML add a
namespace that maps the prefix “kids” to the namespace “[http://kids.mybookstore.com](http://kids.mybookstore.com)”, and then
uses the prefix to place a particular book element in that namespace:

> ```xml
> <bookstore **xmlns:kids="http://kids.mybookstore.com"**>

> <book category="COOKING">
>     <title lang="en">The Boston Cooking-School Cookbook</title>
>     <author>Fannie Merrit Farmer</author>
>     <year>1896</year>
>     <price>49.99</price>
> </book>

> <**kids:**book category="CHILDREN">
>     <title lang="en">The Wonderful Wizard of Oz</title>
>     <author>L. Frank Baum</author>
>     <year>1900</year>
>     <price>39.95</price>
> </**kids:**book>
> ...
> ```

When this namespace is defined, the simple statement `bookstoreXML.book` no longer returns “The
Wonderful Wizard of Oz”, because that book is no longer in the default namespace. To access that book,
you must define a [Namespace object](xml-object-reference.md#namespace-object) for the namespace, and use it to access the element.

For example, this JavaScript code creates a [Namespace object](xml-object-reference.md#namespace-object) for the namespace defined in the
<bookstore> element, and accesses the books in the namespace through that object:

```default
var ns = new Namespace ("http://kids.mybookstore.com");
bookstoreXML.ns::book;
```

---

### Setting a default namespace

By default, the default namespace is a namespace whose URI is the empty string. It is possible to set the
default namespace; in this case, simple accessors access elements that are in that namespace.

To set the default namespace, use the global function [setDefaultXMLNamespace()](xml-object-reference.md#xml-setdefaultxmlnamespace), or this syntax:

```default
default xml namespace = namespace_specifier;
```

The namespace specifier can be either a [Namespace object](xml-object-reference.md#namespace-object), or a URL string. For example:

```default
default xml namespace = "http://books.mybookstore.com";
```

Once you have set the default namespace:

- Elements that are meant to be in the default namespace (and thus accessible with simple accessors)
  must use the namespace prefix.
- All elements that do not have a specific namespace assignment are in the empty namespace, rather
  than the default namespace. In order to access them, you must use a [Namespace object](xml-object-reference.md#namespace-object) with the
  empty string as the URI.

---

### Accessing elements in namespaces

- You can access elements that are in the default namespace directly, without using a [Namespace object](xml-object-reference.md#namespace-object).
  - If you have not set a default, you can use direct access for elements with no namespace specifier.
  - If you have set a default, you can use direct access for elements in that namespace.
- If you have assigned an element to a namespace, and have not made it the default, you must use a
  [Namespace object](xml-object-reference.md#namespace-object) to access those elements. For example:
  ```default
  var ns = new Namespace (**"http://kids.mybookstore.com"**);
  bookstoreXML.**ns::book**;
  ```

  This returns all books that have been assigned to the “kids” namespace.
- If you have set a default namespace, you can still access all objects that do not have any specific
  namespace assignment by using a [Namespace object](xml-object-reference.md#namespace-object) for the empty string, which is the default
  creation case:
  ```default
  var emptyNS = new Namespace ();
  bookstoreXML.emptyNS::book;
  ```

  This returns all books that have not been assigned to any namespace.
- To access all elements, regardless of the namespace assignment, you can use an asterisk (\*) wild-card
  character or null as the namespace name:
  ```default
  bookstoreXML.*::book;
  ```

  or
  > var nullNS = null;
  > bookstoreXML.nullNS::book;

---

## Mixing XML and JavaScript

You can enclose JavaScript statements in curly brackets, and embed them into XML. The JavaScript part is
evaluated during the construction of the XML.

For example, this function returns an XML value, in which embedded JavaScript variables will be evaluated
and included:

```default
function makeXML (first, last) {
    return <person first={first} last={last}>{first + " " + last}</person>;
}
```

Calling this function:

```default
makeXML ( "Jane", "Doe" );
```

results in this XML:

> ```xml
> <person first="Jane" last="Doe">Jane Doe</person>
> ```

You can also use these operators on XML elements:

- Use the plus operator, +, to combine XML elements into a list.
- Use the == operator to make an in-depth comparison of two XML trees.

---

## XML lists

ExtendScript defines an `XMLList` object, which is identical to the [XML object](xml-object-reference.md#xml-object) except that you can create it
by passing it an XML list, and it creates an XML list rather than an XML tag.

All XML statements and functions that collect XML return the result as an `XMLList`, which can be empty if
there is no match. For example, the following statement returns an empty list:

```default
bookstoreXML.magazine;
```
