.. _file-access-error-messages:

File access error messages
==========================
The following messages can be returned in the error property.

================================= ================================================================
File or folder does not exist     The file or folder does not exist, but the parent folder exists.
File or folder already exists     The file or folder already exists.
I/O device is not open            An I/O operation was attempted on a file that was closed.
Read past EOF                     Attempt to read beyond the end of a file.
Conversion error                  The content of the file cannot be converted to Unicode.
Partial multibyte character found The character encoding of the file data has errors.
Permission denied                 The OS did not allow the attempted operation.
Cannot change directory           Cannot change the current folder.
Cannot create                     Cannot create a folder.
Cannot rename                     Cannot rename a file or folder.
Cannot delete                     Cannot delete a file or folder.
I/O error                         Unspecified I/O error.
Cannot set size                   Setting the file size failed.
Cannot open                       Opening of a file failed.
Cannot close                      Closing a file failed.
Read error                        Reading from a file failed.
Write error                       Writing to a file failed.
Cannot seek                       Seek failure.
Cannot execute                    Unable to execute the specified file.
================================= ================================================================
