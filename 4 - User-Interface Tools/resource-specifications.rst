.. _resource-specifications:

Resource specifications
=======================
You can create one or more user-interface elements at a time using a resource specification. This specially
formatted string provides a simple and compact means of creating an element, including any container
element and its component elements. The resource-specification string is passed as the type parameter to
the Window() or add() constructor function.
The general structure of a resource specification is an element type specification (such as dialog),
followed by a set of braces enclosing one or more property definitions.
var myResource = "dialog{ control_specs }";
var myDialog = new Window ( myResource );

Controls are defined as properties within windows and other containers. For each control, give the class
name of the control, followed by the properties of the control enclosed in braces. For example, the
following specifies a button:

testBtn: Button { text: 'Test' }

The following resource string specifies a panel that contains grouped StaticText and EditText controls:
"msgPnl: Panel { orientation:'column', alignChildren:['right', 'top'],\
text: 'Messages', \
title: Group { \
st: StaticText { text:'Alert box title:' }, \
et: EditText { text:'Sample Alert', characters:35 } \
}
msg: Group { \
st: StaticText { text:'Alert message:' }, \
et: EditText { properties:{multiline:true}, \
text:'<your message here>' \
} \
}"

The property with name properties specifies creation properties; see :ref:`creation-properties`.
A property value can be specified as null, true, false, a string, a number, an inline array, or an object.
An inline array contains one or more values in the form:
[value, value,...]

An object can be an inline object, or a named object, in the form:
{classname inlineObject}

In this case, the classname must be one of the control class names list in "Types of controls" on
page 67.
An inline object contains one or more properties, in the form:
{propertyName:propertyValue,propertyName:propertyValue,... }

.. _using-resource-strings:

Using resource strings
----------------------
These examples in the Adobe ExtendScript SDK demonstrate how to use resource specification strings:
AlertBoxBuilder1.jsx

Demonstrates one way to use resource strings, creating a dialog that allows
the user to enter some values, and then using those values to construct the
resource string for a customizable alert dialog.

AlertBoxBuilder2.jsx

Constructs the same dialog, using a resource string (rather than the add()
method) to specify all of the dialog contents for the user-input dialog.

The two Alert Box Builder examples create the same dialog to collect values from the user.

The Build button event handler builds a resource string from the collected values, and returns it from the
dialog invocation function; the script then saves the resource string to a file. That resource string can later
be used to create and display the user-configured alert box.
The resource specification format can also be used to create a single element or container and its child
elements. For instance, if the alertBuilderResource in the example did not contain the panel
btnPnlResource, you could define that resource separately, then add it to the dialog as follows:
var btnPnlResource =
"btnPnl: Panel { orientation:'row', \
text: 'Build it', \
testBtn: Button { text:'Test' }, \
buildBtn: Button { text:'Build', properties:{name:'ok'} }, \
cancelBtn: Button { text:'Cancel', properties:{name:'cancel'} } \
}";
dlg = new Window(alertBuilderResource);
dlg.btnPnl = dlg.add(btnPnlResource);
dlg.show();

