.. _localizing-extendscript-strings:

Localizing ExtendScript strings
===============================
Localization is the process of translating and otherwise manipulating an interface so it looks as if it were
originally designed for a particular language. ExtendScript enables you to localize the strings in your
script's user interface. The language is chosen by the application at startup, according to the current locale
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

ExtendScript matches the current locale and platform to one of the object's properties and uses the
associated string. On a German system, for example, the property de: "Hallo Welt" is converted to the
string "Hallo Welt".

.. _variable-values-in-localized-strings:

Variable values in localized strings
------------------------------------
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

.. _enabling-automatic-localization:

Enabling automatic localization
-------------------------------
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

.. _locale-names:

Locale names
------------
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
1. ExtendScript gets the hosting application's locale; for example, en_US.
2. It appends the platform identifier; for example, en_US_Win.
3. It looks for a matching property, and if found, returns the value string.
4. If not found, it removes the platform identifier (for example, en_US) and retries.

5. If not found, it removes the region identifier (for example, en) and retries.
6. If not found, it tries the identifier en (that is, the default language is English).
7. If not found, it returns the entire localizer object.

.. _testing-localization:

Testing localization
--------------------
ExtendScript stores the current locale in the variable $.locale. This variable is updated whenever the
locale of the hosting application changes.
To test your localized strings, you can temporarily reset the locale. To restore the original behavior, set the
variable to null, false, 0, or the empty string. An example:
$.locale = "ru"; // try your Russian messages
$.locale = null; // restore to the locale of the app

.. _global-localize-function:

Global localize function
------------------------
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
Each expression is evaluated and the result inserted in the variable's position
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

