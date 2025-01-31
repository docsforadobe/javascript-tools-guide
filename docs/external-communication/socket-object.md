<a id="socket-object"></a>

# Socket object

TCP connections are the basic transport layer of the Internet. Every time your Web browser connects to a
server and requests a new page, it opens a TCP connection to handle the request as well as the server’s
reply. The JavaScript Socket object lets you connect to any server on the Internet and to exchange data
with this server.

The `Socket` object provides basic functionality to connect to a remote computer over a TCP/IP network or
the Internet. It provides calls like `open()` and `close()` to establish or to terminate a connection, and
`read()` or `write()` to transfer data. The `listen()` method establishes a simple Internet server; the server
uses the method `poll()` to check for incoming connections.

Many of these connections are based on simple data exchange of ASCII data, while other protocols, like
the FTP protocol, are more complex and involve binary data. One of the simplest protocols is the HTTP
protocol.

The following sample TCP/IP client connects to a WWW server (which listens on port 80); it then
sends a very simple HTTP GET request to obtain the home page of the WWW server, and then it reads the
reply, which is the home page together with a HTTP response header:

```default
reply = "";
conn = new Socket;

// access Adobe's home page
if (conn.open ("www.adobe.com:80")) {

    // send a HTTP GET request
    conn.write ("GET /index.html HTTP/1.0\n\n");

    // and read the server's reply
    reply = conn.read(999999);

    conn.close();
}
```

After executing this code, the variable `reply` contains the contents of the Adobe home page together
with an HTTP response header.

Establishing an Internet server is a bit more complicated. A typical server program sits and waits for
incoming connections, which it then processes. Usually, you would not want your application to run in an
endless loop, waiting for any incoming connection request. Therefore, you can ask a Socket object for an
incoming connection by calling the `poll()` method of a `Socket` object.

This call would just check the incoming connections and then return immediately. If there is a connection request,
the call to `poll()` would return another Socket object containing the brand new connection. Use this connection
object to talk to the calling client; when finished, close the connection and discard the connection object.

Before a `Socket` object is able to check for an incoming connection, it must be told to listen on a specific
port, like port 80 for HTTP requests. Do this by calling the `listen()` method instead of the `open()`
method.

The following example is a very simple Web server. It listens on port 80, waiting until it detects an
incoming request. The HTTP header is discarded, and a dummy HTML page is transmitted to the caller:

```default
conn = new Socket;
// listen on port 80
if (conn.listen (80)) {
    // wait forever for a connection
    var incoming;
    do incoming = conn.poll();
    while (incoming == null);

    // discard the request
    conn.read();

    // Reply with a HTTP header
    incoming.writeln ("HTTP/1.0 200 OK");
    incoming.writeln ("Content-Type: text/html");
    incoming.writeln();

    // Transmit a dummy homepage
    incoming.writeln ("<html><body><h1>Homepage</h1></body></html>");

    // done!
    incoming.close();
    delete incoming;
}
```

Often, the remote endpoint terminates the connection after transmitting data. Therefore, there is a
connected property that contains true as long as the connection still exists. If the connected property
returns false, the connection is closed automatically.

On errors, the `error` property of the `Socket` object contains a short message describing the type of the
error.

The Socket object lets you easily implement software that talks to each other via the Internet. You could,
for example, let two Adobe applications exchange documents and data simply by writing and executing
JavaScript programs.

---

<a id="chat-server-sample"></a>

## Chat server sample

The following sample code implements a very simple chat server. A chat client may connect to the chat
server, who is listening on port number 1234. The server responds with a welcome message and waits for
one line of input from the client. The client types some text and transmits it to the server who displays the
text and lets the user at the server computer type a line of text, which the client computer again displays.
This goes back and forth until either the server or the client computer types the word “bye”:

```default
// A simple Chat server on port 1234
function chatServer() {
    var tcp = new Socket;

    // listen on port 1234
    writeln ("Chat server listening on port 1234");
    if (tcp.listen (1234)) {
        for (;;) {
            // poll for a new connection
            var connection = tcp.poll();
            if (connection != null) {
                writeln ("Connection from " + connection.host);

                // we have a new connection, so welcome and chat
                // until client terminates the session
                connection.writeln ("Welcome to a little chat!");
                chat (connection);
                connection.writeln ( "*** Goodbye ***");
                connection.close();
                delete connection;
                writeln ("Connection closed");
            }
        }
    }
}

function chatClient() {
    var connection = new Socket;

    // connect to sample server
    if (connection.open ("remote-pc.corp.adobe.com:1234")) {
        // then chat with server
        chat (connection);
        connection.close();
        delete connection;
    }
}

function chat (c) {
    // select a long timeout
    c.timeout=1000;

    while (true) {
        // get one line and echo it
        writeln (c.read());

        // stop if the connection is broken
        if (!c.connected)
            break;

        // read a line of text
        write ("chat: ");
        var text = readln();

        if (text == "bye")
            // stop conversation if the user entered "bye"
            break;
        else
            // otherwise transmit to server
            c.writeln (text);
    }
}
```
