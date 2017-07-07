.. _application-and-namespace-specifiers:

Application and namespace specifiers
====================================
All forms of interapplication communication use Application specifiers to identify Adobe applications.
In all ExtendScript scripts, the #target directive can use an specifier to identify the application that
should run that script. See :ref:`preprocessor-directives`.
In interapplication messages, the specifier is used as the value of the target property of the message
object, to identify the target application for the message.
Adobe Bridge (which is integrated with many Adobe applications) uses an application specifier as the
value of the document.owner property, to identify another application that created or opened an
Adobe Bridge browser window. For details, see the Adobe Bridge JavaScript Reference.
When a script for one application invokes cross-DOM or exported functions, it identifies the exporting
application using Namespace specifiers.

.. _application-specifiers:

Application specifiers
----------------------
Application specifiers are strings that encode the application name, a version number and a language
code. They take the following form:
``appname[_instance[[-version[-locale]]]``

============  ==========================================================================================
``appname``   An Adobe application name. For example, these are the identifying strings for applications
              that can use the ExtendScript Toolkit in Creative Suite 4:
              - ``aftereffects``
              - ``bridge``
              - ``estoolkit``
              - ``illustrator``
              - ``incopy``
              - ``indesign``
              - ``indesignserver``
              - ``photoshop``
``instance``  Optional. An additional string appended with an underscore, that distinguishes the
              instance for those applications (such as InDesign Server) that support the launching and
              running of multiple instances.

              For example, for a server launched with SOAP port 12345, the specifier would be
              `indesignserver_configuration_12345.`
``version``   Optional. A number indicating at least a major version. The number should include a minor
              version separated from the major version number by a dot; for example, 1.5.

              If not supplied, assumes the same suite version as the sending application, if possible;
              otherwise, the highest available version number.

              This is the complete list of identifying names and version numbers for applications that can
              use interapplication messaging in Creative Suite 4:
              - ``acrobat-9.0``
              - ``aftereffects-9.0``
              - ``soundbooth-2.0``
              - ``bridge-3.0``
              - ``contribute-5.0``
              - ``devicecentral-2.0``
              - ``dreamweaver-10.0``
              - ``encore-4.0``
              - ``estoolkit-3.0``
              - ``fireworks-10.0``
              - ``flash-10.0``
              - ``illustrator-14.0``
              - ``indesign-6.0``
              - ``indesignserver-6.0``
              - ``incopy-6.0``
              - ``photoshop-11.0``
              - ``premierepro-4.0``
              - ``audition-4.0``
              - ``ame-1.0``
              - ``exman-2.0``
``locale``    Optional. An Adobe locale code, consisting of a 2-letter ISO-639 language code and an
              optional 2-letter ISO 3166 country code separated by an underscore. Case is significant.

              For example, en_us, en_uk, ja_jp, de_de, fr_fr.
              If not supplied, ExtendScript uses the current platform locale.

              Do not specify a locale for a multilingual application, such as Bridge, that has all locale
              versions included in a single installation.
============  ==========================================================================================

The following are examples of legal specifiers:

  - ``photoshop``
  - ``bridge-3.0``
  - ``indesign_1-6.0``
  - ``illustrator-14.0``
  - ``illustrator-14.0-de_de``

If a specifier does not supply specific version and locale information, the framework tries to find the most
appropriate available installation. It tries to match to available applications in this order:

  1. Peer applications (from the same suite)
  2. Applications with the highest available version number
  3. Applications that are currently running
  4. Applications that match the current locale
  5. Applications for any locale

.. _namespace-specifiers:

Namespace specifiers
--------------------
When calling cross-DOM and exported functions from other applications, a namespace specifier qualifies
the function call, directing it to the appropriate application.
Namespace specifiers consist of an application name, as used in an application specifier, with an optional
major version number. Use it as a prefix to an exported function name, with the JavaScript dot notation.
appname[majorVersion].functionName(args)

For example:

- To call the cross-DOM function `quit` in Photoshop, use `photoshop.quit()`, and to call it in Adobe Illustrator®, use `illustrator.quit()`.
- To call the exported function `place`, defined for Illustrator CS5 version 15 call `illustrator15.place(myFiles)`.

For information about the cross-DOM and exported functions, see :ref:`remote-function-calls`.
