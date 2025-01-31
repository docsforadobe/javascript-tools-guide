.. _messaging-framework-api-reference:

Messaging framework API reference
=================================

This application programming interface (API) defines a communication protocol between
message-enabled applications. These objects are available to all ExtendScript scripts when any of the
applications is loaded.

The messaging protocol is extensible. Although it is primarily designed to send scripts, you can use it to
send other kinds of data.

The messaging API defines the BridgeTalk class. Static properties and methods of the class provide
access to environmental information relevant for communication between applications. Instantiate the
class to create a BridgeTalk message object, which encapsulates the message itself. For discussion and
examples, see :ref:`communicating-through-messages`, and the example code provided with the
`Adobe ExtendScript SDK <https://github.com/Adobe-CEP/CEP-Resources/tree/master/ExtendScript-Toolkit>`_.

Example code
************

The sample code distributed with the `Adobe ExtendScript SDK <https://github.com/Adobe-CEP/CEP-Resources/tree/master/ExtendScript-Toolkit>`_ includes these code examples that
specifically demonstrate the use of interapplication messaging:

.. list-table::

  * - **Interapplication messaging**
    -
  * - `MessagingBetweenApps.jsx <https://github.com/Adobe-CEP/CEP-Resources/blob/master/ExtendScript-Toolkit/Samples/javascript/MessagingBetweenApps.jsx>`_
    - Shows how to send a message to a Creative Suite application and receive a response.
  * - `MessageSendingToInDesign.jsx <https://github.com/Adobe-CEP/CEP-Resources/blob/master/ExtendScript-Toolkit/Samples/javascript/MessageSendingToInDesign.jsx>`_
    - Sends message to InDesign through BridgeTalk.
  * - SendArrayToPhotoshop.jsx
    - Sends message to Photoshop that creates an array in the target and passes it back to the sender.
  * - `SendObjectToPhotoshop.jsx <https://github.com/Adobe-CEP/CEP-Resources/blob/master/ExtendScript-Toolkit/Samples/javascript/SendObjectToPhotoshop.jsx>`_
    - Sends message to Photoshop that creates a JavaScript object in the target and passes it back to the sender.
  * - `SendDOMObjectToPhotoshop.jsx <https://github.com/Adobe-CEP/CEP-Resources/blob/master/ExtendScript-Toolkit/Samples/javascript/SnpSendDOMObject.jsx>`_
    - Sends message to Photoshop that creates a Photoshop object in the target and passes values from it back to the sender.
  * - `SaveAsDifferentFileType.jsx <https://github.com/Adobe-CEP/CEP-Resources/blob/master/ExtendScript-Toolkit/Samples/javascript/SaveAsDifferentFileType.jsx>`_
    - Locates an image file, uses messaging to load it into Photoshop and save it as a different file type.
