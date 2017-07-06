.. _communicating-through-messages:

Communicating through messages
==============================
Adobe Bridge provides an application programming interface (API) that defines a communication
protocol between Adobe ExtendScript- and message-enabled applications. This provides the most
general mechanism for communication between applications. A messaging-enabled application can
launch another messaging-enabled application, and send or receive scripts to effect certain actions. For
example, from within Adobe Bridge, a script can launch Photoshop, and then send a script to Photoshop
that requests a photomerge operation.
While the exported functions allow specific access to certain capabilities of the application, the script in an
interapplication message allows full access to the target application's document object model (DOM), in
addition to all cross-DOM and application exported functions.
The messaging API defines the BridgeTalk class, whose globally available static properties and functions
provide access to environmental information relevant for communication between applications. You can
instantiate this class to create a BridgeTalk message object, which encapsulates a message and allows you
to send it to another application. For details of these objects, see :ref:`messaging-framework-api-reference`.

.. _sending-messages:

Sending messages
----------------
To send a script or other data to another application, you must create and configure a BridgeTalk message
object. This object contains the data to be sent (generally a script to be executed in the target application),
and also specifies how to handle the response.
This simple example walks through the steps of sending a script from Adobe Bridge CS5 to Photoshop
CS5, and receiving a response.

*Step 1: Check that the target application is installed*

Before you can actually send a message, you must check that the required version of the target application
is installed. The function ``getSpecifier()``, available in the global namespace through the BridgeTalk
class, provides this information.

For example, this code, which will send a message to Adobe Bridge CS5 as part of a script being executed
by Photoshop CS5, checks that the required version of Adobe Bridge is installed::

  var targetApp = BridgeTalk.getSpecifier( "bridge-3.0");
  if( targetApp ) {
    // construct and send message
  }

When you send the message, the messaging framework automatically launches the target application, if it
is not already running.

*Step 2: Construct a message object*

The next step is to construct a message to send to the application. You do this by creating a BridgeTalk
message object, and assigning values to its properties. You must specify the target application and the
message body, which is usually a script packaged into a string.
Scripts sent in messages can be very complex, and can use the full DOM of the target application. This
example defines a message script that accesses the Adobe Bridge DOM to request the number of files or
folders found in a specific folder::

  // create a new BridgeTalk message object

  var bt = new BridgeTalk;
  // send this msg to the Adobe Bridge CS4 application
  var targetApp = BridgeTalk.getSpecifier( "bridge-3.0");
  bt.target = targetApp;
  // the script to evaluate is contained in a string in the "body" property
  bt.body = "new Document('C:\\BridgeScripts');
  app.document.target.children.length;"

*Step 3: Specify how to handle a response*

If you want to handle a response for this message, or use the data that is returned from the script's
evaluation, you must set up the response-handling mechanism before you send the message. You do this
by defining the onResult callback in the message object.

.. note:: The message callbacks are optional, and are not implemented by all message-enabled applications.
  The response to a message is, by default, the result of evaluation of the script contained in that message's
  body property. The target application might define some different kind of response; see :ref:`receiving-messages`.
  When the target has finished processing this message, it looks for an onResult callback in the message
  object it received. If it is found, the target automatically invokes it, passing it the response. The response is
  packaged into a string, which is in turn packaged into the body property of a new message object. That
  message object is the argument to your onResult callback function.

This handler, for example, processes the returned result using a script-defined processResult function::

  bt.onResult = function(returnBtObj) {
    processResult(returnBtObj.body);
  }

If you want to handle errors that might arise during script processing, you can define an onError callback in
the message object. Similarly, you can define a timeout value and onTimeout callback to handle the case
where the target cannot process the message within a given time. For more information, see :ref:`handling-responses-from-the-message-target`.

.. note:: If you define callbacks to handle a response, you must store the message in a variable that still exists
  when the response is received. Otherwise, JavaScript might garbage-collect the message object, and the
  response would be lost.

*Step 4: Send the message*

