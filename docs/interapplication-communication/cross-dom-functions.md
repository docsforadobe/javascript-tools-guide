# Cross-DOM functions

The cross-DOM is a small application programming interface (API), which provides a set of functions that
are common across message-enabled applications. These include functions to open files, execute scripts,
and print files. For details of the function set, see [Cross-DOM API reference](#cross-dom-api-reference).

You can access cross-DOM functions in any script by prefixing the function name with the namespace
specifier for the target application (see [Namespace specifiers](application-and-namespace-specifiers.md#namespace-specifiers)). For example, a Photoshop CC
script can call indesign.open(file) to open a file in Adobe InDesign® CC.

The cross-DOM functions for each application are implemented in JavaScript. You can see the
implementation for each installed application by reading its associated startup script in the Adobe startup
folder. For example, Adobe Illustrator® CC defines illustrator.open() in the illustrator-14.jsx
startup script (14 is the version number of the installed application). See [Startup folder locations](#startup-folder-locations).

**Example code**

The sample code distributed with the [Adobe ExtendScript SDK](https://github.com/Adobe-CEP/CEP-Resources/tree/master/ExtendScript-Toolkit) includes these code examples that
specifically demonstrate the use of cross-DOM functions:

| **Cross-DOM calls**                                                                                                                                 |                                                            |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| [OpenImageInPhotoshop.jsx](https://github.com/Adobe-CEP/CEP-Resources/blob/master/ExtendScript-Toolkit/Samples/javascript/OpenImageInPhotoshop.jsx) | Shows how to send an image file to be opened in Photoshop. |

---

## Application-specific exported functions

In addition to the required base cross-DOM functions, each message-enabled application can provide
application-specific functionality to all scripts through a simple syntax. You can access exported functions
in any script by prefixing the function name with the namespace specifier for the target application (see
[Namespace specifiers](application-and-namespace-specifiers.md#namespace-specifiers)). For example, Photoshop CS5 exports the photomerge function, so
an Illustrator CS5 script can directly call photoshop.photomerge(files).

The only difference between cross-DOM functions and the application-specific exported functions is that
all applications expose the same set of cross-DOM functions, whereas each application exposes its own set

of application-specific functions. Each application determines the extent of its exported functionality.
Some applications provide extensive support for exported functions, others less.

For details of additional functions that are exported by individual applications, refer to the startup scripts
for those applications. The application startup scripts are named appname-n.jsx, where n is the version
number of the installed application. See [Startup folder locations](#startup-folder-locations).

---

## Startup folder locations

For each platform, there is a startup folder shared by all Adobe Creative Suite 4 applications that support
JavaScript, and an application-specific startup folder.

- In Windows®, the installation startup folders are:
  `%CommonProgramFiles%\Adobe\Startup Scripts CS5\Adobe AppName\`
- In Mac OS®, the installation startup folders are:
  `/Library/Application Support/Adobe/Startup Scripts CS5/Adobe AppName/`

!!! note
    This is not the location in which to store your own startup scripts; see [Scripting for specific applications](../introduction/scripting-for-specific-applications.md#scripting-for-specific-applications).

---

## Cross-DOM API reference

All exported functions, including those of the cross-DOM API, are invoked through the exporting
application, identified by its namespace specifier (see [Namespace specifiers](application-and-namespace-specifiers.md#namespace-specifiers)). For example:

```default
//execute an Illustrator script in version 12
illustrator12.executeScript(myAIScript);
```

A specifier with no version information invokes the highest installed version of the application. For
example:

```default
//execute a Photoshop script in the highest available version
photoshop.executeScript (myPSScript)
```

---

## Cross-DOM Functions

All message-enabled applications implement the following cross-DOM functions:

---

### executeScript()

`appspec.executeScript(script)`

| `script`   | A string containing the script to be evaluated.   |
|------------|---------------------------------------------------|

Performs a JavaScript eval on the specified script. The entire document object model (DOM) of the
target application is available to the script.

Returns `undefined`.

---

### open()

`appspec.open(files)`

| `files`   | A File object or array of File objects.<br/>For applications that use compound documents, this should be a project file.   |
|-----------|----------------------------------------------------------------------------------------------------------------------------|

Performs the equivalent of the target application’s File > Open command on the specified files.

Returns `undefined`.

---

### openAsNew()

`appspec.openAsNew([options])`

| `options`   | Optional. Application-specific creation options:<br/><br/>- Adobe Bridge: none<br/>- Photoshop: none<br/>- InDesign: creation options are:<br/>  `(Boolean:showingWindow, ObjectOrString:documentPresets)`<br/>  See the arguments for `documents.add()` in the Adobe InDesign CS5 Scripting<br/>  Reference.<br/>- Illustrator: creation options are:<br/>  `([DocumentColorSpace:colorspace][, Number:width, Number:height])`<br/>  See the arguments for documents.add() in the Adobe Illustrator CS5 JavaScript<br/>  Reference.   |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Performs the equivalent of the target application’s File > New command.

Returns `true` on success.

---

### print()

`appspec.print(files)`

| `files`   | A File object or array of File objects.<br/>For applications that use compound documents, this should be a project file.   |
|-----------|----------------------------------------------------------------------------------------------------------------------------|

Performs the equivalent of the target application’s File > Print command on the specified files.

Returns `undefined`.

---

### quit()

`appspec.quit()`

Performs the equivalent of the target application’s File > Exit or File > Close command.

!!! note
    This function is available for Adobe Acrobat®, but does nothing. Scripts cannot terminate the
application.

Returns `undefined`.

---

### reveal()

`appspec.reveal(file)`

| `file`   | A File object or string specifying a file that can be opened in the target application.   |
|----------|-------------------------------------------------------------------------------------------|

Gives the target application the operating-system focus, and, if the specified file is open in that
application, brings it to the foreground.

Returns `undefined`.
