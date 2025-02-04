# File Object

Represents a file in the local file system in a platform-independent manner. All properties and methods resolve file system aliases automatically and act on the original file unless otherwise noted.

---

## File Object Constructors

```javascript
File ( [ path ] );    // Can return a Folder object
new File ([ path ] ); // Always returns a File object
```

To create a File object, use the File function or the new operator. The constructor accepts full or partial path names, and returns the new object.

The CRLF sequence for the file is preset to the system default, and the encoding is preset to the default system encoding.

+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter |  Type  |                                                                                                                          Description                                                                                                                           |
+===========+========+================================================================================================================================================================================================================================================================+
| `path`    | String | Optional. The absolute or relative path to the file associated with this object, specified in platform-specific or URI format; see [Specifying paths](using-file-and-folder-objects.md#specifying-paths). The value stored in the object is the absolute path. |
|           |        |                                                                                                                                                                                                                                                                |
|           |        | The path need not refer to an existing file. If not supplied, a temporary name is generated.                                                                                                                                                                   |
|           |        |                                                                                                                                                                                                                                                                |
|           |        | If the path refers to an existing folder:                                                                                                                                                                                                                      |
|           |        |                                                                                                                                                                                                                                                                |
|           |        | - The File function returns a Folder object instead of a File object.                                                                                                                                                                                          |
|           |        | - The new operator returns a File object for a nonexisting file with the same name.                                                                                                                                                                            |
|           |        |                                                                                                                                                                                                                                                                |
|           |        | !!! warning                                                                                                                                                                                                                                                    |
|           |        |     In After Effects on MacOS, if `path.length` is more than 1002, After Effects crashes.                                                                                                                                                                      |
|           |        |                                                                                                                                                                                                                                                                |
|           |        |     This has been reported on MacOS 10.11.6 and After Effects 13.8 and 14.0.                                                                                                                                                                                   |
+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

---

## File Class Attributes

This property is available as a static property of the File class. It is not necessary to create an instance to access it.

### File.fs

`File.fs`

#### Description

The name of the file system.

#### Type

String. Read only. One of `Windows`, `Macintosh`, or `Unix`.

---

## File Class Methods

These functions are available as static methods of the File class. It is not necessary to create an instance to call them.

### File.decode()

`File.decode(uri)`

#### Description

Decodes the specified string as required by RFC 2396.

All special characters must be encoded in UTF-8 and stored as escaped characters starting with the percent sign followed by two hexadecimal digits. Special characters are those with a numeric value greater than 127, except the following:

```javascript
/ - _ . ! ~ * ' ( )
```

For example, the string `"my%20file"` is decoded as `"my<br/>file"`.

#### Parameters

| Parameter |  Type  |          Description          |
| --------- | ------ | ----------------------------- |
| `uri`     | String | The encoded string to decode. |

#### Returns

String

---

### File.encode()

`File.encode(name)`

#### Description

Encodes the specified string as required by RFC 2396.

All special characters are encoded in UTF-8 and stored as escaped characters starting with the percent sign followed by two hexadecimal digits. For example, the string "my file" is encoded as "my%20file". Special characters are those with a numeric value greater than 127, except the following:

```javascript
/ - _ . ! ~ * ' ( )
```

#### Parameters

| Parameter |  Type  |      Description      |
| --------- | ------ | --------------------- |
| `name`    | String | The string to encode. |

#### Returns

String

---

### File.isEncodingAvailable()

`File.isEncodingAvailable( name)`

#### Description

Checks whether a given encoding is available.

#### Parameters

| Parameter |  Type  |                                                                               Description                                                                                |
| --------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name`    | String | The encoding name. Typical values are `"ASCII"`, `"binary"`, or `"UTF-8"`. See [File- and Folder-supported encoding names](file-and-folder-supported-encoding-names.md). |

Boolean. `true` if your system supports the specified encoding, `false` otherwise.

---

### File.openDialog()

`File.openDialog([prompt="", filter="", multiSelect=false])`

#### Description

Opens the built-in platform-specific file-browsing dialog in which a user can select an existing file or multiple files, and creates new File objects to represent the selected files.

#### Parameters

+---------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
|   Parameter   |        Type        |                                                                     Description                                                                     |
+===============+====================+=====================================================================================================================================================+
| `prompt`      | String             | Optional. The prompt text, if the dialog allows a prompt.                                                                                           |
+---------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| `filter`      | String or Function | Optional. A filter that limits the types of files displayed in the dialog.                                                                          |
|               |                    |                                                                                                                                                     |
|               |                    | In Windows, a filter expression, such as `"JavaScript:*.jsx;All files:*.*"`                                                                         |
|               |                    |                                                                                                                                                     |
|               |                    | !!! tip                                                                                                                                             |
|               |                    |     - Separate expression with a semicolon (`;`) to filter by all these types at once; (show `jsx` AND `all`)                                       |
|               |                    |     - Separate with a comma (`,`) to populate the filter dropdown, to select one type at a time (show `jsx` OR `all`)                               |
|               |                    |                                                                                                                                                     |
|               |                    | In Mac OS, a filter function that takes a File instance and returns `true` if the file should be included in the display, `false` if it should not. |
+---------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| `multiSelect` | Boolean            | Optional. When `true`, the user can select multiple files and the return value is an array. Default is `false`.                                     |
+---------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+

#### Returns

The [File](#file-object) for the selected file, or an array of File Objects if multiple files are selected.

If the user cancels, returns `null`.

---

### File.saveDialog()

`File.saveDialog(prompt[, preset=""])`

#### Description

Opens the built-in platform-specific file-browsing dialog in which a user can select an existing file location to which to save information, and creates a new [File object](#file-object) to represent the selected file location.

#### Parameters

+-----------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Parameter |        Type        |                                                             Description                                                              |
+===========+====================+======================================================================================================================================+
| `prompt`  | String             | A string containing the prompt text, if the dialog allows a prompt.                                                                  |
+-----------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| `filter`  | String or Function | Optional. [Windows](../user-interface-tools/window-object.md) only. A filter that limits the types of files displayed in the dialog. |
|           |                    |                                                                                                                                      |
|           |                    | A filter expression, such as `"JavaScript:*.jsx;All files:*.*"`                                                                      |
|           |                    |                                                                                                                                      |
|           |                    | !!! tip                                                                                                                              |
|           |                    |     - Separate expression with a semicolon (`;`) to filter by all these types at once; (show `jsx` AND `all`)                        |
|           |                    |     - Separate with a comma (`,`) to populate the filter dropdown, to select one type at a time (show `jsx` OR `all`)                |
+-----------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------+

#### Returns

A [File](#file-object) for the the selected file location.

If the user cancels, returns `null`.

---

## File Object Attributes

These properties are available for `File` objects.

---

### File.absoluteURI

`fileObj.absoluteURI`

#### Description

The full path name for the referenced file in URI notation.

#### Type

String. Read only.

---

### File.alias

`fileObj.alias`

#### Description

When `true`, the object refers to a file system alias or shortcut.

#### Type

Boolean. Read only.

---

### File.created

`fileObj.created`

#### Description

The creation date of the referenced file, or `null` if the object does not refer to a file on disk.

#### Type

Date. Read only.

---

### File.creator

`fileObj.creator`

#### Description

In Mac OS, the file creator as a four-character string. In Windows or UNIX, value is `"????"`.

#### Type

String. Read only.

---

### File.displayName

`fileObj.displayName`

#### Description

The localized name of the referenced file, without the path.

#### Type

String. Read only.

---

### File.encoding

`fileObj.encoding`

#### Description

Gets or sets the encoding for subsequent read/write operations. One of the encoding constants listed in [File- and Folder-supported encoding names](file-and-folder-supported-encoding-names.md).

If the value is not recognized, uses the system default encoding.

A special encoder, `"BINARY"`, is used to read binary files. It stores each byte of the file as one Unicode character regardless of any encoding. When writing, the lower byte of each Unicode character is treated as a single byte to write.

#### Type

String

---

### File.eof

`fileObj.eof`

#### Description

When `true`, a read attempt caused the current position to be at the end of the file, or the file is not open.

#### Type

Boolean. Read only.

---

### File.error

`fileObj.error`

#### Description

A message describing the last file system error; see [File access error messages](file-access-error-messages.md).

Typically set by the file system, but a script can set it. Setting this value clears any error message and resets the error bit for opened files.

Contains the empty string if there is no error.

#### Type

String

---

### File.exists

`fileObj.exists`

#### Description

When `true`, this object refers to a file or file-system alias that actually exists in the file system.

#### Type

Boolean. Read only.

---

### File.fsName

`fileObj.fsName`

#### Description

The platform-specific full path name for the referenced file.

#### Type

String. Read only.

---

### File.fullName

`fileObj.fullName`

#### Description

The full path name for the referenced file in URI notation.

#### Type

String. Read only.

---

### File.hidden

`fileObj.hidden`

#### Description

When `true`, the file is not shown in the platform-specific file browser. Read/write. If the object references a file-system alias or shortcut, the flag is altered on the alias, not on the original file.

#### Type

Boolea

---

### File.length

`fileObj.length`

#### Description

The size of the file in bytes. Can be set only for a file that is not open, in which case it truncates or pads the file with 0-bytes to the new length.

#### Type

Number

---

### File.lineFeed

`fileObj.lineFeed`

#### Description

How line feed characters are written in the file system.

One of:

- `Windows` - Windows style
- `Macintosh` - Mac OS style
- `Unix` - UNIX style

#### Type

String

---

### File.localizedName

`fileObj.localizedName`

#### Description

A localized version of the file name portion of the absolute URI for the referenced file, without the path specification.

#### Type

String. Read only.

---

### File.modified

`fileObj.modified`

#### Description

The date of the referenced file's last modification, or null if the object does not refer to a file on disk.

#### Type

Date. Read only.

---

### File.name

`fileObj.name`

#### Description

The file name portion of the absolute URI for the referenced file, without the path specification.

#### Type

String. Read only.

---

### File.parent

`fileObj.parent`

#### Description

The Folder object for the folder that contains this file.

#### Type

Folder. Read only.

---

### File.path

`fileObj.path`

#### Description

The path portion of the absolute URI for the referenced file, without the file name.

#### Type

String. Read only.

---

### File.readonly

`fileObj.readonly`

#### Description

When `true`, prevents the file from being altered or deleted. If the referenced file is a file-system alias or shortcut, the flag is altered on the alias, not on the original file.

#### Type

Boolean

---

### File.relativeURI

`fileObj.relativeURI`

#### Description

The path name for the referenced file in URI notation, relative to the current folder.

#### Type

String. Read only.

---

### File.type

`fileObj.type`

#### Description

The file type as a four-character string.

- In Mac OS, the Mac OS file type.
- - In Windows, `"appl"` for `.EXE` files, `"shlb"` for `.DLL` files and `"TEXT"` for any other file.

If the file does not exist, the value is `"????"`.

#### Type

String. Read only.

---

## File Object Methods

These functions are available for File objects.

### File.changePath()

`fileObj.changePath(path)`

#### Description

Changes the path specification of the referenced file.

#### Parameters

| Parameter |  Type  |                        Description                        |
| --------- | ------ | --------------------------------------------------------- |
| `path`    | String | The new path, absolute or relative to the current folder. |

#### Returns

Boolean. `true` on success.

---

### File.close()

`fileObj.close()`

#### Description

Closes this open file.

#### Returns

Boolean. `true` on success, `false` if there are I/O errors.

---

### File.copy()

`fileObj.copy(target)`

#### Description

Copies this object's referenced file to the specified target location.

Resolves any aliases to find the source file. If a file exists at the target location, it is overwritten.

#### Parameters

| Parameter |                 Type                  |                                     Description                                     |
| --------- | ------------------------------------- | ----------------------------------------------------------------------------------- |
| `target`  | String or [File object](#file-object) | The URI path to the target location, or a File that references the target location. |

#### Returns

Boolean. `true` if the copy was successful, `false` otherwise.

---

### File.createAlias()

`fileObj.createAlias( [path])`

#### Description

Makes this file a file-system alias or shortcut to the specified file. The referenced file for this object must not yet exist on disk.

#### Parameters

| Parameter |  Type  |         Description          |
| --------- | ------ | ---------------------------- |
| `path`    | String | The path of the target file. |

#### Returns

Boolean. `true` if the operation was successful, `false` otherwise.

---

### File.execute()

`fileObj.execute()`

#### Description

Opens this file using the appropriate application, as if it had been double-clicked in a file browser.

You can use this method to run scripts, launch applications, and so on.

#### Returns

Boolean. `true` immediately if the application launch was successful.

---

### File.getRelativeURI()

`fileObj.getRelativeURI([basePath])`

#### Description

Retrieves the URI for this file, relative to the specified base path, in URI notation. If no base path is supplied, the URI is relative to the path of the current folder.

#### Parameters

| Parameter  |  Type  |                                           Description                                            |
| ---------- | ------ | ------------------------------------------------------------------------------------------------ |
| `basePath` | String | Optional. A string containing the base path for the relative URI. Default is the current folder. |

#### Returns

String

---

### File.open()

`fileObj.open(mode[, type][, creator])`

#### Description

Opens the referenced file for subsequent read/write operations. The method resolves any aliases to find the file.

The method attempts to detect the encoding of the open file. It reads a few bytes at the current location and tries to detect the Byte Order Mark character 0xFFFE. If found, the current position is advanced behind the detected character and the encoding property is set to one of the strings UCS-2BE, UCS-2LE, UCS4-BE, UCS-4LE, or UTF-8. If the marker character is not found, it checks for zero bytes at the current location and makes an assumption about one of the above formats (except UTF-8). If everything fails, the encoding property is set to the system encoding.

!!! warning
    Be careful about opening a file more than once. The operating system usually permits you to do so, but if you start writing to the file using two different File objects, you can destroy your data.

#### Parameters

+-----------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter |  Type  |                                                                   Description                                                                   |
+===========+========+=================================================================================================================================================+
| `mode`    | String | A string indicating the read/write mode. One of:                                                                                                |
|           |        |                                                                                                                                                 |
|           |        | - `r`: (read) Opens for reading. If the file does not exist or cannot be found, the call fails.                                                 |
|           |        | - `w`: (write) Opens a file for writing. If the file exists, its contents are destroyed. If the file does not exist, creates a new, empty file. |
|           |        | - `e`: (edit) Opens an existing file for reading and writing.                                                                                   |
|           |        | - `a`: (append) Opens the file in Append mode, and moves the current position to the end of the file.                                           |
+-----------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| `type`    | String | Optional. In Mac OS, the type of a newly created file, a 4-character string. Ignored in Windows and UNIX.                                       |
+-----------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| `creator` | String | Optional. In Mac OS, the creator of a newly created file, a 4-character string. Ignored in Windows and UNIX.                                    |
+-----------+--------+-------------------------------------------------------------------------------------------------------------------------------------------------+

#### Returns

Boolean. `true` if the file has been opened successfully, `false` otherwise.

---

### File.openDlg()

`fileObj.openDlg([prompt=""][, filter=""][, multiSelect=false])`

#### Description

Opens the built-in platform-specific file-browsing dialog, in which the user can select an existing file or files, and creates new File objects to represent the selected files. Differs from the class method openDialog() in that it presets the current folder to this File object's parent folder and the current file to this object's associated file.

#### Parameters

+---------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
|   Parameter   |        Type        |                                                                     Description                                                                     |
+===============+====================+=====================================================================================================================================================+
| `prompt`      | String             | Optional. The prompt text, if the dialog allows a prompt.                                                                                           |
+---------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| `filter`      | String or Function | Optional. A filter that limits the types of files displayed in the dialog.                                                                          |
|               |                    |                                                                                                                                                     |
|               |                    | In Windows, a filter expression, such as `"JavaScript:*.jsx;All files:*.*"`                                                                         |
|               |                    |                                                                                                                                                     |
|               |                    | !!! tip                                                                                                                                             |
|               |                    |     - Separate expression with a semicolon (`;`) to filter by all these types at once; (show `jsx` AND `all`)                                       |
|               |                    |     - Separate with a comma (`,`) to populate the filter dropdown, to select one type at a time (show `jsx` OR `all`)                               |
|               |                    |                                                                                                                                                     |
|               |                    | In Mac OS, a filter function that takes a File instance and returns `true` if the file should be included in the display, `false` if it should not. |
+---------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| `multiSelect` | Boolean.           | Optional. When `true`, the user can select multiple files and the return value is an array. Default is `false`.                                     |
+---------------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+

#### Returns

If the user clicks **OK**, returns a [File](#file-object) or [Folder object](./folder-object.md) for the selected file or folder, or an array of objects.

If the user cancels, returns `null`.

---

### File.read()

`fileObj.read([chars])`

#### Description

Reads the contents of the file starting at the current position.

Returns a string that contains up to the specified number of characters.

#### Parameters

| Parameter |  Type  |                                                                                                           Description                                                                                                           |
| --------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `chars`   | Number | Optional. An integer specifying the number of characters to read. By default, reads from the current position to the end of the file. If the file is encoded, multiple bytes might be read to create single Unicode characters. |

#### Returns

String

---

### File.readch()

`fileObj.readch()`

#### Description

Reads a single text character from the file at the current position. Line feeds are recognized as CR, LF, CRLF, or LFCR pairs. If the file is encoded, multiple bytes might be read to create single Unicode characters.

Returns a string that contains the character.

#### Returns

String

---

### File.readln()

`fileObj.readln()`

#### Description

Reads a single line of text from the file at the current position, and returns it in a string. Line feeds are recognized as CR, LF, CRLF, or LFCR pairs. If the file is encoded, multiple bytes might be read to create single Unicode characters.

Returns a string that contains the text.

#### Returns

String

---

### File.remove()

`fileObj.remove()`

#### Description

Deletes the file associated with this object from disk, immediately, without moving it to the system trash.

Does not resolve aliases; instead, deletes the referenced alias or shortcut file itself.

!!! warning
    Cannot be undone. It is recommended that you prompt the user for permission before deleting.

#### Returns

Boolean. `true` if the file is deleted successfully.

---

### File.rename()

`fileObj.rename(newName)`

#### Description

Renames the associated file.

Does not resolve aliases, but renames the referenced alias or shortcut file itself.

#### Parameters

| Parameter |  Type  |           Description            |
| --------- | ------ | -------------------------------- |
| `newName` | String | The new file name, with no path. |

#### Returns

Boolean. `true` on success.

---

### File.resolve()

`fileObj.resolve()`

#### Description

If this object references an alias or shortcut, this method resolves that alias and returns a new File object that references the file-system element to which the alias resolves.

#### Returns

The new [File object](#file-object), or `null` if this object does not reference an alias, or if the alias cannot be resolved.

---

### File.saveDlg()

`fileObj.saveDlg([prompt=""][, preset=""])`

#### Description

Opens the built-in platform-specific file-browsing dialog, in which the user can select an existing file location to which to save information, and creates a new File object to represent the selected file.

Differs from the class method [saveDialog()](#file-savedialog) in that it presets the current folder to this File object's parent folder and the file to this object's associated file.

#### Parameters

+-----------+--------------------+-----------------------------------------------------------------------------------------------------------------------+
| Parameter |        Type        |                                                      Description                                                      |
+===========+====================+=======================================================================================================================+
| `prompt`  | String             | Optional. The prompt text, if the dialog allows a prompt.                                                             |
+-----------+--------------------+-----------------------------------------------------------------------------------------------------------------------+
| `filter`  | String or Function | Optional. A filter that limits the types of files displayed in the dialog.                                            |
|           |                    |                                                                                                                       |
|           |                    | In Windows, a filter expression, such as `"JavaScript:*.jsx;All files:*.*"`                                           |
|           |                    |                                                                                                                       |
|           |                    | !!! tip                                                                                                               |
|           |                    |     - Separate expression with a semicolon (`;`) to filter by all these types at once; (show `jsx` AND `all`)         |
|           |                    |     - Separate with a comma (`,`) to populate the filter dropdown, to select one type at a time (show `jsx` OR `all`) |
|           |                    |                                                                                                                       |
|           |                    | Not used in MacOS                                                                                                     |
+-----------+--------------------+-----------------------------------------------------------------------------------------------------------------------+

#### Returns

The [File object](#file-object) for the selected file.

If the user cancels, returns `null`.

---

### File.seek()

`fileObj.seek(pos[, mode=0])`

#### Description

Seeks to the specified position in the file. The new position cannot be less than 0 or greater than the current file size.

#### Parameters

+-----------+--------+-----------------------------------------------------------------------------------------------------------------------------+
| Parameter |  Type  |                                                         Description                                                         |
+===========+========+=============================================================================================================================+
| `pos`     | Number | The new current position in the file as an offset in bytes from the start, current position, or end, depending on the mode. |
+-----------+--------+-----------------------------------------------------------------------------------------------------------------------------+
| `mode`    | Number | Optional. The seek mode, one of:                                                                                            |
|           |        |                                                                                                                             |
|           |        | - `0`: Seek to absolute position, where pos=0 is the first byte of the file. This is the default.                           |
|           |        | - `1`: Seek relative to the current position.                                                                               |
|           |        | - `2`: Seek backward from the end of the file.                                                                              |
+-----------+--------+-----------------------------------------------------------------------------------------------------------------------------+


#### Returns

Boolean. `true` if the position was changed.

---

### File.tell()

`fileObj.tell()`

#### Description

Retrieves the current position index as a byte offset from the start of the file.

#### Returns

Number

---

### File.write()

`fileObj.write( text[, text...]...)`

#### Description

Writes the specified text to the file at the current position. For encoded files, writing a single Unicode character may write multiple bytes.

!!! warning
    Be careful not to write to a file that is open in another application or object, as this can overwrite existing data.

#### Parameters

| Parameter |  Type  |                                  Description                                  |
| --------- | ------ | ----------------------------------------------------------------------------- |
| `text`    | String | One or more strings to write, which are concatenated to form a single string. |

#### Returns

Boolean. `true` on success.

---

### File.writeln()

`fileObj.writeln (text[, text...]...)`

#### Description

Writes the specified text to the file at the current position, and appends a Line Feed sequence in the style specified by the linefeed property.For encoded files, writing a single Unicode character may write multiple bytes.

!!! warning
    Be careful not to write to a file that is open in another application or object, as this can overwrite existing data.

#### Parameters

| Parameter |  Type  |                                  Description                                  |
| --------- | ------ | ----------------------------------------------------------------------------- |
| `text`    | String | One or more strings to write, which are concatenated to form a single string. |

#### Returns

Boolean. `true` on success.
