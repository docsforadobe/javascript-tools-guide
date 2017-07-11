.. _the-extendscript-toolkit:

The ExtendScript Toolkit
========================
The ExtendScript Toolkit provides an interactive development and testing environment for ExtendScript in
all JavaScript-enabled Adobe applications. It includes a full-featured, syntax-highlighting text editor with
Unicode capabilities and multiple undo/redo support. The Toolkit is the default editor for ExtendScript
files, which use the extension .jsx.

The Toolkit includes a JavaScript debugger that allows you to:

- Single-step through JavaScript scripts (JS or JSX files) inside an application.
- Inspect all data for a running script.
- Set and execute breakpoints.

When you double click a JSX file in the platform's windowing environment, the script runs in the Toolkit,
unless it specifies a particular target application using the #target directive. For more information, see
:ref:`selecting-a-debugging-target` and :ref:`preprocessor-directives`.

.. tip:: When you have completed editing and debugging your JavaScript script, you can choose to save it as
  a binary file (with the extension JSXBIN), using ``File > Export as Binary``. The script loader recognizes both
  source code and compiled code. Photoshop and After Effects can execute compiled scripts. If an application
  recognizes the execution of compiled JavaScript, it lists JSXBIN files along with JSX files in any list of
  available scripts.