To send the message, call the message object's send method. You do not need to specify where to send
the message to, since the target application is set in the message itself::

  bt.send();

You can optionally specify a timeout value, which makes the call synchronous; when you do this, the
method waits for a response from the target application, or for the timeout value to expire, before
returning. When a timeout is not specified, as in this example, the call is asynchronous and the send()
method returns immediately.
A second optional parameter allows you to specify launch parameters, in case the target application is not
currently running, and the messaging framework needs to launch it.

The complete script looks like this::

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
    bt.body = "new Document('C:\\BridgeScripts');
    app.document.target.children.length;"
    // define result handler callback
    bt.onResult = function(returnBtObj) {
    processResult(returnBtObj.body); } //fn defined elsewhere
    // send the message asynchronously
    bt.send();
  }

.. _receiving-messages:

Receiving messages
------------------
An application can be the target of a message; that is, it receives an unsolicited message from another
application. An unsolicited message is handled by the static ``BridgeTalk.onReceive`` callback function in
the target application. See :ref:`handling-unsolicited-messages`.

An application that sends a message can receive response messages; that is, messages that come as the
result of requesting a response when a message was sent. These can be:
  - The result of an error in processing the message
  - The result of a timeout when attempting to process the message
  - A notification of receipt of the message
  - Intermediate responses
  - The final result of processing the message.

All of these response messages are sent automatically by the target application, and are handled by
callbacks defined in the sending message object. For details, see :ref:`handling-responses-from-the-message-target`.

.. _handling-unsolicited-messages:

Handling unsolicited messages
-----------------------------
To specify how the application should handle unsolicited incoming messages, define a callback handler
function in the static ``onReceive`` property of the ``BridgeTalk`` class. This function takes a single argument, a
``BridgeTalk`` message object.

The default behavior of the ``onReceive`` handler is to evaluate the body of the received message with
JavaScript, and return the result of that evaluation. (The result of evaluating a script is the result of the last
line of the script.) To return the result, it creates a new message object, encapsulates the result in a string in
the body property of that object, and passes that object to the onResult callback defined in the original
message.

If an error occurs on evaluation, the default ``onReceive`` handler returns the error information using a
similar mechanism. It creates a new message object, encapsulates the error information in a string in the
body property of that object, and passes that object to the onError callback defined in the original
message.

To change the default behavior set the ``BridgeTalk.onReceive`` property to a function definition in the
following form::

  BridgeTalk.onReceive = function( bridgeTalkObject ) {
    // callback definition here
  };

The ``body`` property of the received message object contains the received data.

The function can return any type.

The function that you define does not need to explicitly create and return a ``BridgeTalk`` message object.
The messaging framework creates a new ``BridgeTal``k message object, and packages the return value of
the ``onReceive`` handler as a string in the body property of that object.

Return values are flattened into a string using the Unicode Transformation Format-8 (UTF-8) encoding. If
the function does not specify a return value, the resulting string is the empty string.

The result object is transmitted back to the sender if the sender has implemented an ``onResult`` callback for
the original message.

Message-handling examples
-------------------------

This example shows the default mechanism for handling unsolicited messages received from other
applications. This simple handler executes the message's data as a script and returns the results of that
execution::

  BridgeTalk.onReceive = function (message) {
    return eval( message.body );
  }

This example shows how you might extend the receive handler to process a new type of message::
  BridgeTalk.onReceive = function (message) {
    switch (message.type) {
      case "Data":
        return processData( message );
        break;
      default: //"ExtendScript"
        return eval( mesage.body );
    }
  }

.. _handling-responses-from-the-message-target:

Handling responses from the message target
------------------------------------------
To handle responses to a message you have sent, you define callback handler functions in the message
object itself. The target application cannot send a response message back to the sender unless the
message object it received has the appropriate callback defined.

.. note:: The message callbacks are optional, and are not implemented by all message-enabled applications.

When your message is received by its target, the target application's static BridgeTalk object's onReceive
method processes that message, and can invoke one of the message object's callbacks to return a
response. In each case, the messaging framework packages the response in a new message object, whose
target application is the sender. Your callback functions receive this response message object as an
argument.

