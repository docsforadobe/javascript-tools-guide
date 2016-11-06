Scripting Access to XMP Metadata
XMPScript, the XMP ExtendScript API, offers JavaScript access to the Adobe XMP Core and XMP Files
libraries. This chapter provides reference information for the JavaScript objects related to XMP, with their
properties and methods.
This chapter is not intended to provide complete details of the XMP metadata technology. For more
information about XMP metadata, see the XMP Specification at Adobe Developer Center,
http://www.adobe.com/devnet/.
Adobe Bridge CS5 makes the XMP library available in its libraries folder. Scripts must load the library at run
time to use the API; it is not automatically loaded when Adobe Bridge launches. The XMPScript API is
separate from the Adobe Bridge DOM. You can use it independently, to get and set metadata in supported
formats; or you can use it with the Adobe Bridge API to modify the metadata that you access from files
using the Adobe Bridge DOM’s Thumbnail object.
NOTE: Adobe Bridge provides a means of embedding metadata values in a script (to describe the script file
itself) using XML delimited by special tags within a comment block. This is not related to metadata access
for files and thumbnails. For details, see the Adobe Bridge JavaScript Guide.

Accessing the XMP scripting API
To use the XMP objects, you must load the XMP library as an ExtendScript ExternalObject. To avoid
loading multiple instances of the library, use code like the following:
// load the library
if (ExternalObject.AdobeXMPScript == undefined) {
ExternalObject.AdobeXMPScript = new
ExternalObject(’lib:AdobeXMPScript’);
}

After the library has been loaded, these primary XMP classes are available in the global JavaScript
namespace:
XMPMeta object

Provides the core services of the XMP Toolkit. Allows you to create and delete
metadata properties, and to retrieve and modify property values.

XMPFile object

Provides convenient I/O access to the main, or document level, XMP for a file. Allows
you to retrieve existing metadata from a file, update file metadata, and add new
metadata to a file.

Additional top-level objects include array-handling utilities, a date-time object, and constant definitions
that include namespace constants. The top-level objects provide access to additional support classes that
encapsulate individual metadata properties, file information, and XMP packet information, and a utility
that allows iteration through properties.
See "XMPScript object reference" on page 261 for details of the classes, their properties, and their
methods.

257

CHAPTER 10: Scripting Access to XMP Metadata

Accessing the XMP scripting API

258

Using the XMP scripting API
The XMPMeta object is the primary means of access to the namespaces and properties of an XMP
metadata packet. Through this object, you can create and delete namespaces and properties, and
examine and modify property values.
You can obtain or create an XMPMeta object in several ways:
You can use an XMPFile object to retrieve existing metadata directly from a file. The
XMPFile.getXMP() method creates an XMPMeta object, which you can use to examine or modify the
properties and their values. You can then use XMPFile.putXMP() to write the modified metadata back
to the file.
You can create an XMPMeta object with the constructor, initializing it with an XMP packet created or
obtained elsewhere.
You can create a new, empty XMPMeta object with the constructor, and use its methods to create
entirely new namespaces and properties. You can then use XMPFile.putXMP() to inject the new
metadata into a file.
In Adobe Bridge, you can pass XMP metadata between the built-in Metadata object and the XMPScript
XMPMeta object using serialized XMP.
You can use XMPScript to examine thumbnail metadata by creating the XMPMeta object from the
metadata stored with a Thumbnail object, using the object constructor. To ensure that the metadata is
up-to-date, use synchronous mode (which is off by default):
var thumb = new Thumbnail(new File("/C/myImage.jpg"));
app.synchronousMode = true;
xmp = new XMPMeta(thumb.metadata.serialize());

or
xmp = new XMPMeta(thumb.synchronousMetadata.serialize());

You can modify the metadata in an Adobe Bridge thumbnail by creating a new Metadata object with
serialized XMP. Continuing the previous example:
// create a compact XMP packet
newPacket = xmp.serialize(XMPConst.SERIALIZE_OMIT_PACKET_WRAPPER |
XMPConst.SERIALIZE_USE_COMPACT_FORMAT));
thumb.metadata = new Metadata(newPacket);

To write metadata back to the file for a thumbnail, you can access the thumbnail’s file and create an
XMPFile object object to access the embedded metadata directly.
xmp = new XMPFile(thumb.spec.fsName, XMPConst.UNKNOWN,
XMPConst.OPEN_FOR_UPDATE);

NOTE: The XMPFile object does not support all of the file formats that Adobe Bridge supports.
Creating new metadata
This code creates an empty XMPMeta object, uses it to set a metadata property, and serializes it to a string,
which you could pass to an authoring tool, for example, or store in a file.
xmp = new XMPMeta();
xmp.setProperty(XMPConst.NS_XMP, "CreatorTool", "My Script");
xmpStr = xmp.serialize(); // serialize the XMP packet to XML

CHAPTER 10: Scripting Access to XMP Metadata

Accessing the XMP scripting API

259

// retrieve property
prop = xmp.getProperty(XMPConst.NS_XMP, "CreatorTool");
$.writeln("namespace: " + prop.namespace + \n + "property path + name: " +
prop.path + \n + "value: " + prop); // same as prop.value

Modifying existing metadata
This code accesses an existing XMP packet, assuming the location has been assigned to a string variable. It
sets the modification-date property to the current date and time, and stores the updated XMP packet back
to the string, making it as small as possible.
xmp = new XMPMeta(xmpStr); // object initialized with xmp packet as string
dateTime = new XMPDateTime(new Date()); // now
$.writeln("old modification date: " +
xmp.getProperty(XMPConst.NS_XMP, "ModifyDate", "xmpdate"));
xmp.setProperty(XMPConst.NS_XMP, "ModifyDate", dateTime, "xmpdate");
// serialize to XML, in compact style
xmpStr = xmp.serialize(XMPConst.SERIALIZE_USE_COMPACT_FORMAT);

Using XMPFile for batch processing
This example iterates through a folder of image files and processes the metadata. The script processes
each picture as follows:
Reads and parses the metadata. If an image file does not contain XMP metadata, the legacy metadata
is automatically converted to XMP.
Deletes the list of existing creators, and adds a new creator value.
Writes the modified metadata back to the file.
$.writeln("XMPFiles batch processing example");
// define folder containing images (make sure that you use copies)
var picFolder = "/c/temp/photos";
// load the XMPScript library
if (ExternalObject.AdobeXMPScript == undefined)
ExternalObject.AdobeXMPScript =
new ExternalObject(’lib:AdobeXMPScript’);
// iterate through the photos in the folder
var pics = Folder(picFolder).getFiles();
for (f in pics) {
var file = pics[f];
$.writeln("process file: " + file.fsName);
// applies only to files, not to folders
if (file instanceof File) {
var xmpFile = new XMPFile(file.fsName, XMPConst.UNKNOWN,
XMPConst.OPEN_FOR_UPDATE);
var xmp = xmpFile.getXMP();
// delete existing authors and add a new one
// existing metadata stays untouched
xmp.deleteProperty(XMPConst.NS_DC, "creator");
xmp.appendArrayItem(XMPConst.NS_DC, "creator", "Judy", 0,
XMPConst.ARRAY_IS_ORDERED);
// write updated metadata into the file
if (xmpFile.canPutXMP(xmp)) {
xmpFile.putXMP(xmp);
}
xmpFile.closeFile(XMPConst.CLOSE_UPDATE_SAFELY);
}
}

CHAPTER 10: Scripting Access to XMP Metadata

Accessing the XMP scripting API

260

