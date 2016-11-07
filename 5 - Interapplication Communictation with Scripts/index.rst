Interapplication Communication with Scripts
The Adobe scripting environment provides an interapplication messaging framework, a way for to send
and receive information and scripts from one Adobe application to another. An application that supports
the messaging framework is said to be message enabled.
Code samples that demonstrate various techniques are provided with the Adobe ExtendScript SDK, and
referenced by name in the relevant sections.

Communications overview
Scripts written for any message-enabled application can communicate with other message-enabled
applications in two ways; through directly calling functions defined in a remote application, and by
sending messages and receiving responses from a remote application. A specific syntax is provided for
identifying applications unambiguously.

Remote function calls
A limited set of basic functions (the cross-DOM) are common across all message-enabled applications, and
allow your script to, for example, open or print files in other applications, simply by calling the open or
print function for that application.
"Cross-DOM functions" on page 167 describes the usage of this feature.
"Cross-DOM API reference" on page 168 provides reference details for the functions of the basic
cross-DOM.
Each message-enabled application can also export a set of functions to provide a selected set of
application-specific functionality; see "Application-specific exported functions" on page 167. For example,
an Adobe Bridge script can request a photo merge in Photoshop by calling
photoshop.photomerge(files). The set of functions available for each application varies widely.

Messaging framework
The interapplication messaging framework is a JavaScript application programming interface (API) that
allows extensive control over communication between applications. The API allows you to send messages
to other applications and receive results, and to receive messages sent by other applications and return
results. Typically the data passed between applications are JavaScript scripts. However, the messaging
framework is extensible. It allows you to define different types of data to send between applications, and
to specify how they are handled.
"Communicating through messages" on page 170 describes the usage of this feature.
"Messaging framework API reference" on page 179 provides complete reference details.



Identifying applications
When calling external functions or exchanging messages, you must identify particular applications using
namespace specifiers. A specifier consists of a specific name string (such as photoshop), and optional
additions that identify a particular release or locale version. Application specifiers are used occasionally in
other contexts as well. For details of the syntax, see "Application and namespace specifiers" on page 191.
Regardless of which method you use to perform interapplication communication, you must place your
script in a location where the application you want to run it can see it. There are different locations for the
startup scripts of the applications themselves, and for scripts provided by developers.
Because all JavaScript-enabled applications look in the same locations for scripts to run, the scripts
themselves must be explicit about which application they are meant for. A script should check that all
applications it needs to communicate with are installed with the correct version, and that any other
applications that might be installed do not run the script. For details, see "Scripting for specific
applications" on page 12.

Cross-DOM functions
The cross-DOM is a small application programming interface (API), which provides a set of functions that
are common across message-enabled applications. These include functions to open files, execute scripts,
and print files. For details of the function set, see the "Cross-DOM API reference" on page 168.
You can access cross-DOM functions in any script by prefixing the function name with the namespace
specifier for the target application (see "Namespace specifiers" on page 193). For example, a Photoshop CC
script can call indesign.open(file) to open a file in Adobe InDesign® CC.
The cross-DOM functions for each application are implemented in JavaScript. You can see the
implementation for each installed application by reading its associated startup script in the Adobe startup
folder. For example, Adobe Illustrator® CC defines illustrator.open() in the illustrator-14.jsx
startup script (14 is the version number of the installed application). See "Startup folder locations" on
page 168.
Example code
The sample code distributed with the Adobe ExtendScript SDK includes these code examples that
specifically demonstrate the use of cross-DOM functions:
Cross-DOM calls
OpenImageInPhotoshop.jsx

Shows how to send an image file to be opened in Photoshop.

Application-specific exported functions
In addition to the required base cross-DOM functions, each message-enabled application can provide
application-specific functionality to all scripts through a simple syntax. You can access exported functions
in any script by prefixing the function name with the namespace specifier for the target application (see
"Namespace specifiers" on page 193). For example, Photoshop CS5 exports the photomerge function, so
an Illustrator CS5 script can directly call photoshop.photomerge(files).
The only difference between cross-DOM functions and the application-specific exported functions is that
all applications expose the same set of cross-DOM functions, whereas each application exposes its own set

of application-specific functions. Each application determines the extent of its exported functionality.
Some applications provide extensive support for exported functions, others less.
For details of additional functions that are exported by individual applications, refer to the startup scripts
for those applications. The application startup scripts are named appname-n.jsx, where n is the version
number of the installed application. See "Startup folder locations" on page 168.

Startup folder locations
For each platform, there is a startup folder shared by all Adobe Creative Suite 4 applications that support
JavaScript, and an application-specific startup folder.
In Windows®, the installation startup folders are:
%CommonProgramFiles%\Adobe\Startup Scripts CS5\Adobe AppName\

In Mac OS®, the installation startup folders are:
/Library/Application Support/Adobe/Startup Scripts CS5/Adobe AppName/

NOTE: This is not the location in which to store your own startup scripts; see "Scripting for specific
applications" on page 12.

Cross-DOM API reference
All exported functions, including those of the cross-DOM API, are invoked through the exporting
application, identified by its namespace specifier (see "Namespace specifiers" on page 193). For example:
//execute an Illustrator script in version 12
illustrator12.executeScript(myAIScript);

A specifier with no version information invokes the highest installed version of the application. For
example:
//execute a Photoshop script in the highest available version
photoshop.executeScript (myPSScript)

All message-enabled applications implement the following cross-DOM functions:
executeScript()
appspec.executeScript(script)
script

A string containing the script to be evaluated.

