Introduction
JavaScript is a platform-independent scripting language that you can use to control many features and
automate many tasks in Adobe® applications. Scripting is easier to learn and use than many other kinds of
programming, and provides a convenient way of automating repetitive tasks or extending applications to
provide additional tools for other users.
If you are new to scripting, see Adobe Creative Suite: Introduction to Scripting, which introduces basic
scripting concepts and describes different scripting languages that are available, including JavaScript.
JavaScript and other scripting languages are object-oriented, and this book also describes the basic
concepts of object-oriented programming and document object models.
Each application that supports JavaScript also provides an application-specific Scripting Guide that
introduces the object model for that application, and reference material for the objects. This
document provides information about the JavaScript features, tools, and objects that are common to
all Adobe applications that support JavaScript.
This document does not teach JavaScript. If you are familiar with scripting or programming in general,
but unfamiliar with JavaScript, see publicly available Web resources and documents, such as:
The public JavaScript standards organization web site: www.ecma-international.org
JavaScript: The Definitive Guide, David Flanagan, O’Reily Media Inc, 2002. ISBN 0-596-00048-0
JavaScript Bible, Danny Goodman, Hungry Minds Inc, 2001. ISBN 0-7645-4718-6
Adobe Scripting, Chandler McWilliams, Wiley Publishing, Inc., 2003. ISBN 0-7645-2455-0
NOTE: Check for updated versions of this document at Adobe Developer Center,
http://www.adobe.com/devnet/scripting.

ExtendScript overview
Adobe provides an extended implementation of JavaScript, called ExtendScript, that is used by many
Adobe applications that provide a scripting interface. In addition to implementing the JavaScript
language according to the ECMA JavaScript specification, ExtendScript provides certain additional
features and utilities.
This document describes JavaScript modules, tools, utilities, and features that are available to all
JavaScript-enabled Adobe applications.
NOTE: Some modules, and features of some modules, are optional. Check the product documentation for
each application for details of which modules and features are implemented.

Example code
The Adobe ExtendScript SDK, which contains this document, also contains a set of code samples that
demonstrate how to use features of ScriptUI, interapplication communication, and external
communication. This book refers to these samples by name for illustration of concepts and techniques.
You can download the SDK from Adobe Developer Center, http://www.adobe.com/devnet/scripting/.
9

CHAPTER 1: Introduction

ExtendScript overview

10

The samples are located under the ExtendScript SDK root directory:
SDKroot/Samples/javascript/
SDKroot/Samples//javascript/resources/

sample scripts
resources, such as image or flash files

Development and debugging tools
For help in developing, debugging, and testing scripts, Adobe provides the ExtendScript Toolkit, an
interactive development and testing environment for ExtendScript, which is installed with all
JavaScript-enabled applications. For complete details, see Chapter 2, "The ExtendScript Toolkit."
ExtendScript also provides global objects that support development and debugging:
A global debugging object, the Dollar ($) object.
A reporting utility for ExtendScript elements, the ExtendScript reflection interface.
For complete details, see Chapter 8, "ExtendScript Tools and Features."

Cross-platform file-system access
Adobe ExtendScript defines File and Folder classes that simplify cross-platform file-system access. These
classes are available to all applications that support a JavaScript interface.
For complete details, see Chapter 3, "File System Access."

User-interface development tools
Adobe provides the ScriptUI module, which works with the ExtendScript JavaScript interpreter to provide
JavaScript scripts with the ability to create and interact with user interface elements. It provides an object
model for windows and user-interface control elements within an Adobe application. For complete details,
see Chapter 4, "User-Interface Tools."
In addition, ExtendScript provides:
Global functions for localization of display strings; see "Localizing ExtendScript strings" on page 224
Global functions for displaying short messages in dialog boxes; see "User notification dialogs" on
page 227.
An object type for specifying measurement values together with their units; see "Specifying
measurement values" on page 230.