Integrating XMPScript with Adobe Bridge
This script adds a command to the context menu for Thumbnails that shows some of the XMP properties.
It demonstrates how to retrieve the XMP metadata that is stored with the Thumbnail object, and use it to
create an XMPMeta object, then use that object to retrieve different types of property values.
To use this script, place it in the "Startup Scripts" folder for Adobe Bridge (see "Startup scripts" on page 12).
When you start Adobe Bridge, select a thumbnail for a document that contains XMP metadata, right click,
and choose Show XMP Properties from the menu.
$.writeln("XMPFiles batch processing example");
// define folder containing images (make sure that you use copies)
var picFolder = "/c/temp/photos";
// load the XMPScript library
$.writeln("XMPScript Adobe Bridge Integration Example");
// load the XMPScript library
if (ExternalObject.AdobeXMPScript == undefined){
ExternalObject.AdobeXMPScript = new
ExternalObject(’lib:AdobeXMPScript’);
}
// add a context menu item to Thumbnails
var xmpCommand = new MenuElement("command", "Show XMP Properties",
"at the end of Thumbnail", "showProperties");
// define command behavior
xmpCommand.onSelect = function(m) {
// get the first selected thumbnail
thumb = app.document.selections[0];
// if there is one, and it has metadata
if (thumb && thumb.metadata) {
// retrieve metadata from the thumbnail into an XMPMeta object
// (if app.synchronousMode is set, use thumb.metadata)
xmp = new XMPMeta(thumb.synchronousMetadata.serialize());
// retrieve some of the XMP property values
// a simple property with a localized string value
var msg = "Title: " + xmp.getLocalizedText(XMPConst.NS_DC,
"title", null, "en") + "\n";
// an array property
msg += "Authors of the document:\n";
num = xmp.countArrayItems(XMPConst.NS_DC, "creator");
for (i = 1; i <= num; i++)
msg += "* " + xmp.getArrayItem(XMPConst.NS_DC,
"creator", i) + "\n";
// a simple property with a date value
msg += "Creation Date: " + xmp.getProperty(XMPConst.NS_XMP,
"CreateDate")
// display the values
Window.alert(msg);
}
else
Window.alert("No thumbnail selected or no XMP contained");
};

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

261

XMPScript object reference
The classes defined for the XMP JavaScript API, with their properties and methods, are listed here in
alphabetical order.
After the library has been loaded, these XMP classes are available in the global JavaScript namespace:
XMPMeta object

Provides the core services of the XMP Toolkit.

XMPFile object

Provides convenient I/O access to the main, or document level, XMP for a file.

XMPUtils object

Provides additional utility functions for array handling.

XMPDateTime object Represents date-time values.
XMPConst object

Contains numeric and string constant values for use with the JavaScript API.

These top-level objects provide access to additional support classes:
XMPIterator object

Allows iteration through properties in an XMPMeta object.

XMPProperty object

Describes a metadata property.

XMPAliasInfo object

Describes a metadata alias.

XMPFileInfo object

Describes a file.

XMPPacketInfo object

Describes a raw XMP packet in a file.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

262

XMPAliasInfo object
This object is returned by XMPMeta.resolveAlias(). The read-only properties describe an XMP metadata
alias.

XMPAliasInfo object properties
arrayForm

Number

A constant that describes the property type of the resolved alias, 0 for a
simple property. Constants are:
XMPConst.ALIAS_TO_SIMPLE_PROP: A direct mapping. It can be

simple-to-simple, array-to-array, or structure-to-structure.
XMPConst.ALIAS_TO_ARRAY: The actual property is an unordered
array; the alias is to the first element.
XMPConst.ALIAS_TO_ORDERED_ARRAY: The actual property is an
ordered array; the alias is to the first element.
XMPConst.ALIAS_TO_ALT_ARRAY: The actual property is an alternate

array; the alias is to the first element.

XMPConst.ALIAS_TO_ALT_TEXT: The actual property is an alternate
text array; the alias is to the x-default element.
name

String

The name of the property to which the alias resolves.

namespace

String

The namespace of the property to which the alias resolves. See "Schema
namespace string constants" on page 262.

XMPConst object
This object contains the read-only constant definitions for use with the JavaScript XMP API. Some of these
are listed in the context in which they are used. Longer lists are provided here.

Schema namespace string constants
Constant values for the namespace URI strings used in all get and set property operations. See XMPMeta
object.
NS_DC

The XML namespace for the Dublin Core schema,
http://purl.org/dc/elements/1.1

NS_IPTC_CORE

The XML namespace for the IPTC Core schema.

NS_RDF

The XML namespace for RDF.

NS_XML

The XML namespace for XML.

NS_XMP

The XML namespace for the XMP basic schema.

NS_XMP_RIGHTS

The XML namespace for the XMP copyright schema.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

263

NS_XMP_MM

The XML namespace for the XMP digital asset management schema.

NS_XMP_BJ

The XML namespace for the job management schema.

NS_XMP_NOTE

The XML namespace for the XMP note schema. An Adobe private
namespace; do not create new properties.

NS_PDF

The XML namespace for the PDF schema.

NS_PDFX

The XML namespace for the PDFX schema. An Adobe private namespace; do
not create new properties.

NS_PHOTOSHOP

The XML namespace for the Adobe Photoshop custom schema.

NS_PS_ALBUM

The XML namespace for the Adobe Photoshop Album custom schema.

NS_EXIF

The XML namespace for Adobe's EXIF schema.

NS_EXIF_AUX

The XML namespace for Adobe's EXIF auxiliary schema.

NS_TIFF

The XML namespace for Adobe's TIFF schema.

NS_PNG

The XML namespace for the PNG schema.

NS_JPEG

The XML namespace for the JPEG schema.

NS_SWF

The XML namespace for the Flash small web format schema.

NS_JPK

The XML namespace for the JPK schema.

NS_CAMERA_RAW

The XML namespace for the Camera Raw schema.

NS_DM

The XML namespace for the DM schema.

NS_ADOBE_STOCK_PHOTO

The XML namespace for the Adobe Stock Photos schema.

NS_ASF

The XML namespace for the Microsoft advanced streaming format schema.

Type namespace string constants
Constant values for the field-type namespace URI strings used in all structured property operations. See
XMPMeta object.
TYPE_IDENTIFIER_QUAL

The XML namespace for qualifiers of the xmp:Identifier property.

TYPE_DIMENSIONS

The XML namespace for fields of the Dimensions type.

TYPE_TEXT

The XML namespace for the XMP text document schema.

TYPE_PAGEDFILE

The XML namespace for the XMP paged document schema.

TYPE_GRAPHICS

The XML namespace for a structure containing the characteristics of a
colorant (swatch) used in a document.

TYPE_IMAGE

The XML namespace for fields of a graphical image. Used for the Thumbnail
type.

TYPE_FONT

The XML namespace for a structure containing the characteristics of a font
used in a document.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

TYPE_RESOURCE_EVENT

The XML namespace for fields of the ResourceEvent type.

TYPE_RESOURCE_REF

The XML namespace for fields of the ResourceRef type.

TYPE_ST_VERSION

The XML namespace for fields of the Version type.

TYPE_ST_JOB

The XML namespace for fields of the JobRef type.

TYPE_MANIFEST_ITEM

The XML namespace for the elements of a manifest array.

TYPE_PDFA_SCHEMA
TYPE_PDFA_PROPERTY
TYPE_PDFA_TYPE
TYPE_PDFA_FIELD
TYPE_PDFA_ID
TYPE_PDFA_EXTENSION

The XML namespaces for PDF subtypes

File format numeric constants
Constant values for supported file types, used in I/O operations. See XMPFile object.
FILE_UNKNOWN

Unknown file-format.

FILE_PDF

PDF

FILE_POSTSCRIPT

PS, general PostScript following DSC conventions

FILE_EPS

