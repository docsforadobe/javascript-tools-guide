# Using File and Folder objects

Because path name syntax is very different on Windows, Mac OS, and UNIX®, Adobe ExendScript defines
the `File` and `Folder` objects to provide platform-independent access to the underlying file system. A
File object represents a disk file, a Folder object represents a directory or folder.

- The `Folder` object supports file system functionality such as traversing the hierarchy; creating,
  renaming or removing files; or resolving file aliases.
- The `File` object supports input/output functions to read or write files.

There are several ways to distinguish between a File and a Folder object. For example:

```default
if ( f instanceof File ) ...
if ( typeof f.open == "undefined" ) ... // Folders do not open
```

File and Folder objects can be used anywhere that a path name is required, such as in properties and
arguments for files and folders.

!!! note
    When you create two File objects that refer to the same disk file, they are treated as distinct
objects. If you open one of them for I/O, the operating system may inhibit access from the other object,
because the disk file already is open.

---

## Specifying paths

When creating a File or Folder object, you can specify a platform-specific path name, or an absolute or
relative path in a platform-independent format known as universal resource identifier (URI) notation. The
path stored in the object is always an absolute, full path name that points to a fixed location on the disk.

- Use the toString method to obtain the name of the file or folder as string containing an absolute
  path name in URI notation.
- Use the `fsName` property to obtain the platform-specific file name.

### Absolute and relative path names

An absolute path name in URI notation describes the full path from a root directory down to a specific file
or folder. It starts with one or two slashes (`/`), and a slash separates path elements. For example, the
following describes an absolute location for the file `myFile.jsx`:

```default
/dir1/dir2/mydir/myFile.jsx
```

A relative path name in URI notation is appended to the path of the current directory, as stored in the
globally available `current` property of the Folder class. It starts with a folder or file name, or with one of
the special names dot (`.`) for the current directory, or dot dot (`..`) for the parent of the current directory. A
slash (`/`) separates path elements. For example, the following paths describe various relative locations for
the file `myFile.jsx`:

| myFile.jsx         | In the current directory.                            |
|--------------------|------------------------------------------------------|
| ./myFile.jsx       |                                                      |
| ../myFile.jsx      | In the parent of the current directory.              |
| ../../myFile.jsx   | In the grandparent of the current directory.         |
| ../dir1/myFile.jsx | In dir1, which is parallel to the current directory. |

Relative path names are independent of different volume names on different machines and operating
systems, and therefore make your code considerably more portable. You can, for example, use an absolute
path for a single operation, to set the current directory in the Folder.current property, and use relative
paths for all other operations. You would then need only a single code change to update to a new platform
or file location.

### Character interpretation in paths

There are some platform differences in how pathnames are interpreted:

