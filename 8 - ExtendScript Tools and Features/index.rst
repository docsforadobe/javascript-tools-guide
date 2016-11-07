ExtendScript Tools and Features
In addition to the specific functional modules and development tools, ExtendScript provides these tools
and features:
Global objects that support debugging and object inspection; these include the Dollar ($) object and
the ExtendScript reflection interface.
A localization utility for providing user-interface string values in different languages. See Localizing
ExtendScript strings.
Global functions for displaying short messages in dialog boxes. See User notification dialogs.
An object type for specifying measurement values together with their units. See Specifying
measurement values.
Preprocessor directives that allow you to include scripts in one another and specify an execution
target application.
Support for extending or overriding math and logical operator behavior on a class-by-class basis. See
Operator overloading.
ExtendScript also provides a common scripting environment for all Adobe JavaScript-enabled
applications, and allows interapplication communication through scripts. For information on these
features, see Chapter 5, "Interapplication Communication with Scripts."

Dollar ($) object
This global ExtendScript object provides a number of debugging facilities and informational methods. The
properties of the $ object allow you to get global information such as the most recent run-time error, and
set flags that control debugging and localization behavior. The methods allow you to output text to the
JavaScript Console during script execution, control execution and other ExtendScript behavior
programmatically, and gather statistics on object use.

Dollar ($) object properties
appEncoding

String

The Internet name of the application’s default character encoding, such as
"CP1252" or "X-SHIFT-JIS". Valid values are implementation- and
OS-dependent.
Set to change the default encoding for the application. The returned value
can differ from the value set. In Windows, for example, if set to "x-latin1",
the returned value is the synonymous "ISO-8859-1".

build

String

The version information for the current ExtendScript build. Read only.

buildDate

Date

The date the current JavaScript engine was built. Read only.

decimalPoint

String

The character used in formatted numeric output for a decimal point, for
the current locale. Read only.

engineName

String

The name of the current JavaScript engine, if set. Read only.

error

Error
String

The most recent run-time error information, contained in a JavaScript
Error object.

217

Assigning error text to this property generates a run-time error; however,
the preferred way to generate a run-time error is to throw an Error object.
fileName

String

The file name of the current script. Read only.

flags

Number

Gets or sets low-level debug output flags. A logical AND of the following
bit flag values:
0x0002 (2): Displays each line with its line number as it is executed.
0x0040 (64): Enables excessive garbage collection. Usually, garbage

collection starts when the number of objects has increased by a
certain amount since the last garbage collection. This flag causes
ExtendScript to garbage collect after almost every statement. This
impairs performance severely, but is useful when you suspect that an
object gets released too soon.
0x0080 (128): Displays all calls with their arguments and the return

value.

0x0100 (256): Enables extended error handling (see strict).
0x0200 (512): Enables the localization feature of the toString
method. Equivalent to the localize property.

NOTE: Other bit values are not public and should not be used.
global

Global

Provides access to the Global object, which contains the JavaScript global
namespace.

hiresTimer

Number

A high-resolution timer that measures the number of microseconds since
this property was last accessed. Value is initialized as early as possible, so
the first access returns the startup time for ExtendScript. The property is
thread-local; that is, the first access on a thread returns the time needed to
create and initialize that thread. Read only.

includePath

String

The path for include files for the current script. Read only.

level

Number

The current debugging level, which enables or disables the JavaScript
debugger. Read only. One of:
0: No debugging
1: Break on runtime errors
2: Full debug mode

line

Number

The current line of the currently executing script; the first line is number 1.
Read only.

locale

String

Gets or sets the current locale. The string contains five characters in the
form LL_RR, where LL is an ISO 639 language specifier, and RR is an ISO
3166 region specifier.
Initially, this is the value that the application or the platform returns for the
current user. You can set it to temporarily change the locale for testing. To
return to the application or platform setting, set to undefined, null, or the
empty string.

localize

Boolean

Enable or disable the extended localization features of the built-in

toString method. See Localizing ExtendScript strings.

memCache

Number

Gets or sets the ExtendScript memory cache size in bytes.

os

String

The current operating system version information. Read only.

screens

Array

An array of objects containing information about the display screens
attached to your computer.
Each object has the properties left, top, right, and bottom, which
contain the four corners of the drawable area of each screen in global
coordinates.
A property primary is true if that object describes the primary display.