A response message can be:

- The result of an error in processing the message. This is handled by the onError callback.
  If an error occurs in processing the message body (as the result of a JavaScript syntax error, for
  instance), the target application invokes the onError callback, passing a response message that
  contains the error code and error message. If you do not have an onError callback defined, the error is
  completely transparent. It can appear that the message has not been processed, since no result is ever
  returned to the onResult callback.
- A notification of receipt of the message. This is handled by the onReceived callback.
  Message sending is asynchronous. Getting a true result from the send method does not guarantee
  that your message was actually received by the target application. If you want to be notified of the
  receipt of your message, define the onReceived callback in the message object. The target sends back
  the original message object to this callback, first replacing the body value with an empty string.
- The result of a time-out. This is handled by the onTimeout callback.
  You can specify a number of seconds in a message object's timeout property. If the message is not
  removed from the input queue for processing before the time elapses, it is discarded. If the sender has
  defined an onTimeout callback for the message, the target application sends a time-out message back
  to the sender.
- Intermediate responses. These are handled by the onResult callback.
  The script that you send can send back intermediate responses by invoking the original message
  object's sendResult() method. It can send data of any type, but that data is packaged into a body string
  in a new message object, which is passed to your callback. See :ref:`passing-values-between-applications`.
- The final result of processing the message. This is handled by the onResult callback.
  When it finishes processing your message, the target application can send back a result of any type. If
  you have sent a script, and the target application is using the default BridgeTalk.onReceive callback
  to process messages, the return value is the final result of evaluating that script. In any case, the return
  value is packaged into a body string in a new message object, which is passed to your callback. See
  :ref:`passing-values-between-applications`.

The following examples demonstrate how to handle simple responses and multiple responses, and how to
integrate error handling with response handling.

Example: Receiving a simple response
------------------------------------------

In this example, an application script asks Adobe Bridge to find out how many files and folders are in a
certain folder, which the evaluation of the script returns. (The default BridgeTalk.onReceive method
processes this correctly.)
The ``onResult`` method saves that number in ``fileCountResult``, a script-defined property of the message,
for later use::

  var bt = new BridgeTalk;
  bt.target = "bridge-3.0";
  bt.body = "new Document('C:\\BridgeScripts');
  app.document.target.children.length;"
  bt.onResult = function( retObj ) {
    processFileCount(retObj.body);
  }

  bt.send();

Example: Handling any error
---------------------------

In this example, the onError handler re-throws the error message within the sending application::

  var bt = new BridgeTalk;
  bt.onError = function (btObj) {
    var errorCode = parseInt (btObj.headers ["Error-Code"]);
    throw new Error (errorCode, btObj.body);
  }

Example: Handling expected errors and responses
-----------------------------------------------

This example creates a message that asks Adobe Bridge to return XMP metadata for a specific file. The
onResult method processes the data using a script-defined processFileSize function. Any errors are
handled by the onError method. For example, if the file requested is not an existing file, the resulting error
is returned to the onError method::

  var bt = new BridgeTalk;
  bt.target = "bridge-3.0";
  bt.body = "var tn = new Thumbnail('C/MyPhotos/temp.gif');
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
-------------------------------------------------------

This example integrates the sending of multiple responses with the evaluation of a message body. It sets
up a handler for a message such as the one sent in the following example.

The target application (Adobe Bridge) defines a static onReceive method to allow for a new type of
message, which it calls an iterator. An iterator type of message expects the message.body to use the
iteration variable i within the script, so that different results are produced for each pass through the while
loop. Each result is sent back to the sending application with the sendResult() method. When the
message.body has finished processing its task, it sets a flag to end the while loop::

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
          i++;
        }
        break;
      default: //"ExtendScript"
        return eval( message.body );
    }
  }

Example: Setting up a sender to receive multiple responses
----------------------------------------------------------

This example sends a message of the type iterator, to be handled by the onReceive handler in the
previous example, and processes the responses received from that target.