- On Windows and Mac OS, path names are not case sensitive. In UNIX, paths are case sensitive.
- On Windows, both the slash (`/`) and the backslash (`\`) are valid path element separators. Backslash is
  the escape character, so you must use a double backslash (`\\`) to indicate the character.
- On Mac OS, both the slash (`/`) and the colon (`:`) are valid path element separators.

If a path name starts with two slashes (or backslashes on Windows), the first element refers to a remote
server. For example, `//myhost/mydir/myfile` refers to the path `/mydir/myfile` on the server myhost.

URI notation allows special characters in pathnames, but they must specified with an escape character (%)
followed by a hexadecimal character code. Special characters are those which are not alphanumeric and
not one of the characters:

```default
/ - - . ! ~ * ' ( )
```

A space, for example, is encoded as `%20`, so the file name `"my file"` is specified as `"my%20file"`. Similarly,
the character `ä` is encoded as `%E4`, so the file name `"Bräun"` is specified as `"Br%E4un"`.

This encoding scheme is compatible with the global JavaScript functions `encodeURI` and `decodeURI`.

### The home directory

A path name can start with a tilde (`~`) to indicate the user's home directory. It corresponds to the platform's
`HOME` environment variable.

UNIX and Mac OS assign the HOME environment variable according to the user login. On Mac OS, the
default home directory is `/Users/username`. In UNIX, it is typically `/home/username` or `/users/username.`
ExtendScript assigns the home directory value directly from the platform value.

On Windows, the `HOME` environment variable is optional. If it is assigned, its value must be a Windows path
name or a path name referring to a remote server (such as `\\myhost\mydir`). If the `HOME` environment
variable is undefined, the ExtendScript default is the user's home directory, usually the `C:\Users\username` folder.

!!! note
    A script can access many of the folders that are specified with platform-specific variables through
static, globally available Folder class properties; for instance, `appData` contains the folder that stores
application data for all users.

### Volume and drive names

A volume or drive name can be the first part of an absolute path in URI notation. The values are interpreted
according to the platform.

#### Mac OS volumes

When Mac OS X starts, the startup volume is the root directory of the file system. All other volumes,
including remote volumes, are part of the /Volumes directory. The File and Folder objects use these
rules to interpret the first element of a path name:

- If the name is the name of the startup volume, discard it.
- If the name is a volume name, prepend `/Volumes`.
- Otherwise, leave the path as is.

Mac OS 9 is not supported as an operating system, but the use of the colon as a path separator is still
supported and corresponds to URI and to Mac OS X paths as shown in the following table. These examples
assume that the startup volume is `MacOSX`, and that there is a mounted volume `Remote`.

| URI path name    | Mac OS 9 path name   | Mac OS X path name       |
|------------------|----------------------|--------------------------|
| /MacOSX/dir/file | MacOSX:dir:file      | /dir/file                |
| /Remote/dir/file | Remote:dir:file      | /Volumes/Remote/dir/file |
| /root/dir/file   | Root:dir:file        | /root/dir/file           |
| ~/dir/file       |                      | /Users/jdoe/dir/file     |

#### Windows drives

On Windows, volume names correspond to drive letters. The URI path /c/temp/file normally translates
to the Windows path `C:\temp\file`.

If a drive exists with a name matching the first part of the path, that part is always interpreted as that drive.
It is possible for there to be a folder in the root that has the same name as the drive; imagine, for example,
a folder `C:\C` on Windows. A path starting with /c always addresses the drive `C:`, so in this case, to access
the folder by name, you must use both the drive name and the folder name, for example `/c/c` for `C:\C`.

If the current drive contains a root folder with the same name as another drive letter, that name is
considered to be a folder. That is, if there is a folder `D:\C`, and if the current drive is `D:`, the URI path
`/c/temp/file` translates to the Windows path `D:\c\temp\file`. In this case, to access drive `C`, you would
have to use the Windows path name conventions.

To access a remote volume, use a uniform naming convention (UNC) path name of the form
`//servername/sharename`. These path names are portable, because both Max OS X and UNIX ignore
multiple slash characters. Note that on Windows, UNC names do not work for local volumes.
These examples assume that the current drive is `D:`

| URI path name    | Windows path name          |
|------------------|----------------------------|
| /c/dir/file      | c:\\dir\\file              |
| /remote/dir/file | D:\\remote\\dir\\file      |
| /root/dir/file   | D:\\root\\dir\\file        |
| ~/dir/file       | C:\\Users\\jdoe\\dir\\file |

### Aliases

When you access an alias, the operation is transparently forwarded to the real file. The only operations that
affect the alias are calls to `rename` and `remove`, and setting properties `readonly` and `hidden`. When a File
object represents an alias, the `alias` property of the object returns true, and the `resolve` method returns
the File or Folder object for the target of the alias.

On Windows, all file system aliases (called shortcuts) are actual files whose names end with the extension
`.lnk`. Never use this extension directly; the File and Folder objects work without it.

For example, suppose there is a shortcut to the file `/folder1/some.txt` in the folder `/folder2`. The full
Windows file name of the shortcut file is `\folder2\some.txt.lnk`.

To access the shortcut from a File object, specify the path `/folder2/some.txt`. Calling that File object's
open method opens the linked file (in `/folder1`). Calling the File object's `rename` method renames the
shortcut file itself (leaving the `.lnk` extension intact).

However, Windows permits a file and its shortcut to reside in the same folder. In this case, the File object
always accesses the original file. You cannot create a File object to access the shortcut when it is in the
same folder as its linked file.

A script can create a file alias by creating a File object for a file that does not yet exist on disk, and using its
createAlias method to specify the target of the alias.

### Portability issues

If your application will run on multiple platforms, use relative path names, or try to originate path names
from the home directory. If that is not possible, work with Mac OS X and UNIX aliases, and store your files
on a machine that is remote to your Windows machine so that you can use UNC names.

As an example, suppose you use the UNIX machine myServer for data storage. If you set up an alias share
in the root directory of `myServer`, and if you set up a Windows-accessible share at share pointing to the
same data location, the path name `//myServer/share/file` would work for all three platforms.

---

## Unicode I/O

When doing file I/O, Adobe applications convert 8-bit character encoding to Unicode. By default, this
conversion process assumes that the system encoding is used (code page 1252 on Windows or Mac
Roman on Mac OS). The `encoding` property of a File object returns the current encoding. You can set the
encoding property to the name of the desired encoding. The File object looks for the corresponding
encoder in the operating system to use for subsequent I/O. The name is one of the standard Internet
names that are used to describe the encoding of HTML files, such as `ASCII`, `X-SJIS`, or `ISO-8859-1`. For a
complete list, see [File- and Folder-supported encoding names](file-and-folder-supported-encoding-names.md#file-and-folder-supported-encoding-names).

A special encoder, `BINARY`, is provided for binary I/O. This encoder simply extends every 8-bit character it
finds to a Unicode character between 0 and 255. When using this encoder to write binary files, the encoder
writes the lower 8 bits of the Unicode character. For example, to write the Unicode character `1000`, which is
`0x3E8`, the encoder actually writes the character 232 (`0xE8`).

The data of some of the common file formats (UCS-2, UCS-4, UTF-8, UTF-16) starts with a special byte order
mark (BOM) character (`\uFEFF`). The `File.open` method reads a few bytes of a file looking for this
character. If it is found, the corresponding encoding is set automatically and the character is skipped. If
there is no BOM character at the beginning of the file, open() reads the first 2 KB of the file and checks
whether the data might be valid UTF-8 encoded data, and if so, sets the encoding to UTF-8.

To write 16-bit Unicode files in UTF-16 format, use the encoding UCS-2. This encoding uses whatever
byte-order format the host platform supports.

When using UTF-8 encoding or 16-bit Unicode, always write the BOM character `"\uFEFF"` as the first
character of the file.

---

## File error handling

Each object has an `error` property. If accessing a property or calling a method causes an error, this
property contains a message describing the type of the error. On success, the property contains the empty
string. You can set the property, but setting it only causes the error message to be cleared. If a file is open,
assigning an arbitrary value to the property also resets its error flag.

For a complete list of supported error messages, see [File access error messages](file-access-error-messages.md#file-access-error-messages).