stack

String

The current stack trace.

strict

Boolean

When true, any attempt to write to a read-only property causes a runtime
error. Some objects do not permit the creation of new properties when
true.

version

String

The version number of the JavaScript engine as a three-part number and
description; for example: "3.92.95 (debug)" Read only.

Dollar ($) object functions
Function

Return type

about()
$.about ()

String

Displays the About box for the ExtendScript component, and returns the text of the About
box as a string.
bp()
$.bp ([condition])

Executes a breakpoint at the current position.
condition: Optional. A string containing a JavaScript statement to be used as a
condition. If the statement evaluates to true or nonzero when this point is reached,
execution stops.

If no condition is needed, it is recommended that you use the JavaScript debugger
statement in the script, rather than this method.

undefined

Function

Return type

colorPicker()
$.colorPicker (name)

Number

Invokes the platform-specific color selection dialog, and returns the selected color as a
hexadecimal RGB value: 0xRRGGBB.
name: The color to be preselected in the dialog, as a hexadecimal RGB value
(0xRRGGBB), or -1 for the platform default.
evalFile()
$.evalFile (path[, timeout])

Any

Loads a JavaScript script file from disk, evaluates it, and returns the result of evaluation.
path: The name and location of the file.
timeout: Optional. A number of milliseconds to wait before returning undefined, if

the script cannot be evaluated. Default is 10000 milliseconds.
gc()
$.gc ()

undefined

Initiates garbage collection in the JavaScript engine.
getenv()
$.getenv (envname)

String

Retrieves the value of the specified environment variable, or null if no such variable is
defined.
envname: The name of the environment variable.
setenv()
$.setenv (envname, value)

undefined

Sets the value of the specified environment variable, if no such variable is defined.
envname: The name of the environment variable.
value: The new value, a string.
sleep()
$.sleep (milliseconds)

Suspends the calling thread for the given number of milliseconds.
milliseconds: The number of milliseconds to wait.

During a sleep period, checks at 100 millisecond intervals to see whether the sleep should
be terminated. This can happen if there is a break request, or if the script timeout has
expired.

undefined

Function

Return type

write()
$.write (text[, text...]...)

undefined

Writes the specified text to the JavaScript Console.
text: One or more strings to write, which are concatenated to form a single string.
writeln()
$.writeln (text[, text...]...)

Writes the specified text to the JavaScript Console and appends a linefeed sequence.
text: One or more strings to write, which are concatenated to form a single string.

undefined

ExtendScript reflection interface
ExtendScript provides a reflection interface that allows you to find out everything about an object,
including its name, a description, the expected data type for properties, the arguments and return value
for methods, and any default values or limitations to the input values.

Reflection object
Every object has a reflect property that returns a reflection object that reports the contents of the
object. You can, for example, show the values of all the properties of an object with code like this:
var f = new File ("myfile");
var props = f.reflect.properties;
for (var i = 0; i < props.length; i++) {
$.writeln(’this property ’ + props[i].name + ’ is ’ + f[props[i].name]);
}

Reflection object properties
All properties are read only.
description

String

help

String

Short text describing the reflected object, or undefined if no
description is available.
Longer text describing the reflected object more completely, or

undefined if no description is available.

methods

Array of
ReflectionInfo

An Array of ReflectionInfo objects containing all methods of the
reflected object, defined in the class or in the specific instance.

name

String

The class name of the reflected object.

properties

Array of
ReflectionInfo

An Array of ReflectionInfo objects containing all properties of the
reflected object, defined in the class or in the specific instance. For
objects with dynamic properties (defined at runtime) the list contains
only those dynamic properties that have already been accessed by
the script. For example, in an object wrapping an HTML tag, the
names of the HTML attributes are determined at run time.

Reflection object functions
find()
reflectionObj.find (name)
name

The property for which to retrieve information.

Returns the ReflectionInfo object for the named property of the reflected object, or null if no such
property exists.
Use this method to get information about dynamic properties that have not yet been accessed, but
that are known to exist.

Examples
This code determines the class name of an object:
obj = new String ("hi");
obj.reflect.name; // => String

This code gets a list of all methods:
obj = new String ("hi");
obj.reflect.methods; //=> indexOf,slice,...
obj.reflect.find ("indexOf"); // => the method info