EPS, encapsulated PostScript

FILE_JPEG

JPEG

FILE_JPEG2K

JPX, JPEG 2000 file

FILE_TIFF

TIFF

FILE_GIF

GIF

FILE_PNG

PNG

FILE_SWF

SWF, Flash file

FILE_FLA

FLA, Flash authoring file

FILE_FLV

FLV, Flash video file

FILE_MOV

MOV, Quicktime

FILE_AVI

AVI

FILE_CIN

CIN, Cineon

FILE_WAV

WAV

FILE_MP3

MP3

FILE_SES

SES, Audition session

FILE_CEL

CEL, Audition loop

FILE_MPEG

MPEG

264

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

FILE_MPEG2

MP2

FILE_MPEG4

MP4

FILE_WMAV

WMAV, Windows Media Audio and Video

FILE_AIFF

AIFF

FILE_HTML

HTML

FILE_XML

XML

FILE_TEXT

TEXT

FILE_PHOTOSHOP

PSD, Photoshop

FILE_ILLUSTRATOR

AI, Illustrator

FILE_INDESIGN

INDD, Indesign

FILE_AE_PROJECT

AE, After Effects

FILE_AE_PROJECT_TEMPLATE

AET, After Effects Project Template

FILE_AE_FILTER_PRESET

FFX, After Effects Filter Preset file

FILE_ENCORE_PROJECT

NCOR, Encore DVD project file

FILE_PREMIERE_PROJECT

PRPJ, Premiere Project file

FILE_PREMIERE_TITLE

PRTL, Premiere Title file

265

XMPDateTime object
This class represents a date and time. Times include a time zone, and can have up to nanosecond
resolution.

XMPDateTime object constructors
new XMPDateTime ( ); // creates an object containing a 0 date
new XMPDateTime ( date ); // initializes the object with a JavaScript date
new XMPDateTime ( iso8601Date ); // initializes the object with an ISO date
date

A JavaScript Date object.
The time zone is set to the local operation-system time-zone value.
Times in the XMP Toolkit can have up to nanosecond resolution; however, when
converting to or from a JavaScript Date value, time resolution is reduced to milliseconds.

iso8601Date

A string containing a date-time in ISO 8601 format; for example:
"2007-04-10T17:54:50+01:00"

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

266

XMPDateTime object properties
All properties are read-write, and allow you to modify the date-time value. If values are set outside the
allowed range, they are automatically set to the minimum or maximum allowed value.
year

Number

The year, in the range [0000...9999].

month

Number

The month, in the range [1...12].

day

Number

The day, in the range [1...31].

hour

Number

The hour, in the range [1...23].

minute

Number

The minute, in the range [1...59].

second

Number

