The ExtendScript Toolkit
The ExtendScript Toolkit provides an interactive development and testing environment for ExtendScript in
all JavaScript-enabled Adobe applications. It includes a full-featured, syntax-highlighting text editor with
Unicode capabilities and multiple undo/redo support. The Toolkit is the default editor for ExtendScript
files, which use the extension .jsx.
The Toolkit includes a JavaScript debugger that allows you to:
Single-step through JavaScript scripts (JS or JSX files) inside an application.
Inspect all data for a running script.
Set and execute breakpoints.
When you double click a JSX file in the platform’s windowing environment, the script runs in the Toolkit,
unless it specifies a particular target application using the #target directive. For more information, see
"Selecting a debugging target" on page 27 and "Preprocessor directives" on page 233.
TIP: When you have completed editing and debugging your JavaScript script, you can choose to save it as
a binary file (with the extension JSXBIN), using File > Export as Binary. The script loader recognizes both
source code and compiled code. Any application can execute a compiled script. If an application
recognizes the execution of compiled JavaScript, it lists JSXBIN files along with JSX files in any list of
available scripts."

Configuring the Toolkit window
The ExtendScript Toolkit initially appears with a default workspace arrangement, containing a default
configuration of tabbed panels and Script Editor document windows contained in a parent frame. The
arrangement is highly configurable, through the Window menu, the context menus of individual panels
and panel groups, or directly using drag and drop.

Document
windows

Panels

13

CHAPTER 2: The ExtendScript Toolkit

Configuring the Toolkit window

14

You can, for example, adjust the relative sizes of the panels by dragging the separators up or down, or right
or left, and can rearrange the groupings. To move a tabbed panel, drag the tab into another pane.
If you drag a tab so that the entire destination group is highlighted, it becomes another stacked panel in
that group. If you drag a tab to the top or bottom of a group (so that only the top or bottom bar of the
destination group is highlighted), that group splits to show the panels in a tiled format.
You can dock the entire panel group to different edges of the Toolkit window.
You can collapse the entire panel group, then expose individual panels.
You can open and close, or collapse and expand individual panels, regardless of the dock state.
You can undock individual tabs or the entire control panel, making them floating panels. Floating
panels can be docked to each other, or can be independent.
There are predefined configurations, called workspaces, suitable for various uses, and you can save your
favorite configurations as workspaces. See "Workspaces" on page 16.

Panel menus
Panel groups have a context menu, which you invoke with a right click in the tab or on the background of
the title bar. These menus have panel-control commands, including Close Panel and Close Group to hide
the individual panel or entire group.
Right click in top bar for panel-group menu

Panel-specific flyout menu

You can also show or hide specific panels by toggling them on or off in the Window menu. Use the
Window menu to show a hidden panel, or to bring a floating panel to the front.
Use Window > Hide panels to close all of the panels.
Some panels also have a flyout menu, specific to that panel, which you access through the menu icon in
the upper right corner. The JavaScript Console has a right-click menu that allows you to copy and paste
text.
The individual panels are discussed in detail in the following sections.

CHAPTER 2: The ExtendScript Toolkit

Configuring the Toolkit window

15

Document windows
When you open scripts or text files, each file appears in its own Script Editor document window. By default,
the document windows are docked; that is, shown as tabbed panes in the main window. However, like the
panels, you can drag any document window out of the frame to make it an independent floating window.
If you are displaying more than one document, and you have undocked one or more of them, you can
choose to show the document windows in tiled or cascade style-that is, side by side in the main window,
or overlapping in the main window. To do this, choose Window > Tile Documents or Window > Cascade.
You can edit or run scripts in multiple document windows simultaneously. The current document window
is highlighted and has the input focus. You can select another document window by clicking in it, or you
can switch between them with the commands Window > Next document and Window > Previous
document. The default keyboard shortcuts for these commands are F6 and SHIFT-F6; you can change these
using the Keyboard Shortcuts page in the Preferences dialog (Edit > Preferences).
NOTE: Because you can run scripts in the same application simultaneously, you should be careful not to
interrupt the processing of one script with another. For example, if one script opens a modal dialog in
Photoshop, and you run another script that targets Photoshop while the dialog is still open, the second
script is likely to generate an error.
A button in the upper right corner of the document window allows you to split that window.

Split document button

Second view of document