Performs a JavaScript eval on the specified script. The entire document object model (DOM) of the
target application is available to the script. Returns undefined.
open()
appspec.open(files)
files

A File object or array of File objects. For applications that use compound documents,
this should be a project file.

Performs the equivalent of the target application’s File > Open command on the specified files.
Returns undefined.

openAsNew()
appspec.openAsNew([options])
options

Optional. Application-specific creation options:
Adobe Bridge: none
Photoshop: none
InDesign: creation options are:
(Boolean:showingWindow, ObjectOrString:documentPresets)

See the arguments for documents.add() in the Adobe InDesign CS5 Scripting
Reference.
Illustrator: creation options are:
([DocumentColorSpace:colorspace][, Number:width, Number:height])

See the arguments for documents.add() in the Adobe Illustrator CS5 JavaScript
Reference.
Performs the equivalent of the target application’s File > New command. Returns true on success.
print()
appspec.print(files)
files

A File object or array of File objects. For applications that use compound documents,
this should be a project file.

Performs the equivalent of the target application’s File > Print command on the specified files.
Returns undefined.
quit()
appspec.quit()

Performs the equivalent of the target application’s File > Exit or File > Close command. Returns
undefined.
NOTE: This function is available for Adobe Acrobat®, but does nothing. Scripts cannot terminate the
application.
reveal()
appspec.reveal(file)
file

A File object or string specifying a file that can be opened in the target application.

Gives the target application the operating-system focus, and, if the specified file is open in that
application, brings it to the foreground. Returns undefined.

Communicating through messages
Adobe Bridge provides an application programming interface (API) that defines a communication
protocol between Adobe ExtendScript- and message-enabled applications. This provides the most
general mechanism for communication between applications. A messaging-enabled application can
launch another messaging-enabled application, and send or receive scripts to effect certain actions. For
example, from within Adobe Bridge, a script can launch Photoshop, and then send a script to Photoshop
that requests a photomerge operation.
While the exported functions allow specific access to certain capabilities of the application, the script in an
interapplication message allows full access to the target application’s document object model (DOM), in
addition to all cross-DOM and application exported functions.
The messaging API defines the BridgeTalk class, whose globally available static properties and functions
provide access to environmental information relevant for communication between applications. You can
instantiate this class to create a BridgeTalk message object, which encapsulates a message and allows you
to send it to another application. For details of these objects, see "Messaging framework API reference" on
page 179.

Sending messages
To send a script or other data to another application, you must create and configure a BridgeTalk message
object. This object contains the data to be sent (generally a script to be executed in the target application),
and also specifies how to handle the response.
This simple example walks through the steps of sending a script from Adobe Bridge CS5 to Photoshop
CS5, and receiving a response.
Step 1: Check that the target application is installed
Before you can actually send a message, you must check that the required version of the target application
is installed. The function getSpecifier(), available in the global namespace through the BridgeTalk
class, provides this information.
For example, this code, which will send a message to Adobe Bridge CS5 as part of a script being executed
by Photoshop CS5, checks that the required version of Adobe Bridge is installed:
var targetApp = BridgeTalk.getSpecifier( "bridge-3.0");
if( targetApp ) {
// construct and send message
}

When you send the message, the messaging framework automatically launches the target application, if it
is not already running.
Step 2: Construct a message object
The next step is to construct a message to send to the application. You do this by creating a BridgeTalk
message object, and assigning values to its properties. You must specify the target application and the
message body, which is usually a script packaged into a string.
Scripts sent in messages can be very complex, and can use the full DOM of the target application. This
example defines a message script that accesses the Adobe Bridge DOM to request the number of files or
folders found in a specific folder:
// create a new BridgeTalk message object

var bt = new BridgeTalk;
// send this msg to the Adobe Bridge CS4 application
var targetApp = BridgeTalk.getSpecifier( "bridge-3.0");
bt.target = targetApp;
// the script to evaluate is contained in a string in the "body" property
bt.body = "new Document(’C:\\BridgeScripts’);
app.document.target.children.length;"

Step 3: Specify how to handle a response
If you want to handle a response for this message, or use the data that is returned from the script’s
evaluation, you must set up the response-handling mechanism before you send the message. You do this
by defining the onResult callback in the message object.
NOTE: The message callbacks are optional, and are not implemented by all message-enabled applications.
The response to a message is, by default, the result of evaluation of the script contained in that message’s
body property. The target application might define some different kind of response; see "Receiving
messages" on page 172.
When the target has finished processing this message, it looks for an onResult callback in the message
object it received. If it is found, the target automatically invokes it, passing it the response. The response is
packaged into a string, which is in turn packaged into the body property of a new message object. That
message object is the argument to your onResult callback function.
This handler, for example, processes the returned result using a script-defined processResult function.
bt.onResult = function(returnBtObj)
{ processResult(returnBtObj.body); }

If you want to handle errors that might arise during script processing, you can define an onError callback in
the message object. Similarly, you can define a timeout value and onTimeout callback to handle the case
where the target cannot process the message within a given time. For more information, see "Handling
responses from the message target" on page 173.
NOTE: If you define callbacks to handle a response, you must store the message in a variable that still exists
when the response is received. Otherwise, JavaScript might garbage-collect the message object, and the
response would be lost.
Step 4: Send the message
To send the message, call the message object’s send method. You do not need to specify where to send
the message to, since the target application is set in the message itself.
bt.send();

You can optionally specify a timeout value, which makes the call synchronous; when you do this, the
method waits for a response from the target application, or for the timeout value to expire, before
returning. When a timeout is not specified, as in this example, the call is asynchronous and the send()
method returns immediately.
A second optional parameter allows you to specify launch parameters, in case the target application is not
currently running, and the messaging framework needs to launch it.
The complete script looks like this:
// script to be executed in Photoshop CS4
#target "photoshop-11.0"
// check that the target app is installed

