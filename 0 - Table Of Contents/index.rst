======================
JAVASCRIPT TOOLS GUIDE
======================

--------
Contents
--------

Introduction

ExtendScript overview

    - Example code
    - Development and debugging tools
    - Cross-platform file-system access
    - User-interface development tools
    - Interapplication communication and messaging
    - External communication
    - External shared-library integration
    - Additional utilities and features
    - Copyright

Scripting for specific applications

    - Startup scripts
    - JavaScript variables


The ExtendScript Toolkit

    - Configuring the Toolkit window
    - Panel menus
    - Document windows
    - Workspaces
    - Dialogs

Selecting scripts

    - The Scripts panel and favorite script locations
    - The Script Editor
    - Navigation aids
    - Coding aids
    - Searching in text
    - Syntax marking

Debugging in the Toolkit

    - Selecting a debugging target
    - The JavaScript console
    - Controlling code execution
    - Visual indication of execution states
    - Setting breakpoints
    - Evaluation in help tips
    - Tracking data
    - The call stack

Code profiling for optimization
Inspecting object models


File System Access

    - Using File and Folder objects
    - Specifying paths
    - Unicode I/O
    - File error handling

File access error messages
File- and Folder-supported encoding names

    - Additional encodings

File object

    - File object constructors
    - File class properties
    - File class functions
    - File object properties
    - File object functions

Folder object

    - Folder object constructors
    - Folder class properties
    - Folder class functions
    - Folder object properties
    - Folder object functions


User-Interface Tools
Code examples for ScriptUI
ScriptUI programming model

    - Creating a window
    - Container elements
    - Window layout
    - Adding elements to containers
    - Removing elements

Types of controls

    - Containers
    - User-interface controls
    - Displaying images
    - Creating multi-column lists
    - Prompts and alerts
    - Modal dialogs

Size and location objects

    - Size and location object types

Drawing objects
Resource specifications

    - Using resource strings

Defining behavior with event callbacks and listeners

    - Defining event-handler callback functions
    - Simulating user events
    - Registering event listeners for windows or controls
    - How registered event-handlers are called
    - Communicating with the Flash application

Automatic layout

    - Default layout behavior
    - Automatic layout properties
    - Custom layout-manager example
    - The AutoLayoutManager algorithm
    - Automatic layout restrictions

Managing control titles

    - Title alignment and orientation
    - Title character width and justification
    - Title truncation
    - Margins around the title and graphic object

Localization in ScriptUI objects

    - Variable values in localized strings
    - Enabling automatic localization

ScriptUI object reference
ScriptUI class

    - ScriptUI class properties
    - ScriptUI class functions
    - Environment object

Common properties
Window class

    - Window class properties
    - Window class functions

Window object

    - Window object constructor
    - Window object properties
    - Container properties
    - Window object functions
    - Window event-handling callbacks

Control objects

    - Control object constructors
    - Control types and creation parameters
    - Control object properties
    - Control object functions
    - Control event-handling callbacks
    - DrawState object

Event handling

    - UIEvent base class
    - KeyboardEvent object
    - MouseEvent object
    - Keyboard state object

Graphic customization objects

    - ScriptUIGraphics object
    - ScriptUIBrush object
    - ScriptUIFont object
    - ScriptUIImage object
    - ScriptUIPath object
    - ScriptUIPen object
    - Custom element class

LayoutManager object

    - AutoLayoutManager object constructor
    - AutoLayoutManager object properties
    - AutoLayoutManager object functions


Interapplication Communication with Scripts
Communications overview

    - Remote function calls
    - Messaging framework
    - Identifying applications

Cross-DOM functions

    - Application-specific exported functions
    - Startup folder locations
    - Cross-DOM API reference

Communicating through messages

    - Sending messages
    - Receiving messages
    - Handling unsolicited messages
    - Handling responses from the message target
    - Passing values between applications

Messaging framework API reference
BridgeTalk class

    - BridgeTalk class properties
    - BridgeTalk class functions

BridgeTalk message object

    - BridgeTalk message object constructor
    - BridgeTalk message object properties
    - BridgeTalk message object callbacks
    - BridgeTalk message object functions

Messaging error codes
Application and namespace specifiers

    - Application specifiers
    - Namespace specifiers

External Communication Tools
Socket object

    - Chat server sample

Socket object reference


Integrating External Libraries
Loading and using shared libraries
ExternalObject object

    - ExternalObject constructor
    - ExternalObject class properties
    - ExternalObject class function
    - ExternalObject instance function

Defining entry points for direct access

    - Additional functions
    - Library initialization
    - Library termination

Defining entry points for indirect access

    - Shared-library function API
    - Support structures

ExtendScript Tools and Features
Dollar ($) object

    - Dollar ($) object properties
    - Dollar ($) object functions

ExtendScript reflection interface

    - Reflection object
    - ReflectionInfo object

Localizing ExtendScript strings

    - Variable values in localized strings
    - Enabling automatic localization
    - Locale names
    - Testing localization
    - Global localize function

User notification dialogs

    - Global alert function
    - Global confirm function
    - Global prompt function

Specifying measurement values

    - UnitValue object
    - Converting pixel and percentage values
    - Computing with unit values

Preprocessor directives
Operator overloading


Integrating XML into JavaScript
The XML Object

    - Accessing XML elements
    - Accessing XML attributes
    - Viewing XML objects
    - Modifying XML elements and attributes
    - Deleting elements and attributes
    - Retrieving contained elements
    - Creating and accessing namespaces
    - Mixing XML and JavaScript
    - XML lists

XML Object Reference

    - XML object
    - Global functions
    - QName object
    - Namespace object


Scripting Access to XMP Metadata

    - Accessing the XMP scripting API
    - Using the XMP scripting API

XMPScript object reference

    - XMPAliasInfo object
    - XMPConst object
    - XMPDateTime object
    - XMPFile object
    - XMPFileInfo object
    - XMPIterator object
    - XMPMeta object
    - XMPPacketInfo object
    - XMPProperty object
    - XMPUtils object

Porting Guide

Index