This code gets a list of properties:
Math.reflect.properties; //=> PI,LOG10,...

This code gets the data type of a property:
Math.reflect.find ("PI").type; // => number

ReflectionInfo object
This object contains information about a property, a method, or a method argument.
You can access ReflectionInfo objects in a Reflection object’s properties and methods arrays, by
name or index:
obj = new String ("hi");
obj.reflect.methods[0];
obj.reflect.methods["indexOf"];

You can access the ReflectionInfo objects for the arguments of a method in the arguments array of
the ReflectionInfo object for the method, by index:
obj.reflect.methods["indexOf"].arguments[0];
obj.reflect.methods.indexOf.arguments[0];

ReflectionInfo object properties
arguments

Array of
For a reflected method, an array of ReflectionInfo objects describing
ReflectionInfo each method argument.

dataType

String

The data type of the reflected element. One of:
boolean
number
string
Classname: The class name of an object.

NOTE: Class names start with a capital letter. Thus, the value
string stands for a JavaScript string, while String is a
JavaScript String wrapper object.
*: Any type. This is the default.
null
undefined: Return data type for a function that does not return

any value.
unknown
defaultValue

any

The default value for a reflected property or method argument, or
undefined if there is no default value, if the property is undefined, or
if the element is a method.

description

String

Short text describing the reflected object, or undefined if no
description is available.

help

String

Longer text describing the reflected object more completely, or
undefined if no description is available.

isCollection

Boolean

When true, the reflected property or method returns a collection;
otherwise, false.

max

Number

The maximum numeric value for the reflected element, or
undefined if there is no maximum or if the element is a method.

min

Number

The minimum numeric value for the reflected element, or undefined
if there is no minimum or if the element is a method.

name

String
Number

The name of the reflected element. A string, or a number for an array
index.

type

String

The type of the reflected element. One of:
readonly: A Read only property.
readwrite: A read-write property.
createonly: A property that is valid only during creation of an

object.

method: A method.

Localizing ExtendScript strings
Localization is the process of translating and otherwise manipulating an interface so it looks as if it were
originally designed for a particular language. ExtendScript enables you to localize the strings in your
script’s user interface. The language is chosen by the application at startup, according to the current locale
provided by the operating system.
For parts of your user interface that are displayed on the screen, you may want to localize the displayed
text. You can localize any string explicitly, using the Global localize function, which takes as its argument a
localization object containing the localized versions of a string.
A localization object is a JavaScript object literal whose property names are locale names and whose
property values are the localized text strings. The locale name is a standard language code with an
optional region identifier. For syntax details, see Locale names.
In this example, a msg object contains localized text strings for two locales. This object supplies the text for
an alert dialog.
msg = { en: "Hello, world", de: "Hallo Welt" };
alert (msg);

ExtendScript matches the current locale and platform to one of the object’s properties and uses the
associated string. On a German system, for example, the property de: "Hallo Welt" is converted to the
string "Hallo Welt".

Variable values in localized strings
Some localization strings need to contain additional data whose position and order may change according
to the language used.
You can include variables in the string values of the localization object, in the form %n. The variables are
replaced in the returned string with the results of JavaScript expressions, supplied as additional arguments
to the localize function. The variable %1 corresponds to the first additional argument, %2 to the second,
and so on.
Because the replacement occurs after the localized string is chosen, the variable values are inserted in the
correct position. For example:
today = {
en: "Today is %1/%2.",
de: "Heute ist der %2.%1."
};
d = new Date();
alert (localize (today, d.getMonth()+1, d.getDate()));

Enabling automatic localization
ExtendScript offers an automatic localization feature. When it is enabled, you can specify a localization
object directly as the value of any property that takes a localizable string, without using the localize
function. For example:
msg = { en: "Yes", de: "Ja", fr: "Oui" };
alert (msg);

To use automatic translation of localization objects, you must enable localization in your script with this
statement:
$.localize = true;

The localize function always performs its translation, regardless of the setting of the $.localize
variable; for example:
msg = { en: "Yes", de: "Ja", fr: "Oui" };
//Only works if the $.localize=true
alert (msg);
//Always works, regardless of $.localize value
alert ( localize (msg));

If you need to include variables in the localized strings, use the localize function.