var targetApp = BridgeTalk.getSpecifier( "bridge-3.0");
if( targetApp ) {
// construct a message object
var bt = new BridgeTalk;
// the message is intended for Adobe Bridge CS4
bt.target = targetApp;
// the script to evaluate is contained in a string in the "body" property
bt.body = "new Document(’C:\\BridgeScripts’);
app.document.target.children.length;"
// define result handler callback
bt.onResult = function(returnBtObj) {
processResult(returnBtObj.body); } //fn defined elsewhere
// send the message asynchronously
bt.send();
}

Receiving messages
An application can be the target of a message; that is, it receives an unsolicited message from another
application. An unsolicited message is handled by the static BridgeTalk.onReceive callback function in
the target application. See "Handling unsolicited messages" on page 172.
An application that sends a message can receive response messages; that is, messages that come as the
result of requesting a response when a message was sent. These can be:
The result of an error in processing the message
The result of a timeout when attempting to process the message
A notification of receipt of the message
Intermediate responses
The final result of processing the message.
All of these response messages are sent automatically by the target application, and are handled by
callbacks defined in the sending message object. For details, see "Handling responses from the message
target" on page 173.

Handling unsolicited messages
To specify how the application should handle unsolicited incoming messages, define a callback handler
function in the static onReceive property of the BridgeTalk class. This function takes a single argument, a
BridgeTalk message object.
The default behavior of the onReceive handler is to evaluate the body of the received message with
JavaScript, and return the result of that evaluation. (The result of evaluating a script is the result of the last
line of the script.) To return the result, it creates a new message object, encapsulates the result in a string in
the body property of that object, and passes that object to the onResult callback defined in the original
message.
If an error occurs on evaluation, the default onReceive handler returns the error information using a
similar mechanism. It creates a new message object, encapsulates the error information in a string in the
body property of that object, and passes that object to the onError callback defined in the original
message.

To change the default behavior set the BridgeTalk.onReceive property to a function definition in the
following form:
BridgeTalk.onReceive = function( bridgeTalkObject ) {
// callback definition here
};

The body property of the received message object contains the received data.
The function can return any type.
The function that you define does not need to explicitly create and return a BridgeTalk message object.
The messaging framework creates a new BridgeTalk message object, and packages the return value of
the onReceive handler as a string in the body property of that object.
Return values are flattened into a string using the Unicode Transformation Format-8 (UTF-8) encoding. If
the function does not specify a return value, the resulting string is the empty string.
The result object is transmitted back to the sender if the sender has implemented an onResult callback for
the original message.
Message-handling examples
This example shows the default mechanism for handling unsolicited messages received from other
applications. This simple handler executes the message’s data as a script and returns the results of that
execution.
BridgeTalk.onReceive = function (message) {
return eval( message.body );
}

This example shows how you might extend the receive handler to process a new type of message.
BridgeTalk.onReceive = function (message) {
switch (message.type) {
case "Data":
return processData( message );
break;
default: //"ExtendScript"
return eval( mesage.body );
}
}

Handling responses from the message target
To handle responses to a message you have sent, you define callback handler functions in the message
object itself. The target application cannot send a response message back to the sender unless the
message object it received has the appropriate callback defined.
NOTE: The message callbacks are optional, and are not implemented by all message-enabled applications.
When your message is received by its target, the target application’s static BridgeTalk object’s onReceive
method processes that message, and can invoke one of the message object’s callbacks to return a
response. In each case, the messaging framework packages the response in a new message object, whose
target application is the sender. Your callback functions receive this response message object as an
argument.

A response message can be:
The result of an error in processing the message. This is handled by the onError callback.
If an error occurs in processing the message body (as the result of a JavaScript syntax error, for
instance), the target application invokes the onError callback, passing a response message that
contains the error code and error message. If you do not have an onError callback defined, the error is
completely transparent. It can appear that the message has not been processed, since no result is ever
returned to the onResult callback.
A notification of receipt of the message. This is handled by the onReceived callback.
Message sending is asynchronous. Getting a true result from the send method does not guarantee
that your message was actually received by the target application. If you want to be notified of the
receipt of your message, define the onReceived callback in the message object. The target sends back
the original message object to this callback, first replacing the body value with an empty string.
The result of a time-out. This is handled by the onTimeout callback.
You can specify a number of seconds in a message object’s timeout property. If the message is not
removed from the input queue for processing before the time elapses, it is discarded. If the sender has
defined an onTimeout callback for the message, the target application sends a time-out message back
to the sender.
Intermediate responses. These are handled by the onResult callback.
The script that you send can send back intermediate responses by invoking the original message
object’s sendResult() method. It can send data of any type, but that data is packaged into a body string
in a new message object, which is passed to your callback. See "Passing values between applications"
on page 176.
The final result of processing the message. This is handled by the onResult callback.
When it finishes processing your message, the target application can send back a result of any type. If
you have sent a script, and the target application is using the default BridgeTalk.onReceive callback
to process messages, the return value is the final result of evaluating that script. In any case, the return
value is packaged into a body string in a new message object, which is passed to your callback. See
"Passing values between applications" on page 176.
The following examples demonstrate how to handle simple responses and multiple responses, and how to
integrate error handling with response handling.
Example: Receiving a simple response
In this example, an application script asks Adobe Bridge to find out how many files and folders are in a
certain folder, which the evaluation of the script returns. (The default BridgeTalk.onReceive method
processes this correctly.)
The onResult method saves that number in fileCountResult, a script-defined property of the message,
for later use.
var bt = new BridgeTalk;
bt.target = "bridge-3.0";
bt.body = "new Document(’C:\\BridgeScripts’);
app.document.target.children.length;"
bt.onResult = function( retObj ) {
processFileCount(retObj.body);
}

