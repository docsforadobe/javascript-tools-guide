<a id="file-object"></a>

# File object

Represents a file in the local file system in a platform-independent manner. All properties and methods
resolve file system aliases automatically and act on the original file unless otherwise noted.

---

<a id="file-object-constructors"></a>

## File object constructors

To create a File object, use the File function or the new operator. The constructor accepts full or partial
path names, and returns the new object. The CRLF sequence for the file is preset to the system default, and
the encoding is preset to the default system encoding.

```default
File ( [ path ] ); // Can return a Folder object
new File ([ path ] ); // Always returns a File object
```

| `path`   | Optional. The absolute or relative path to the file associated with this object, specified in<br/>platform-specific or URI format; see [Specifying paths](using-file-and-folder-objects.md#specifying-paths). The value stored in the<br/>object is the absolute path.<br/><br/>The path need not refer to an existing file. If not supplied, a temporary name is generated.<br/><br/>If the path refers to an existing folder:<br/><br/>- The File function returns a Folder object instead of a File object.<br/>- The new operator returns a File object for a nonexisting file with the same name.   |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### WARNING
In After Effects on MacOS, if `path.length` is more than 1002, After Effects crashes.
This has been reported on MacOS 10.11.6 and After Effects 13.8 and 14.0.

---

<a id="file-class-properties"></a>

## File class properties

This property is available as a static property of the File class. It is not necessary to create an instance to
access it.

| **fs**   | String   | The name of the file system. Read only. One of `Windows`, `Macintosh`, or `Unix`.   |
|----------|----------|-------------------------------------------------------------------------------------|

---

<a id="file-class-functions"></a>

## File class functions

These functions are available as static methods of the File class. It is not necessary to create an instance to
call them.

<a id="file-decode"></a>

### decode()

`File.decode( uri )`

| `uri`   | String. The encoded string to decode. All special characters must be encoded in<br/>UTF-8 and stored as escaped characters starting with the percent sign followed by<br/>two hexadecimal digits. For example, the string `"my%20file"` is decoded as `"my<br/>file"`.   |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Special characters are those with a numeric value greater than 127, except the following:

```default
/ - _ . ! ~ * ' ( )
```

Decodes the specified string as required by RFC 2396.

Returns the decoded string.

<a id="file-encode"></a>

### encode()

`File.encode( name )`

| `name`   | String. The string to encode.   |
|----------|---------------------------------|

Encodes the specified string as required by RFC 2396. All special characters are encoded in UTF-8
and stored as escaped characters starting with the percent sign followed by two hexadecimal digits.
For example, the string “my file” is encoded as “my%20file”.
Special characters are those with a numeric value greater than 127, except the following:

```default
/ - _ . ! ~ * ' ( )
```

Returns the encoded string.

<a id="file-isencodingavailable"></a>

### isEncodingAvailable()

`File.isEncodingAvailable( name )`

| `name`   | String. The encoding name. Typical values are “ASCII,” “binary,” or “UTF-8.”<br/>See [File- and Folder-supported encoding names](file-and-folder-supported-encoding-names.md#file-and-folder-supported-encoding-names).   |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Checks whether a given encoding is available.
Returns true if your system supports the specified encoding, false otherwise.

<a id="file-opendialog"></a>

### openDialog()

`File.openDialog( [prompt, filter, multiSelect] )`

| `prompt`      | Optional. A string containing the prompt text, if the dialog allows a prompt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `filter`      | Optional. A filter that limits the types of files displayed in the dialog.<br/><br/>> - In Windows, a filter expression, such as `"JavaScript:*.jsx;All files:*.*"`<br/><br/>>   #### NOTE<br/>>   - Separate expression with a semicolon (`;`) to filter by all these types at once; (show `jsx` AND `all`)<br/>>   - Separate with a comma (`,`) to populate the filter dropdown, to select one type at a time (show `jsx` OR `all`)<br/>> - In Mac OS, a filter function that takes a File instance and returns true if the file<br/>>   should be included in the display, false if it should not. |
| `multiSelect` | Optional. Boolean. When true, the user can select multiple files and the return<br/>value is an array. Default is false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

Opens the built-in platform-specific file-browsing dialog in which a user can select an existing file or
multiple files, and creates new File objects to represent the selected files.

If the user clicks **OK**, returns a File object for the selected file, or an array of objects if multiple files
are selected. If the user cancels, returns `null`.

<a id="file-savedialog"></a>

### saveDialog()

`File.saveDialog( prompt[, preset] )`

| `prompt`   | A string containing the prompt text, if the dialog allows a prompt.                                                                                                                                                                                                                                                                                                                                                                            |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `filter`   | Optional, in Windows only. A filter that limits the types of files displayed in the<br/>dialog. A filter expression, such as `"JavaScript:*.jsx;All files:*.*"`<br/>Not used in Mac OS.<br/><br/>#### NOTE<br/>- Separate expression with a semicolon (`;`) to filter by all these types at once; (show `jsx` AND `all`)<br/>- Separate with a comma (`,`) to populate the filter dropdown, to select one type at a time (show `jsx` OR `all`) |

Opens the built-in platform-specific file-browsing dialog in which a user can select an existing file
location to which to save information, and creates a new File object to represent the selected file
location.

If the user clicks **OK**, returns a File object for the selected file location. If the user cancels, returns
`null`.

---

<a id="file-object-properties"></a>

## File object properties

These properties are available for `File` objects.

| **absoluteURI**   | String   | The full path name for the referenced file in URI notation. Read only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **alias**         | Boolean  | When true, the object refers to a file system alias or shortcut. Read only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **created**       | Date     | The creation date of the referenced file, or null if the object does not<br/>refer to a file on disk. Read only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **creator**       | String   | In Mac OS, the file creator as a four-character string. In Windows or UNIX,<br/>value is “????”. Read only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **displayName**   | String   | The localized name of the referenced file, without the path. Read only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **encoding**      | String   | Gets or sets the encoding for subsequent read/write operations. One of<br/>the encoding constants listed in [File- and Folder-supported encoding names](file-and-folder-supported-encoding-names.md#file-and-folder-supported-encoding-names).<br/>If the value is not recognized, uses the system default encoding.<br/><br/>A special encoder, BINARY, is used to read binary files. It stores each byte<br/>of the file as one Unicode character regardless of any encoding. When<br/>writing, the lower byte of each Unicode character is treated as a single<br/>byte to write. |
| **eof**           | Boolean  | When true, a read attempt caused the current position to be at the end of<br/>the file, or the file is not open. Read only.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **error**         | String   | A message describing the last file system error; see [File access error messages](file-access-error-messages.md#file-access-error-messages).<br/>Typically set by the file system, but a script can set<br/>it. Setting this value clears any error message and resets the error bit for<br/>opened files. Contains the empty string if there is no error.                                                                                                                                                                                                                           |
| **exists**        | Boolean  | When true, this object refers to a file or file-system alias that actually<br/>exists in the file system. Read only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **fsName**        | String   | The platform-specific full path name for the referenced file. Read only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **fullName**      | String   | The full path name for the referenced file in URI notation. Read only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **hidden**        | Boolean  | When true, the file is not shown in the platform-specific file browser.<br/>Read/write. If the object references a file-system alias or shortcut, the flag<br/>is altered on the alias, not on the original file.                                                                                                                                                                                                                                                                                                                                                                    |
| **length**        | Number   | The size of the file in bytes. Can be set only for a file that is not open, in<br/>which case it truncates or pads the file with 0-bytes to the new length.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **lineFeed**      | String   | How line feed characters are written in the file system. One of:<br/>`Windows` - Windows style<br/>`Macintosh` - Mac OS style<br/>`Unix` - UNIX style                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **localizedName** | String   | A localized version of the file name portion of the absolute URI for the<br/>referenced file, without the path specification. Read only.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **modified**      | Date     | The date of the referenced file’s last modification, or null if the object<br/>does not refer to a file on disk. Read only.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **name**          | String   | The file name portion of the absolute URI for the referenced file, without<br/>the path specification. Read only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **parent**        | Folder   | The Folder object for the folder that contains this file. Read only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **path**          | String   | The path portion of the absolute URI for the referenced file, without the<br/>file name. Read only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **readonly**      | Boolean  | When true, prevents the file from being altered or deleted. If the<br/>referenced file is a file-system alias or shortcut, the flag is altered on the<br/>alias, not on the original file.                                                                                                                                                                                                                                                                                                                                                                                           |
| **relativeURI**   | String   | The path name for the referenced file in URI notation, relative to the<br/>current folder. Read only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **type**          | String   | The file type as a four-character string.<br/><br/>- In Mac OS, the Mac OS file type.<br/>- In Windows, `"appl"` for `.EXE` files, `"shlb"` for `.DLL` files and `"TEXT"`<br/>  for any other file.<br/><br/>If the file does not exist, the value is “????”. Read only.                                                                                                                                                                                                                                                                                                             |

---

<a id="file-object-functions"></a>

## File object functions

These functions are available for File objects.

<a id="file-changepath"></a>

### changePath()

`fileObj.changePath( path )`

| `path`   | A string containing the new path, absolute or relative to the current folder.   |
|----------|---------------------------------------------------------------------------------|

Changes the path specification of the referenced file.

Returns true on success.

<a id="file-close"></a>

### close()

`fileObj.close()`

Closes this open file.

Returns true on success, false if there are I/O errors.

<a id="file-copy"></a>

### copy()

`fileObj.copy( target )`

| `target`   | A string with the URI path to the target location, or a File object<br/>that references the target location.   |
|------------|----------------------------------------------------------------------------------------------------------------|

Copies this object’s referenced file to the specified target location. Resolves any aliases to find the
source file. If a file exists at the target location, it is overwritten.

Returns true if the copy was successful, false otherwise.

<a id="file-createalias"></a>

### createAlias()

`fileObj.createAlias( [path] )`

| `path`   | A string containing the path of the target file.   |
|----------|----------------------------------------------------|

Makes this file a file-system alias or shortcut to the specified file. The referenced file for this object
must not yet exist on disk.

Returns true if the operation was successful, false otherwise.

<a id="file-execute"></a>

### execute()

`fileObj.execute()`

Opens this file using the appropriate application, as if it had been double-clicked in a file browser.
You can use this method to run scripts, launch applications, and so on.

Returns true immediately if the application launch was successful.

<a id="file-getrelativeuri"></a>

### getRelativeURI()

`fileObj.getRelativeURI( [basePath] )`

| `basePath`   | Optional. A string containing the base path for the relative URI.<br/>Default is the current folder.   |
|--------------|--------------------------------------------------------------------------------------------------------|

Retrieves the URI for this file, relative to the specified base path, in URI notation. If no base path is
supplied, the URI is relative to the path of the current folder.

Returns a string containing the relative URI.

<a id="file-open"></a>

### open()

`fileObj.open( mode [,type] [,creator] )`

| `mode`   | A string indicating the read/write mode. One of:<br/>: - `r`: (read) Opens for reading. If the file does not exist<br/>    or cannot be found, the call fails.<br/>  - `w`: (write) Opens a file for writing. If the file exists,<br/>    its contents are destroyed. If the file does not exist,<br/>    creates a new, empty file.<br/>  - `e`: (edit) Opens an existing file for reading and writing.<br/>  - `a`: (append) Opens the file in Append mode, and moves the<br/>    current position to the end of the file.<br/>  - `type`: Optional. In Mac OS, the type of a newly created file,<br/>    a 4-character string. Ignored in Windows and UNIX.<br/>  - `creator`: Optional. In Mac OS, the creator of a newly created file,<br/>    a 4-character string. Ignored in Windows and UNIX.   |
|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Opens the referenced file for subsequent read/write operations. The method resolves any aliases to
find the file.

Returns true if the file has been opened successfully, false otherwise.

The method attempts to detect the encoding of the open file. It reads a few bytes at the current
location and tries to detect the Byte Order Mark character 0xFFFE. If found, the current position is
advanced behind the detected character and the encoding property is set to one of the strings
UCS-2BE, UCS-2LE, UCS4-BE, UCS-4LE, or UTF-8. If the marker character is not found, it checks for
zero bytes at the current location and makes an assumption about one of the above formats (except
UTF-8). If everything fails, the encoding property is set to the system encoding.

#### NOTE
Be careful about opening a file more than once. The operating system usually permits you to
do so, but if you start writing to the file using two different File objects, you can destroy your data.

<a id="file-opendlg"></a>

### openDlg()

`fileObj.openDlg( [prompt][,filter][,multiSelect] )`

| `prompt`      | Optional. A string containing the prompt text, if the dialog allows a prompt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `filter`      | Optional. A filter that limits the types of files displayed in the dialog.<br/>: - In Windows, a filter expression, such as `"JavaScript:*.jsx;All files:*.*"`<br/>  <br/><br/>  #### NOTE<br/>  - Separate expression with a semicolon (`;`) to filter by all these types at once; (show `jsx` AND `all`)<br/>  - Separate with a comma (`,`) to populate the filter dropdown, to select one type at a time (show `jsx` OR `all`)<br/>  <br/><br/>  - In Mac OS, a filter function that takes a File instance and returns true if the file<br/>    should be included in the display, false if it should not. |
| `multiSelect` | Optional. Boolean. When true, the user can select multiple files and the return value is an array. Default is false.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

Opens the built-in platform-specific file-browsing dialog, in which the user can select an existing file
or files, and creates new File objects to represent the selected files. Differs from the class method
openDialog() in that it presets the current folder to this File object’s parent folder and the current
file to this object’s associated file.

If the user clicks **OK**, returns a File or Folder object for the selected file or folder, or an array of
objects. If the user cancels, returns `null`.

<a id="file-read"></a>

### read()

`fileObj.read( [chars] )`

| `chars`   | Optional. An integer specifying the number of characters to read. By default, reads<br/>from the current position to the end of the file. If the file is encoded, multiple bytes<br/>might be read to create single Unicode characters.   |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Reads the contents of the file starting at the current position.

Returns a string that contains up to the specified number of characters.

<a id="file-readch"></a>

### readch()

`fileObj.readch()`

Reads a single text character from the file at the current position. Line feeds are recognized as CR, LF,
CRLF, or LFCR pairs. If the file is encoded, multiple bytes might be read to create single Unicode
characters.

Returns a string that contains the character.

<a id="file-readln"></a>

### readln()

`fileObj.readln()`

Reads a single line of text from the file at the current position, and returns it in a string. Line feeds
are recognized as CR, LF, CRLF, or LFCR pairs. If the file is encoded, multiple bytes might be read to
create single Unicode characters.

Returns a string that contains the text.

<a id="file-remove"></a>

### remove()

`fileObj.remove()`

Deletes the file associated with this object from disk, immediately, without moving it to the system
trash. Does not resolve aliases; instead, deletes the referenced alias or shortcut file itself.

#### NOTE
Cannot be undone. It is recommended that you prompt the user for permission before deleting.

Returns true if the file is deleted successfully.

<a id="file-rename"></a>

### rename()

`fileObj.rename( newName )`

| `newName`   | The new file name, with no path.   |
|-------------|------------------------------------|

Renames the associated file. Does not resolve aliases, but renames the referenced alias or shortcut
file itself.

Returns true on success.

<a id="file-resolve"></a>

### resolve()

`fileObj.resolve()`

If this object references an alias or shortcut, this method resolves that alias and returns a new File
object that references the file-system element to which the alias resolves.

Returns the new File object, or null if this object does not reference an alias, or if the alias cannot
be resolved.

<a id="file-savedlg"></a>

### saveDlg()

`fileObj.saveDlg( [prompt][, preset] )`

| `prompt`   | Optional. A string containing the prompt text, if the dialog allows a prompt.                                                                                                                                                                                                                                                                                                                                                                  |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `preset`   | Optional, in Windows only. A filter that limits the types of files displayed in the<br/>dialog. A filter expression, such as `"JavaScript:*.jsx;All files:*.*"`<br/>Not used in Mac OS.<br/><br/>#### NOTE<br/>- Separate expression with a semicolon (`;`) to filter by all these types at once; (show `jsx` AND `all`)<br/>- separate with a comma (`,`) to populate the filter dropdown, to select one type at a time (show `jsx` OR `all`) |

Opens the built-in platform-specific file-browsing dialog, in which the user can select an existing file
location to which to save information, and creates a new File object to represent the selected file.

Differs from the class method [saveDialog()](#file-savedialog) in that it presets the current folder to this File object’s
parent folder and the file to this object’s associated file.

If the user clicks **OK**, returns a File object for the selected file. If the user cancels, returns `null`.

<a id="file-seek"></a>

### seek()

`fileObj.seek( pos[, mode] )`

| `pos`   | The new current position in the file as an offset in bytes from the start, current<br/>position, or end, depending on the mode.                                                                                                                                |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `mode`  | Optional. The seek mode, one of:<br/><br/>> - `0`: Seek to absolute position, where pos=0 is the first byte of the file. This is the<br/>>   default.<br/>> - `1`: Seek relative to the current position.<br/>> - `2`: Seek backward from the end of the file. |

Seeks to the specified position in the file. The new position cannot be less than 0 or greater than the
current file size.

Returns true if the position was changed.

<a id="file-tell"></a>

### tell()

`fileObj.tell()`

Retrieves the current position as a byte offset from the start of the file.

Returns a number, the position index.

<a id="file-write"></a>

### write()

`fileObj.write( text[, text...]... )`

| `text`   | One or more strings to write, which are concatenated to form a single string.   |
|----------|---------------------------------------------------------------------------------|

Writes the specified text to the file at the current position. For encoded files, writing a single
Unicode character may write multiple bytes.

#### NOTE
Be careful not to write to a file that is open in another application or object, as this can
overwrite existing data.

Returns true on success.

<a id="file-writeln"></a>

### writeln()

`fileObj.writeln (text[, text...]...)`

| `text`   | One or more strings to write, which are concatenated to form a single string.   |
|----------|---------------------------------------------------------------------------------|

Writes the specified text to the file at the current position, and appends a Line Feed sequence in the
style specified by the linefeed property.For encoded files, writing a single Unicode character may
write multiple bytes.

#### NOTE
Be careful not to write to a file that is open in another application or object, as this can
overwrite existing data.

Returns true on success.
