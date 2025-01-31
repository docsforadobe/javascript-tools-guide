.. _socket-object-reference:

Socket object reference
=======================
This section provides details of the object's properties and methods.

Socket object constructor::

  [new] Socket ();

Creates and returns a new ``Socket`` object.

--------------------------------------------------------------------------------

.. _socket-object-properties:

Socket object properties
------------------------

=============  =======  =================================================================
``connected``  Boolean  When true, the connection is active. Read only.
``encoding``   String   Sets or retrieves the name of the encoding used to transmit data.
                        Typical values are "ASCII," "BINARY," or "UTF-8."
``eof``        Boolean  When true, the receive buffer is empty. Read only.
``error``      String   A message describing the most recent error.
                        Setting this value clears any error message.
``host``       String   The name of the remote computer when a connection is established.
                        If the connection is shut down or does not exist, the property
                        contains the empty string. Read only.
``timeout``    Number   The timeout in seconds to be applied to read or write operations.
                        Default is 10.
=============  =======  =================================================================

--------------------------------------------------------------------------------

.. _socket-object-functions:

Socket object functions
-----------------------

.. _socket-object-functions-close:

close()
*******
``socketObj.close ();``

Terminates the open connection. Deleting the object also closes the connection, but not until
JavaScript garbage-collects the object.

The connection might stay open longer than you wish if you do not close it explicitly.

Returns ``true`` if the connection was closed, ``false`` on I/O errors.

--------------------------------------------------------------------------------

.. _socket-object-functions-listen:

listen()
********
``socketObj.listen (port [, encoding]);``

============  ===============================================================================
``port``      Number. The TCP/IP port number to listen on. Valid port numbers are 1 to 65535.
              Typical values are 80 for a Web server, 23 for a Telnet server and so on.
``encoding``  Optional. String. The encoding to be used for the connection.
              Typical values are "ASCII," "binary," or "UTF-8." Default is "ASCII."
============  ===============================================================================

Instructs the object to start listening for an incoming connection.

The call to ``open()`` and the call to ``listen()`` are mutually exclusive.
Call one function or the other, not both.

Returns ``true`` on success.

--------------------------------------------------------------------------------

.. _socket-object-functions-open:

open()
******
``socketObj.open (host [, encoding]);``

============  ===============================================================================
``host``      String. The name or IP address of the remote computer, followed by a colon and the
              port number to connect to. The port number is required. Valid computer names are,
              for example, "www.adobe.com:80" or "192.150.14.12:80".
``encoding``  Optional. String. The encoding to be used for the connection.
              Typical values are "ASCII," "binary," or "UTF-8." Default is "ASCII."
============  ===============================================================================

Opens the connection for subsequent read/write operations.

The call to open() and the call to listen() are mutually exclusive.
Call one function or the other, not both.

Returns ``true`` on success.

--------------------------------------------------------------------------------

.. _socket-object-functions-poll:

poll()
******
``socketObj.poll ();``

Checks a listening object for a new incoming connection. If a connection request was detected, the
method returns a new Socket object that wraps the new connection. Use this connection object to
communicate with the remote computer.

After use, close the connection and delete the JavaScript object.
If no new connection request was detected, the method returns null.

Returns a ``Socket`` object or ``null``.

--------------------------------------------------------------------------------

.. _socket-object-functions-read:

read()
******
``socketObj.read ([count]);``

=========  =================================================================
``count``  Optional. Number. The number of characters to read; default is 0.
           If negative, the call is equivalent to ``readln()``
=========  =================================================================

Reads up to the specified number of characters from the connection, waiting if necessary.
Ignores CR characters unless encoding is set to ``BINARY``.

Returns a string that contains up to the number of characters that were supposed to be read, or the
number of characters read before the connection closed or timed out.

--------------------------------------------------------------------------------

.. _socket-object-functions-readln:

readln()
********
``socketObj.readln ();``

Reads one line of text up to the next line feed. Line feeds are recognized as LF or CRLF pairs.
CR characters are ignored.

Returns a string.

--------------------------------------------------------------------------------

.. _socket-object-functions-write:

write()
*******
``socketObj.write (text[, text...]);``

========  ===============================================================================
``text``  String. Any number of string values. All arguments are concatenated to form the
          string to be written.
========  ===============================================================================

Concatenates all arguments into a single string and writes that string to the connection.
CRLF sequences are converted to LFs unless encoding is set to ``BINARY.``

Returns ``true`` on success.

--------------------------------------------------------------------------------

.. _socket-object-functions-writeln:

writeln()
*********
``socketObj.writeln (text[, text...]);``

========  ===============================================================================
``text``  String. Any number of string values. All arguments are concatenated to form the
          string to be written.
========  ===============================================================================

Concatenates all arguments into a single string, appends a Line Feed character,
and writes that string to the connection.

Returns ``true`` on success.