bt.send();

Example: Handling any error
In this example, the onError handler re-throws the error message within the sending application.
var bt = new BridgeTalk;
bt.onError = function (btObj) {
var errorCode = parseInt (btObj.headers ["Error-Code"]);
throw new Error (errorCode, btObj.body);
}

Example: Handling expected errors and responses
This example creates a message that asks Adobe Bridge to return XMP metadata for a specific file. The
onResult method processes the data using a script-defined processFileSize function. Any errors are
handled by the onError method. For example, if the file requested is not an existing file, the resulting error
is returned to the onError method.
var bt = new BridgeTalk;
bt.target = "bridge-3.0";
bt.body = "var tn = new Thumbnail(’C/MyPhotos/temp.gif’);
tn.core.immediate.size;"
bt.onResult = function( resultMsg ) {
processFileSize(resultMsg.body);
}
bt.onError = function( errorMsg ) {
var errCode = parseInt (errorMsg.headers ["Error-Code"]);
throw new Error (errCode, errorMsg.body);
}
bt.send();

Example: Setting up a target to send multiple responses
This example integrates the sending of multiple responses with the evaluation of a message body. It sets
up a handler for a message such as the one sent in the following example.
The target application (Adobe Bridge) defines a static onReceive method to allow for a new type of
message, which it calls an iterator. An iterator type of message expects the message.body to use the
iteration variable i within the script, so that different results are produced for each pass through the while
loop. Each result is sent back to the sending application with the sendResult() method. When the
message.body has finished processing its task, it sets a flag to end the while loop.
// Code for processing the message and sending intermediate responses
// in the target application (Adobe Bridge)
BridgeTalk.onReceive = function (message){
switch (message.type) {
case "iterator":
done = false;
i = 0;
while (!done) {
// the message.body uses "i" to produce different results
// for each execution of the message.
// when done, the message.body sets "done" to true
// so this onReceive method breaks out of the loop.
message.sendResult(eval(message.body));
i++; }
break;
default: //"ExtendScript"
return eval( message.body );

}
}

Example: Setting up a sender to receive multiple responses
This example sends a message of the type iterator, to be handled by the onReceive handler in the
previous example, and processes the responses received from that target.
The sending application creates a message whose script (contained in the body string) iterates through all
files in a specific folder (represented by an Adobe Bridge Thumbnail object), using the iterator variable i.
For each file in the folder, it returns file size data. For each contained folder, it returns -1. The last executed
line in the script is the final result value for the message.
The onResult method of the message object receives each intermediate result, stores it into an array,
resArr, and processes it immediately using a script-defined function processInterResult.
// Code for send message and handling response
// in the sending application (any message-enabled application)
var idx = 0;
var resArr = new Array;
bt = new BridgeTalk;
bt.target = "bridge";
bt.type = "iterator";
bt.body = "
var fld = new Thumbnail(Folder(’C/Junk’));
if (i == (fld.children.length - 1))
done = true; //no more files, end loop
tn = fld.children[i];
if (tn.spec.constructor.name == ’File’)
md = tn.core.immediate.size;
else md = -1;
";
// store intermediate results
bt.onResult = function(rObj) {
resArr[idx] = rObj.body;
processInterResult(resArr[idx]);
idx++;};
bt.onError = function(eObj) {
bt.error = eObj.body };
bt.send();

Passing values between applications
The BridgeTalk.onReceive static callback function can return values of any type. The messaging
framework, however, packages the response into a response message, and passes any returned values in
the message body, first converting the result to a UTF-8-encoded string.

Passing simple types
When your message object’s onResult callback receives a response, it must interpret the string it finds in
the body of the response message to obtain a result of the correct type. Results of various types can be
identified and processed as follows:
Number

JavaScript allows you to access a string that contains a number directly as a number, without
doing any type conversion. However, be careful when using the plus operator (+), which
works with either strings or numbers. If one of the operands is a string, both operands are
converted to strings and concatenated.

String

No conversion is required.

Boolean

The result string is either "true" or "false." You can convert it to a true boolean by evaluating it
with the eval method.

Date

The result string contains the date in the form:
"dow mmm dd yyyy hh:mm:ss GMT-nnnn".

For example "Wed Jun 23 2004 00:00:00 GMT-0700".
Array

The result string contains a comma delimited list of the elements of the array. For example, If
the result array is [12, "test", 432], the messaging framework flattens this into the string
"12,test,432".
As an alternative to simply returning the array, the message target can use the toSource
method to return the code used to create the array. In this case, the sender must reconstitute
the array by using the eval method on the result string in the response body. See discussion
below.

Passing complex types
When returning complex types (arrays and objects), the script that you send must construct a result string,
using the toSource method to serialize the array or object. In this case, the sender must reconstitute the
array or object by using the eval method on the result string in the response body.
Passing an array with toSource and eval
For example, the following code sends a script that returns an array in this way. The onResult callback that
receives the response uses eval to reconstruct the array.
// Code for send message and handling response
// in the sending application (any message-enabled application)
var idx = 0;
var resArr = new Array;
var bt = new BridgeTalk;
bt.target = "bridge-3.0";
// the script passed to the target application
// needs to return the array using "toSource"
bt.body = "var arr = [10, "this string", 324];
arr.toSource();"
bt.onResult = function(resObj) {
// use eval to reconstruct the array
arr = eval(resObj.body);

// now you can access the returned array
for (i=0; i< arr.length(); i++)
doSomething(arr[i]);
}
// send the message
bt.send();