Locale names
A locale name is an identifier string in that contains an ISO 639 language specifier, and optionally an ISO
3166 region specifier, separated from the language specifier by an underscore.
The ISO 639 standard defines a set of two-letter language abbreviations, such as en for English and de
for German.
The ISO 3166 standard defines a region code, another two-letter identifier, which you can optionally
append to the language identifier with an underscore. For example, en_US identifies U.S. English,
while en_GB identifies British English.
This object defines one message for British English, another for all other flavors of English, and another for
all flavors of German:
message = {
en_GB: "Please select a colour."
en: "Please select a colour."
de: "Bitte wählen Sie eine Farbe."
};

If you need to specify different messages for different platforms, you can append another underline
character and the name of the platform, one of Win, Mac, or Unix. For example, this objects defines one
message in British English to be displayed on Mac OS, one for all other flavors of English on Mac OS, and
one for all other flavors of English on all other platforms:
pressMsg = {
en_GB_Mac: "Press Cmd-S to select a colour.",
en_Mac: "Press Cmd-S to select a color.",
en: "Press Ctrl-S to select a color."
};

All these identifiers are case sensitive; for example, EN_US is not valid.
How locale names are resolved
1. ExtendScript gets the hosting application’s locale; for example, en_US.
2. It appends the platform identifier; for example, en_US_Win.
3. It looks for a matching property, and if found, returns the value string.
4. If not found, it removes the platform identifier (for example, en_US) and retries.

5. If not found, it removes the region identifier (for example, en) and retries.
6. If not found, it tries the identifier en (that is, the default language is English).
7. If not found, it returns the entire localizer object.

Testing localization
ExtendScript stores the current locale in the variable $.locale. This variable is updated whenever the
locale of the hosting application changes.
To test your localized strings, you can temporarily reset the locale. To restore the original behavior, set the
variable to null, false, 0, or the empty string. An example:
$.locale = "ru"; // try your Russian messages
$.locale = null; // restore to the locale of the app

Global localize function
The globally available localize function can be used to provide localized strings anywhere a displayed
text value is specified. The function takes a specially formatted set of localized versions of a display string,
and returns the version appropriate to the current locale.
localize()
localize (localization_obj[, args])
localize (ZString)
localization_obj

A JavaScript object literal whose property names are locale names, and
whose property values are the localized text strings. The locale name is an
identifier as specified in the ISO 3166 standard, a set of two-letter language
abbreviations, such as "en" for English and "de" for German.
For example:
btnText = { en: "Yes", de: "Ja", fr: "Oui" };
b1 = w.add ("button", undefined, localize (btnText));

The string value of each property can contain variables in the form %1, %2,
and so on, corresponding to additional arguments. The variable is replaced
with the result of evaluating the corresponding argument in the returned
string.
args

Optional. Additional JavaScript expressions matching variables in the string
values supplied in the localization object. The first argument corresponds to
the variable %1, the second to %2, and so on.
Each expression is evaluated and the result inserted in the variable’s position
in the returned string.

ZString

Internal use only. A ZString is an internal Adobe format for localized strings,
which you might see in Adobe scripts. It is a string that begins with $$$ and
contains a path to the localized string in an installed ZString dictionary. For
example:
w = new Window ("dialog", localize ("$$$/UI/title1=Sample"));

For example:
today = {
en: "Today is %1/%2",
de: "Heute ist der %2.%1."
};
d = new Date();
alert (localize (today, d.getMonth()+1, d.getDate()));

User notification dialogs
ExtendScript provides a set of globally available functions that allow you to display short messages to the
user in platform-standard dialog boxes. There are three types of message dialogs:
Alert - Displays a dialog containing a short message and an OK button.
Confirm - Displays a dialog containing a short message and two buttons, Yes and No, allowing the
user to accept or reject an action.
Prompt - Displays a dialog containing a short message, a text entry field, and OK and Cancel
buttons, allowing the user to supply a value to the script.
These dialogs are customizable to a small degree. The appearance is platform specific.

Global alert function
Displays a platform-standard dialog containing a short message and an OK button.
alert()
alert (message[, title, errorIcon]);
message

The string for the displayed message.

title

Optional. A string to appear as the title of the dialog, if the platform supports a title.
Mac OS does not support titles for alert dialogs. The default title string is "Script Alert."