The second, in the range [1...59.

nanosecond

Number

The nanosecond, in the range [0...1e+9 -1].

tzSign

Number

The time zone direction of offset.
0: UTC
-1: west
1: east

tzHour

Number

The time zone hour offset from the prime meridian, in the range [1...23].

tzMinute

Number

The time zone minute offset from the prime meridian, in the range [1...59].

XMPDateTime object functions
compareTo()
XMPDateTimeObj.compareTo(xmpDateTime)
xmpDataTime

Another XMPDateTime object.

Reports the time order of two date-time values.
Returns 0 if the two values are the same, 1 if this date-time is later than the comparison value, -1 if
this date-time is earlier than the comparison value.
convertToLocalTime()
XMPDateTimeObj.convertToLocalTime()

Sets the time zone in this object to the local operating-system time zone, adjusting the time values
from the previous time zone, if necessary.
Returns undefined.
convertToUTCTime()
XMPDateTimeObj.convertToUTCTime()

Sets the time zone in this object to UTC (coordinated universal time), adjusting the time values from
the previous time zone, if necessary.
Returns undefined.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

267

getDate()
XMPDateTimeObj.getDate()

Converts this date-time value to a JavaScript Date. The time zone is normalized (time zones are not
supported in the JavaScript format), and the accuracy is reduced to milliseconds.
Returns a JavaScript Date object.
setLocalTimeZone()
XMPDateTimeObj.setLocalTimeZone()

Sets the time zone in this object to the current operation-system value, replacing any existing value.
Does not affect other fields.
Returns undefined.

XMPFile object
This class corresponds to the Adobe XMP Toolkit's File Handler component, which provides convenient I/O
access to the main, or document level, XMP for a file.
The File Handler supports those file formats in which you can embed XMP metadata, as defined in the XMP
Specification. It allows you to add XMP where none currently exists, expand existing XMP without regard
to existing padding, and reconcile XMP with other metadata formats.
The XMP Toolkit also supplies the Packet Scanner as a fallback solution for unsupported file formats. It
provides more limited accesses to all file formats by performing a dump file scan. It can update a file, but
cannot extend the packet or reconcile other metadata formats.
The XMPScript API does not currently support retrieving thumbnails.
NOTE: You can also use the Adobe Bridge Metadata object to access embedded metadata in files. It
supports thumbnails and previews, and additional file formats such as PDF and Camera Raw. For details,
see the Adobe Bridge JavaScript Guide and Adobe Bridge JavaScript Reference.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

268

XMPFile object constructors
new XMPFile( filePath, format, openFlags)
filePath

A string containing the file path of a document.

format

The file format constant. See "File format numeric constants" on page 264.

openFlags

The open options for the file. One of these constants:
XMPConst.OPEN_FOR_READ Open for read-only access.
XMPConst.OPEN_FOR_UPDATE Open for reading and writing.
XMPConst.OPEN_ONLY_XMP Only the XMP is wanted, allows space/time

optimizations.

XMPConst.OPEN_STRICTLY Be strict about locating XMP and reconciling with other

forms.

XMPConst.OPEN_USE_SMART_HANDLER Require the use of a smart handler. No packet

scanning is performed.

XMPConst.OPEN_USE_PACKET_SCANNING Force packet scanning, do not use a smart

handler.

XMPConst.OPEN_LIMITED_SCANNING Only packet-scan files known to need scanning.

XMPFile class properties
This property is available as a static property of the XMPFile class. It is not necessary to create an instance
to access it.
version

String

The descriptive string for this version of the XMP Toolkit.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

269

XMPFile class functions
This function is available as a static method of the XMPFile class. It is not necessary to create an instance to
call it.
getFormatInfo()
XMPFile.getFormatInfo(format)
format

The file format constant. See "File format numeric constants" on page 264.

Reports the supported features for the given file format.
Returns a logical OR of bit-flag constants, or 0 if the format is not handled. Constants are:
XMPConst.HANDLER_CAN_INJECT_XMP - Can inject first-time XMP into an existing file.
XMPConst.HANDLER_CAN_EXPAND - Can expand XMP or other metadata in an existing file.
XMPConst.HANDLER_CAN_REWRITE - Can copy one file to another, writing new metadata.
XMPConst.HANDLER_PPEFERS_IN_PLACE - Can expand, but prefers in-place update.
XMPConst.HANDLER_CAN_RECONCILE - Supports reconciliation between XMP and other forms.
XMPConst.HANDLER_ALLOWS_ONLY_XMP - Allows access to just the XMP, ignoring other forms.
XMPConst.HANDLER_RETURNS_RAW_PACKETS - File handler returns raw XMP packet information.
XMPConst.HANDLER_RETURNS_TNAIL - File handler returns native thumbnail.
XMPConst.HANDLER_OWNS_FILE - File handler does the file open and close.
XMPConst.HANDLER_ALLOWS_SAFE_UPDATE - File handler allows crash-safe file updates.
XMPConst.HANDLER_NEEDS_READONLY_PACKET - File format needs XMP packet to be read-only.
XMPConst.HANDLER_USES_SIDECAR_XMP - Fle handler uses a sidecar file for the XMP.

XMPFile object functions
canPutXMP()
XMPFileObj.canPutXMP(xmpObj)
XMPFileObj.canPutXMP(xmpPacket)
XMPFileObj.canPutXMP(xmpBuffer)
xmpObj

The XMP metadata as an XMPMeta object.

xmpPacket

The XMP metadata as a string containing an XMP packet.

xmpBuffer

The XMP metadata as an Array of Number containing raw XMP packet data.

Reports whether XMP metadata of a given size can be updated for this file. This is particularly
important if the packet size is increased.
Considers only the length of the serialized packet; does not keep the provided XMP. Use putXMP() to
actually update the XMP in the open file.
Returns true if the given XMP can be put into this file.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

270

closeFile()
XMPFileObj.closeFile(closeFlags)
closeFlags

A close-option constant, or 0. Close options are:
XMPConst.CLOSE_UPDATE_SAFELY Write into a temporary file then swap for

crash safety.

Closes this open file, after writing to it as necessary; that is, if the file was opened for update, and if
the XMP metadata was updated or injected. The options provided when the file was opened
determine whether this function reconciles the XMP with other forms of metadata; that is, whether
any legacy metadata is also updated to be consistent with the XMP metadata.
Returns undefined.
getXMP()
XMPFileObj.getXMP()

Retrieves and parses the existing XMP metadata from this file. If the file format contains legacy
metadata in a format that is recognized by the File Handler, the function creates an XMP packet
containing the metadata.
Returns an XMPMeta object, or null if the files does not contain XMP or convertible legacy
metadata.
getPacketInfo()
XMPFileObj.getPacketInfo()

Retrieves the raw XMP packet from this file, along with information about the packet. The options
with which the file was opened determine whether this function reconciles other forms of metadata
with the XMP.
Returns an XMPPacketInfo object, or null if the files does not contain XMP metadata.
getFileInfo()
XMPFileObj.getFileInfo()

Retrieves basic information about this file.
Returns an XMPFileInfo object.
putXMP()
XMPFileObj.putXMP(xmpObj)
XMPFileObj.putXMP(xmpPacket)
XMPFileObj.putXMP(xmpOBuffer)
xmpObj

The XMP metadata as an XMPMeta object.

xmpPacket

The XMP metadata as a String containing an XMP packet.

xmpBuffer

The XMP metadata as an Array of Number containing raw XMP packet data.

Supplies new XMP metadata for this file. The file is not actually written until closeFile() is called. The
options provided when the file was opened determine whether that function reconciles the XMP
with other forms of metadata; that is, whether any legacy metadata is also updated to be consistent
with the XMP metadata.
Returns undefined.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

271

XMPFileInfo object
This object is returned by XMPFile.getFileInfo(). The read-only properties describe the file represented by
the XMPFile object.
NOTE: This object is not related to the XMP File Info dialog that Adobe Creative Suite 4 applications use to
display metadata.

XMPFileInfo object properties
filePath

String

The absolute path of the file, in JavaScript notation.

format

Number One of the file-format constants. See "File format numeric constants" on
page 264.

handlerFlags

Number The features that are supported for this format. A logical OR of these
bit-flag constants:
XMPConst.HANDLER_CAN_INJECT_XMP - Can inject first-time XMP

into an existing file.

XMPConst.HANDLER_CAN_EXPAND - Can expand XMP or other

metadata in an existing file.

XMPConst.HANDLER_CAN_REWRITE - Can copy one file to another,

writing new metadata.

XMPConst.HANDLER_PPEFERS_IN_PLACE - Can expand, but prefers

in-place update.

XMPConst.HANDLER_CAN_RECONCILE - Supports reconciliation

between XMP and other forms.

XMPConst.HANDLER_ALLOWS_ONLY_XMP - Allows access to just the

XMP, ignoring other forms.

XMPConst.HANDLER_RETURNS_RAW_PACKETS - File handler returns

raw XMP packet information.

XMPConst.HANDLER_RETURNS_TNAIL - File handler returns native

thumbnail.

XMPConst.HANDLER_OWNS_FILE - File handler does the file open and

close.

XMPConst.HANDLER_ALLOWS_SAFE_UPDATE - File handler allows

crash-safe file updates.

CHAPTER 10: Scripting Access to XMP Metadata

openFlags

XMPScript object reference

272

Number The options with which this file was opened. One of these constants:
XMPConst.OPEN_FOR_READ - Open for read-only access.
XMPConst.OPEN_FOR_UPDATE - Open for reading and writing.
XMPConst.OPEN_ONLY_XMP - Only the XMP is wanted, allows

space/time optimizations.

XMPConst.OPEN_STRICTLY - Be strict about locating XMP and

reconciling with other forms.

XMPConst.OPEN_USE_SMART_HANDLER - Require the use of a smart
handler. No packet scanning is performed.
XMPConst.OPEN_USE_PACKET_SCANNING - Force packet scanning, do
not use a smart handler.
XMPConst.OPEN_LIMITED_SCANNING - Only packet-scan files known
to need scanning.

XMPIterator object
Created by a call to XMPMeta.iterator(). Walks recursively through the properties and qualifiers of an
XMPMeta object, and returns them as XMPProperty objects.
The object has no JavaScript properties.

XMPIterator object functions
next()
XMPIteratorObj.next ( )

Retrieves the next item in the metadata.
Returns an XMPProperty object, or null if there are no more items.
skipSiblings()
XMPIteratorObj.skipSiblings ( )

Skips the subtree below and the siblings of the current node on the subsequent call to next().
Returns undefined.
skipSubtree()
XMPIteratorObj.skipSubtree ( )

Skips the subtree below the current node on the subsequent call to next().
Returns undefined.

XMPMeta object
This class provides the core services of the XMP Toolkit. The functions provide the ability to create and
query metadata properties from an XMP namespace. The class also provides static functions that allow
you to create and query namespaces and aliases.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

273

There is one static property on the class that provides XMP version information; there are no JavaScript
properties in the instance. The object encapsulates a set of metadata properties, which you access
through the object functions.
The generic functions getProperty(), setProperty(), and deleteProperty() allow you to manipulate all types
of properties, when used with appropriately composed path expressions. For convenience, the object also
provides more specific functions for use with specific types of properties, such as arrays.

XMPMeta object constructors
To create an XMPMeta object, use the new operator. The constructor accepts an RDF/XML serialized
metadata packet as a string, or as an array of numbers that contain only byte values. It returns the new
object. If no argument is supplied, the new object is empty; you can use the object’s functions to add
namespaces and properties.
The first call to any of these constructors initializes the library by registering the standard namespaces and
aliases.
new XMPMeta ( ); // creates an empty object
new XMPMeta ( packet );
new XMPMeta ( buffer );
packet

A String containing an XML file or an XMP packet.

buffer

An Array of Number. The UTF-8 or UTF-16 encoded bytes of an XML file or an XMP packet.
This array is the result of XMPMeta.serializeToArray().

XMPMeta class properties
The XMPMeta class provides this static property. It is not necessary to create an instance to access it.
version

String

The descriptive string for this version of the XMP Toolkit.

XMPMeta class functions
The XMPMeta class provides these static functions. It is not necessary to create an instance to call them.
deleteAlias()
XMPMeta.deleteAlias (aliasNS, aliasProp)
aliasNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

aliasProp

The alias property string.

Deletes the specified alias; does not delete the aliased property. If the alias does not exist, does
nothing.
NOTE: Not yet implemented in the XMP Toolkit.
Returns undefined.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

deleteNamespace()
XMPMeta.deleteNamespace (namespaceURI)
namespaceURI

The namespace URI string. See "Schema namespace string constants" on
page 262.

Deletes a registered prefix - namespace URI pair.
NOTE: Not yet implemented in the XMP Toolkit.
Returns undefined.
dumpAliases()
XMPMeta.dumpAliases ( )

Creates and returns a human-readable string containing the list of registered aliases and their
targets.
Returns a String.
dumpNamespaces()
XMPMeta.dumpNamespaces ( )

Creates and returns a human-readable string containing the list of registered namespace URIs and
their associated prefixes.
Returns a String.
getNamespacePrefix()
XMPMeta.getNamespacePrefix (namespaceURI)
namespaceURI

The namespace URI string. See "Schema namespace string constants" on
page 262.

Retrieves the prefix associated with a registered namespace URI.
Returns the prefix string followed by a colon.
getNamespaceURI()
XMPMeta.getNamespaceURI (namespacePrefix)
namespacePrefix

The namespace prefix string.

Retrieves the registered namespace URI associated with a namespace prefix.
Returns the URI String.

274

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

275

registerAlias()
XMPMeta.registerAlias (aliasNS, aliasProp, actualNS, actualProp, arrayForm )
aliasNS

The alias namespace string. See "Schema namespace string constants" on
page 262.

aliasProp

The alias property, a simple name string.

actualNS

The namespace string of the aliased property. See "Schema namespace string
constants" on page 262.

actualProp

The aliased property, a simple name string.

arrayForm

Number. The array form for a simple alias to an array item, which controls how
the array is created if it is set for the first time through the alias. One of these
constants:
XMPConst.ALIAS_TO_SIMPLE_PROP (default) - A direct mapping. It can be

simple-to-simple, array-to-array, or structure-to-structure.
XMPConst.ALIAS_TO_ARRAY - The actual is an unordered array, the alias
is to the first element of the array.
XMPConst.ALIAS_TO_ORDERED_ARRAY - The actual is an ordered array,
the alias is to the first element of the array.
XMPConst.ALIAS_TO_ALT_ARRAY - The actual is an alternate array, the
alias is to the first element of the array.
XMPConst.ALIAS_TO_ALT_TEXT - The actual is an alternate-text array (a
localized property), the alias is to the x-default element of the array.

Defines an alias mapping from one namespace and property to another. An alias can be a direct
mapping where the alias and actual property have the same data type, or it can map a simple alias
to an item in an array, either the first item, or the x-default item in an alternate-text array.
Multiple alias names can map to the same actual property, as long as the forms match. If the same
alias and form exists, the call does nothing.
Returns undefined.
registerNamespace()
XMPMeta.registerNamespace (namespaceURI, suggestedPrefix)
namespaceURI

The namespace URI string. See "Schema namespace string constants" on
page 262.

suggestedPrefix

The suggested namespace prefix string.

Registers a namespace with a prefix. If the suggested prefix is already in use, generates, registers,
and returns a different prefix.
Returns a String containing the actual registered prefix. This is the suggestedPrefix, unless that
one is already assigned to another namespace.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

276

resolveAlias()
XMPMeta.resolveAlias (aliasNS, aliasProp)
schemaNS

The alias namespace URI string. See "Schema namespace string constants" on
page 262.

aliasProp

The alias property string.

Retrieves information about the actual property to which an alias is mapped.
Returns an XMPAliasInfo object.

XMPMeta object functions
appendArrayItem()
XMPMetaObj.appendArrayItem(schemaNS, arrayName[, itemOptions],
itemValue[, arrayOptions])
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

arrayName

The array-type property name string. Can be a general path expression.

itemOptions

Optional. A flag that describes the new item, if it is being created. One of:
0: The default. A simple item, or the type implied by the arrayOptions value.
XMPConst.PROP_IS_ARRAY: The item is an array (of type alt, bag, or seq).
XMPConst.PROP_IS_STRUCT: The item is a structure with nested fields.

itemValue

The new item value string. Pass null for array items that do not have values.

arrayOptions

Optional. A flag that describes the array form. Must be provided if the array is
being created; ignored if the array already exists. One of:
XMPConst.ARRAY_IS_ORDERED - Item order is significant. Implies
XMPConst.PROP_IS_ARRAY.
XMPConst.ARRAY_IS_ALTERNATIVE - Items are mutually exclusive
alternates. Implies XMPConst.PROP_IS_ARRAY and
XMPConst.ARRAY_IS_ORDERED.

Appends an item to an existing array, or creates a new array-type property if the named array does
not exist.
Returns undefined.
countArrayItems()
XMPMetaObj.countArrayItems(schemaNS, arrayName)
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

arrayName

The array-type property name string. Can be a general path expression.

Reports the number of items in an array-type metadata property.
Returns the number of items.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

277

deleteArrayItem()
XMPMetaObj.deleteArrayItem(schemaNS, arrayName,itemIndex)
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

arrayName

The array-type property name string. Can be a general path expression.

itemIndex

Number. The 1-based position index of the item. Use
XMPConst.ARRAY_LAST_ITEM to reference the last existing item in the array.

Deletes the metadata tree that has the given array item as its root.
Returns undefined.
deleteProperty()
XMPMetaObj.deleteProperty(schemaNS, propName)
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

propName

The property name string. Can be a general path expression.

Deletes the metadata tree that has the given property as its root. If the property does not exist, does
nothing.
Returns undefined.
deleteStructField()
XMPMetaObj.deleteStructField(schemaNS, structName, fieldNS, fieldName)
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

structName

The structure name string. Can be a general path expression.

fieldNS

The field type namespace string. See "Schema namespace string constants" on
page 262.

fieldName

The field name string. Must be a simple XML name.

Deletes the metadata tree that has the given structure field as its root.
Returns undefined.
deleteQualifier()
XMPMetaObj.deleteQualifier(schemaNS, structName, qualNS, qualName)
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

structName

The structure name string. Can be a general path expression.

qualNS

The URI string of the qualifier namespace.

qualName

The qualifier name string. Must be a simple XML name.

Deletes the metadata tree that has the given qualifier as its root. If the qualifier does not exist, does
nothing.
Returns undefined.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

doesArrayItemExist()
XMPMetaObj.doesArrayItemExist(schemaNS, arrayName, itemIndex)
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

arrayName

The array name string. Can be a general path expression.

itemIndex

Number. The 1-based position index of the item.

Reports whether an array item with a given index currently exists in an existing array in the
metadata.
Returns true if the array and item exist.
doesPropertyExist()
XMPMetaObj.doesPropertyExist(schemaNS, propName)
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

propName

The property name string. Can be a general path expression.

Reports whether a property with a given name currently exists in the metadata.
Returns true if the property exists.
doesStructFieldExist()
XMPMetaObj.deleteStructField(schemaNS, structName, fieldNS, fieldName)
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

structName

The structure name string. Can be a general path expression.

fieldNS

The field type namespace string. See "Type namespace string constants" on
page 263.

fieldName

The field name string. Must be a simple XML name.

Reports whether a structure field with a given name currently exists in the metadata.
Returns true if the structure and field exist.
doesQualifierExist()
XMPMetaObj.deleteQualifier(schemaNS, structName, qualNS, qualName)
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

structName

The structure name string. Can be a general path expression.

qualNS

The qualifier namespace URI string.

qualName

The qualifier name string. Must be a simple XML name.

Reports whether a qualifier with a given name currently exists for a given property.
Returns true if the property and qualifier exist.

278

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

279

dumpObject()
XMPMetaObj.dumpObject ( )

Creates and returns a string containing the metadata content of this object as RDF.
Returns a String.
getArrayItem()
XMPMetaObj.getArrayItem(schemaNS, arrayName, itemIndex)
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

arrayName

The array name string. Can be a general path expression.

itemIndex

Number. The 1-based position index of the item. Use
XMPConst.ARRAY_LAST_ITEM to reference the last existing item in the array.

Retrieves an item from an array-type metadata property.
Returns an XMPProperty object, or undefined if the property is not found.
getLocalizedText()
XMPMetaObj.getLocalizedText(schemaNS, altTextName, genericLang, specificLang)
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

altTextName

The alternate-text array name string. Can be a general path expression.

genericLang

The name of the generic language as an RFC 3066 primary subtag. Can be null or
the empty string.

specificLang

The name of the specific language as an RFC 3066 primary subtag; for example,
en-US. Must be specified.

Retrieves the text value for a specific language from an alternate-text array. First tries to match the
specific language. If not found, tries to match the generic language, if specified. If not found, gets
the x-default item, if any. Otherwise, gets the first item.
Returns a String, or undefined if no matching value is not found.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

280

getProperty()
XMPMetaObj.getProperty(schemaNS, propName[, valueType])
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

propName

The property name string. Can be a general path expression.

valueType

Optional, String. The property data type, one of:
XMPConst.STRING
XMPConst.INTEGER
XMPConst.NUMBER
XMPConst.BOOLEAN
XMPConst.XMPDATE

Retrieves the value and options of a metadata property. Use for top-level, simple properties, or after
using the path-composition functions in the XMPUtils object.
Returns an XMPProperty object, or undefined if the property is not found.
getStructField()
XMPMetaObj.getStructField(schemaNS, structName, fieldNS, fieldName)
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

structName

The structure name string. Can be a general path expression.

fieldNS

The field type namespace string. See "Type namespace string constants" on
page 263.

fieldName

The field name string. Must be a simple XML name.

Retrieves a field value from within a nested structure in metadata.
Returns an XMPProperty object, or undefined if the property is not found.
getQualifier()
XMPMetaObj.getQualifier(schemaNS, structName, qualNS, qualName)
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

structName

String. The structure name. Can be a general path expression.

qualNS

String. The URI of the qualifier namespace.

qualName

String. The qualifier name. Must be a simple XML name.

Retrieves a qualifier attached to a metadata property.
Returns an XMPProperty object, or undefined if the property is not found.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

281

insertArrayItem()
XMPMetaObj.insertArrayItem(schemaNS, arrayName, itemIndex, itemValue[, itemOptions])
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

arrayName

String. The name of an existing array. Can be a general path expression.

itemIndex

Number. The 1-based position index at which to insert the new item. Use
XMPConst.ARRAY_LAST_ITEM to reference the last existing item in the array.

itemValue

String. The new item value. Pass null for array items that do not have values.

itemOptions

Optional. A flag that describes the new item, if it is being created. One of:
0: A simple item, the default.

XMPConst.PROP_IS_ARRAY: The item is an array (of type alt, bag, or seq).
XMPConst.PROP_IS_STRUCT: The item is a structure with nested fields.

Inserts an item into an array, before an existing item. The index positions of all later items are
incremented. The array must exist.
Returns undefined.
iterator()
XMPMetaObj.iterator(options, schemaNS, propName)
options

The set of options that control how the iteration is performed, and how values are
returned. A logical OR of these bit-flag constants:
XMPConst.ITERATOR_JUST_CHILDREN - Limit iteration to immediate
children of the root property. By default, iterates into subtrees.
XMPConst.ITERATOR_JUST_LEAFNODES - Limit iteration to leaf nodes. By

default, iterates into all nodes of a subtree.

XMPConst.ITERATOR_JUST_LEAFNAMES - Return only the leaf part of the

path. By default, returns a full path.

XMPConst.ITERATOR_INCLUDE_ALIASES - Include aliases. By default,

considers only actual properties.

XMPConst.ITERATOR_OMIT_QUALIFIERS - Omit qualifiers from iteration.
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

propName

The name string of a property within which to iterate. Can be a general path
expression.

Creates an iteration object that can iterate over the properties, arrays, and qualifiers within this
metadata. Specify options, a namespace, and a property to limit the range and granularity of the
resulting items.
Returns an XMPIterator object for this metadata object.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

282

serialize()
XMPMetaObj.serialize([options, padding, indent, newline, baseIndent])
options

Optional. The set of options that control how the serialization is performed. The
options must be logically consistent; if they conflict, the function throws an
exception. A logical OR of these bit-flag constants:
XMPConst.SERIALIZE_OMIT_PACKET_WRAPPER - Do not include an XML

packet wrapper.

XMPConst.SERIALIZE_READ_ONLY_PACKET - Create a read-only XML packet

wrapper.

XMPConst.SERIALIZE_USE_COMPACT_FORMAT - Use a highly compact RDF

syntax and layout.

XMPConst.SERIALIZE_USE_PLAIN_XMP - Serialize a plain XMP (not currently

supported).

XMPConst.SERIALIZE_INCLUDE_THUMBNAIL_PAD - Include typical space for
a JPEG thumbnail in the padding if no xmp:Thumbnail property is present.
XMPConst.SERIALIZE_EXACT_PACKET_LENGTH - Compute padding to meet
the overall packet length provided by the padding parameter. Throws an

exception if the unpadded packet exceeds this length.

XMPConst.SERIALIZE_WRITE_ALIAS_COMMENTS - Include XML comments

for aliases.

padding

Optional, Number.
If the options value is SERIALIZE_EXACT_PACKET_LENGTH, this the exact
length of the packet, including padding characters that are added to meet this
length.
If the options value is not SERIALIZE_EXACT_PACKET_LENGTH, this is a
number of padding characters to add.
Default is 0, meaning to use the appropriate amount of padding.

indent

Optional, String. The string to use as an indent. Default is two spaces.

newline

Optional, String. The newline character to use. Default is U+000A.

baseIndent

Optional, Number. The level of indentation of the outermost XML element. Default
is 0.

Serializes this XMP metadata into a string as RDF.
Returns a String.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

283

serializeToArray()
XMPMetaObj.serializeToArray([options, padding, indent, newline, baseIndent])
options

Optional. The set of options that control how the serialization is performed. The
options must be logically consistent; if they conflict, the function throws an
exception. A logical OR of these bit-flag constants:
XMPConst.SERIALIZE_OMIT_PACKET_WRAPPER: - Do not include an XML

packet wrapper.

XMPConst.SERIALIZE_READ_ONLY_PACKET - Create a read-only XML packet

wrapper.

XMPConst.SERIALIZE_USE_COMPACT_FORMAT - Use a highly compact RDF

syntax and layout.

XMPConst.SERIALIZE_USE_PLAIN_XMP - Serialize plain XMP (not currently

supported).

XMPConst.SERIALIZE_INCLUDE_THUMBNAIL_PAD - Include typical space for
a JPEG thumbnail in the padding if no xmp:Thumbnail property is present.
XMPConst.SERIALIZE_EXACT_PACKET_LENGTH - Compute padding to meet
the overall packet length provided by the padding parameter. Throws an

exception if the unpadded packet exceeds this length.

XMPConst.SERIALIZE_WRITE_ALIAS_COMMENTS - Include XML comments

for aliases.

padding

Optional, Number.
If the options value is SERIALIZE_EXACT_PACKET_LENGTH, this the exact
length of the packet, including padding characters that are added to meet this
length.
If the options value is not SERIALIZE_EXACT_PACKET_LENGTH, this is a
number of padding characters to add.
Default is 0, meaning to use the appropriate amount of padding.

indent

Optional, String. The string to use as an indent. Default is two spaces.

newline

Optional, String. The newline character to use. Default is U+000A.

baseIndent

Optional, Number. The level of indentation of the outermost XML element. Default
is 0.

Serializes this XMP metadata into a string as RDF, then converts that to an array of one-byte numeric
values, the UTF-8 or UTF-16 encoded characters.
Returns an Array of Numbers.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

284

setArrayItem()
XMPMetaObj.setArrayItem(schemaNS, arrayName, itemIndex, itemValue[, itemOptions])
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

arrayName

The name string of an existing array. Can be a general path expression.

itemIndex

Number. The 1-based position index of the item. Use
XMPConst.ARRAY_LAST_ITEM to replace the last existing item in the array.

itemValue

The new item value string. Pass null for array items that do not have values.

itemOptions

Optional, a flag that describes the new item, if it is being created. One of:
0 - A simple item, the default.

XMPConst.PROP_IS_ARRAY - The item is an array (of type alt, bag, or seq).
XMPConst.PROP_IS_STRUCT - The item is a structure with nested fields.

Replaces an item within an array, or appends an item. The array must exist. To create an item,
appendArrayItem() and insertArrayItem() are preferred.
Returns undefined.
setLocalizedText()
XMPMetaObj.setLocalizedText(schemaNS, altTextName, genericLang, specificLang,
itemValue, setOptions)
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

altTextName

The name string of the alternate-text array. Can be a general path expression.

genericLang

The name of the generic language as an RFC 3066 primary subtag. Can be null or

the empty string.

specificLang

The name of the specific language as an RFC 3066 primary subtag; for example,
de-CH. Must be specified.

itemValue

The new string value.

setOptions

Not used.

Sets the text value for a specific language in an alternate-text array. Handles special cases for the
x-default item.
Returns undefined.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

285

setStructField()
XMPMetaObj.setStructField(schemaNS, structName, fieldNS, fieldName,
fieldValue[, options])
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

structName

The name string of an existing structure. Can be a general path expression.

fieldNS

The field type namespace string. See "Type namespace string constants" on
page 263.

fieldName

The field name string. Must be a simple XML name.

fieldValue

The new field value string. Pass null for fields that do not have values.

options

Optional, option flags that describe a new structure. Used only if the structure is
being created. One of:
0 - A simple item, the default.

XMPConst.PROP_IS_ARRAY - The item is an array (of type alt, bag, or seq).
XMPConst.PROP_IS_STRUCT - The item is a structure with nested fields.

Sets the value of a field within a structure-type property, or creates a new field if the named field
does not exist in the structure, or creates a new structure containing the named field if the named
structure does not exist.
Returns undefined.
setQualifier()
XMPMetaObj.setQualifier(schemaNS, propName, qualNS, qualName, qualValue[, options])
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

propName

The name string of an existing property. Can be a general path expression.

qualNS

The URI of the qualifier namespace. Has the same URI and prefix usage as a schema
namespace.

qualName

String. The name of the qualifier. Must be a simple XML name. Has the same prefix
usage as a property name.

qualValue

The new qualifier value string. Pass null for qualifiers that do not have values.

options

Optional, option flags that describe the qualifier. Used only if the qualifier is being
created. One of:
0 - A simple item, the default.

XMPConst.PROP_IS_ARRAY - The item is an array (of type alt, bag, or seq).
XMPConst.PROP_IS_STRUCT - The item is a structure with nested fields.

Attaches a new qualifier to a metadata property. A qualifier can be added to a simple property, an
array item, a struct field, or another qualifier.
Returns undefined.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

286

setProperty()
XMPMetaObj.setProperty(schemaNS, propName, propValue[, setOptions, valueType])
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

propName

The property name string. Can be a general path expression.

propValue

The new property value string. Pass null to create an array or non-leaf level
structure property.

setOptions

Optional. The type of property to create, if the named property does not exist.
Default is 0, a simple-valued property. Other constant values are:
XMPConst.PROP_IS_ARRAY - The property is an array (of type alt, bag, or seq).
XMPConst.PROP_IS_STRUCT - The property is a structure with nested fields.

valueType

Optional. The property data type. If supplied, the value is converted to this type.
One of:
XMPConst.STRING
XMPConst.INTEGER
XMPConst.NUMBER
XMPConst.BOOLEAN
XMPConst.XMPDATE

Sets the value of a simple metadata property, creating the property if necessary, or creates a new
array or structure property. For creating array and structure properties, setArrayItem() and
setStructField() are preferred. Use this call to create or set top-level, simple properties, or after using
the path-composition functions in the XMPUtils object.
Returns undefined.
sort()
XMPMetaObj.sort ( )

Sorts the XMP contents alphabetically.
At the top level, sorts namespaces by their prefixes.
Within a namespace, sorts top-level properties are sorted by name.
Within a struct, sorts fields by their qualified name (that is, the XML prefix:local form.
Sorts unordered arrays of simple items by value.
Sorts language alternative arrays by the xml:lang qualifiers, with the "x-default" item placed
first.
Returns undefined.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

287

XMPPacketInfo object
This object is returned by XMPFile.getPacketInfo(). The read-only properties describe the XMP packet for
the file represented by the XMPFile object.

XMPPacketInfo object properties
charForm

Number

The character encoding in the packet, one of:
0 - UTF8
2 - UTF-16, MSB-first (big-endian)
3 - UTF-16, LSB-first (little-endian)
4 - UTF 32, MSB-first (big-endian)
5 - UTF 32, LSB-first (little-endian)

length

Number

The length of the packet in bytes.

offset

Number

The byte-offset from the start of the file where the packet begins.

packet

String

The raw packet data.

padSize

Number

The packet’s padding size in bytes, 0 if unknown.

writeable

Boolean

If true, the packet is writeable.

XMPProperty object
This object is returned by various property accessor functions of the XMPMeta object, such as
getProperty(). The read-only properties describe a metadata property.

XMPProperty object properties
locale

String

The language of the property value. This value is set by calls to
getLocalizedText(), which assigns the language of the selected alternative text
item, if an appropriate item is found.

namespace

String

The namespace of the property; see "Schema namespace string constants" on
page 262. Typically used when browsing metadata with an XMPIterator object.

options

Number A constant that describes the property type, 0 for a simple property. Constants
are:
XMPConst.PROP_IS_ARRAY - The property is an array (of type alt, bag, or
seq).
XMPConst.PROP_IS_STRUCT - The property is a structure with nested

fields.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

288

path

String

The property path, including the property name. For a simple property, the
entire path is the property name.

value

Variant

The value of the property, if any. Arrays and non-leaf levels of structures do not
have values.

XMPUtils object
This class provides additional utility functions for the XMP Toolkit, layered upon the functionality of the
XMPMeta object. It has only static functions, you cannot create an instance.
Path-composition functions such as composeArrayItemPath(), provide support for composing path
expressions to deeply nested properties, which you can then pass to the accessor functions in
XMPMeta object, such as getProperty().
Higher-level functions such as duplicateSubtree() allow you to manipulate the metadata tree in an
XMPMeta object.

XMPUtils class functions
appendProperties()
XMPUtils.appendProperties(source, dest, options)
source

The source XMPMeta object.

dest

The destination XMPMeta object.

options

Option flags that control the copying operation. A logical OR of these bit-flag
constants:
XMPConst.APPEND_ALL_PROPERTIES - Include both internal and external
properties. By default, copies only external properties. This applies only to
top-level properties.
XMPConst.APPEND_REPLACE_OLD_VALUES - Replace the values of existing

properties with the value from the source object. By default, existing values
are retained. This applies to properties at all levels of hierarchy.

XMPConst.APPEND_DELETE_EMPTY_VALUES - Delete properties if the new

value is empty.
Default is 0.

Copies properties from a source XMPMeta object and appends them to a destination XMPMeta
object.
Returns undefined.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

289

catenateArrayItems()
XMPUtils.catenateArrayItems(xmpObj, schemaNS, arrayName, separator, quotes, options)
xmpObj

The XMPMeta object containing the array.

schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

arrayName

The array property name string. Can be a general path expression. Each item in
the array must be a simple string value.

separator

The string used to separate the items in the result string. Default is '; ', an ASCII
semicolon and space (U+003B,U+0020).

quotes

The character used to quote items that contain a separator. Default is '"', an ASCII
double quote (U+0022).

options

Option flag that controls the concatenation. This constant value:
XMPConst.SEPARATE_ALLOW_COMMAS - Allow commas in item values (such
as "LastName, FirstName"). This option must be set the same way in this
function and in separateArrayItems() to reconstruct the items correctly.

Default is 0.
Concatenates a set of array item values into a single string. The resulting string can be separated
back out into array items using separateArrayItems().
Returns the concatenated String.
composeArrayItemPath()
XMPUtils.composeArrayItemPath(schemaNS, arrayName, itemIndex)
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

arrayName

The array property name string. Can be a general path expression.

itemIndex

Number. The 1-based position index of the item. Use
XMPConst.ARRAY_LAST_ITEM to reference the last existing item in the array. In
this case, the resulting path is ns:arrayName[last()].

Creates and returns a string containing the path expression for an item in an array, using the
registered prefix for the namespace, in the form:
schemaNS:arrayName[itemIndex]

Returns a String.
composeFieldSelector()
XMPUtils.composeFieldSelector(schemaNS, arrayName, fieldNS, fieldName, fieldValue)
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

arrayName

The array property name string. Can be a general path expression.

CHAPTER 10: Scripting Access to XMP Metadata

fieldNS

The field namespace URI string.

fieldName

The field name. Must be a simple XML name.

fieldValue

The desired field value.

XMPScript object reference

290

Creates and returns a string containing the path expression to select an alternate item by a field’s
value, using the registered prefixes for the namespaces, in the form:
schemaNS:arrayName[fieldNS:fieldName=’fieldValue’]

Returns a String.
composeLanguageSelector()
XMPUtils.composeLanguageSelector(schemaNS, arrayName, locale)
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

arrayName

The array property name string. Can be a general path expression.

locale

The RFC3066 locale code string for the desired language.

Creates and returns a string containing the path expression to select an alternate item in an alt
text array by language, using the registered prefix for the namespace, in the form:
schemaNS:arrayName[@xml:lang=’langName’]

Returns a String.
NOTE: Do not use this in place of getLocalizedText() or setLocalizedText(). Those functions provide
extra logic to choose the appropriate language and maintain consistency with the x-default value.
This function provides a path expression for an explicit language, and only for that language.
composeStructFieldPath()
XMPUtils.composeStructFieldPath(schemaNS, structName, fieldNS, fieldName)
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

structName

The structure property name string. Can be a general path expression.

fieldNS

The field namespace URI string.

fieldName

The field name. Must be a simple XML name.

Creates and returns a string containing the path expression for a field in a structure, using the
registered prefixes for the namespaces, in the form:
schemaNS:structName/fieldNS:fieldName

Returns a String.
composeQualifierPath()
XMPUtils.composeQualifierPath(schemaNS, propName, qualNS, qualName)
schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

propName

The property name string. Can be a general path expression.

qualNS

The qualifier namespace URI string.

CHAPTER 10: Scripting Access to XMP Metadata

qualName

XMPScript object reference

291

The qualifier name. Must be a simple XML name.

Creates and returns a string containing the path expression for a qualifier attached to a property,
using the registered prefix for the namespace, in the form:
schemaNS:propName/?qualNS:qualName

Returns a String.
duplicateSubtree()
XMPUtils.duplicateSubtree(source, dest, sourceNS, sourceRoot,
destNS, destRoot, options)
source

The source XMPMeta object.

dest

The destination XMPMeta object.

sourceNS

The source namespace URI string. See "Schema namespace string constants" on
page 262.

sourceRoot

The property name string for the root location of the source subtree. Can be a
general path expression.

destNS

The destination namespace URI string. See "Schema namespace string constants"
on page 262.

destRoot

Optional. The property name string for the root location of the destination
subtree. Can be a general path expression. Default is the source root location.

options

Option flags that control the copying operation. A logical OR of these bit-flag
constants:
XMPConst.APPEND_ALL_PROPERTIES - Include both internal and external
properties. By default, copies only external properties. This applies only to
top-level properties.
XMPConst.APPEND_REPLACE_OLD_VALUES - Replace the values of existing

properties with the value from the source object. By default, existing values
are retained. This applies to properties at all levels of hierarchy.

XMPConst.APPEND_DELETE_EMPTY_VALUES - Delete properties if the new

value is empty.
Default is 0.

Copies properties in the specified subtree from a source XMPMeta object and adds them into a
destination XMPMeta object.
Returns undefined.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

292

removeProperties()
XMPUtils.removeProperties(xmpObj, schemaNS, propName, options)
xmpObj

The XMPMeta object.

schemaNS

Optional. The namespace URI string. See "Schema namespace string constants"
on page 262. Must be supplied if a property name is supplied.

propName

Optional. The property name string. Can be a general path expression.

options

Option flags that control the deletion operation. A logical OR of these bit-flag
constants:
XMPConst.REMOVE_ALL_PROPERTIES - Remove internal and external
properties. By default, removes only external properties. Applies only to
top-level properties.
XMPConst.REMOVE_INCLUDE_ALIASES - Remove aliases defined in the
namespace. If the property name is supplied, removes it regardless of this
option.

Default is 0.
Removes multiple properties from an XMPMeta object.
If both the namespace and property name are supplied, removes the property if it is external,
even if it is an alias. If it is internal, removes it if the option XMPConst.REMOVE_ALL_PROPERTIES
is specified.
If the namespace is supplied and the property name is not, removes all external properties in
the namespace, and optionally all internal properties. Removes aliases only if the option
XMPConst.REMOVE_INCLUDE_ALIASES is specified.
If neither the namespace nor the property name are supplied, removes all external properties,
and optionally all internal properties. Aliases are handled implicitly, because the associated
actual is removed.
Returns undefined.

CHAPTER 10: Scripting Access to XMP Metadata

XMPScript object reference

293

separateArrayItems()
XMPUtils.separateArrayItems(xmpObj, schemaNS, arrayName, arrayOptions, concatString)
xmpObj

The XMPMeta object containing the array.

schemaNS

The namespace URI string. See "Schema namespace string constants" on
page 262.

arrayName

The array property name string. Can be a general path expression. Each item in
the array must be a simple string value.

arrayOptions

Option flags that control how the array property is updated from the separated
string. A logical OR of these bit-flag constants:
XMPConst.APPEND_ALL_PROPERTIES - Include both internal and external
properties. By default, copies only external properties. This applies only to
top-level properties.
XMPConst.APPEND_REPLACE_OLD_VALUES - Replace the values of existing

properties with the value from the source object. By default, existing values
are retained. This applies to properties at all levels of hierarchy.

XMPConst.APPEND_DELETE_EMPTY_VALUES - Delete properties if the new

value is empty.

XMPConst.SEPARATE_ALLOW_COMMAS - Allow commas in item values. If not
specified, an item containing a comma (such as "LastName, FirstName") is
separated into two array items.

Default is 0.
concatString

The string containing the concatenated array values, as returned by
catenateArrayItems().

Updates individual array item strings in the XMPMeta object from a concatenated string returned by
catenateArrayItems(). Recognizes a large set of separator characters, including semicolons, commas,
tab, return, linefeed, and multiple spaces.
Returns undefined.