Passing an object with toSource and eval
This technique is the only way to pass objects between applications. For example, this
code sends a script that returns an object containing some of the metadata for a
specific file and defines an onResult callback that receives the object.
var bt = new BridgeTalk;
bt.target = "bridge-3.0";
//the script passed to the target application
// returns the object using "toSource"
bt.body = "var tn = new Thumbnail(File(’C:\\Myphotos\\photo1.jpg’));
var md = {fname:tn.core.immediate.name,
fsize:tn.core.immediate.size};
md.toSource();"
//For the result, use eval to reconstruct the object
bt.onResult = function(resObj) {
md = bt.result = eval(resObj.body);
// now you can access fname and fsize properties
doSomething (md.fname, md.fsize);
}
// send the message
bt.send();

Passing a DOM object
You can send a script that returns a DOM object, but the resulting object contains only those properties
that were accessed within the script. For example, the following script requests the return of the Adobe
Bridge DOM Thumbnail object. Only the properties path and uri are accessed by the script, and only
those properties are returned:
var bt = new BridgeTalk;
bt.target = "bridge";
//set up the script passed to the target application
// to return the array using "toSource"
bt.body = "var tn = new Thumbnail(File(’C:\\Myphotos\\photo1.jpg’));
var p = tn.path; var u = tn.uri;
tn.toSource();"
//For the result, use eval to reconstruct the object
bt.onResult = function(resObj) {
// use eval to reconstruct the object
tn = eval(resObj.body);
// now the script can access tn.path and tn.uri,
// but no other properties of the Adobe Bridge DOM Thumbnail object
doSomething (tn.path, tn.uri);
}
// send the message
bt.send();

Messaging framework API reference
This application programming interface (API) defines a communication protocol between
message-enabled applications. These objects are available to all ExtendScript scripts when any of the
applications is loaded.
The messaging protocol is extensible. Although it is primarily designed to send scripts, you can use it to
send other kinds of data.
The messaging API defines the BridgeTalk class. Static properties and methods of the class provide
access to environmental information relevant for communication between applications. Instantiate the
class to create a BridgeTalk message object, which encapsulates the message itself. For discussion and
examples, see "Communicating through messages" on page 170, and the example code provided with the
Adobe ExtendScript SDK.
Example code
The sample code distributed with the Adobe ExtendScript SDK includes these code examples that
specifically demonstrate the use of interapplication messaging:
Interapplication messaging
MessagingBetweenApps.jsx
MessageSendingToInDesign.jsx

Shows how to send a message to a Creative Suite application
and receive a response.

SendArrayToPhotoshop.jsx

Sends message to Photoshop that creates an array in the
target and passes it back to the sender.

SendObjectToPhotoshop.jsx

Sends message to Photoshop that creates a JavaScript object
in the target and passes it back to the sender.

SendDOMObjectToPhotoshop.jsx

Sends message to Photoshop that creates a Photoshop object
in the target and passes values from it back to the sender.

SaveAsDifferentFileType.jsx

Locates an image file, uses messaging to load it into
Photoshop and save it as a different file type.

BridgeTalk class
Static properties and methods of this class provide a way for your script to determine basic messaging
system information before you create any specific message objects. Static methods allow you to check if
an application is installed and is already running, and to launch the application. A callback defined on the
class determines how the application processes incoming messages.
You can access static properties and methods in the BridgeTalk class, which is available in the global
namespace. For example:
var thisApp = BridgeTalk.appName;

NOTE: You must instantiate the BridgeTalk class to create the BridgeTalk message object, which is used
to send message packets between applications. Dynamic properties and methods can be accessed only in
instances.

BridgeTalk class properties
The BridgeTalk class provides these static properties, which are available in the global namespace:
appInstance

String

The instance identifier of an application launched by the messaging
framework, the instance portion of an application specifier; see
"Application specifiers" on page 191. Read only.
Used only for those applications, such as InDesign, that support launching
and running multiple instances.

appLocale

String

The locale of this application, the locale portion of an application
specifier; see "Application specifiers" on page 191. When a message is
sent, this is the locale of the sending application. Read only.

appName

String

The name of this application, the appname portion of an application
specifier; see "Application specifiers" on page 191. When a message is
sent, this is the name of the sending application. Read only.

appSpecifier

String

A lower-case string containing the complete specifier for this application;
see "Application specifiers" on page 191. Read/write.

appStatus

String

The current processing status of this application. Read only. One of:
busy - The application is currently busy, but not processing

messages. This is the case, for example, when a modal dialog is shown.

idle - The application is currently idle, but processes messages

regularly.

not installed - The application is not installed.
appVersion

String

The version number of this application, the version portion of an
application specifier; see "Application specifiers" on page 191. When a
message is sent, this is the version of the sending application. Read only.

onReceive

Function A callback function that this application applies to unsolicited incoming
messages. The default function evaluates the body of the received
message and returns the result of evaluation. To change the default
behavior, set this to a function definition in the following form:
BridgeTalk.onReceive = function( bridgeTalkObject ) {
// act on received message
};

The body property of the received message object contains the received
data. The function can return any type. See "Handling unsolicited
messages" on page 172.
NOTE: This function is not applied to a message that is received in response
to a message sent from this application. Response messages are processed
by the onResult, onReceived, or onError callbacks associated with the
sent message.

