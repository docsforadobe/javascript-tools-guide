# Accessing the XMP scripting API

To use the XMP objects, you must load the XMP library as an ExtendScript ExternalObject. To avoid loading multiple instances of the library, use code like the following:

```javascript
// load the library
if ( ExternalObject.AdobeXMPScript == undefined ) {
    ExternalObject.AdobeXMPScript = new ExternalObject( "lib:AdobeXMPScript");
}
```

After the library has been loaded, these primary XMP classes are available in the global JavaScript namespace:

| [XMPMeta object](xmpscript-object-reference.md#xmpmeta-object)   | Provides the core services of the XMP Toolkit. Allows you to create and delete<br/>metadata properties, and to retrieve and modify property values.                                                |
|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [XMPFile object](xmpscript-object-reference.md#xmpfile-object)   | Provides convenient I/O access to the main, or document level, XMP for a file. Allows<br/>you to retrieve existing metadata from a file, update file metadata, and add new<br/>metadata to a file. |

Additional top-level objects include array-handling utilities, a date-time object, and constant definitions that include namespace constants. The top-level objects provide access to additional support classes that encapsulate individual metadata properties, file information, and XMP packet information, and a utility that allows iteration through properties.

See [XMPScript object reference](xmpscript-object-reference.md) for details of the classes, their properties, and their methods.

---

## Using the XMP scripting API

The [XMPMeta object](xmpscript-object-reference.md#xmpmeta-object) is the primary means of access to the namespaces and properties of an XMP metadata packet. Through this object, you can create and delete namespaces and properties, and examine and modify property values.

You can obtain or create an [XMPMeta object](xmpscript-object-reference.md#xmpmeta-object) in several ways:

- You can use an [XMPFile object](xmpscript-object-reference.md#xmpfile-object) to retrieve existing metadata directly from a file. The `XMPFile.`[getXMP()](xmpscript-object-reference.md#xmpfile-getxmp) method creates an [XMPMeta object](xmpscript-object-reference.md#xmpmeta-object), which you can use to examine or modify the properties and their values. You can then use `XMPFile.`[putXMP()](xmpscript-object-reference.md#xmpfile-putxmp) to write the modified metadata back to the file.
- You can create an [XMPMeta object](xmpscript-object-reference.md#xmpmeta-object) with the constructor, initializing it with an XMP packet created or obtained elsewhere.
- You can create a new, empty [XMPMeta object](xmpscript-object-reference.md#xmpmeta-object) with the constructor, and use its methods to create entirely new namespaces and properties. You can then use `XMPFile.`[putXMP()](xmpscript-object-reference.md#xmpfile-putxmp) to inject the new metadata into a file.

In Adobe Bridge, you can pass XMP metadata between the built-in `Metadata` object and the XMPScript [XMPMeta object](xmpscript-object-reference.md#xmpmeta-object) using serialized XMP.

- You can use XMPScript to examine thumbnail metadata by creating the [XMPMeta object](xmpscript-object-reference.md#xmpmeta-object) from the metadata stored with a `Thumbnail` object, using the object constructor. To ensure that the metadata is up-to-date, use synchronous mode (which is off by default):
    ```javascript
    var thumb = new Thumbnail( new File( "/C/myImage.jpg") );
    app.synchronousMode = true;
    xmp = new XMPMeta( thumb.metadata.serialize() );
    ```

    or:
    ```javascript
    xmp = new XMPMeta( thumb.synchronousMetadata.serialize() );
    ```
- You can modify the metadata in an Adobe Bridge thumbnail by creating a new `Metadata` object with serialized XMP. Continuing the previous example:
    ```javascript
    // Create a compact XMP packet
    newPacket = xmp.serialize( XMPConst.SERIALIZE_OMIT_PACKET_WRAPPER | XMPConst.SERIALIZE_USE_COMPACT_FORMAT ) );
    thumb.metadata = new Metadata( newPacket );
    ```
- To write metadata back to the file for a thumbnail, you can access the thumbnail's file and create an [XMPFile object](xmpscript-object-reference.md#xmpfile-object) object to access the embedded metadata directly:
    ```javascript
    xmp = new XMPFile( thumb.spec.fsName, XMPConst.UNKNOWN, XMPConst.OPEN_FOR_UPDATE );
    ```

!!! note
    The `XMPFile` object does not support all of the file formats that Adobe Bridge supports.

---

### Creating new metadata

This code creates an empty [XMPMeta object](xmpscript-object-reference.md#xmpmeta-object), uses it to set a metadata property, and serializes it to a string, which you could pass to an authoring tool, for example, or store in a file.

```javascript
xmp = new XMPMeta();
xmp.setProperty( XMPConst.NS_XMP, "CreatorTool", "My Script" );
xmpStr = xmp.serialize(); // Serialize the XMP packet to XML

// Retrieve property
prop = xmp.getProperty(XMPConst.NS_XMP, "CreatorTool");
$.writeln( "namespace: " + prop.namespace + "\n" +
    "property path + name: " + prop.path + "\n" +
    "value: " + prop ); // same as prop.value
```

---

### Modifying existing metadata

This code accesses an existing XMP packet, assuming the location has been assigned to a string variable. It sets the modification-date property to the current date and time, and stores the updated XMP packet back to the string, making it as small as possible.

```javascript
xmp = new XMPMeta( xmpStr ); // Object initialized with xmp packet as string
dateTime = new XMPDateTime( new Date() ); // Now
oldModificationDate = mp.getProperty( XMPConst.NS_XMP, "ModifyDate", "xmpdate" );
$.writeln( "Old modification date: " + oldModificationDate );
xmp.setProperty( XMPConst.NS_XMP, "ModifyDate", dateTime, "xmpdate" );

// Serialize to XML, in compact style
xmpStr = xmp.serialize( XMPConst.SERIALIZE_USE_COMPACT_FORMAT );
```

---

### Using XMPFile for batch processing

This example iterates through a folder of image files and processes the metadata. The script processes each picture as follows:

- Reads and parses the metadata. If an image file does not contain XMP metadata, the legacy metadata is automatically converted to XMP.
- Deletes the list of existing creators, and adds a new creator value.
- Writes the modified metadata back to the file.

```javascript
$.writeln( "XMPFiles batch processing example" );

// Define folder containing images (make sure that you use copies)
var picFolder = "/c/temp/photos";
// Load the XMPScript library
if ( ExternalObject.AdobeXMPScript == undefined ) {
    ExternalObject.AdobeXMPScript = new ExternalObject( "lib:AdobeXMPScript" );
}
// Iterate through the photos in the folder
var pics = Folder(picFolder).getFiles();
for ( var i = 0; i < pics.length; i++ ) {
    var file = pics[i];
    $.writeln( "Process file: " + file.fsName );

    // Applies only to files, not to folders
    if ( file instanceof File ) {
        var xmpFile = new XMPFile( file.fsName, XMPConst.UNKNOWN, XMPConst.OPEN_FOR_UPDATE );
        var xmp = xmpFile.getXMP();

        // Delete existing authors and add a new one
        // Existing metadata stays untouched
        xmp.deleteProperty( XMPConst.NS_DC, "creator" );
        xmp.appendArrayItem( XMPConst.NS_DC, "creator", "Judy", 0, XMPConst.ARRAY_IS_ORDERED );

        // Write updated metadata into the file
        if ( xmpFile.canPutXMP( xmp ) ) {
            xmpFile.putXMP( xmp );
        }
        xmpFile.closeFile( XMPConst.CLOSE_UPDATE_SAFELY );
    }
}
```

---

### Integrating XMPScript with Adobe Bridge

This script adds a command to the context menu for Thumbnails that shows some of the XMP properties.

It demonstrates how to retrieve the XMP metadata that is stored with the Thumbnail object, and use it to create an [XMPMeta object](xmpscript-object-reference.md#xmpmeta-object), then use that object to retrieve different types of property values.

To use this script, place it in the "Startup Scripts" folder for Adobe Bridge (see [Startup scripts](../introduction/scripting-for-specific-applications.md#startup-scripts)). When you start Adobe Bridge, select a thumbnail for a document that contains XMP metadata, right click, and choose **Show XMP Properties** from the menu.

```javascript
$.writeln("XMPFiles batch processing example");

// Define folder containing images (make sure that you use copies)
var picFolder = "/c/temp/photos";

// Load the XMPScript library
$.writeln("XMPScript Adobe Bridge Integration Example");

// Load the XMPScript library
if ( ExternalObject.AdobeXMPScript == undefined ) {
    ExternalObject.AdobeXMPScript = new ExternalObject( "lib:AdobeXMPScript" );
}
// Add a context menu item to Thumbnails
var xmpCommand = new MenuElement( "command", "Show XMP Properties", "at the end of Thumbnail", "showProperties" );

// Define command behavior
xmpCommand.onSelect = function(m) {

// Get the first selected thumbnail
thumb = app.document.selections[0];

// If there is one, and it has metadata
if ( thumb && thumb.metadata ) {

    // Retrieve metadata from the thumbnail into an XMPMeta object`
    // ( if app.synchronousMode is set, use thumb.metadata )

    xmp = new XMPMeta( thumb.synchronousMetadata.serialize() );

    // Retrieve some of the XMP property values
    // A simple property with a localized string value
    var msg = "Title: " + xmp.getLocalizedText( XMPConst.NS_DC, "title", null, "en" ) + "\n";

    // An array property
    msg += "Authors of the document:\n";
    num = xmp.countArrayItems( XMPConst.NS_DC, "creator" );
    for ( var i = 1; i <= num; i++ ) {}
        msg += "* " + xmp.getArrayItem( XMPConst.NS_DC, "creator", i ) + "\n";
    }

    // A simple property with a date value
    msg += "Creation Date: " + xmp.getProperty( XMPConst.NS_XMP, "CreateDate" )

    // Display the values
    Window.alert( msg );
} else {
    Window.alert( "No thumbnail selected or no XMP contained" );
}
```