Interapplication communication and messaging
ExtendScript provides a common scripting environment for all Adobe JavaScript-enabled applications,
and allows interapplication communication through scripts.
Different levels of communication are provided through the cross-DOM and the messaging framework.
Cross-DOM functions are a limited set of basic functions common across all message-enabled
applications, which allow your script to, for example, open or print files in other applications, simply by
calling the open or print function for that application.

CHAPTER 1: Introduction

ExtendScript overview

11

In addition to the basic set of common functions, some applications provide more extensive sets of
exported JavaScript functions to other applications.
The interapplication messaging framework is an application programming interface (API) that allows
extensive control over communication between applications. The API allows you to send messages to
other applications and receive results, and to receive messages sent by other applications and return
results. Typically the data passed between applications are JavaScript scripts. However, the messaging
framework is extensible. It allows you to define different types of data to send between applications,
and to specify how they are handled.
For complete details, see Chapter 5, "Interapplication Communication with Scripts."

External communication
ExtendScript offers tools for communicating with other computers or the internet using standard
protocols. The Socket object supports low-level TCP connections.
For complete details, see Chapter 6, "External Communication Tools."

External shared-library integration
You can extend the JavaScript DOM for an application by writing a C or C++ shared library, compiling it for
the platform you are using, and loading it into JavaScript as an ExternalObject instance. A shared library
is implemented by a DLL in Windows, a bundle or framework in Mac OS, or a SharedObject in UNIX.
For complete details, see Chapter 7, "Integrating External Libraries."

Additional utilities and features
ExtendScript provides these utilities and features:
JavaScript language enhancements:
Tools for combining scripts, such as a #include directive. See "Preprocessor directives" on
page 233.
Support for extending or overriding math and logical operator behavior on a class-by-class basis.
See "Operator overloading" on page 235.
For complete details, see Chapter 8, "ExtendScript Tools and Features."
JavaScript compilation, through the ExtendScript Toolkit. See Chapter 2, "The ExtendScript Toolkit.
XML integration: ExtendScript defines the XML object, which allows you to process XML with your
JavaScript scripts. For complete details, see Chapter 9, "Integrating XML into JavaScript."
Scripting support for XMP metadata manipulation: XMPScript provides a JavaScript API for the Adobe
XMP Toolkit. For complete details, see Chapter 10, "Scripting Access to XMP Metadata."

CHAPTER 1: Introduction

Scripting for specific applications

12

Scripting for specific applications
On startup, all Adobe JavaScript-enabled applications execute JSX files that they find in their startup
directories; some of these are installed by applications, and some can be installed by scripters. The policies
of different applications vary as to the locations, write access, and loading order.
In addition, individual applications may look for application-specific scripts in particular directories, which
may be configurable. Some applications allow access to scripts from menus; all of them allow you to load
and run scripts using the ExtendScript Toolkit.
For details of how to load and run scripts for any individual application, see the JavaScript Scripting Guide
for that application.

Startup scripts
A script in a startup directory might be executed on startup by multiple applications. If you place a script in
such a directory, it must contain code to check whether it is being run by the intended application. You can
do this using the appName static property of the BridgeTalk class. For example:
if( BridgeTalk.appName == "bridge" ) {
//continue executing script
}

If a script that is run by one application will communicate with another application or add functionality
that depends on another application, it must first check whether that application/version is installed. You
can do this using the BridgeTalk.getSpecifier() static function. For example:
if( BridgeTalk.appName == "bridge-2.0" ) {
// Check to see that Photoshop is installed.
if( BridgeTalk.getSpecifier("photoshop",10)){
// Add the Photoshop automate menu to the Adobe Bridge UI.
}
}

For details of interapplication communication, see Chapter 5, "Interapplication Communication with
Scripts."

JavaScript variables
Scripting shares a global environment, so any script executed at startup can define variables and functions
that are available to all scripts. In all cases, variables and functions, once defined by running a script that
contains them, persist in subsequent scripts during a given application session. Once the application is
quit, all such globally defined variables and functions are cleared. Scripters should be careful about giving
variables in scripts unique names, so that a script does not inadvertently reassign global variables
intended to persist throughout a session.