errorIcon Optional. When true, the platform-standard alert icon is replaced by the

platform-standard error icon in the dialog. Default is false.

Returns undefined
Examples
This figure shows simple alert dialogs in Windows and in Mac OS.

This figure shows alert dialogs with error icons.

Global confirm function
Displays a platform-standard dialog containing a short message and two buttons labeled Yes and No.
confirm()
confirm (message[,noAsDflt ,title ]);
message

The string for the displayed message.

noAsDflt

Optional. When true, the No button is the default choice, selected when the user types
ENTER. Default is false, meaning that Yes is the default choice.

title

Optional. A string to appear as the title of the dialog, if the platform supports a title.
Mac OS does not support titles for confirmation dialogs. The default title string is
"Script Alert."

Returns true if the user clicked Yes, false if the user clicked No.
Examples
This figure shows simple confirmation dialogs on Windows and Mac OS.

This figure shows confirmation dialogs with No as the default button.

Global prompt function
Displays a platform-standard dialog containing a short message, a text edit field, and two buttons labeled
OK and Cancel.
prompt()
prompt (message, preset[, title ]);
message

The string for the displayed message.

preset

The initial value to be displayed in the text edit field.

title

Optional. A string to appear as the title of the dialog. On Windows, this appears in the
window’s frame, while on Mac OS it appears above the message. The default title string
is "Script Prompt."

Returns the value of the text edit field if the user clicked OK, null if the user clicked Cancel.
Examples
This figure shows simple prompt dialogs on Windows and Mac OS.

This figure shows confirmation dialogs with a title value specified.

Specifying measurement values
ExtendScript provides the UnitValue object to represent measurement values. The properties and
methods of the UnitValue object make it easy to change the value, the unit, or both, or to perform
conversions from one unit to another.

UnitValue object
Represents measurement values that contain both the numeric magnitude and the unit of measurement.

UnitValue object constructor
The UnitValue constructor creates a new UnitValue object. The keyword new is optional:
myVal = new UnitValue (value, unit);
myVal = new UnitValue ("value unit");
myVal = new UnitValue (value, "unit");

The value is a number, and the unit is specified with a string in abbreviated, singular, or plural form, as
shown in the following table.
Abbreviation

Singular

Plural

Comments

in

inch

inches

2.54 cm

ft

foot

feet

30.48 cm

yd

yard

yards

91.44 cm

mi

mile

miles

1609.344 m

mm

millimeter

millimeters

cm

centimeter

centimeters

m

meter

meters

km

kilometer

kilometers

pt

point

points

inches / 72

pc

pica

picas

points * 12

tpt

traditional point

traditional points

inches / 72.27

tpc

traditional pica

traditional picas

12 tpt

ci

cicero

ciceros

12.7872 pt

px

pixel

pixels

baseless (see below)

%

percent

percent

baseless (see below)

If an unknown unit type is supplied, the type is set to "?", and the UnitValue object prints as "UnitValue
0.00000".

For example, all the following formats are equivalent:
myVal = new UnitValue (12, "cm");
myVal = new UnitValue ("12 cm");
myVal = UnitValue ("12 centimeters");

UnitValue object properties
baseUnit

UnitValue

A UnitValue object that defines the size of one pixel, or a total size to use as a
base for percentage values. This is used as the base conversion unit for pixels
and percentages; see Converting pixel and percentage values.
Default is 0.013889 inches (1/72 in), which is the base conversion unit for
pixels at 72 dpi. Set to null to restore the default.

type

String

The unit type in abbreviated form; for example, "cm" or "in".

value

Number

The numeric measurement value.

UnitValue object functions
as()
unitValueObj.as (unit)
unit

The unit type in abbreviated form; for example, "cm" or "in".

Returns the numeric value of this object in the given unit. If the unit is unknown or cannot be
computed, generates a run-time error.
convert()
unitValueObj.convert (unit)
unit

The unit type in abbreviated form; for example, "cm" or "in".

Converts this object to the given unit, resetting the type and value accordingly.
Returns true if the conversion is successful. If the unit is unknown or the object cannot be
converted, generates a run-time error and returns false.