When the window is split, the second window is another view of exactly the same source. Any changes
you make in the text, breakpoints that you add, and so on, appear simultaneously in both windows. The
copy is, by default, positioned to the right of the original, docked window, as shown. However, if you use
CTRL-click to split the window, the second appears below the original.
For more information about the document windows and the Script Editor, see "The Script Editor" on
page 18.

CHAPTER 2: The ExtendScript Toolkit

Configuring the Toolkit window

16

Workspaces
The Toolkit saves the current layout when you exit, and restores it at the next startup. It saves and restores
the open documents, the current positions within the documents, any breakpoints that have been set, and
other preferences that have been set in the Preferences dialog.
The Startup page in the Preferences dialog (Edit > Preferences) offers a choice of whether to open a
blank document window, no document window, or display a previously opened document on startup.
The Tookit defines a number of workspace configurations that are suitable for specific usage types. To
choose a predefined or user-defined workspace, use the workspace menu that drops down from the
upper right corner of the Toolkit. When you choose a workspace, its name appears here. You can also
add and remove workspaces from this menu.

Current workspace name appears in this space

You can save any configuration as a named workspace, using the Create new Workspace menu
command, or the Add button on the Workspaces page in the Preferences dialog (Edit > Preferences).
You can remove workspaces you have defined, either individually using the menu or the Workspaces
page in the Preferences dialog, or all at once using the Default button at the bottom of the Workspace
page.
The Keyboard Shortcuts page in the Preferences dialog (Edit > Preferences) allows you to set or
modify keyboard shortcuts for all menu commands. There is a warning if you assign a key combination
that is already in use. If you assign the combination to a new command, it is removed from the
previous command.
You can restore all preferences to their default values by holding the SHIFT key down while the Toolkit
loads.

Dialogs
Some dialog windows offer the option "Don’t show again". If you select this option, the Toolkit remembers
the choices made in this dialog, and next time it would appear, makes the same choices without showing
the dialog.
To make these dialogs display again, click Reset Dialogs on the User Interface page in the Preferences
dialog (Edit > Preferences).

CHAPTER 2: The ExtendScript Toolkit

Selecting scripts

17

Selecting scripts
You can open multiple scripts (or text files, including programs in other languages). You can find and open
scripts in a number of ways:
Use File > Open to bring up the platform-specific file browser.
Choose from recently opened files using File > Recent files.
Create a new script using File > New JavaScript.
Drop files from the Explorer or the Finder onto the Toolkit to open them in a document window.
For JavaScript scripts in trusted locations (the user-script folders of installed Adobe applications), a
double-click on the file runs it in the target application or in the Toolkit. For script files in other
locations, you must confirm that you want to run the script.
Search for scripts containing particular text using Edit > Find and Replace. You can search in a
particular document window, among all scripts open in document windows, or among scripts
associated with an application, or kept in favorite locations. See "Searching in text" on page 24.
Use the Scripts panel to display and open scripts made available by loaded Adobe applications, or
those kept in favorite locations.

The Scripts panel and favorite script locations
The Scripts panel offers a list of debuggable scripts, which can be JS or JSX files or (for some applications)
HTML files that contain embedded scripts.
You can display a list of scripts made available by a particular target application. Select the target
application in the leftmost drop-down list; the available JavaScript engines for that application become
available in the right-hand list.
When you select a target application, the Toolkit offers to open that application if it is not running, then
displays the scripts which that application makes public. Select a script in this panel to load it and display
its contents in a new document window, where you can modify it, save it, or run it within the target
application.
When you choose the target Favorites, the right-hand list shows the default favorite script location, and
any other favorite locations that have been defined. You can create your own list of favorite script locations
using the flyout menu.

flyout menu

CHAPTER 2: The ExtendScript Toolkit

The Script Editor

18

The favorite script locations that you define are also available to the Find and Replace dialog; see
"Searching in text" on page 24.
You can also examine and set favorite locations using the Favorites page of the Preferences dialog (Edit >
Preferences). Use the Add, Modify, and Remove buttons to edit the list of folders.

Adobe Scripts folder
On first launch, the Toolkit creates a folder named Adobe Scripts in the user's Documents folder. The
Default favorite in the Scripts panel displays the contents of this folder.
When double-clicking a JSX file, the Toolkit normally acts as an invisible security filter. Before actually
launching the file, a security dialog asks if it is OK to execute the script. The Toolkit treats the user's
Documents/Adobe Scripts folder, however, as a trusted location; when you double-click a JSX file in that
folder, the Toolkit does not display the security alert.

