.. _getting-started-with-vscode-debugger:

Getting Started with the VS Code Debugger
=========================================

Unlike the ExtendScript Toolkit, the VS Code debugger takes some work to get up and running. This document is intended to make that process as straightforward as possible.

.. note::

  This guide is meant to walk you through how to install and run the Extendscript for VS Code debugger.

  If you're looking on how to use specific features of the extension, see :ref:`vscode-extension-features`.

Generally, you'll need to follow these steps:

- :ref:`installing-the-extension`
- :ref:`opening-a-project`
- :ref:`creating-a-debug-launch-task`
- :ref:`attaching-the-debugger`
- :ref:`running-the-debugger`
- :ref:`further-reading`

--------------------------------------------------------------------------------

.. _installing-the-extension:

Installing the extension
------------------------

Either head to the `extension marketplace link <https://marketplace.visualstudio.com/items?itemName=Adobe.extendscript-debug>`_ and install from there, or search "ExtendScript Debugger" within VS Code's extension browser and install.

If you're going the latter route, make sure you're installing the one from Adobe!

--------------------------------------------------------------------------------

.. _opening-a-project:

Opening a project directory
---------------------------

- `File > Open Folder`
- Choose your project directory

--------------------------------------------------------------------------------

.. _creating-a-debug-launch-task:

Creating a debug launch task
----------------------------

To use the extension, you need to create a debug task for VS Code to run when you want to debug extendscript.

In your project directory:

  - create a folder called `.vscode` (with the period)
  - in that folder, create a file `launch.json`
  - paste in the following code
    ::

    {
        "version": "0.2.0",
        "configurations": [ 
            {
                "type": "extendscript-debug",
                "request": "attach",
                "name": "extendScript-Debug attach",
            }
        ]
    }

This creates a config for VSCode's debugger that attaches to the host app of your choice.
 
Attaching the debugger
----------------------

Once the extension is installed:

- Open a JS workspace
- Launch your Adobe app of choice
- Select the run and Debug tab from the sidebar or hit Ctrl+Shift+D, then in the drop-down menu choose "extendScript-Debug attach"
- Choose the host app from the drop-down that appears

The bottom Status bar will turn orange indicating that the debugger is now attached to the host app. You can use the debug console to evaluate commands and query variables, even if a script is not running.

--------------------------------------------------------------------------------

.. _running-the-debugger:

Running the debugger
--------------------

Once you've set up your environment and built your script:

- Click on the status bar button labelled "▷ Eval in `host app name`" to launch the current script, or use the command pallette and choose `ExtendScript - Evaluate Script In Attached Host`.
- If the script throws any errors, you'll be able to view variables & a call stack

.. note::

  If you're compiling the end jsx file from a number of source files, the debugger will catch errors in the *compiled* script, not the source files -- you'll need to backtrack yourself to figure out what source file the error came from, unless you're building source maps in some way.

  This may not apply to compiled files using `#include`

--------------------------------------------------------------------------------

.. _further-reading:

Futher reading
--------------

- `Debugging in VS Code <https://code.visualstudio.com/docs/editor/debugging>`_