Converting pixel and percentage values
Converting measurements among different units requires a common base unit. For example, for length,
the meter is the base unit. All length units can be converted into meters, which makes it possible to
convert any length unit into any other length unit.
Pixels and percentages do not have a standard common base unit. Pixel measurements are relative to
display resolution, and percentages are relative to an absolute total size.
To convert pixels into length units, you must know the size of a single pixel. The size of a pixel depends
on the display resolution. A common resolution measurement is 72 dpi, which means that there are 72
pixels to the inch. The conversion base for pixels at 72 dpi is 0.013889 inches (1/72 inch).

Percentage values are relative to a total measurement. For example, 10% of 100 inches is 10 inches,
while 10% of 1 meter is 0.1 meters. The conversion base of a percentage is the unit value
corresponding to 100%.
The default baseUnit of a unitValue object is 0.013889 inches, the base for pixels at 72 dpi. If the
unitValue is for pixels at any other dpi, or for a percentage value, you must set the baseUnit value
accordingly. The baseUnit value is itself a unitValue object, containing both a magnitude and a unit.
For a system using a different DPI, you can change the baseUnit value in the UnitValue class, thus
changing the default for all new unitValue objects. For example, to double the resolution of pixels:
UnitValue.baseUnit = UnitValue (1/144, "in"); //144 dpi

To restore the default, assign null to the class property:
UnitValue.baseUnit = null; //restore default

You can override the default value for any particular unitValue object by setting the property in that
object. For example, to create a unitValue object for pixels with 96 dpi:
pixels = UnitValue (10, "px");
myPixBase = UnitValue (1/96, "in");
pixels.baseUnit = myPixBase;

For percentage measurements, set the baseUnit property to the measurement value for 100%. For
example, to create a unitValue object for 40% of 10 feet:
myPctVal = UnitValue (40, "%");
myBase = UnitValue (10, "ft")
myPctVal.baseUnit = myBase;

Use the as() method to get to a percentage value as a unit value:
myFootVal = myPctVal.as ("ft"); // => 4
myInchVal = myPctVal.as ("in"); // => 36

You can convert a unitValue from an absolute measurement to pixels or percents in the same way:
myMeterVal = UnitValue (10, "m"); // 10 meters
myBase = UnitValue (1, "km");
myMeterVal.baseUnit = myBase; //as a percentage of 1 kilometer
pctOfKm = myMeterVal.as (’%’); // => 1
myVal = UnitValue ("1 in"); // Define measurement in inches
// convert to pixels using default base
myVal.convert ("px"); // => value=72 type=px

Computing with unit values
UnitValue objects can be used in computational JavaScript expressions. The way the value is used
depends on the type of operator.

Unary operators (~, !, +, -)
~unitValue

The numeric value is converted to a 32-bit integer with inverted bits.

!unitValue

Result is true if the numeric value is nonzero, false if it is not.


+unitValue

Result is the numeric value.

-unitValue

Result is the negated numeric value.


Binary operators (+, -, *, /, %)
If one operand is unitValue object and the other is a number, the operation is applied to the number
and the numeric value of the object. The expression returns a new unitValue object with the result as
its value. For example:
val = new UnitValue ("10 cm");
res = val * 20;
// res is a UnitValue (200, "cm");

If both operands are unitValue objects, JavaScript converts the right operand to the same unit as the
left operand and applies the operation to the resulting values. The expression returns a new
unitValue object with the unit of the left operand, and the result value. For example:
a = new UnitValue ("1 m");
b = new UnitValue ("10 cm");
a + b;
// res is a UnitValue (1.1, "m");
b + a;
// res is a UnitValue (110, "cm");

Comparisons (=, ==, <, >, <=, >=)
If one operand is a unitValue object and the other is a number, JavaScript compares the number with
the unitValue’s numeric value.
If both operands are unitValue objects, JavaScript converts both objects to the same unit, and
compares the converted numeric values.
For example:
a
b
a
a
a

= new UnitValue ("98 cm");
= new UnitValue ("1 m");
< b;
// => true
< 1;
// => false
== 98; // => true

Preprocessor directives
ExtendScript provides preprocessor directives for including external scripts, naming scripts, specifying a
JavaScript engine, and setting certain flags. Specify these with a C-style statement starting with the #
character:
#include "file.jsxinc"

When a directive takes one or more arguments, and an argument contains any nonalphanumeric
characters, the argument must be enclosed in single or double quotes. This is generally the case with
paths and file names, for example, which contain dots and slashes.