The Script Editor
The Script Editor is a full-featured source code editor for JavaScript. You can open any number of Script
Editor document windows; each displays one Unicode source code document.
The Script Editor offers many useful and powerful text editing and navigation features. Some are intended
specifically for use with JavaScript, while others are useful for all kinds of text editing. Features include:
Navigation aids and options applicable to any kind of text, and specific code navigation for JavaScript;
see "Navigation aids" on page 19.
General editing and coding support such as undo-redo, and specific JavaScript coding support such
as syntax checking; see "Coding aids" on page 22.

CHAPTER 2: The ExtendScript Toolkit

The Script Editor

19

A full-featured text search tool that can search in multiple files; see "Searching in text" on page 24.
Syntax marking (color and font styles for specific syntactic structures) for JavaScript and for many
other computer languages. The marking styles are configurable; see "Syntax marking" on page 26.

Navigation aids
You can configure the Script Editor to display text with various features that help you track the structure of
your code, or that help you move around in the file. It also offers mouse and keyboard shortcuts for specific
types of cursor movement and text selection.

View options
The Script Editor offers a number of viewing options that aid in code navigation, including the following:
Automatic line numbering. View > Line Numbers toggles numbering on and off.
A collapsible tree view of code, where you can open or close logical units of the structure, such as
comments or function definitions. View > Code Collapse toggles the tree view on and off.
A line-wrapping mode, where there is no horizontal scroll bar, and lines are wrapped at word breaks.
View > Word Wrap toggles line-wrapping on and off.
Syntax marking, which uses color and font styles to highlight specific syntactic structures. View >
Syntax Highlighting allows you to turn syntax marking off, or set it to mark a particular language,
JavaScript or many other computer languages. The marking styles are configurable; see "Syntax
marking" on page 26.
You can set the default values for any of these states using the Documents page of the Preferences dialog
(Edit > Preferences).

Function finders
The Functions panel, and the flyout menu at the top right of the document window, both offer lists of
functions defined in the current document. When you select a function in either list, the document jumps
directly to that function definition in the code.

CHAPTER 2: The ExtendScript Toolkit

The Script Editor

20

