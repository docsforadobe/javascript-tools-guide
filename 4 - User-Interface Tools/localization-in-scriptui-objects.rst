.. _localization-in-scriptui-objects:

Localization in ScriptUI objects
================================
For portions of your user interface that are displayed on the screen, you may want to localize the displayed
text. You can localize the display strings in any ScriptUI object simply and efficiently, using the global
``localize`` function. This function takes as its argument a *localization object* containing the localized
versions of a string.

For complete details of this ExtendScript feature, see :ref:`localizing-extendscript-strings`.
A localization object is a JavaScript object literal whose property names are locale names, and whose
property values are the localized text strings. The locale name is an identifier as specified in the ISO 31
standard. In this example, a ``btnText`` object contains localized text strings for several locales. This object
supplies the text for a Button to be added to a window ``win``::

    btnText = { en: "Yes", de: "Ja", fr: "Oui" };
    b1 = win.add ( "button", undefined, localize( btnText ) );

The ``localize`` function extracts the proper string for the current locale. It matches the current locale and
platform to one of the object's properties and returns the associated string. On a German system, for
example, the property ``de`` provides the string ``"Ja"``.

When your script uses localization to provide language-appropriate strings for user-interface elements, it
should also take advantage of the Automatic layout feature. The layout manager can determine the best
size for each user-interface element based on its localized ``text`` value, automatically adjusting the layout
of your script-defined dialogs to allow for the varying widths of strings for different languages.

.. _variable-values-in-localized-strings:

Variable values in localized strings
------------------------------------
The localize function allows you to include variables in the string values. Each variable is replaced with
the result of evaluating an additional argument. For example::

    var today = {
        en: "Today is %1/%2.",
        de: "Heute ist der %2.%1."
    };
    var date = new Date();
    Window.alert( localize( today, date.getMonth() + 1, date.getDate() ) );

.. _enabling-automatic-localization:

Enabling automatic localization
-------------------------------
If you do not need variable replacement, you can use automatic localization. To turn on automatic
localization, set the global value::

    $.localization = true

When it is enabled, you can specify a localization object directly as the value of any property that takes a
localizable string, without using the ``localize`` function. For example::

    var btnText = { en: "Yes", de: "Ja", fr: "Oui" };
    b1 = win.add( "button", undefined, btnText );

The ``localize`` function always performs its translation, regardless of the setting of the ``$.localize``
variable. For example::

    // Only works if the $.localize = true
    var b1 = win.add ( "button", undefined, btnText );
    // Always works, regardless of $.localize value
    var b1 = win.add ( "button", undefined, localize( btnText ) );

If you need to include variables in the localized strings, use the ``localize`` function.
