<a id="vscode-extension-features"></a>

# VS Code Extension Features

Once you have the Extendscript VS Code Extension up and running, there are a few other things you can do; [export to jsxbin](#exporting-as-binary), [use breakpoints in your code](#using-breakpoint), and more.

#### NOTE
This guide is meant to give insight on how to use specific Extendscript for VS Code features.

If you’re looking on how to get up and running with the extension, see [Getting Started with the VS Code Debugger](getting-started-with-vscode-debugger.md#getting-started-with-vscode-debugger).

---

<a id="using-breakpoint"></a>

## Using Breakpoints

Breakpoints allow you to stop your code running at a specific line, letting you explore the call stack, variable status, and function arguments at that exact point.

You can create breakpoints one of two ways; either using [VS Code’s native Breakpoints system](#vs-code-breakpoints), or using [Extendscript’s inline breakpoint method](#extendscript-breakpoints).

<a id="vs-code-breakpoints"></a>

### VS Code Breakpoints

One advantage of using VS Code is that we can set VS Code breakpoints and have the debugger respect them! See the official [Visual Studio article on breakpoints](https://code.visualstudio.com/docs/editor/debugging#_breakpoints).

<a id="extendscript-breakpoints"></a>

### Extendscript Breakpoints

You can add in `$.bp()` anywhere in your source file, and the debugger will catch on it at the correct place, allowing you to view the call stack / data browser at that point.

This works identically to the `debugger;` method in browser-based Javascript.

See [bp()](../extendscript-tools-features/dollar-object.md#dollar-bp) for more info.

---

<a id="exporting-as-binary"></a>

## Exporting as Binary

In the old Extendscript ToolKit, you could very easily save your projects as an obfuscated binary file. This functionality still exists in the VS Code debugger!

You can export either [from the vscode interface](#jsxbin-from-vs-code), or [via the command line](#jsxbin-from-the-command-line).

<a id="jsxbin-from-vs-code"></a>

### JSXBIN from VS Code

To export your script as binary, you have a few options:

> - With the file open, right-click the document and press ‘Export as Binary’
> - Open the command palette (Ctrl + Shift + P) and type ‘Export as Binary’
> - Use the keyboard shortcut for the same command (Ctrl + Shift + J)

<a id="jsxbin-from-the-command-line"></a>

### JSXBIN from the Command Line

The VS Code extension allows you to export either single files or entire directories via the command line, but it takes a bit of work on your end.

#### WARNING
While there is a built-in way to do it, it can be a fairly unfriendly process. As an alternative, consider the gulp-accessible [npm package jsxbin](https://www.npmjs.com/package/jsxbin). It does the same as below, but with much less user involvement.

There are reports that this package has issues on Windows. As an alternative gulp task, you can try [this script](https://bitbucket.org/motiondesign/workspace/snippets/aLzaX5) from [Justin Taylor](http://justintaylor.tv/).

Both methods above require the VS Code extension be installed.

All of the files are saved in the same directory with the same filename (though the suffix will be .jsxbin). Any passed directories will be recursively traversed.

1. Within the Extension install directory, there’s a `exportToJSX.js` script file that accepts a file path or directory to convert. We need to get this path.
   > - Note that you’ll need to swap X.X.X with the current version #
   > - MacOS: `$HOME/.vscode/extensions/adobe.extendscript-debug-X.X.X/public-scripts/exportToJSX.js`
   > - Windows: `%USERPROFILE%\.vscode\extensions\adobe.extendscript-debug-X.X.X\public-scripts\exportToJSX.js`
2. This script accepts a few arguments;
   > - `-f`, `--force`: Overwrite the ‘.jsxbin’ file/files if already exists
   > - `-n`, `--name`: The ‘.js/.jsx’ script path or path to some directory having these files.
   > - `h`, `--help`: Show this help and exit
3. Running the script
   > - From your command line, run `node path/to/exportToJSX.js [options] [file/directory]`

<a id="examples"></a>

#### Examples

**Exporting a single script**

```default
sh node "C:/Users/Dev/.vscode/extensions/adobe.extendscript-debug-1.1.2/public-scripts/exportToJSX.js" "d:/projects/scripting/coolTool.jsx"
```

**Exporting a folder, overwriting**

```default
sh node "C:/Users/Dev/.vscode/extensions/adobe.extendscript-debug-1.1.2/public-scripts/exportToJSX.js" --force "d:/projects/scripting/"
```