BridgeTalk class functions
The BridgeTalk class provides these static methods, which are available in the global namespace:
bringToFront()
BridgeTalk.bringToFront (app)
app

A specifier for the target application; see "Application specifiers" on page 191.

Brings all windows of the specified application to the front of the screen.
In Mac OS, an application can be running but have no windows open. In this case, calling this
function might or might not open a new window, depending on the application. For Adobe Bridge,
it opens a new browser window.
getAppPath()
BridgeTalk.getAppPath (app)
app

A specifier for the target application; see "Application specifiers" on page 191.

Retrieves the full path of the executable file for a specified application.
Returns a string.
getDisplayName()
BridgeTalk.getSpecifier (app)
app

A specifier for the target application; see "Application specifiers" on page 191.

Returns a localized display name for an application, or NULL if the application is not installed. For
example:
BridgeTalk.getDisplayName("photoshop-10.0");
=> Adobe Photoshop CS4

getSpecifier()
BridgeTalk.getSpecifier (appName,[version],[locale])
appName

The base name of the application to search for.

version

Optional. The specific version number to search for. If 0 or not supplied, returns the
most recent version. If negative, returns the highest version up to and including the
absolute value.
If a major version is specified, returns the highest minor-version variation. For
example, if Photoshop CS versions 9, 9.1, and 10 are installed:
BridgeTalk.Specifier( "photoshop", "9" )
=> ["photoshop-9.1"]

locale

Optional. The specific locale to search for.
If not supplied and multiple language versions are installed, prefers the version for
the current locale.

Retrieves a complete application specifier.
Returns a complete specifier (see "Application specifiers" on page 191) for a messaging-enabled
application version installed on this computer, or null if the requested version of the application is
not installed.
For example, assuming installed applications include Photoshop CS4 11.0 en_us, Photoshop CS2
8.5 de_de, Photoshop CS2 9.0 de_de, and Photoshop CS2 9.5 de_de, and that the current locale is
en_US:
BridgeTalk.getSpecifier ("photoshop");
=> ["photoshop-11.0-en_us"]
BridgeTalk.getSpecifier ("photoshop", 0, "en_us");
=> ["photoshop-11.0-en_us"]
BridgeTalk.getSpecifier ("photoshop", 0, "de_de");
=> ["photoshop-9.5-de_de"]
BridgeTalk.getSpecifier ("photoshop", -9.2, "de_de");
=> ["photoshop-9.0-de_de"]
BridgeTalk.getSpecifier ("photoshop", 8);
=> ["photoshop-8.5-de_de"]

getStatus()
BridgeTalk.getStatus (targetSpec)
targetSpec

Optional, a specifier for the target application; see "Application specifiers" on
page 191.
If not supplied, returns the processing status of the current application.

Retrieves the processing status of an application. Returns a string, one of:
BUSY: The application is currently busy, but not processing messages. This is the case, for

example, when a modal dialog is shown.

IDLE: The application is currently idle, but processes messages regularly.
PUMPING: The application is currently processing messages.
ISNOTRUNNING: The application is installed but not running.
ISNOTINSTALLED: The application is not installed.
UNDEFINED: The application is running but not responding to ping requests. This can be true of
a CS2 application that uses an earlier version of the messaging framework.
getTargets()
BridgeTalk.getTargets ([version],[locale])
version

Optional. The specific version number to search for, or null to return the most
appropriate version (matching, most recent, or running), with version information.
Specify only a major version number to return the highest minor-version
variation. For example, if Photoshop CS versions 9, 9.5, and 10 are installed:
BridgeTalk.getTargets( "9" )
=> [photoshop-9.5]

Specify a negative value to return all versions up to the absolute value of the
version number. For example:
BridgeTalk.getTargets( "-9.9" )
=> [photoshop-9.0, photoshop-9.5]
locale

Optional. The specific locale to search for, or null to return applications for all
locales, with locale information.
If not supplied when version is supplied, returns specifiers with version
information only.

Retrieves a list of messaging-enabled applications installed on this computer.
Returns an array of "Application specifiers" on page 191.
If version is supplied, specifiers include the base name plus the version information.
If locale is supplied, specifiers include the full name, with both version and locale information.

If neither version nor locale is supplied, returns base specifiers with neither version nor locale
information, but tries to find the most appropriate version and locale; see "Application
specifiers" on page 191.
For example, assuming installed applications include Photoshop CS3 10.0 en_US, Photoshop CS4
11.0 en_us, and Illustrator CS4 14.0 de_de:
BridgeTalk.getTargets();
=> [photoshop,illustrator]
BridgeTalk.getTargets( "10.0" );
=> [photoshop-10.0]
BridgeTalk.getTargets( null );
=> [photoshop-11.0, illustrator-14.0]
BridgeTalk.getTargets( null, "en_US" );
=> [photoshop-10.0-en_US, photoshop-11.0-en_US]
BridgeTalk.getTargets( null, null );
=> [photoshop-10.0-en_US, photoshop-11.0-en_us, illustrator-14.0-de_de]
isRunning()
BridgeTalk.isRunning (specifier)
specifier

A specifier for the target application; see "Application specifiers" on page 191.

Returns true if the given application is running and active on the local computer.
launch()
BridgeTalk.launch (specifier [, where])
specifier

A specifier for the target application; see "Application specifiers" on page 191.

where

Optional. If the value "background" is specified, the application’s main window is
not brought to the front of the screen.

Launches the given application on the local computer. It is not necessary to launch an application
explicitly in order to send it a message; sending a message to an application that is not running
automatically launches it.
Returns true if the application has already been launched, false if it was launched by this call.
loadAppScript()
BridgeTalk.loadAppScript (specifier)
specifier

