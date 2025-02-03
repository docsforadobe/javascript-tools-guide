# Preprocessor directives

ExtendScript provides preprocessor directives for including external scripts, naming scripts, specifying a JavaScript engine, and setting certain flags.

Specify these with either a C-style statement starting with the # character, or a comment followed by @:

```default
#include "file.jsxinc"
//@include "file.jsxinc"
```

When a directive takes one or more arguments, and an argument contains any nonalphanumeric characters, the argument must be enclosed in single or double quotes. This is generally the case with paths and file names, for example, which contain dots and slashes.

---

## #include file

Includes a JavaScript source file from another location. Inserts the contents of the named file into this file at the location of this statement. The `file` argument is an Adobe portable file specification. See [Specifying paths](../file-system-access/using-file-and-folder-objects.md#specifying-paths).

As a convention, use the file extension .jsxinc for JavaScript include files. For example:

```default
#include "../include/lib.jsxinc"
//@include "../include/file.jsxinc"
```

To set one or more paths for the #include statement to scan, use the `#includepath` preprocessor directive.

If the file to be included cannot be found, ExtendScript throws a run-time error. Included source code is not shown in the debugger, so you cannot set breakpoints in it.

---

## #includepath path

One or more paths that the `#include` statement should use to locate the files to be included. The semicolon (;) separates path names.

If a `#include` file name starts with a slash (/), it is an absolute path name, and the include paths are ignored. Otherwise, ExtendScript attempts to find the file by prefixing the file with each path set by the `#includepath` statement.

For example:

```default
#includepath "include;../include"
#include "file.jsxinc"
//@includepath "include;../include"
//@include "file.jsxinc"
```

Multiple `#includepath` statements are allowed; the list of paths changes each time an `#includepath` statement is executed.

As a fallback, ExtendScript also uses the contents of the environment variable `JSINCLUDE` as a list of include paths.

Some engines can have a predefined set of include paths. If so, the path provided by `#includepath` is tried before the predefined paths. If, for example, the engine has a predefined path set to `predef;predef/include`, the preceding example causes the following lookup sequence:

> `file.jsxinc`                literal lookup
> `include/file.jsxinc`        first #includepath path
> `../include/file.jsxinc`     second #includepath path
> `predef/file.jsxinc`         first predefined engine path
> `predef/include/file.jsxinc` second predefined engine path

---

## #script name

Names a script. Enclosing quotes are optional, but required for names that include spaces or special characters. For example:

```default
#script SetupPalette
#script "Load image file"
```

The `name` value is displayed in the Toolkit Editor tab. An unnamed script is assigned a unique name generated from a number.

---

## #strict on

Turns on strict error checking. See the [Dollar ($) object](dollar-object.md)'s [strict](dollar-object.md#dollar-strict) property.

---

## #target name

Defines the target application for this JSX file. The name value is an application specifier; see [Application and namespace specifiers](../interapplication-communication/application-and-namespace-specifiers.md). Enclosing quotes are optional.

If the Toolkit is registered as the handler for files with the `.jsx` extension (as it is by default), opening the file opens the target application to run the script.

If this directive is not present, the Toolkit loads and displays the script. A user can open a file by double-clicking it in a file browser, and a script can open a file using a `File` object's `execute` method.

---

## #targetengine enginename

Defines the target JavaScript engine for this JSX file, within the designated target application.

Supported by Adobe Illustrator CS5 and Adobe InDesign CS5; other applications ignore the directive.

- For Adobe Illustrator CS5 and Adobe InDesign CS5, if the named engine does not exist, and if the script originates within the application (rather than being executed in the ExtendScript Toolkit or received in an interapplication message), the application creates a new JavaScript engine with this name, which persists for the lifetime of the application session.
- If the script originates outside the application, and the named engine does not exist, the directive is ignored.
