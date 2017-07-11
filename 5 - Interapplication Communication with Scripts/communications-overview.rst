.. _communications-overview:

Communications overview
=======================
Scripts written for any message-enabled application can communicate with other message-enabled
applications in two ways; through directly calling functions defined in a remote application, and by
sending messages and receiving responses from a remote application. A specific syntax is provided for
identifying applications unambiguously.

--------------------------------------------------------------------------------

.. _remote-function-calls:

Remote function calls
---------------------
A limited set of basic functions (the cross-DOM) are common across all message-enabled applications, and
allow your script to, for example, open or print files in other applications, simply by calling the open or
print function for that application.

:ref:`cross-dom-functions` describes the usage of this feature.
:ref:`cross-dom-api-reference` provides reference details for the functions of the basic
cross-DOM.

Each message-enabled application can also export a set of functions to provide a selected set of
application-specific functionality; see :ref:`application-specific-exported-functions`.

For example, an Adobe Bridge script can request a photo merge in Photoshop by calling
photoshop.photomerge(files). The set of functions available for each application varies widely.

--------------------------------------------------------------------------------

.. _messaging-framework:

Messaging framework
-------------------
The interapplication messaging framework is a JavaScript application programming interface (API) that
allows extensive control over communication between applications. The API allows you to send messages
to other applications and receive results, and to receive messages sent by other applications and return
results. Typically the data passed between applications are JavaScript scripts. However, the messaging
framework is extensible. It allows you to define different types of data to send between applications, and
to specify how they are handled.

:ref:`communicating-through-messages` describes the usage of this feature.
:ref:`messaging-framework-api-reference` provides complete reference details.

--------------------------------------------------------------------------------

.. _identifying-applications:

Identifying applications
------------------------
When calling external functions or exchanging messages, you must identify particular applications using
namespace specifiers. A specifier consists of a specific name string (such as photoshop), and optional
additions that identify a particular release or locale version. Application specifiers are used occasionally in
other contexts as well. For details of the syntax, see :ref:`application-and-namespace-specifiers`.

Regardless of which method you use to perform interapplication communication, you must place your
script in a location where the application you want to run it can see it. There are different locations for the
startup scripts of the applications themselves, and for scripts provided by developers.

Because all JavaScript-enabled applications look in the same locations for scripts to run, the scripts
themselves must be explicit about which application they are meant for. A script should check that all
applications it needs to communicate with are installed with the correct version, and that any other
applications that might be installed do not run the script. For details, see :ref:`scripting-for-specific-applications`.