A specifier for the target application; see "Application specifiers" on page 191.

Loads the startup script for an application from the common StartupScripts folders. Use to
implement late loading of startup scripts.
Returns true if the script was successfully loaded.

ping()
BridgeTalk.ping (specifier, pingRequest)
specifier

A specifier for the target application; see "Application specifiers" on page 191.

pingRequest

An identifying key string for a specific type of return value. One of:
STATUS: Returns the processing status; see getStatus().
DIAGNOSTICS: Returns a diagnostic report that includes a list of valid ping keys.
ECHO_REQUEST: Returns ECHO_RESPONSE for a simple ping request.

Sends a message to another application to determine whether it can be contacted. Returns a string
whose meaning is defined by the ping-request key.
pump()
BridgeTalk.pump ()

Checks all active messaging interfaces for outgoing and incoming messages, and processes them if
there are any.
Returns true if any messages have been processed, false otherwise.
(Most applications have a message processing loop that continually checks the message queues, so
use of this method is rarely required.)

BridgeTalk message object
The message object defines the basic communication packet that is sent between applications. Its
properties allow you to specify the receiving application (the target), the data to send to the target (the
body), and the type of data that is sent. The messaging protocol is extensible; it allows you to define new
types of data for the type property, and to send and receive arbitrary additional information with the
headers property.

BridgeTalk message object constructor
Create a new message object using a simple constructor:
var bt = new BridgeTalk;

Before you send a message to another application, you must set the target property to the receiving
application, and the body property to the data message (typically a script) you want to send.

BridgeTalk message object properties
body

String

The data payload of the message. Read/write.
If this is an unsolicited message to another application, typically contains a
script packaged as a string. The target application’s full document object
model (DOM) is available within the script.
If this message is a result returned from the static BridgeTalk onReceive
method of a target application, directed to an onResult callback in this object,
contains the return result from that method flattened into a string. See
"Passing values between applications" on page 176.
If this message contains an error notification for the onError callback, contains
the error message.

headers

Object

A JavaScript object containing script-defined headers. Read/write.
Use this property to define custom header data to send supplementary
information between applications. You can add any number of new headers. The
headers are name/value pairs, and can be accessed with the JavaScript dot
notation (msgObj.headers.propName), or bracket notation
(msgObj.headers[propName]). If the header name conforms to JavaScript symbol
syntax, use the dot notation. If not, use the bracket notation.
The predefined header ["Error-Code"] is used to return error messages to a
sender; see "Messaging error codes" on page 190.
Examples of setting headers:
bt.headers.info = "Additional Information";
bt.headers ["Error-Code"] = 8;

Examples of getting header values:
var info = bt.headers.info;
var error = bt.headers ["Error-Code"];
sender

String

The application specifier for the sending application (see "Application specifiers"
on page 191). Read/write.

target

String