The sending application creates a message whose script (contained in the body string) iterates through all
files in a specific folder (represented by an Adobe Bridge Thumbnail object), using the iterator variable i.

For each file in the folder, it returns file size data. For each contained folder, it returns -1. The last executed
line in the script is the final result value for the message.

The onResult method of the message object receives each intermediate result, stores it into an array,
resArr, and processes it immediately using a script-defined function processInterResult::

  // Code for send message and handling response
  // in the sending application (any message-enabled application)
  var idx = 0;
  var resArr = new Array;
  bt = new BridgeTalk;
  bt.target = "bridge";
  bt.type = "iterator";
  bt.body = "
  var fld = new Thumbnail(Folder('C/Junk'));
  if (i == (fld.children.length - 1))
  done = true; //no more files, end loop
  tn = fld.children[i];
  if (tn.spec.constructor.name == 'File')
  md = tn.core.immediate.size;
  else md = -1;
  ";

  // store intermediate results
  bt.onResult = function(rObj) {
    resArr[idx] = rObj.body;
    processInterResult(resArr[idx]);
    idx++;
  };

  bt.onError = function(eObj) {
    bt.error = eObj.body
  };

  bt.send();

.. _passing-values-between-applications:

Passing values between applications
-----------------------------------
The BridgeTalk.onReceive static callback function can return values of any type. The messaging
framework, however, packages the response into a response message, and passes any returned values in
the message body, first converting the result to a UTF-8-encoded string.

Passing simple types
--------------------

When your message object's onResult callback receives a response, it must interpret the string it finds in
the body of the response message to obtain a result of the correct type. Results of various types can be
identified and processed as follows:

=======  =========================================================================================================
Number   JavaScript allows you to access a string that contains a number directly as a number, without
         doing any type conversion. However, be careful when using the plus operator (+), which
         works with either strings or numbers. If one of the operands is a string, both operands are
         converted to strings and concatenated.
String   No conversion is required.
Boolean  The result string is either "true" or "false." You can convert it to a true boolean by evaluating it
         with the ``eval`` method.
Date     The result string contains the date in the form: ``"dow mmm dd yyyy hh:mm:ss GMT-nnnn".``

         For example "Wed Jun 23 2004 00:00:00 GMT-0700".
Array    The result string contains a comma delimited list of the elements of the array. For example, If
         the result array is ``[12, "test", 432]``, the messaging framework flattens this into the string
         ``"12,test,432"``.

         As an alternative to simply returning the array, the message target can use the ``toSource``
         method to return the code used to create the array. In this case, the sender must reconstitute
         the array by using the ``eval`` method on the result string in the response body. See discussion
         below.
=======  =========================================================================================================

Passing complex types
---------------------

When returning complex types (arrays and objects), the script that you send must construct a result string,
using the toSource method to serialize the array or object. In this case, the sender must reconstitute the
array or object by using the eval method on the result string in the response body.

**Passing an array with toSource and eval**

For example, the following code sends a script that returns an array in this way. The onResult callback that
receives the response uses eval to reconstruct the array::

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

**Passing an object with toSource and eval**

This technique is the only way to pass objects between applications. For example, this
code sends a script that returns an object containing some of the metadata for a
specific file and defines an onResult callback that receives the object::

  var bt = new BridgeTalk;
  bt.target = "bridge-3.0";

  //the script passed to the target application
  // returns the object using "toSource"
  bt.body = "var tn = new Thumbnail(File('C:\\Myphotos\\photo1.jpg'));
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

**Passing a DOM object**

You can send a script that returns a DOM object, but the resulting object contains only those properties
that were accessed within the script. For example, the following script requests the return of the Adobe
Bridge DOM Thumbnail object. Only the properties path and uri are accessed by the script, and only
those properties are returned::

  var bt = new BridgeTalk;
  bt.target = "bridge";

  //set up the script passed to the target application
  // to return the array using "toSource"
  bt.body = "var tn = new Thumbnail(File('C:\\Myphotos\\photo1.jpg'));
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
