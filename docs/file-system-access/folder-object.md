# Folder object

Represents a file-system folder or directory in a platform-independent manner. All properties and
methods resolve file system aliases automatically and act on the original file unless otherwise noted.

---

## Folder object constructors

To create a Folder object, use the Folder function or the new operator. The constructor accepts full or
partial path names, and returns the new object.

```default
Folder( [path] ); // Can return a File object
new Folder( [path] ); // Always returns a Folder object
```

| `path`   | Optional. The absolute or relative path to the folder associated with this object, specified in URI<br/>format; see [Specifying paths](using-file-and-folder-objects.md#specifying-paths). The value stored in the object is the absolute path.<br/><br/>The path need not refer to an existing folder. If not supplied, a temporary name is generated.<br/><br/>If the path refers to an existing file:<br/><br/>- The Folder function returns a File object instead of a Folder object.<br/>- The new operator returns a Folder object for a nonexisting folder with the same name.   |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

!!! warning
    In After Effects on MacOS, if `path.length` is more than 1002, After Effects crashes.
This has been reported on MacOS 10.11.6 and After Effects 13.8 and 14.0.

---

## Folder class properties

These properties are available as static properties of the Folder class. It is not necessary to create an
instance to access them.

| `appData`     | Folder   | A Folder object for the folder that contains application data for all users. Read<br/>only.<br/><br/>- In Windows, the value of `%PROGRAMDATA%` (by default, `C:\ProgramData`)<br/>- In Mac OS, `/Library/Application Support`                                                                              |
|---------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `appPackage`  | String   | The Folder object for the folder that contains the bundle of the<br/>running application. Read only.<br/><br/>- In Windows, for example: `C:\Program Files (x86)\Adobe\Adobe ExtendScript Toolkit CC\`<br/>- In Mac OS, for example: `/Applications/Adobe ExtendScript Toolkit CC/ExtendScript Toolkit.app` |
| `commonFiles` | Folder   | A Folder object for the folder that contains files common to all programs.<br/>Read only.<br/><br/>- In Windows, the value of `%CommonProgramFiles%` (by default,<br/>  `C:\Program Files\Common Files`)<br/>- In Mac OS, `/Library/Application Support`                                                    |
| `current`     | Folder   | A Folder object for the current folder. Assign either a Folder object or a<br/>string containing the new path name to set the current folder.                                                                                                                                                               |
| `desktop`     | Folder   | A Folder object for the folder that contains the user's desktop. Read only.<br/><br/>- In Windows, `C:\Users\[username]\Desktop`<br/>- In Mac OS, `~/Desktop`                                                                                                                                               |
| `fs`          | String   | The name of the file system. Read only. One of `Windows`, `Macintosh`, or `Unix`.                                                                                                                                                                                                                           |
| `myDocuments` | Folder   | A Folder object for the user's default document folder. Read only.<br/><br/>- In Windows, `C:\Users\[username]\Documents`<br/>- In Mac OS, `~/Documents`                                                                                                                                                    |
| `startup`     | Folder   | A Folder object for the folder containing the executable image of the running<br/>application. Read only.                                                                                                                                                                                                   |
| `system`      | Folder   | A Folder object for the folder containing the operating system files. Read<br/>only.<br/><br/>- In Windows, the value of `%windir%` (by default, `C:\Windows`)<br/>- In Mac OS, `/System`                                                                                                                   |
| `temp`        | Folder   | A Folder object for the default folder for temporary files. Read only.                                                                                                                                                                                                                                      |
| `trash`       | Folder   | - In Mac OS, a Folder object for the folder containing deleted items.<br/>- In Windows, where the Recycle Bin is a database rather than a folder, value<br/>  is `null`.<br/><br/>Read only.                                                                                                                |
| `userData`    | Folder   | A Folder object for the folder that contains application data for the current<br/>user. Read only.<br/><br/>- In Windows, the value of %APPDATA% (by default, `C:\Users\[username]\Appdata\Roaming`)<br/>- In Mac OS, `~/Library/Application Support`                                                       |

---

## Folder class functions

These functions are available as a static methods of the Folder class. It is not necessary to create an
instance in order to call them.

### decode()

`Folder.decode( uri )`

| `uri`   | String. The encoded string to decode. All special characters must be encoded in UTF-8<br/>and stored as escaped characters starting with the percent sign followed by two<br/>hexadecimal digits. For example, the string `"my%20file"` is decoded as `"my file"`.   |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Special characters are those with a numeric value greater than 127, except the following:

```default
``/ - _ . ! ~ * ' ( )``
```

Decodes the specified string as required by RFC 2396.

Returns the decoded string.

---

### encode()

`Folder.encode( name )`

| `name`   | String. The string to encode.   |
|----------|---------------------------------|

Encodes the specified string as required by RFC 2396. All special characters are encoded in UTF-8
and stored as escaped characters starting with the percent sign followed by two hexadecimal digits.
For example, the string `"my file"` is encoded as `"my%20file"`.

Special characters are those with a numeric value greater than 127, except the following:

```default
``/ - _ . ! ~ * ' ( )``
```

Returns the encoded string.

---

### isEncodingAvailable()

`Folder.isEncodingAvailable( name )`

| `name`   | String. The encoding name. Typical values are "ASCII," "binary," or "UTF-8."<br/>See [File- and Folder-supported encoding names](file-and-folder-supported-encoding-names.md#file-and-folder-supported-encoding-names).   |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Checks whether a given encoding is available.

Returns true if your system supports the specified encoding, false otherwise.

---

### selectDialog()

`Folder.selectDialog( [prompt] )`

| `prompt`   | Optional. A string containing the prompt text, if the dialog allows a prompt.   |
|------------|---------------------------------------------------------------------------------|

Opens the built-in platform-specific file-browsing dialog, and creates a new File or Folder object
for the selected file or folder. Differs from the object method [selectDlg()](#folder-selectdlg) in that it does not
preselect a folder.

If the user clicks `OK`, returns a File or Folder object for the selected file or folder. If the user
cancels, returns null.

---

## Folder object properties

These properties are available for Folder objects.

| `absoluteURI`   | String   | The full path name for the referenced folder in URI notation. Read only.                                                                                                                                                                                                                                                                                          |
|-----------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `alias`         | Boolean  | When true, the object refers to a file system alias or shortcut. Read only.                                                                                                                                                                                                                                                                                       |
| `created`       | Date     | The creation date of the referenced folder, or null if the object does not<br/>refer to a folder on disk. Read only.                                                                                                                                                                                                                                              |
| `displayName`   | String   | The localized name of the referenced folder, without the path. Read only.                                                                                                                                                                                                                                                                                         |
| `error`         | String   | A message describing the most recent file system error; see [File access error messages](file-access-error-messages.md#file-access-error-messages).<br/>Typically set by the file system, but a script<br/>can set it. Setting this value clears any error message and resets the error<br/>bit for opened files. Contains the empty string if there is no error. |
| `exists`        | Boolean  | When true, this object refers to a folder that currently exists in the file<br/>system. Read only.                                                                                                                                                                                                                                                                |
| `fsName`        | String   | The platform-specific name of the referenced folder as a full path name.<br/>Read only.                                                                                                                                                                                                                                                                           |
| `fullName`      | String   | The full path name for the referenced folder in URI notation. Read only.                                                                                                                                                                                                                                                                                          |
| `localizedName` | String   | A localized version of the folder name portion of the absolute URI for the<br/>referenced file, without the path specification. Read only.                                                                                                                                                                                                                        |
| `modified`      | Date     | The date of the referenced folder's last modification, or `null` if the object<br/>does not refer to a folder on disk. Read only.                                                                                                                                                                                                                                 |
| `name`          | String   | The folder name portion of the absolute URI for the referenced file,<br/>without the path specification. Read only.                                                                                                                                                                                                                                               |
| `parent`        | Folder   | The Folder object for the folder that contains this folder, or `null` if this<br/>object refers to the root folder of a volume. Read only.                                                                                                                                                                                                                        |
| `path`          | String   | The path portion of the absolute URI for the referenced folder, without the<br/>folder name. Read only.                                                                                                                                                                                                                                                           |
| `relativeURI`   | String   | The path name for the referenced folder in URI notation, relative to the<br/>current folder. Read only.                                                                                                                                                                                                                                                           |

---

## Folder object functions

These functions are available for Folder objects.

---

### changePath()

`folderObj.changePath( path )`

| `path`   | A string containing the new path, absolute or relative to the current parent folder.   |
|----------|----------------------------------------------------------------------------------------|

Changes the path specification of the referenced folder.

Returns true on success.

---

### create()

`folderObj.create()`

Creates a folder at the location given by this object's path property.

Returns true if the folder was created successfully.

---

### execute()

`folderObj.execute ()`

Opens this folder in the platform-specific file browser (as if it had been double-clicked in the file
browser).

Returns true immediately if the folder was opened successfully.

---

### getFiles()

`folderObj.getFiles( [mask] )`

| `mask`   | Optional. A search mask for file names. A string that can contain question mark (`?`) and<br/>asterisk (`*`) wild cards. Default is "`*`", which matches all file names.   |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Can also be the name of a function that takes a File or Folder object as its argument.
It is called for each file or folder found in the search; if it returns true, the object is added
to the return array.

!!! note
    In Windows, all aliases end with the extension `.lnk`; ExtendScript strips this from
the file name when found, in order to preserve compatibility with other operating
systems. You can search for all aliases by supplying the search mask `"*.lnk"`, but note
that such code is not portable.

Retrieves the contents of this folder, filtered by the supplied mask.

Returns an array of File and Folder objects, or null if this object's referenced folder does not exist.

---

### getRelativeURI()

`folderObj.getRelativeURI( [basePath] )`

| `basePath`   | Optional. A string containing the base path for the relative URI.<br/>Default is the current folder.   |
|--------------|--------------------------------------------------------------------------------------------------------|

Retrieves the path for this folder relative to the specified base path or the current folder, in URI
notation.

Returns a string containing the relative URI.

---

### remove()

`folderObj.remove()`

Deletes the empty folder associated with this object from disk, immediately, without moving it to
the system trash. Folders must be empty before they can be deleted. Does not resolve aliases;
instead, deletes the referenced alias or shortcut file itself.

!!! note
    Cannot be undone. It is recommended that you prompt the user for permission before deleting.

Returns true if the folder is deleted successfully.

---

### rename()

`folderObj.rename( newName )`

| `newName`   | The new folder name, with no path.   |
|-------------|--------------------------------------|

Renames the associated folder. Does not resolve aliases; instead, renames the referenced alias or
shortcut file itself.

Returns true on success.

---

### resolve()

`folderObj.resolve()`

If this object references an alias or shortcut, this method resolves that alias

Returns a new `Folder` object that references the file-system element to which the alias resolves, or
null if this object does not reference an alias, or if the alias cannot be resolved.

---

### selectDlg()

`folderObj.selectDlg( prompt )`

| `prompt`   | A string containing the prompt text, if the dialog allows a prompt.   |
|------------|-----------------------------------------------------------------------|

Opens the built-in platform-specific file-browsing dialog, and creates a new File or Folder object
for the selected file or folder. Differs from the class method selectDialog() in that it preselects
this folder.

If the user clicks `OK`, returns a File or Folder object for the selected file or folder. If the user
cancels, returns `null`.