The application specifier for the target, or receiving, application (see "Application
specifiers" on page 191). Read/write.

timeout

Number The number of seconds before the message times out. Read/write.
If a message has not been removed from the input queue for processing before
this time elapses, the message is discarded. If the sender has defined an
onTimeout callback for the message, the target application sends a time-out
message back to the sender.


type

String

The message type, which indicates what type of data the body contains.
Read/write. Default is ExtendScript.
You can define a type for script-defined data. If you do so, the target application
must have a static BridgeTalk onReceive method that checks for and processes
that type.

BridgeTalk message object callbacks
NOTE: The message callbacks are optional, and are not implemented by all message-enabled applications.
onError

Function

A callback function that the target application invokes to return an error
response to the sender. It can send JavaScript run-time errors or exceptions,
or C++ exceptions.
To define error-response behavior, set this to a function definition in the
following form:
bridgeTalkObj.onError = function( errorMsgObject ) {
// error handler defined here
};

The body property of the received message object contains the error
message, and the headers property contains the error code in its
Error-Code property. See "Messaging error codes" on page 190.
The function returns undefined.
onReceived

Function

A callback function that the target application invokes to confirm that the
message was received. (Note that this is different from the static onReceive
method of the BridgeTalk class that handles unsolicited messages.)
To define a response to receipt notification, set this to a function definition
in the following form:
bridgeTalkObj.onReceived = function( origMsgObject ) {
// handler defined here
};

The target passes back the original message object, with the body property
set to the empty string.
The function returns undefined.


onResult

Function



A callback function that the target application invokes to return a response
to the sender. This can be an intermediate response or the final result of
processing the message.
To handle the response, set this to a function definition in the following
form:
bridgeTalkObj.onResult = function( responseMsgObject ) {
// handler defined here
};

The target passes a new message object, with the body property set to the
result string. This is the result of the target application’s static BridgeTalk
onReceive method, packaged as a UTF-8-encoded string. See "Passing
values between applications" on page 176.
onTimeout

Function

A callback function that the target application invokes with a time-out
message if time-out occurred before the target finished processing another
message previously sent by this application. To enable this callback, the
message must specify a value for the timeout property.
To define a response to the timeout event, set this to a function definition in
the following form:
bridgeTalkObj.onTimeout = function( timeoutMsgObject ) {
// handler defined here
};

BridgeTalk message object functions
send()
bridgeTalkObj.send ([timoutInSecs[, launchParameters]])
timoutInSecs

Optional. A maximum number of seconds to wait for a result before returning
from this function. The message is sent synchronously, and the function does
not return until the target has processed the message or this number of
seconds have passed.
If not supplied or 0, the message is sent asynchronously, and the function
returns immediately without waiting for a result.

launchParameters

Optional. A string of parameters to append to the name of the target
application when launching it, if the application is not already running.
If the target application is already running, this value is ignored.

Sends this message to the target application.
Returns true if the message could be sent immediately, false if it could not be sent or was queued
for sending later.
If the target application is not running and the message contains a body, the messaging system
automatically launches the target application, passing in any supplied launch parameters. In this
case, the message is queued rather than sent immediately, and this method returns false. The
message is processed once the application is running.
Sending the message does not guarantee that the target actually receives it. You can request
notification of receipt by defining an onReceived callback for this message object. (Note that this is
different from the static onReceive method of the BridgeTalk class that handles unsolicited
messages.)
sendResult()
bridgeTalkObj.sendResult (result)
result

You can send data of any type as the result value. The messaging framework
creates a BridgeTalk message object, and flattens this value into a string
which it stores in the body of that message. See "Passing values between
applications" on page 176.

When processing an unsolicited message, the static BridgeTalk onReceive method can return an
intermediate result to the sender by calling this method in the received message object. It invokes
the onResult callback of the original message, passing a new message object containing the
specified result value.
This allows you to send multiple responses to messages.
Returns true if the received message has an onResult callback defined and the response message
can be sent, false otherwise.

CHAPTER 5: Interapplication Communication with Scripts

Messaging error codes

Messaging error codes
The interapplication messaging protocol defines the following error codes, which are compatible with
ExtendScript error codes. Negative values indicate unrecoverable errors that cause ExtendScript to
terminate a running script.
1

General error

8

Syntax error

20

Bad argument list

27

Stack overrun

-28

Out of memory

-29

Uncaught exception

31

Bad URI

32

Cannot perform requested action

-33

Internal error

-36

Not yet implemented

41

Range error

44

Cannot convert

47

Type mismatch

48

File or folder does not exist

49

File of folder already exists

50

I/O device is not open

51

Read past EOF

52

I/O error

53

Permission denied

54

JavaScript execution

56

Cannot connect

57

Cannot resolve reference

58

I/O timeout

59

No response



Application and namespace specifiers
All forms of interapplication communication use Application specifiers to identify Adobe applications.
In all ExtendScript scripts, the #target directive can use an specifier to identify the application that
should run that script. See "Preprocessor directives" on page 233.
In interapplication messages, the specifier is used as the value of the target property of the message
object, to identify the target application for the message.
Adobe Bridge (which is integrated with many Adobe applications) uses an application specifier as the
value of the document.owner property, to identify another application that created or opened an
Adobe Bridge browser window. For details, see the Adobe Bridge JavaScript Reference.
When a script for one application invokes cross-DOM or exported functions, it identifies the exporting
application using Namespace specifiers.

Application specifiers
Application specifiers are strings that encode the application name, a version number and a language
code. They take the following form:
appname[_instance[[-version[-locale]]]
appname

An Adobe application name. For example, these are the identifying strings for applications
that can use the ExtendScript Toolkit in Creative Suite 4:
aftereffects
bridge
estoolkit
illustrator
incopy
indesign
indesignserver
photoshop

instance

Optional. An additional string appended with an underscore, that distinguishes the
instance for those applications (such as InDesign Server) that support the launching and
running of multiple instances.
For example, for a server launched with SOAP port 12345, the specifier would be
indesignserver_configuration_12345.


version



Optional. A number indicating at least a major version. The number should include a minor
version separated from the major version number by a dot; for example, 1.5.
If not supplied, assumes the same suite version as the sending application, if possible;
otherwise, the highest available version number.
This is the complete list of identifying names and version numbers for applications that can
use interapplication messaging in Creative Suite 4:
acrobat-9.0
aftereffects-9.0
soundbooth-2.0
bridge-3.0
contribute-5.0
devicecentral-2.0
dreamweaver-10.0
encore-4.0
estoolkit-3.0
fireworks-10.0
flash-10.0
illustrator-14.0
indesign-6.0
indesignserver-6.0
incopy-6.0
photoshop-11.0
premierepro-4.0
audition-4.0
ame-1.0
exman-2.0

locale

Optional. An Adobe locale code, consisting of a 2-letter ISO-639 language code and an
optional 2-letter ISO 3166 country code separated by an underscore. Case is significant. For
example, en_us, en_uk, ja_jp, de_de, fr_fr.
If not supplied, ExtendScript uses the current platform locale.
Do not specify a locale for a multilingual application, such as Bridge, that has all locale
versions included in a single installation.

The following are examples of legal specifiers:
photoshop
bridge-3.0
indesign_1-6.0
illustrator-14.0
illustrator-14.0-de_de

If a specifier does not supply specific version and locale information, the framework tries to find the most
appropriate available installation. It tries to match to available applications in this order:
1. Peer applications (from the same suite)
2. Applications with the highest available version number
3. Applications that are currently running
4. Applications that match the current locale
5. Applications for any locale

Namespace specifiers
When calling cross-DOM and exported functions from other applications, a namespace specifier qualifies
the function call, directing it to the appropriate application.
Namespace specifiers consist of an application name, as used in an application specifier, with an optional
major version number. Use it as a prefix to an exported function name, with the JavaScript dot notation.
appname[majorVersion].functionName(args)

For example:
To call the cross-DOM function quit in Photoshop, use photoshop.quit(), and to call it in Adobe
Illustrator®, use illustrator.quit().
To call the exported function place, defined for Illustrator CS5 version 15 call
illustrator15.place(myFiles).
For information about the cross-DOM and exported functions, see "Remote function calls" on page 166.
