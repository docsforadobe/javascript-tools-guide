# ExtendScript overview

Adobe provides an extended implementation of JavaScript, called ExtendScript, that is used by many
Adobe applications that provide a scripting interface. In addition to implementing the JavaScript
language according to the ECMA JavaScript specification, ExtendScript provides certain additional
features and utilities.

This document describes JavaScript modules, tools, utilities, and features that are available to all
JavaScript-enabled Adobe applications.

!!! note
    Some modules, and features of some modules, are optional. Check the product documentation for each application for details of which modules and features are implemented.

## Example code

The [Adobe ExtendScript SDK](https://github.com/Adobe-CEP/CEP-Resources/tree/master/ExtendScript-Toolkit), which contains this document, also contains a set of code samples that
demonstrate how to use features of ScriptUI, interapplication communication, and external
communication. This book refers to these samples by name for illustration of concepts and techniques.

You can download the latest (and last) SDK from [Github](https://github.com/Adobe-CEP/CEP-Resources/tree/master/ExtendScript-Toolkit). Earlier versions might still be accessible through [direct links](https://github.com/aenhancers/javascript-tools-guide/issues/2#issuecomment-1019312237).

The samples are located under the ExtendScript SDK root directory:

- `SDKroot/Samples/javascript/`: sample scripts
- `SDKroot/Samples/resources/`: resources, such as image or flash files

## Development and debugging tools

For help in developing, debugging, and testing scripts, Adobe provides the ExtendScript Toolkit, an
interactive development and testing environment for ExtendScript, which is installed with all
JavaScript-enabled applications.

For complete details, see [The ExtendScript Toolkit](../extendscript-toolkit/index.md#the-extendscript-toolkit).

ExtendScript also provides global objects that support development and debugging:

- A global debugging object, the Dollar ($) object.
- A reporting utility for ExtendScript elements, the ExtendScript reflection interface.

For complete details, see [ExtendScript Tools and Features](../extendscript-tools-features/index.md#extendscript-tools-and-features).

## Cross-platform file-system access

Adobe ExtendScript defines File and Folder classes that simplify cross-platform file-system access. These
classes are available to all applications that support a JavaScript interface.

For complete details, see [File System Access](../file-system-access/index.md#file-system-access).

## User-interface development tools

Adobe provides the ScriptUI module, which works with the ExtendScript JavaScript interpreter to provide
JavaScript scripts with the ability to create and interact with user interface elements. It provides an object
model for windows and user-interface control elements within an Adobe application. For complete details,
see [User-Interface Tools](../user-interface-tools/index.md#user-interface-tools).
In addition, ExtendScript provides:

- Global functions for localization of display strings; see [Localizing ExtendScript strings](../extendscript-tools-features/localizing-extendscript-strings.md#localizing-extendscript-strings)
- Global functions for displaying short messages in dialog boxes; see [User notification dialogs](../extendscript-tools-features/user-notification-dialogs.md#user-notification-dialogs).
- An object type for specifying measurement values together with their units; see [Specifying measurement values](../extendscript-tools-features/specifying-measurement-values.md#specifying-measurement-values).

## Interapplication communication and messaging

ExtendScript provides a common scripting environment for all Adobe JavaScript-enabled applications,
and allows interapplication communication through scripts.
Different levels of communication are provided through the cross-DOM and the messaging framework.

- Cross-DOM functions are a limited set of basic functions common across all message-enabled applications, which allow your script to, for example, open or print files in other applications, simply by calling the open or print function for that application. In addition to the basic set of common functions, some applications provide more extensive sets of exported JavaScript functions to other applications.
- The interapplication messaging framework is an application programming interface (API) that allows
  extensive control over communication between applications. The API allows you to send messages to
  other applications and receive results, and to receive messages sent by other applications and return
  results. Typically the data passed between applications are JavaScript scripts. However, the messaging
  framework is extensible. It allows you to define different types of data to send between applications,
  and to specify how they are handled.

For complete details, see [Interapplication Communication with Scripts](../interapplication-communication/index.md#interapplication-communication-with-scripts).

## External communication

ExtendScript offers tools for communicating with other computers or the internet using standard
protocols. The Socket object supports low-level TCP connections.

For complete details, see [External Communication Tools](../external-communication/index.md#external-communication-tools).

## External shared-library integration

You can extend the JavaScript DOM for an application by writing a C or C++ shared library, compiling it for
the platform you are using, and loading it into JavaScript as an ExternalObject instance. A shared library
is implemented by a DLL in Windows, a bundle or framework in Mac OS, or a SharedObject in UNIX.

For complete details, see [Integrating External Libraries](../integrating-external-libraries/index.md#integrating-external-libraries).

## Additional utilities and features

ExtendScript provides these utilities and features:

- JavaScript language enhancements
  - Tools for combining scripts, such as a `#include` directive. See [Preprocessor directives](../extendscript-tools-features/preprocessor-directives.md#preprocessor-directives).
  - Support for extending or overriding math and logical operator behavior on a class-by-class basis.
      See [Operator overloading](../extendscript-tools-features/operator-overloading.md#operator-overloading).
  - For complete details, see [ExtendScript Tools and Features](../extendscript-tools-features/index.md#extendscript-tools-and-features).
- JavaScript compilation, through the ExtendScript Toolkit. See [The ExtendScript Toolkit](../extendscript-toolkit/index.md#the-extendscript-toolkit).
- XML integration: ExtendScript defines the XML object, which allows you to process XML with your JavaScript scripts. For complete details, see [Integrating XML into JavaScript](../integrating-xml/index.md#integrating-xml-into-javascript).
- Scripting support for XMP metadata manipulation: XMPScript provides a JavaScript API for the Adobe