#include file



Includes a JavaScript source file from another location. Inserts the contents of the
named file into this file at the location of this statement. The file argument is an
Adobe portable file specification. See Specifying paths.
As a convention, use the file extension .jsxinc for JavaScript include files. For
example:
#include "../include/lib.jsxinc"

To set one or more paths for the #include statement to scan, use the #includepath
preprocessor directive.
If the file to be included cannot be found, ExtendScript throws a run-time error.
Included source code is not shown in the debugger, so you cannot set breakpoints
in it.
#includepath
path

One or more paths that the #include statement should use to locate the files to be
included. The semicolon (;) separates path names.
If a #include file name starts with a slash (/), it is an absolute path name, and the
include paths are ignored. Otherwise, ExtendScript attempts to find the file by
prefixing the file with each path set by the #includepath statement.
For example:
#includepath "include;../include"
#include "file.jsxinc"

Multiple #includepath statements are allowed; the list of paths changes each time
an #includepath statement is executed.
As a fallback, ExtendScript also uses the contents of the environment variable

JSINCLUDE as a list of include paths.

Some engines can have a predefined set of include paths. If so, the path provided by
#includepath is tried before the predefined paths. If, for example, the engine has a
predefined path set to predef;predef/include, the preceding example causes the
following lookup sequence:
file.jsxinc
include/file.jsxinc
../include/file.jsxinc
predef/file.jsxinc
predef/include/file.jsxinc
#script name

literal lookup
first #includepath path
second #includepath path
first predefined engine path
second predefined engine path

Names a script. Enclosing quotes are optional, but required for names that include
spaces or special characters. For example:
#script SetupPalette
#script "Load image file"

The name value is displayed in the Toolkit Editor tab. An unnamed script is assigned a
unique name generated from a number.
#strict on

Turns on strict error checking. See the Dollar ($) object’s strict property.

#target name

Defines the target application for this JSX file. The name value is an application
specifier; see Application and namespace specifiers. Enclosing quotes are optional.
If the Toolkit is registered as the handler for files with the .jsx extension (as it is by
default), opening the file opens the target application to run the script. If this
directive is not present, the Toolkit loads and displays the script. A user can open a
file by double-clicking it in a file browser, and a script can open a file using a File
object’s execute method.

#targetengine
enginename

Defines the target JavaScript engine for this JSX file, within the designated target
application.
Supported by Adobe Illustrator CS5 and Adobe InDesign CS5; other applications
ignore the directive.
For Adobe Illustrator CS5 and Adobe InDesign CS5, if the named engine does
not exist, and if the script originates within the application (rather than being
executed in the ExtendScript Toolkit or received in an interapplication message),
the application creates a new JavaScript engine with this name, which persists
for the lifetime of the application session.
If the script originates outside the application, and the named engine does not
exist, the directive is ignored.

Operator overloading
ExtendScript allows you to extend or override the behavior of a math or a Boolean operator for a specific
class by defining a method in that class with same name as the operator. For example, this code defines
the addition (+) operator for the class MyClass. In this case, the addition operator simply adds the operand
to the property value:
// define the constructor method
function MyClass (initialValue) {
this.value = initialValue;
}
// define the addition operator
MyClass.prototype ["+"] = function (operand) {
return this.value + operand;
}

This allows you to perform the "+" operation with any object of this class:
var obj = new MyClass (5);
Result: [object Object]
obj + 10;
Result: 15

You can override the following operators:
Unary

+, ~

Binary

+, *, /, %, ^
<, <=, ==
<<, >>, >>>
&, |, ===

The operators > and >= are implemented by executing NOT operator <= and NOT operator <.
Combined assignment operators such as *= are not supported.
All operator overload implementations must return the result of the operation. To perform the default
operation, return undefined.
Unary operator functions work on the this object, while binary operators work on the this object and
the first argument. The + and - operators have both unary and binary implementations. If the first
argument is undefined, the operator is unary; if it is supplied, the operator is binary.
For binary operators, a second argument indicates the order of operands. For noncommutative operators,
either implement both order variants in your function or return undefined for combinations that you do
not support. For example:
this ["/"] = function (operand, rev) {
if (rev) {
// do not resolve operand / this
return;
} else {
// resolve this / operand
return this.value / operand;
}
