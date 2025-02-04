# Folder Object

Represents a file-system folder or directory in a platform-independent manner. All properties and methods resolve file system aliases automatically and act on the original file unless otherwise noted.

---

## Folder Object Constructors

```javascript
Folder( [path] ); // Can return a File object
new Folder( [path] ); // Always returns a Folder object
```

To create a Folder object, use the Folder function or the new operator. The constructor accepts full or partial path names, and returns the new object.

+-----------+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter |  Type  |                                                                                                                           Description                                                                                                                            |
+===========+========+==================================================================================================================================================================================================================================================================+
| `path`    | String | Optional. The absolute or relative path to the Folder associated with this object, specified in platform-specific or URI format; see [Specifying paths](using-file-and-folder-objects.md#specifying-paths). The value stored in the object is the absolute path. |
|           |        |                                                                                                                                                                                                                                                                  |
|           |        | The path need not refer to an existing Folder. If not supplied, a temporary name is generated.                                                                                                                                                                   |
|           |        |                                                                                                                                                                                                                                                                  |
|           |        | If the path refers to an existing file:                                                                                                                                                                                                                          |
|           |        |                                                                                                                                                                                                                                                                  |
|           |        | - The Folder function returns a File object instead of a File object.                                                                                                                                                                                            |
|           |        | - The new operator returns a Folder object for a nonexisting folder with the same name.                                                                                                                                                                          |
|           |        |                                                                                                                                                                                                                                                                  |
|           |        | !!! warning                                                                                                                                                                                                                                                      |
|           |        |     In After Effects on MacOS, if `path.length` is more than 1002, After Effects crashes.                                                                                                                                                                        |
|           |        |                                                                                                                                                                                                                                                                  |
|           |        |     This has been reported on MacOS 10.11.6 and After Effects 13.8 and 14.0.                                                                                                                                                                                     |
+-----------+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

---

## Folder Class Attributes

These properties are available as static properties of the Folder class. It is not necessary to create an instance to access them.

### Folder.appData

`Folder.appData`

#### Description

A Folder object for the folder that contains application data for all users.

- In Windows, the value of `%PROGRAMDATA%` (by default, `C:\ProgramData`)
- In Mac OS, `/Library/Application Support`

#### Type

Folder. Read only.

---

### Folder.appPackage

`Folder.appPackage`

#### Description

The Folder object for the folder that contains the bundle of the running application.

- In Windows, for example: `C:\Program Files (x86)\Adobe\Adobe ExtendScript Toolkit CC\`
- In Mac OS, for example: `/Applications/Adobe ExtendScript Toolkit CC/ExtendScript Toolkit.app`

#### Type

String. Read only.

---

### Folder.commonFiles

`Folder.commonFiles`

#### Description

A Folder object for the folder that contains files common to all programs.

- In Windows, the value of `%CommonProgramFiles%` (by default, `C:\Program Files\Common Files`)
- In Mac OS, `/Library/Application Support`

#### Type

Folder. Read only.

---

### Folder.current

`Folder.current`

#### Description

A Folder object for the current folder. Assign either a Folder object or a string containing the new path name to set the current folder.

#### Type

Folder

---

### Folder.desktop

`Folder.desktop`

#### Description

A Folder object for the folder that contains the user's desktop.

- In Windows, `C:\Users\[username]\Desktop`
- In Mac OS, `~/Desktop`

#### Type

Folder. Read only.

---

### Folder.fs

`Folder.fs`

#### Description

The name of the file system.

One of:

- `Windows`,
- `Macintosh`, or
- `Unix`

#### Type

String. Read only.

---

### Folder.myDocuments

`Folder.myDocuments`

#### Description

A Folder object for the user's default document folder.

- In Windows, `C:\Users\[username]\Documents`
- In Mac OS, `~/Documents`

#### Type

Folder. Read only.

---

### Folder.startup

`Folder.startup`

#### Description

A Folder object for the folder containing the executable image of the running application.

#### Type

Folder. Read only.

---

### Folder.system

`Folder.system`

#### Description

A Folder object for the folder containing the operating system files.

- In Windows, the value of `%windir%` (by default, `C:\Windows`)
- In Mac OS, `/System`

#### Type

Folder. Read only.

---

### Folder.temp

`Folder.temp`

#### Description

A Folder object for the default folder for temporary files.

#### Type

Folder. Read only.

---

### Folder.trash

`Folder.trash`

#### Description

- In Mac OS, a Folder object for the folder containing deleted items.
- In Windows, where the Recycle Bin is a database rather than a folder, value is `null`.

#### Type

Folder or `null`. Read only.

---

### Folder.userData

`Folder.userData`

#### Description

A Folder object for the folder that contains application data for the current user.

- In Windows, the value of %APPDATA% (by default, `C:\Users\[username]\Appdata\Roaming`)
- In Mac OS, `~/Library/Application Support`

#### Type

Folder. Read only.

---

## Folder Class Methods

These functions are available as a static methods of the Folder class. It is not necessary to create an instance in order to call them.

### Folder.decode()

`Folder.decode(uri)`

#### Description

Decodes the specified string as required by RFC 2396.

All special characters must be encoded in UTF-8 and stored as escaped characters starting with the percent sign followed by two hexadecimal digits. For example, the string `"my%20file"` is decoded as `"my file"`. Special characters are those with a numeric value greater than 127, except the following:

```javascript
``/ - _ . ! ~ * ' ( )``
```

#### Parameters

| Parameter |  Type  |          Description          |
| --------- | ------ | ----------------------------- |
| `uri`     | String | The encoded string to decode. |

#### Returns

String

---

### Folder.encode()

`Folder.encode(name)`

#### Description

Encodes the specified string as required by RFC 2396.

All special characters must be encoded in UTF-8 and stored as escaped characters starting with the percent sign followed by two hexadecimal digits. For example, the string `"my%20file"` is decoded as `"my file"`. Special characters are those with a numeric value greater than 127, except the following:

```javascript
``/ - _ . ! ~ * ' ( )``
```

#### Parameters

| Parameter |  Type  |      Description      |
| --------- | ------ | --------------------- |
| `name`    | String | The string to encode. |

#### Returns

String

---

### Folder.isEncodingAvailable()

`Folder.isEncodingAvailable(name)`

#### Description

Checks whether a given encoding is available.

#### Parameters

| Parameter |  Type  |                                                                               Description                                                                                |
| --------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name`    | String | The encoding name. Typical values are `"ASCII"`, `"binary"`, or `"UTF-8"`. See [File- and Folder-supported encoding names](file-and-folder-supported-encoding-names.md). |

#### Returns

Boolean. `true` if your system supports the specified encoding, `false` otherwise.

---

### Folder.selectDialog()

`Folder.selectDialog([prompt])`

#### Description

Opens the built-in platform-specific file-browsing dialog, and creates a new File or Folder object for the selected file or folder. Differs from the object method [selectDlg()](#folderselectdlg) in that it does not preselect a folder.

#### Parameters

| Parameter |  Type  |          Description          |
| --------- | ------ | ----------------------------- |
| `prompt`   | String | Optional. The prompt text, if the dialog allows a prompt.   |

#### Returns

If the user clicks `OK`, returns a [File](./file-object.md) or Folder object for the selected file or folder.

If the user cancels, returns `null`.

---

## Folder Object Attributes

These properties are available for Folder objects.

### Folder.absoluteURI

`folderObj.absoluteURI`

#### Description

The full path name for the referenced folder in URI notation.

#### Type

String. Read only.

---

### Folder.alias

`folderObj.alias`

#### Description

When `true`, the object refers to a file system alias or shortcut.

#### Type

Boolean. Read only.

---

### Folder.created

`folderObj.created`

#### Description

The creation date of the referenced folder, or null if the object does not refer to a folder on disk.

#### Type

Date. Read only.

---

### Folder.displayName

`folderObj.displayName`

#### Description

The localized name of the referenced folder, without the path.

#### Type

String. Read only.

---

### Folder.error

`folderObj.error`

#### Description

A message describing the most recent file system error; see [File access error messages](file-access-error-messages.md).

Typically set by the file system, but a script can set it. Setting this value clears any error message and resets the error bit for opened files. Contains the empty string if there is no error.

#### Type

String

---

### Folder.exists

`folderObj.exists`

#### Description

When `true`, this object refers to a folder that currently exists in the file system.

#### Type

Boolean. Read only.

---

### Folder.fsName

`folderObj.fsName`

#### Description

The platform-specific name of the referenced folder as a full path name.

#### Type

String. Read only.

---

### Folder.fullName

`folderObj.fullName`

#### Description

The full path name for the referenced folder in URI notation.

#### Type

String. Read only.

---

### Folder.localizedName

`folderObj.localizedName`

#### Description

A localized version of the folder name portion of the absolute URI for the referenced file, without the path specification.

#### Type

String. Read only.

---

### Folder.modified

`folderObj.modified`

#### Description

The date of the referenced folder's last modification, or `null` if the object does not refer to a folder on disk.

#### Type

Date. Read only.

---

### Folder.name

`folderObj.name`

#### Description

The folder name portion of the absolute URI for the referenced file, without the path specification.

#### Type

String. Read only.

---

### Folder.parent

`folderObj.parent`

#### Description

The Folder object for the folder that contains this folder, or `null` if this object refers to the root folder of a volume.

#### Type

Folder. Read only.

---

### Folder.path

`folderObj.path`

#### Description

The path portion of the absolute URI for the referenced folder, without the folder name.

#### Type

String. Read only.

---

### Folder.relativeURI

`folderObj.relativeURI`

#### Description

The path name for the referenced folder in URI notation, relative to the current folder.

#### Type

String. Read only.

---

## Folder Object Methods

These functions are available for Folder objects.

### Folder.changePath()

`folderObj.changePath(path)`

#### Description

#### Parameters

| Parameter |  Type  |                           Description                            |
| --------- | ------ | ---------------------------------------------------------------- |
| `path`    | String | The new path, absolute or relative to the current parent folder. |

Changes the path specification of the referenced folder.

#### Returns

Boolean. `true` on success.

---

### Folder.create()

`folderObj.create()`

#### Description

Creates a folder at the location given by this object's path property.

#### Returns

Boolean. `true` if the folder was created successfully.

---

### Folder.execute()

`folderObj.execute()`

#### Description

Opens this folder in the platform-specific file browser (as if it had been double-clicked in the file browser).

#### Returns

Boolean. `true` immediately if the folder was opened successfully.

---

### Folder.getFiles()

`folderObj.getFiles([mask])`

#### Description

Retrieves the contents of this folder, filtered by the supplied mask.

#### Parameters

+-----------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter |        Type        |                                                                                                                                             Description                                                                                                                                             |
+===========+====================+=====================================================================================================================================================================================================================================================================================================+
| `mask`    | String or Function | Optional. A search mask for file names.                                                                                                                                                                                                                                                             |
|           |                    |                                                                                                                                                                                                                                                                                                     |
|           |                    | A string that can contain question mark (`?`) and asterisk (`*`) wild cards. Default is "`*`", which matches all file names.                                                                                                                                                                        |
|           |                    |                                                                                                                                                                                                                                                                                                     |
|           |                    | Can also be the name of a function that takes a File or Folder object as its argument.                                                                                                                                                                                                              |
|           |                    |                                                                                                                                                                                                                                                                                                     |
|           |                    | It is called for each file or folder found in the search; if it returns `true`, the object is added to the return array.                                                                                                                                                                            |
|           |                    |                                                                                                                                                                                                                                                                                                     |
|           |                    | !!! note                                                                                                                                                                                                                                                                                            |
|           |                    |     In Windows, all aliases end with the extension `.lnk`; ExtendScript strips this from the file name when found, in order to preserve compatibility with other operating systems. You can search for all aliases by supplying the search mask `"*.lnk"`, but note that such code is not portable. |
+-----------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


#### Returns

Returns an array of [File](./file-object.md) and Folder objects, or `null` if this object's referenced folder does not exist.

---

### Folder.getRelativeURI()

`folderObj.getRelativeURI([basePath])`

#### Description

Retrieves the path for this folder relative to the specified base path or the current folder, in URI notation.

#### Parameters

| Parameter  |  Type  |                                 Description                                  |
| ---------- | ------ | ---------------------------------------------------------------------------- |
| `basePath` | String | Optional. The base path for the relative URI. Default is the current folder. |

#### Returns

String

---

### Folder.remove()

`folderObj.remove()`

#### Description

Deletes the empty folder associated with this object from disk, immediately, without moving it to the system trash.

Folders must be empty before they can be deleted. Does not resolve aliases; instead, deletes the referenced alias or shortcut file itself.

!!! note
    Cannot be undone. It is recommended that you prompt the user for permission before deleting.

#### Returns

Boolean. `true` if the folder is deleted successfully.

---

### Folder.rename()

`folderObj.rename(newName)`

#### Description

#### Parameters

| Parameter |  Type  |            Description             |
| --------- | ------ | ---------------------------------- |
| `newName` | String | The new folder name, with no path. |

Renames the associated folder. Does not resolve aliases; instead, renames the referenced alias or shortcut file itself.

#### Returns

Boolean. `true` on success.

---

### Folder.resolve()

`folderObj.resolve()`

#### Description

If this object references an alias or shortcut, this method resolves that alias

#### Returns

A new [Folder object](#) that references the file-system element to which the alias resolves, or `null` if this object does not reference an alias, or if the alias cannot be resolved.

---

### Folder.selectDlg()

`folderObj.selectDlg(prompt)`

#### Description

Opens the built-in platform-specific file-browsing dialog, and creates a new File or Folder object for the selected file or folder.

Differs from the class method [`selectDialog()`](#folderselectdialog) in that it preselects this folder.

#### Parameters

| Parameter |  Type  |                   Description                   |
| --------- | ------ | ----------------------------------------------- |
| `prompt`  | String | The prompt text, if the dialog allows a prompt. |

#### Returns

If the user clicks `OK`, returns a [File](./file-object.md) or Folder object for the selected file or folder.

If the user cancels, returns `null`.