Bookmarks
The Edit > Bookmarks menu allows you to set and clear navigation points in your text. The F2 function
key is the default shortcut key for the bookmark commands:
Toggle the bookmark for the current line using CTRL-F2.
Move the cursor to the next bookmark with F2, or to the previous one with SHIFT-F2. The bookmarks
wrap, so that the first follows the last.
Use SHIFT-CTRL-F2 to clear all bookmarks in the current text.
When you navigate to a bookmark in a collapsed section of code, that section automatically opens.
Bookmarks are marked with a blue, right-pointing arrow at the left of the line (to the right of the line
number if it is shown). This is the same place where a breakpoint is marked with a dot (see "Setting
breakpoints" on page 31). If you have both a breakpoint and a bookmark set in the same line, the blue
arrow is superimposed on the breakpoint dot.

CHAPTER 2: The ExtendScript Toolkit

The Script Editor

21

line numbers
bookmark

collapsible
code sections

bookmark and
breakpoint

Mouse navigation and selection
You can use the mouse or special keyboard shortcuts to move the insertion point or to select text in the
document window. Click the left mouse button in the document window to move the position caret.
To select text with the mouse, click in unselected text, then drag over the text to be selected. If you drag
above or below the currently displayed text, the text scrolls, continuing to select while scrolling. You can
also double-click to select a word, or triple-click to select a line.
To initiate a drag-and-drop of selected text, click in the block of selected text, then drag to the destination.
You can drag text from one document window to another. You can also drag text out of the Toolkit into
another application that accepts dragged text, and drag text from another application into a Toolkit
document window.
You can drop files from the Explorer or the Finder onto the Toolkit to open them in a document window.

Keyboard navigation and selection
The Keyboard Shortcuts page in the Preferences dialog (Edit > Preferences) allows you to set or modify
keyboard shortcuts for all menu commands.
In addition to the keyboard shortcuts specified for menu commands, and the usual keyboard input, the
document window accepts these special movement keys. You can also select text by using a movement
key while pressing SHIFT.
ENTER

Insert a Line Feed character

Backspace

Delete character to the left

DELETE

Delete character to the right

Left arrow

Move insertion point left one character

CHAPTER 2: The ExtendScript Toolkit

The Script Editor

Right arrow

Move insertion point right one character

Up arrow

Move insertion point up one line; stay in column if possible

Down arrow

Move insertion point down one line; stay in column if possible

Page up

Move insertion point one page up

Page down

Move insertion point one page down

CTRL + Up arrow

Scroll up one line without moving the insertion point

CTRL + Down arrow

Scroll down one line without moving the insertion point

CTRL + Page up

Scroll one page up without moving the insertion point

CTRL + page down

Scroll one page down without moving the insertion point

CTRL + Left arrow

Move insertion point one word to the left

CTRL + right arrow

Move insertion point one word to the right

HOME

Move insertion point to start of line

END

Move insertion point to end of line

CTRL + HOME

Move insertion point to start of text

CTRL + END

Move insertion point to end of text

22

The Script Editor supports extended keyboard input via IME (Windows) or TMS (Mac OS). This is especially
important for Far Eastern characters.

Coding aids
The Script Editor offers a number of visual and editing features that help you navigate in and maintain the
syntactic structure of your JavaScript code, including the following.

Code completion
When you position the cursor in a document and begin typing, the Toolkit offers completion choices from
among keywords, global functions, functions that are defined in the current document, and functions
defined in the object-model dictionary that is currently selected from the flyout menu.

CHAPTER 2: The ExtendScript Toolkit

The Script Editor

23

You can use the flyout menu at the upper right corner of the document window to choose an
object-model dictionary to use for completion. Available dictionaries depend on which applications are
loaded. See "Inspecting object models" on page 36.

flyout menu
Select object
model dictionary
for completion

Brace matching
The Edit menu offers two kinds of brace-matching selection, that operate when the cursor is placed
immediate after an opening brace character, or immediately before a closing brace:
Edit > Select to Brace: Moves the cursor to the matching bracing, but does not select any text. The
default keyboard shortcut is CTRL 0 (zero).
Edit > Select Including Brace: Selects all text between the braces. The default keyboard shortcut is
SHIFT CTRL 0 (zero).
Brace characters include parentheses, curly braces, and square brackets.

Block indentation
When Word Wrap is off, you can automatically indent or outdent entire blocks of text. To indent a block of
text, select some or all of the text on the line or lines, and press TAB. (Be careful; if Word Wrap is on, this
deletes the selected text.) To outdent, press SHIFT TAB.

Comment and uncomment commands
Use Edit > Comment or Uncomment Selection to temporarily remove parts of a JavaScript program from
the path of execution. This command is a toggle. When you first issue the command, it places the special
comment sequence //~ at the front of any line that is wholly or partially selected. When you next issue the
command with such a line selected, it removes that comment marker.
The command affects only the comment markers it places in the text; it ignores any comment markers that
were already in the selected lines. This allows you to temporarily remove and replace blocks of text that
include both code and comments.

Version comments
A special comment format is reserved for a code versioning statement, which is used internally by Adobe
scripts, but is available to all scripters. Use Edit > Insert Version Tag to insert a comment containing the
file name and current date-time, in this format:

CHAPTER 2: The ExtendScript Toolkit

The Script Editor

24

/**
* @@@BUILDINFO@@@ SnpCreateDialog.jsx !Version! Tue Dec 05 2006 08:03:38 GMT-0800
*/

You are responsible for manually updating the !Version! portion with your own version information.

Undo and redo
Choose Undo or Redo from the Edit menu or from the document window’s right-click context menu to
revoke and reinstate multiple editing changes sequentially. The change history is kept from when a file is
created or loaded, and maintained through file-save operations.

Syntax checking
Before running the new script or saving the text as a script file, use Edit > Check Syntax to check whether
the text contains JavaScript syntax errors. The default keyboard shortcut is F7.
If the script is syntactically correct, the status line shows "No syntax errors."
If the Toolkit finds a syntax error, such as a missing quote, it highlights the affected text, plays a sound,
and shows the error message in the status line so you can fix the error.

Multiline statements
The Script Editor supports triple-quote syntax to allow strings to span several source code lines. When
entering a very long string, you can:
Enter it all on one line:
var myString = "This very long string might wrap onto a second line visually, but you
typed no CR character when entering it."

Enter on multiple lines, using a backslash (\) continuation character at the end of each line:
var myString = "This string spans \
two lines."

Use triple quotes around the entire string on multiple lines:
var myString = """This "quoted" word is inside the
multiline string enclosed by triple quotes."""

The triple-quote option allows the string to contain embedded quotes.

Searching in text
The Toolkit offers a search utility through the Edit > Find and Replace command. This command brings
up the Find and Replace panel. If the panel is not docked, you can hide it by pressing ESC.
The Find and Replace panel allows you to search through multiple documents for text that matches a
specific search string or regular expression. You can choose to search in:
The current document, or the current selection in the current document
All open documents

CHAPTER 2: The ExtendScript Toolkit

The Script Editor

25

All scripts made public by the current target application
Folders that you have defined as favorite locations; see "The Scripts panel and favorite script locations"
on page 17.

The results of a search are listed in the Find Results tab; by default, this is stacked with the Find and Replace
panel, but you can drag it to another stack, or display it as an independent floating panel.

Double-click a result line in the Find Results panel to jump directly to the document and line where the
text was found.

Using regular-expression syntax
The Toolkit supports a limited set of Regular Expression syntax for the Find and Replace dialog:
.

Matches any character

(

Marks the start of a region for capturing a match.

)

Marks the end of a capturing region.

\<

Matches the start of a word using the editor's current definition of words.

\>

Matches the end of a word using the editor's current definition of words.

CHAPTER 2: The ExtendScript Toolkit

The Script Editor

\x

Escapes a character x that would otherwise have a special meaning. For example, \[ is
interpreted as a left bracket, rather than the start of a character set.

[...]

A set of characters; for example, [abc] means any of the characters a, b or c. You can also use
ranges, for example [a-z] for any lower case character.

[^...]

The complement of the characters in a set. For example, [^A-Za-z] means any character
except an alphabetic character.

^

Matches the start of a line (unless used inside a set).

$

Matches the end of a line.

*

Matches 0 or more times. For example, Sa*m matches Sm, Sam, Saam, Saaam etc.

+

Matches 1 or more times. For example, Sa+m matches Sam, Saam, Saaam and so on.

26

In a replace operation, you can use the captured regions of a match in the replacement expression by
using the placeholders \1 through \9, where \1 refers to the first captured region, \2 to the second, and so
on.
For example, if the search string is Fred\([1-9]\)XXX and the replace string is Sam\1YYY, when applied to
Fred2XXX the search generates Sam2YYY.

Syntax marking
The Script Editor offers language-based syntax highlighting to aid in editing code. Although the
debugging features (including syntax checking) are only available for JavaScript, you can choose to edit
other kinds of code, and the syntax is highlighted according to the language. The style of syntax marking is
automatically set to match the file extension, or you can choose the language from the View > Syntax
Highlighting menu.
The style of highlighting is configurable, using the Fonts and Colors page of the Preferences dialog.

CHAPTER 2: The ExtendScript Toolkit

Debugging in the Toolkit

27

Select language for syntax
highlighting in Script Editor
Customize highlighting
styles in Preferences dialog

Debugging in the Toolkit
You can debug the code in the currently active document window. Select one of the debugging
commands to either run or to single-step through the program.
When you run code from the document window, it runs in the current target application’s selected
JavaScript engine. The Toolkit itself runs an independent JavaScript engine, so you can quickly edit and
run a script without connecting to a target application.

Selecting a debugging target
The Toolkit can debug multiple applications at one time. If you have more than one Adobe application
installed, use the drop-down list at the upper left of a document window to select the target application
for that window. All installed applications that support JavaScript are shown in this list. If you try to run a
script in an application that is not running, the Toolkit prompts for permission to run it.
Some applications use multiple JavaScript engines; all available engines in the selected target application
are shown in a drop-down list to the right of the application list, with an icon that shows the current
debugging status of that engine. A target application can have more than one JavaScript engine, and
more than one engine can be active, although only one is current. An active engine is one that is currently

CHAPTER 2: The ExtendScript Toolkit

Debugging in the Toolkit

28

executing code, is halted at a breakpoint, or, having executed all scripts, is waiting to receive events. An
icon by each engine name indicates whether it is running, halted, or waiting for input:
running
halted
waiting
The current engine is the one whose data and state is displayed in the Toolkit’s panes. If an application has
only one engine, its engine becomes current when you select the application as the target. If there is more
than one engine available in the target application, you can select an engine in the list to make it current.
When you open the Toolkit, the Toolkit itself is the default target application. When you select another
target, if the target application that you select is not running, the Toolkit prompts for permission and
launches the application. Similarly, if you run a script that specifies a target application that is not running
(using the #target directive), the Toolkit prompts for permission to launch it. If the application is running
but not selected as the current target, the Toolkit prompts you to switch to it.
If you select an application that cannot be debugged in the Toolkit, an error dialog reports that the Toolkit
cannot connect to the selected application.
The ExtendScript Toolkit is the default editor for JSX files. If you double-click a JSX file in a file browser, the
Toolkit looks for a #target directive in the file and launches that application to run the script; however, it
first checks for syntax errors in the script. If any are found, the Toolkit displays the error in a message box
and quits silently, rather than launching the target application. For example:

The JavaScript console
The JavaScript console is a command shell and output window for the currently selected JavaScript
engine. It connects you to the global namespace of that engine.

CHAPTER 2: The ExtendScript Toolkit

Debugging in the Toolkit

29

The console is a JavaScript listener, that expects input text to be JavaScript code.
You can use the console to evaluate expressions or call functions. Enter any JavaScript statement and
execute it by pressing ENTER. The statement executes within the stack scope of the line highlighted in the
Call Stack panel, and the result appears in the next line.
You can use the up- and down-arrow keys to scroll through previous entries, or place the cursor with
the mouse. Pressing ENTER executes the line that contains the cursor, or all selected lines.
The right-click context menu provides the same editing commands as that of the document window.
You can copy, cut, and paste text, and undo and redo previous actions.
You can select text with the mouse, and use the normal copy and paste shortcuts.
The flyout menu allows you to clear the current content.
Commands entered in the console execute with a timeout of one second. If a command takes longer than
one second to execute, the Toolkit generates a timeout error and terminates the attempt.
The console is the standard output location for JavaScript execution. If any script generates a syntax error,
the error is displayed here along with the file name and the line number. The Toolkit displays errors here
during its own startup phase.

Controlling code execution
The debugging commands are available from the Debug menu, from the document window’s right-click
context menu, through keyboard shortcuts, and from the toolbar buttons. Use these menu commands
and buttons to control the execution of code when the JavaScript Debugger is active.
Run
F5 (Windows)
Continue Ctrl R (Mac OS)

Starts or resumes execution of a script.

Break

Halts the currently executing script temporarily and reactivates
the JavaScript Debugger.

Ctrl F5 (Windows)
Cmd . (Mac OS)

Disabled when script is executing.

Enabled when a script is executing.
Stop

Step
Over

Shift F5 (Windows)
Ctrl K (Mac OS)

Stops execution of the script and generates a runtime error.

F10 (Windows)
Ctrl S (Mac OS)

Halts after executing a single JavaScript line in the script. If the
statement calls a JavaScript function, executes the function in
its entirety before stopping (do not step into the function).

Enabled when a script is executing.

Step Into F11 (Windows)
Ctrl T (Mac OS)

Halts after executing a single JavaScript line statement in the
script or after executing a single statement in any JavaScript
function that the script calls.

Step Out

When paused within the body of a JavaScript function, resumes
script execution until the function returns.

Shift F11
(Windows)
Ctrl U (Mac OS)

When paused outside the body of a function, resumes script
execution until the script terminates.

CHAPTER 2: The ExtendScript Toolkit

Debugging in the Toolkit

30

Visual indication of execution states
When the execution of a script halts because the script reached a breakpoint, or when the script reaches
the next line when stepping line by line, the document window displays the current script with the current
line highlighted in yellow.

current line
If the script encounters a runtime error, the Toolkit halts the execution of the script, displays the current
script with the current line highlighted in orange, and displays the error message in the status line. Use the
Data Browser to get further details of the current data assignments.

error line

error message
Scripts often use a try/catch clause to execute code that may cause a runtime error, in order to catch the
error programmatically rather than have the script terminate. You can choose to allow regular processing
of such errors using the catch clause, rather than breaking into the debugger. To set this behavior, choose
Debug > Don’t Break On Guarded Exceptions. Some runtime errors, such as Out Of Memory, always
cause the termination of the script, regardless of this setting.

CHAPTER 2: The ExtendScript Toolkit

Debugging in the Toolkit

31

Setting breakpoints
When debugging a script, it is often helpful to make it stop at certain lines so that you can inspect the state
of the environment, whether function calls are nested properly, or whether all variables contain the
expected data.
To stop execution of a script at a given line, click to the left of the line number to set a breakpoint. A
red dot indicates the breakpoint.
Click a second time to temporarily disable the breakpoint; the icon changes color.
Click a third time to delete the breakpoint. The icon is removed.
Some breakpoints need to be conditional. For example, if you set a breakpoint in a loop that is executed
several thousand times, you would not want to have the program stop each time through the loop, but
only on each 1000th iteration.
You can attach a condition to a breakpoint, in the form of a JavaScript expression. Every time execution
reaches the breakpoint, it runs the JavaScript expression. If the expression evaluates to a nonzero number
or true, execution stops.
To set a conditional breakpoint in a loop, for example, the conditional expression could be "i >= 1000",
which means that the program execution halts if the value of the iteration variable i is equal to or greater
than 1000.
TIP: It is often useful to check the boundary conditions for loops; to do this, you can set the condition for a
breakpoint within a loop to trigger on the first and last iterations.
You can set breakpoints on lines that do not contain any code, such as comment lines. When the Toolkit
runs the program, it automatically moves such a breakpoint down to the next line that actually contains
code.

The Breakpoints panel
The Breakpoints panel displays all breakpoints set in the current document window. You can use the
panel’s flyout menu to add, change, or remove a breakpoint.

You can edit a breakpoint by double-clicking it, or by selecting it and choosing Add or Modify from the
panel menu. A dialog allows you to change the line number, the breakpoint’s enabled state, and the

CHAPTER 2: The ExtendScript Toolkit

Debugging in the Toolkit

32

condition statement. You can also specify a hit count, which allows you to skip the breakpoint some
number of times before entering the debugger. The default is 1, which breaks at the first execution.

When execution reaches this breakpoint after the specified number of hits, the debugger evaluates this
condition. If it does not evaluate to true, the breakpoint is ignored and execution continues. This allows
you to break only when certain conditions are met, such as a variable having a particular value.

Breakpoint icons

Breakpoints
panel

Document
window

Each breakpoint is indicated by an icon to the left of the line number in the document window, and an
icon and line number in the Breakpoints panel. Different icons are used in the document window and in
the Breakpoints panel.

Unconditional breakpoint. Execution stops here.
Unconditional breakpoint, disabled. Execution does not stop.
Conditional breakpoint. Execution stops if the attached JavaScript expression evaluates
to true.
Conditional breakpoint, disabled. Execution does not stop.

CHAPTER 2: The ExtendScript Toolkit

Debugging in the Toolkit

33

Evaluation in help tips
If you let your mouse pointer rest over a variable or function in a document window, the result of
evaluating that variable or function is displayed as a help tip. When you are not debugging the program,
this is helpful only if the variables and functions are already known to the JavaScript engine. During
debugging, however, this is an extremely useful way to display the current value of a variable, along with
its current data type.

Tracking data
The Data Browser panel is your window into the JavaScript engine. It displays all live data defined in the
current context, as a list of variables with their current values. If execution has stopped at a breakpoint, it
shows variables that have been defined using var in the current function, and the function arguments. To
show variables defined in the global or calling scope, use the Call Stack to change the context (see "The
call stack" on page 34).
You can use the Data Browser to examine and set variable values.
Click a variable name to show its current value in the edit field at the top of the panel.
To change the value, enter a new value and press ENTER. If a variable is Read only, the edit field is
disabled.
flyout
menu

Examine or modify
selected variable’s value
Object opened to
show properties

The flyout menu for this panel lets you control the amount of data displayed:
Undefined Variables toggles the display of variables whose value is undefined (as opposed to null).
Functions toggles the display of all functions that are attached to objects. Most often, the interesting
data in an object are its callable methods.
Core JavaScript Elements toggles the display of all data that is part of the JavaScript language
standard, such as the Array constructor or the Math object.
Prototype Elements toggles the display of the JavaScript object prototype chain.
Each variable has a small icon that indicates the data type. An invalid object (that is, a reference to an
object that has been deleted) shows the object icon crossed out in red. An undefined value has no icon.

CHAPTER 2: The ExtendScript Toolkit

Debugging in the Toolkit

34

Boolean
Number
String
Object
Method
null
You can inspect the contents of an object by clicking its icon. The list expands to show the object’s
properties (and methods, if Functions display is enabled), and the triangle points down to indicate that
the object is open.

The call stack
The Call Stack panel is active while debugging a program. When an executing program stops because of a
breakpoint or runtime error, the panel displays the sequence of function calls that led to the current
execution point. The Call Stack panel shows the names of the active functions, along with the actual
arguments passed in to that function.
For example, this panel shows a break occurring at a breakpoint in a function RGBColorPicker():

The function containing the breakpoint is highlighted in the Call Stack panel. The line containing the
breakpoint is highlighted in the Document Window.
You can click any function in the call hierarchy to inspect it. In the document window, the line containing
the function call that led to that point of execution is marked with a green background. In the example,
when you select the run() function in the call stack, the Document Window highlights the line in that
function where the RGBColorPicker() function was called.

CHAPTER 2: The ExtendScript Toolkit

Code profiling for optimization

35

Switching between the functions in the call hierarchy allows you to trace how the current function was
called. The Console and Data Browser panels coordinate with the Call Stack panel. When you select a
function in the Call Stack:
The Console panel switches its scope to the execution context of that function, so you can inspect and
modify its local variables. These would otherwise be inaccessible to the running JavaScript program
from within a called function.
The Data Browser panel displays all data defined in the selected context.

Code profiling for optimization
The Profiling tool helps you to optimize program execution. When you turn profiling on, the JavaScript
engine collects information about a program while it is running. It counts how often the program
executed a line or function, or how long it took to execute a line or function. You can choose exactly which
profiling data to display.
Because profiling significantly slows execution time, the Profile menu offers these profiling options.
:

Off

Profiling turned off. This is the default.

Functions

The profiler counts each function call. At the end of execution, displays the total to
the left of the line number where the function header is defined.

Lines

The profiler counts each time each line is executed. At the end of execution,
displays the total to the left of the line number.
Consumes more execution time, but delivers more detailed information.

Add Timing Info

Instead of counting the functions or lines, records the time taken to execute each
function or line. At the end of execution, displays the total number of
microseconds spent in the function or line, to the left of the line number.
This is the most time-consuming form of profiling.

No Profiler Data

When selected, do not display profiler data.

CHAPTER 2: The ExtendScript Toolkit

Inspecting object models

Show Hit Count

When selected, display hit counts.

Show Timing

When selected, display timing data.

Erase Profiler Data

Clear all profiling data.

Save Data As

Save profiling data as comma-separated values in a CSV file that can be loaded
into a spreadsheet program such as Excel.

36

When execution halts (at termination, at a breakpoint, or due to a runtime error), the Toolkit displays this
information in the Document Window, line by line. The profiling data is color coded:
Green indicates the lowest number of hits, or the fastest execution time.
Orange or yellow indicates a trouble spot, such as a line that has been executed many times, or which
line took the most time to execute.
This example shows number-of-hits information:

This example displays timing information for the program, in microseconds. The timing might not be
accurate down to the microsecond; it depends on the resolution and accuracy of the hardware timers built
into your computer.

Inspecting object models
The ExtendScript Toolkit offers the ability to inspect the object model of any loaded dictionary, using the
Object Model Viewer that you invoke from the Help menu.

CHAPTER 2: The ExtendScript Toolkit

Inspecting object models

37

The Object Model Viewer (OMV) comes up as a separate, floating window. The OMV allows you to browse
through the object hierarchy and inspect the type and description of each property, and the description
and parameters for each method.

The drop-down menu in the Browser section at the top left allows you to choose from any loaded
dictionary of objects. A dictionary provides access to the object model for one application or subsystem.
The Core JavaScript Classes dictionary includes Adobe tools and utilities such as File and Folder.
The ScriptUI Classes dictionary shows the interface elements defined in the ScriptUI JavaScript
module.

CHAPTER 2: The ExtendScript Toolkit

Inspecting object models

38

Each Adobe application defines a dictionary for that application’s Document Object Model (DOM). The
dictionary for a particular application may not be available until you launch that application, or until
you select it as a target in the Toolkit.

To inspect an object model, select the appropriate dictionary from the Browser menu. The classes defined
in that model appear in the Classes panel. Select a class to populate the Types panel with the available
element types (Constructor, Class, Instance, Event). Select the type to populate the Properties and
Methods panel with elements of that type.
Each time you select a class or element, its description appears on the right; descriptions are stacked,
remaining in view until you close them. You can close each description individually, using the mouse-over
menu that appears in the lower right of the description itself, or you can close all open descriptions using
the Close All button at the top left of the OMV window.

Clear all
descriptions

Mouse-over
menu

The mouse-over menu also allows you to bookmark an element for easy access, or copy text from the
description. Live links in the descriptions take you to related objects and elements, and you can search for
text in names or descriptions.
