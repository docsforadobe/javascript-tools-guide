# XMPScript object reference

The classes defined for the XMP JavaScript API, with their properties and methods, are listed here in alphabetical order.

After the library has been loaded, these XMP classes are available in the global JavaScript namespace:

|                  Object                   |                                  Description                                   |
| ----------------------------------------- | ------------------------------------------------------------------------------ |
| [XMPMeta object](#xmpmeta-object)         | Provides the core services of the XMP Toolkit.                                 |
| [XMPFile object](#xmpfile-object)         | Provides convenient I/O access to the main, or document level, XMP for a file. |
| [XMPUtils object](#xmputils-object)       | Provides additional utility functions for array handling.                      |
| [XMPDateTime object](#xmpdatetime-object) | Represents date-time values.                                                   |
| [XMPConst object](#xmpconst-object)       | Contains numeric and string constant values for use with the JavaScript API.   |

These top-level objects provide access to additional support classes:

|                    Object                     |                                 Description                                  |
| --------------------------------------------- | ---------------------------------------------------------------------------- |
| [XMPIterator object](#xmpiterator-object)     | Allows iteration through properties in an [XMPMeta object](#xmpmeta-object). |
| [XMPProperty object](#xmpproperty-object)     | Describes a metadata property.                                               |
| [XMPAliasInfo object](#xmpaliasinfo-object)   | Describes a metadata alias.                                                  |
| [XMPFileInfo object](#xmpfileinfo-object)     | Describes a file.                                                            |
| [XMPPacketInfo object](#xmppacketinfo-object) | Describes a raw XMP packet in a file.                                        |

---

## XMPAliasInfo object

This object is returned by [XMPMeta.resolveAlias](#resolvealias). The read-only properties describe an XMP metadata alias.

### XMPAliasInfo object properties

+-----------+--------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Property  |  Type  |                                                               Description                                                               |
+===========+========+=========================================================================================================================================+
| arrayForm | Number | A constant that describes the property type of the resolved alias, 0 for a simple property. Constants are:                              |
|           |        |                                                                                                                                         |
|           |        | - `XMPConst.ALIAS_TO_SIMPLE_PROP`: A direct mapping. It can be simple-to-simple, array-to-array, or structure-to-structure.             |
|           |        | - `XMPConst.ALIAS_TO_ARRAY`: The actual property is an unordered array; the alias is to the first element.                              |
|           |        | - `XMPConst.ALIAS_TO_ORDERED_ARRAY`: The actual property is an ordered array; the alias is to the first element.                        |
|           |        | - `XMPConst.ALIAS_TO_ALT_ARRAY`: The actual property is an alternate array; the alias is to the first element.                          |
|           |        | - `XMPConst.ALIAS_TO_ALT_TEXT`: The actual property is an alternate text array; the alias is to the `x-default` element.                |
+-----------+--------+-----------------------------------------------------------------------------------------------------------------------------------------+
| name      | String | The name of the property to which the alias resolves.                                                                                   |
+-----------+--------+-----------------------------------------------------------------------------------------------------------------------------------------+
| namespace | String | The namespace of the property to which the alias resolves. See [Schema namespace string constants](#schema-namespace-string-constants). |
+-----------+--------+-----------------------------------------------------------------------------------------------------------------------------------------+

---

## XMPConst object

This object contains the read-only constant definitions for use with the JavaScript XMP API. Some of these are listed in the context in which they are used. Longer lists are provided here.

### Schema namespace string constants

Constant values for the namespace URI strings used in all get and set property operations. See [XMPMeta object](#xmpmeta-object).

|       Namespace        |                                                   Description                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `NS_DC`                | The XML namespace for the Dublin Core schema, [http://purl.org/dc/elements/1.1](http://purl.org/dc/elements/1.1) |
| `NS_IPTC_CORE`         | The XML namespace for the IPTC Core schema.                                                                      |
| `NS_RDF`               | The XML namespace for RDF.                                                                                       |
| `NS_XML`               | The XML namespace for XML.                                                                                       |
| `NS_XMP`               | The XML namespace for the XMP basic schema.                                                                      |
| `NS_XMP_RIGHTS`        | The XML namespace for the XMP copyright schema.                                                                  |
| `NS_XMP_MM`            | The XML namespace for the XMP digital asset management schema.                                                   |
| `NS_XMP_BJ`            | The XML namespace for the job management schema.                                                                 |
| `NS_XMP_NOTE`          | The XML namespace for the XMP note schema. An Adobe private namespace; do not create new properties.             |
| `NS_PDF`               | The XML namespace for the PDF schema.                                                                            |
| `NS_PDFX`              | The XML namespace for the PDFX schema. An Adobe private namespace; do not create new properties.                 |
| `NS_PHOTOSHOP`         | The XML namespace for the Adobe Photoshop custom schema.                                                         |
| `NS_PS_ALBUM`          | The XML namespace for the Adobe Photoshop Album custom schema.                                                   |
| `NS_EXIF`              | The XML namespace for Adobe's EXIF schema.                                                                       |
| `NS_EXIF_AUX`          | The XML namespace for Adobe's EXIF auxiliary schema.                                                             |
| `NS_TIFF`              | The XML namespace for Adobe's TIFF schema.                                                                       |
| `NS_PNG`               | The XML namespace for the PNG schema.                                                                            |
| `NS_JPEG`              | The XML namespace for the JPEG schema.                                                                           |
| `NS_SWF`               | The XML namespace for the Flash small web format schema.                                                         |
| `NS_JPK`               | The XML namespace for the JPK schema.                                                                            |
| `NS_CAMERA_RAW`        | The XML namespace for the Camera Raw schema.                                                                     |
| `NS_DM`                | The XML namespace for the DM schema.                                                                             |
| `NS_ADOBE_STOCK_PHOTO` | The XML namespace for the Adobe Stock Photos schema.                                                             |
| `NS_ASF`               | The XML namespace for the Microsoft advanced streaming format schema.                                            |

---

### Type namespace string constants

Constant values for the field-type namespace URI strings used in all structured property operations. See [XMPMeta object](#xmpmeta-object).

|       Namespace        |                                                 Description                                                 |
| ---------------------- | ----------------------------------------------------------------------------------------------------------- |
| `TYPE_IDENTIFIER_QUAL` | The XML namespace for qualifiers of the xmp:Identifier property.                                            |
| `TYPE_DIMENSIONS`      | The XML namespace for fields of the Dimensions type.                                                        |
| `TYPE_TEXT`            | The XML namespace for the XMP text document schema.                                                         |
| `TYPE_PAGEDFILE`       | The XML namespace for the XMP paged document schema.                                                        |
| `TYPE_GRAPHICS`        | The XML namespace for a structure containing the characteristics of a colorant (swatch) used in a document. |
| `TYPE_IMAGE`           | The XML namespace for fields of a graphical image. Used for the Thumbnail type.                             |
| `TYPE_FONT`            | The XML namespace for a structure containing the characteristics of a font used in a document.              |
| `TYPE_RESOURCE_EVENT`  | The XML namespace for fields of the ResourceEvent type.                                                     |
| `TYPE_RESOURCE_REF`    | The XML namespace for fields of the ResourceRef type.                                                       |
| `TYPE_ST_VERSION`      | The XML namespace for fields of the Version type.                                                           |
| `TYPE_ST_JOB`          | The XML namespace for fields of the JobRef type.                                                            |
| `TYPE_MANIFEST_ITEM`   | The XML namespace for the elements of a manifest array.                                                     |
| `TYPE_PDFA_SCHEMA`     |                                                                                                             |
| `TYPE_PDFA_PROPERTY`   |                                                                                                             |
| `TYPE_PDFA_TYPE`       |                                                                                                             |
| `TYPE_PDFA_FIELD`      |                                                                                                             |
| `TYPE_PDFA_ID`         |                                                                                                             |
| `TYPE_PDFA_EXTENSION`  | The XML namespaces for PDF subtypes                                                                         |

---

### File format numeric constants

Constant values for supported file types, used in I/O operations. See [XMPFile object](#xmpfile-object).

|          Constant          |                   Description                    |
| -------------------------- | ------------------------------------------------ |
| `FILE_UNKNOWN`             | Unknown file-format.                             |
| `FILE_PDF`                 | PDF                                              |
| `FILE_POSTSCRIPT`          | PS, general PostScript following DSC conventions |
| `FILE_EPS`                 | EPS, encapsulated PostScript                     |
| `FILE_JPEG`                | JPEG                                             |
| `FILE_JPEG2K`              | JPX, JPEG 2000 file                              |
| `FILE_TIFF`                | TIFF                                             |
| `FILE_GIF`                 | GIF                                              |
| `FILE_PNG`                 | PNG                                              |
| `FILE_SWF`                 | SWF, Flash file                                  |
| `FILE_FLA`                 | FLA, Flash authoring file                        |
| `FILE_FLV`                 | FLV, Flash video file                            |
| `FILE_MOV`                 | MOV, Quicktime                                   |
| `FILE_AVI`                 | AVI                                              |
| `FILE_CIN`                 | CIN, Cineon                                      |
| `FILE_WAV`                 | WAV                                              |
| `FILE_MP3`                 | MP3                                              |
| `FILE_SES`                 | SES, Audition session                            |
| `FILE_CEL`                 | CEL, Audition loop                               |
| `FILE_MPEG`                | MPEG                                             |
| `FILE_MPEG2`               | MP2                                              |
| `FILE_MPEG4`               | MP4                                              |
| `FILE_WMAV`                | WMAV, Windows Media Audio and Video              |
| `FILE_AIFF`                | AIFF                                             |
| `FILE_HTML`                | HTML                                             |
| `FILE_XML`                 | XML                                              |
| `FILE_TEXT`                | TEXT                                             |
| `FILE_PHOTOSHOP`           | PSD, Photoshop                                   |
| `FILE_ILLUSTRATOR`         | AI, Illustrator                                  |
| `FILE_INDESIGN`            | INDD, Indesign                                   |
| `FILE_AE_PROJECT`          | AE, After Effects                                |
| `FILE_AE_PROJECT_TEMPLATE` | AET, After Effects Project Template              |
| `FILE_AE_FILTER_PRESET`    | FFX, After Effects Filter Preset file            |
| `FILE_ENCORE_PROJECT`      | NCOR, Encore DVD project file                    |
| `FILE_PREMIERE_PROJECT`    | PRPJ, Premiere Project file                      |
| `FILE_PREMIERE_TITLE`      | PRTL, Premiere Title file                        |

---

## XMPDateTime object

This class represents a date and time. Times include a time zone, and can have up to nanosecond resolution.

### XMPDateTime object constructors

```javascript
new XMPDateTime();            // creates an object containing a 0 date
new XMPDateTime(date);        // initializes the object with a JavaScript date
new XMPDateTime(iso8601Date); // initializes the object with an ISO date
```

#### Parameter

|  Parameter  |            Type             |                                                                                                                 Description                                                                                                                 |
| ----------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| date        | A JavaScript `Date` object. | The time zone is set to the local operation-system time-zone value. Times in the XMP Toolkit can have up to nanosecond resolution; however, when converting to or from a JavaScript Date value, time resolution is reduced to milliseconds. |
| iso8601Date | String                      | The date-time in ISO 8601 format; for example: `"2007-04-10T17:54:50+01:00"`                                                                                                                                                                |

---

### XMPDateTime object properties

All properties are read-write, and allow you to modify the date-time value. If values are set outside the allowed range, they are automatically set to the minimum or maximum allowed value.

+--------------+--------+-------------------------------------------------------------------------------+
|   Property   |  Type  |                                  Description                                  |
+==============+========+===============================================================================+
| `year`       | Number | The year, in the range `[0000...9999]`.                                       |
+--------------+--------+-------------------------------------------------------------------------------+
| `month`      | Number | The month, in the range `[1...12]`.                                           |
+--------------+--------+-------------------------------------------------------------------------------+
| `day`        | Number | The day, in the range `[1...31]`.                                             |
+--------------+--------+-------------------------------------------------------------------------------+
| `hour`       | Number | The hour, in the range `[1...23]`.                                            |
+--------------+--------+-------------------------------------------------------------------------------+
| `minute`     | Number | The minute, in the range `[1...59]`.                                          |
+--------------+--------+-------------------------------------------------------------------------------+
| `second`     | Number | The second, in the range `[1...59]`.                                          |
+--------------+--------+-------------------------------------------------------------------------------+
| `nanosecond` | Number | The nanosecond, in the range `[0...1e+9 -1]`.                                 |
+--------------+--------+-------------------------------------------------------------------------------+
| `tzSign`     | Number | The time zone direction of offset.                                            |
|              |        | - `0`: UTC                                                                    |
|              |        | - `-1`: west                                                                  |
|              |        | - `1`: east                                                                   |
+--------------+--------+-------------------------------------------------------------------------------+
| `tzHour`     | Number | The time zone hour offset from the prime meridian, in the range `[1...23]`.   |
+--------------+--------+-------------------------------------------------------------------------------+
| `tzMinute`   | Number | The time zone minute offset from the prime meridian, in the range `[1...59]`. |
+--------------+--------+-------------------------------------------------------------------------------+

---

### XMPDateTime object functions

#### XMPDateTime.compareTo()

`XMPDateTime.compareTo(xmpDateTime)`

##### Description

Reports the time order of two date-time values.

##### Parameters

|  Parameter  |        Type        |     Description      |
| ----------- | ------------------ | -------------------- |
| xmpDataTime | XMPDateTime object | Object to compare to |

##### Returns

- `0` if the two values are the same,
- `1` if this date-time is later than the comparison value
- `-1` if this date-time is earlier than the comparison value

---

#### XMPDateTime.convertToLocalTime()

`XMPDateTime.convertToLocalTime()`

##### Description

Sets the time zone in this object to the local operating-system time zone, adjusting the time values from the previous time zone, if necessary.

##### Returns

Nothing

---

#### XMPDateTime.convertToUTCTime()

`XMPDateTime.convertToUTCTime()`

##### Description

Sets the time zone in this object to UTC (coordinated universal time), adjusting the time values from the previous time zone, if necessary.

##### Returns

Nothing

---

#### XMPDateTime.getDate()

`XMPDateTime.getDate()`

##### Description

Converts this date-time value to a JavaScript Date. The time zone is normalized (time zones are not supported in the JavaScript format), and the accuracy is reduced to milliseconds.

##### Returns

Returns a JavaScript `Date` object.

---

#### XMPDateTime.setLocalTimeZone()

`XMPDateTime.setLocalTimeZone()`

##### Description

Sets the time zone in this object to the current operation-system value, replacing any existing value.

Does not affect other fields.

##### Returns

Nothing

---

## XMPFile object

This class corresponds to the Adobe XMP Toolkit's File Handler component, which provides convenient I/O access to the main, or document level, XMP for a file.

The File Handler supports those file formats in which you can embed XMP metadata, as defined in the XMP Specification. It allows you to add XMP where none currently exists, expand existing XMP without regard to existing padding, and reconcile XMP with other metadata formats.

The XMP Toolkit also supplies the Packet Scanner as a fallback solution for unsupported file formats. It provides more limited accesses to all file formats by performing a dump file scan. It can update a file, but cannot extend the packet or reconcile other metadata formats.

The XMPScript API does not currently support retrieving thumbnails.

!!! note
    You can also use the Adobe Bridge `Metadata` object to access embedded metadata in files. It supports thumbnails and previews, and additional file formats such as PDF and Camera Raw.

    For details, see the Adobe Bridge JavaScript Guide and Adobe Bridge JavaScript Reference.

---

### XMPFile object constructors

`new XMPFile(filePath, format, openFlags)`

+-------------+------------------------------------------------------------------------------------------------------------+--------------------------------+
|  Property   |                                                    Type                                                    |          Description           |
+=============+============================================================================================================+================================+
| `filePath`  | String                                                                                                     | File path                      |
+-------------+------------------------------------------------------------------------------------------------------------+--------------------------------+
| `format`    | [File format numeric constant](#file-format-numeric-constants)                                             | Format to create as.           |
+-------------+------------------------------------------------------------------------------------------------------------+--------------------------------+
| `openFlags` | Constant. One of:                                                                                          | The open options for the file. |
|             |                                                                                                            |                                |
|             | - `XMPConst.OPEN_FOR_READ` - Open for read-only access.                                                    |                                |
|             | - `XMPConst.OPEN_FOR_UPDATE` - Open for reading and writing.                                               |                                |
|             | - `XMPConst.OPEN_ONLY_XMP` - Only the XMP is wanted, allows space/time optimizations.                      |                                |
|             | - `XMPConst.OPEN_STRICTLY` - Be strict about locating XMP and reconciling with other forms.                |                                |
|             | - `XMPConst.OPEN_USE_SMART_HANDLER` - Require the use of a smart handler. No packet scanning is performed. |                                |
|             | - `XMPConst.OPEN_USE_PACKET_SCANNING` - Force packet scanning, do not use a smart handler.                 |                                |
|             | - `XMPConst.OPEN_LIMITED_SCANNING` - Only packet-scan files known to need scanning.                        |                                |
+-------------+------------------------------------------------------------------------------------------------------------+--------------------------------+

---

### XMPFile class properties

This property is available as a static property of the XMPFile class. It is not necessary to create an instance to access it.

| Property  |  Type  |                        Descriptiopn                         |
| --------- | ------ | ----------------------------------------------------------- |
| `version` | String | The descriptive string for this version of the XMP Toolkit. |

---

### XMPFile class functions

This function is available as a static method of the XMPFile class. It is not necessary to create an instance to call it.

#### XMPFile.getFormatInfo()

`XMPFile.getFormatInfo(format)`

##### Description

Reports the supported features for the given file format.

##### Parameters

| Parameter |                              Type                               |         Description         |
| --------- | --------------------------------------------------------------- | --------------------------- |
| `format`  | [File format numeric constants](#file-format-numeric-constants) | The format to get info from |

##### Returns

A logical OR of bit-flag constants, or 0 if the format is not handled. Constants are:

- `XMPConst.HANDLER_CAN_INJECT_XMP` - Can inject first-time XMP into an existing file.
- `XMPConst.HANDLER_CAN_EXPAND` - Can expand XMP or other metadata in an existing file.
- `XMPConst.HANDLER_CAN_REWRITE` - Can copy one file to another, writing new metadata.
- `XMPConst.HANDLER_PPEFERS_IN_PLACE` - Can expand, but prefers in-place update.
- `XMPConst.HANDLER_CAN_RECONCILE` - Supports reconciliation between XMP and other forms.
- `XMPConst.HANDLER_ALLOWS_ONLY_XMP` - Allows access to just the XMP, ignoring other forms.
- `XMPConst.HANDLER_RETURNS_RAW_PACKETS` - File handler returns raw XMP packet information.
- `XMPConst.HANDLER_RETURNS_TNAIL` - File handler returns native thumbnail.
- `XMPConst.HANDLER_OWNS_FILE` - File handler does the file open and close.
- `XMPConst.HANDLER_ALLOWS_SAFE_UPDATE` - File handler allows crash-safe file updates.
- `XMPConst.HANDLER_NEEDS_READONLY_PACKET` - File format needs XMP packet to be read-only.
- `XMPConst.HANDLER_USES_SIDECAR_XMP` - Fle handler uses a sidecar file for the XMP.

---

### XMPFile object functions

#### XMPFile.canPutXMP()

`XMPFileObj.canPutXMP(xmpObj)`

`XMPFileObj.canPutXMP(xmpPacket)`

`XMPFileObj.canPutXMP(xmpBuffer)`

##### Description

Reports whether XMP metadata of a given size can be updated for this file. This is particularly important if the packet size is increased.

Considers only the length of the serialized packet; does not keep the provided XMP. Use [putXMP()](#xmpfile-putxmp) to actually update the XMP in the open file.

##### Parameters

|  Parameter  |               Type                |            Description             |
| ----------- | --------------------------------- | ---------------------------------- |
| `xmpObj`    | [XMPMeta object](#xmpmeta-object) | The XMP metadata to check          |
| `xmpPacket` | String                            | A string containing an XMP packet. |
| `xmpBuffer` | Array of Number                   | The raw XMP packet data.           |

##### Retrurns

Boolean. `true` if the given XMP can be put into this file.

---

#### XMPFile.closeFile()

`XMPFileObj.closeFile(closeFlags)`

##### Description

Closes this open file, after writing to it as necessary; that is, if the file was opened for update, and if the XMP metadata was updated or injected. The options provided when the file was opened determine whether this function reconciles the XMP with other forms of metadata; that is, whether any legacy metadata is also updated to be consistent with the XMP metadata.

##### Parameters

+--------------+--------------------------------------------------------------------------------------------+--------------------------+
|  Parameter   |                                            Type                                            |       Description        |
+==============+============================================================================================+==========================+
| `closeFlags` | Close-option constant, or `0`. One of:                                                     | Flags to use for closing |
|              | - `XMPConst.CLOSE_UPDATE_SAFELY` - Write into a temporary file then swap for crash safety. |                          |
+--------------+--------------------------------------------------------------------------------------------+--------------------------+

##### Returns

Nothing

---

#### XMPFile.getXMP()

`XMPFileObj.getXMP()`

##### Description

Retrieves and parses the existing XMP metadata from this file. If the file format contains legacy metadata in a format that is recognized by the File Handler, the function creates an XMP packet containing the metadata.

##### Returns

An [XMPMeta object](#xmpmeta-object), or `null` if the files does not contain XMP or convertible legacy metadata.

---

#### XMPFile.getPacketInfo()

`XMPFileObj.getPacketInfo()`

##### Description

Retrieves the raw XMP packet from this file, along with information about the packet. The options with which the file was opened determine whether this function reconciles other forms of metadata with the XMP.

##### Returns

An [XMPPacketInfo object](#xmppacketinfo-object), or `null` if the files does not contain XMP metadata.

---

#### XMPFile.getFileInfo()

`XMPFileObj.getFileInfo()`

##### Description

Retrieves basic information about this file.

##### Returns

An [XMPFileInfo object](#xmpfileinfo-object).

---

#### XMPFile.putXMP()

`XMPFileObj.putXMP(xmpObj)`

`XMPFileObj.putXMP(xmpPacket)`

`XMPFileObj.putXMP(xmpOBuffer)`

##### Description

##### Parameters

|  Parameter  |       Type       |                              Description                               |
| ----------- | ---------------- | ---------------------------------------------------------------------- |
| `xmpObj`    | XMPMeta object   | The XMP metadata as an XMPMeta object.                                 |
| `xmpPacket` | String           | The XMP metadata as a String containing an XMP packet.                 |
| `xmpBuffer` | Array of Numbers | The XMP metadata as an Array of Number containing raw XMP packet data. |

Supplies new XMP metadata for this file. The file is not actually written until [closeFile()](#xmpfile-closefile) is called. The options provided when the file was opened determine whether that function reconciles the XMP with other forms of metadata; that is, whether any legacy metadata is also updated to be consistent with the XMP metadata.

##### Returns

Nothing

---

## XMPFileInfo object

This object is returned by [XMPFile.getFileInfo](#getfileinfo). The read-only properties describe the file represented by the [XMPFile object](#xmpfile-object).

!!! note
    This object is not related to the XMP File Info dialog that Adobe Creative Suite 4 applications use to display metadata.

---

### XMPFileInfo object properties

+----------------+--------+------------------------------------------------------------------------------------------------------------+
|    Property    |  Type  |                                                Description                                                 |
+================+========+============================================================================================================+
| `filePath`     | String | The absolute path of the file, in JavaScript notation.                                                     |
+----------------+--------+------------------------------------------------------------------------------------------------------------+
| `format`       | Number | One of the file-format constants. See [File format numeric constants](#file-format-numeric-constants).     |
+----------------+--------+------------------------------------------------------------------------------------------------------------+
| `handlerFlags` | Number | The features that are supported for this format. A logical OR of these bit-flag constants:                 |
|                |        |                                                                                                            |
|                |        | - `XMPConst.HANDLER_CAN_INJECT_XMP` - Can inject first-time XMP into an existing file.                     |
|                |        | - `XMPConst.HANDLER_CAN_EXPAND` - Can expand XMP or other metadata in an existing file.                    |
|                |        | - `XMPConst.HANDLER_CAN_REWRITE` - Can copy one file to another, writing new metadata.                     |
|                |        | - `XMPConst.HANDLER_PPEFERS_IN_PLACE` - Can expand, but prefers in-place update.                           |
|                |        | - `XMPConst.HANDLER_CAN_RECONCILE` - Supports reconciliation between XMP and other forms.                  |
|                |        | - `XMPConst.HANDLER_ALLOWS_ONLY_XMP` - Allows access to just the XMP, ignoring other forms.                |
|                |        | - `XMPConst.HANDLER_RETURNS_RAW_PACKETS` - File handler returns raw XMP packet information.                |
|                |        | - `XMPConst.HANDLER_RETURNS_TNAIL` - File handler returns native thumbnail.                                |
|                |        | - `XMPConst.HANDLER_OWNS_FILE` - File handler does the file open and close.                                |
|                |        | - `XMPConst.HANDLER_ALLOWS_SAFE_UPDATE` - File handler allows crash-safe file updates.                     |
+----------------+--------+------------------------------------------------------------------------------------------------------------+
| `openFlags`    | Number | The options with which this file was opened. One of these constants:                                       |
|                |        |                                                                                                            |
|                |        | - `XMPConst.OPEN_FOR_READ` - Open for read-only access.                                                    |
|                |        | - `XMPConst.OPEN_FOR_UPDATE` - Open for reading and writing.                                               |
|                |        | - `XMPConst.OPEN_ONLY_XMP` - Only the XMP is wanted, allows space/time optimizations.                      |
|                |        | - `XMPConst.OPEN_STRICTLY` - Be strict about locating XMP and reconciling with other forms.                |
|                |        | - `XMPConst.OPEN_USE_SMART_HANDLER` - Require the use of a smart handler. No packet scanning is performed. |
|                |        | - `XMPConst.OPEN_USE_PACKET_SCANNING` - Force packet scanning, do not use a smart handler.                 |
|                |        | - `XMPConst.OPEN_LIMITED_SCANNING` - Only packet-scan files known to need scanning.                        |
+----------------+--------+------------------------------------------------------------------------------------------------------------+

---

## XMPIterator object

Created by a call to [XMPMeta.iterator](#iterator). Walks recursively through the properties and qualifiers of an [XMPMeta object](#xmpmeta-object), and returns them as [XMPProperty object](#xmpproperty-object).

The object has no JavaScript properties.

---

### XMPIterator object functions

#### XMPIterator.next()

`XMPIteratorObj.next()`

##### Description

Retrieves the next item in the metadata.

##### Returns

An [XMPProperty object](#xmpproperty-object), or null if there are no more items.

---

#### XMPIterator.skipSiblings()

`XMPIteratorObj.skipSiblings()`

##### Description

Skips the subtree below and the siblings of the current node on the subsequent call to [next()](#xmpiterator-next).

##### Returns

Nothing

---

#### XMPIterator.skipSubtree()

`XMPIteratorObj.skipSubtree()`

##### Description

Skips the subtree below the current node on the subsequent call to [next()](#xmpiterator-next).

##### Returns

Nothing

---

## XMPMeta object

This class provides the core services of the XMP Toolkit. The functions provide the ability to create and query metadata properties from an XMP namespace. The class also provides static functions that allow you to create and query namespaces and aliases.

There is one static property on the class that provides XMP version information; there are no JavaScript properties in the instance. The object encapsulates a set of metadata properties, which you access through the object functions.

The generic functions [getProperty()](#xmpmetaobj-getproperty), [setProperty()](#xmpmetaobj-setproperty), and [deleteProperty()](#xmpmetaobj-deleteproperty) allow you to manipulate all types of properties, when used with appropriately composed path expressions. For convenience, the object also provides more specific functions for use with specific types of properties, such as arrays.

---

### XMPMeta object constructors

To create an `XMPMeta` object, use the `new` operator. The constructor accepts an RDF/XML serialized metadata packet as a string, or as an array of numbers that contain only byte values. It returns the new object. If no argument is supplied, the new object is empty; you can use the object's functions to add namespaces and properties.

The first call to any of these constructors initializes the library by registering the standard namespaces and aliases:

```javascript
new XMPMeta ( ); // creates an empty object
new XMPMeta ( packet );
new XMPMeta ( buffer );
```

##### Parameters

| Parameter |       Type       |                                                                  Description                                                                  |
| --------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `packet`  | String           | An XML file or an XMP packet.                                                                                                                 |
| `buffer`  | Array of Numbers | The UTF-8 or UTF-16 encoded bytes of an XML file or an XMP packet. This array is the result of [XMPMeta.serializeToArray](#serializetoarray). |

---

### XMPMeta class properties

The `XMPMeta` class provides this static property. It is not necessary to create an instance to access it.

##### Properties

| Property  |  Type  |                         Description                         |
| --------- | ------ | ----------------------------------------------------------- |
| `version` | String | The descriptive string for this version of the XMP Toolkit. |

---

### XMPMeta class functions

The `XMPMeta` class provides these static functions. It is not necessary to create an instance to call them.

#### XMPMeta.deleteAlias()

`XMPMeta.deleteAlias(aliasNS, aliasProp)`

##### Description

Deletes the specified alias; does not delete the aliased property.

If the alias does not exist, does nothing.

!!! note
    Not yet implemented in the XMP Toolkit.

##### Parameters

|  Parameter  |  Type  |                                              Description                                               |
| ----------- | ------ | ------------------------------------------------------------------------------------------------------ |
| `aliasNS`   | String | The namespace URI string. See [Schema namespace string constants](#schema-namespace-string-constants). |
| `aliasProp` | String | The alias property string.                                                                             |

##### Returns

Nothing

---

#### XMPMeta.deleteNamespace()

`XMPMeta.deleteNamespace(namespaceURI)`

##### Description

Deletes a registered prefix - namespace URI pair.

!!! note
    Not yet implemented in the XMP Toolkit.

##### Parameters

|   Parameter    |  Type  |                                              Description                                               |
| -------------- | ------ | ------------------------------------------------------------------------------------------------------ |
| `namespaceURI` | String | The namespace URI string. See [Schema namespace string constants](#schema-namespace-string-constants). |

##### Returns

Nothing

---

#### XMPMeta.dumpAliases()

`XMPMeta.dumpAliases()`

##### Description

Creates and returns a human-readable string containing the list of registered aliases and their targets.

##### Returns

String

---

#### XMPMeta.dumpNamespaces()

`XMPMeta.dumpNamespaces()`

##### Description

Creates and returns a human-readable string containing the list of registered namespace URIs and their associated prefixes.

##### Returns

String

---

#### XMPMeta.getNamespacePrefix()

`XMPMeta.getNamespacePrefix(namespaceURI)`

##### Description

Retrieves the prefix associated with a registered namespace URI.

##### Parameters

|   Parameter    |  Type  |                                              Description                                               |
| -------------- | ------ | ------------------------------------------------------------------------------------------------------ |
| `namespaceURI` | String | The namespace URI string. See [Schema namespace string constants](#schema-namespace-string-constants). |

##### Returns

The prefix string followed by a colon.

---

#### XMPMeta.getNamespaceURI()

`XMPMeta.getNamespaceURI(namespacePrefix)`

##### Description

Retrieves the registered namespace URI associated with a namespace prefix.

##### Parameters

|     Parameter     |  Type  |         Description          |
| ----------------- | ------ | ---------------------------- |
| `namespacePrefix` | String | The namespace prefix string. |

##### Returns

The URI String.

---

#### XMPMeta.registerAlias()

`XMPMeta.registerAlias(aliasNS, aliasProp, actualNS, actualProp, arrayForm)`

##### Description

Defines an alias mapping from one namespace and property to another. An alias can be a direct mapping where the alias and actual property have the same data type, or it can map a simple alias to an item in an array, either the first item, or the `x-default` item in an alternate-text array.

Multiple alias names can map to the same actual property, as long as the forms match. If the same alias and form exists, the call does nothing.

##### Parameters

+--------------+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  Parameter   |                                  Type                                   |                                                                              Description                                                                               |
+==============+=========================================================================+========================================================================================================================================================================+
| `aliasNS`    | String                                                                  | The alias namespace string. See [Schema namespace string constants](#schema-namespace-string-constants).                                                               |
+--------------+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `aliasProp`  | String                                                                  | The alias property, a simple name string.                                                                                                                              |
+--------------+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `actualNS`   | [Schema namespace string constants](#schema-namespace-string-constants) | The namespace string of the aliased property.                                                                                                                          |
+--------------+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `actualProp` | String                                                                  | The aliased property, a simple name string.                                                                                                                            |
+--------------+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `arrayForm`  | Number                                                                  | The array form for a simple alias to an array item, which controls how the array is created if it is set for the first time through the alias. One of these constants: |
|              |                                                                         |                                                                                                                                                                        |
|              |                                                                         | - `XMPConst.ALIAS_TO_SIMPLE_PROP` (default) - A direct mapping. It can be simple-to-simple, array-to-array, or structure-to-structure.                                 |
|              |                                                                         | - `XMPConst.ALIAS_TO_ARRAY` - The actual is an unordered array, the alias is to the first element of the array.                                                        |
|              |                                                                         | - `XMPConst.ALIAS_TO_ORDERED_ARRAY` - The actual is an ordered array, the alias is to the first element of the array.                                                  |
|              |                                                                         | - `XMPConst.ALIAS_TO_ALT_ARRAY` - The actual is an alternate array, the alias is to the first element of the array.                                                    |
|              |                                                                         | - `XMPConst.ALIAS_TO_ALT_TEXT` - The actual is an alternate-text array (a localized property), the alias is to the x-default element of the array.                     |
+--------------+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### Returns

Nothing

---

#### XMPMeta.registerNamespace()

`XMPMeta.registerNamespace(namespaceURI, suggestedPrefix)`

##### Description

Registers a namespace with a prefix. If the suggested prefix is already in use, generates, registers, and returns a different prefix.

##### Parameters

|    Parameter    |                                  Type                                   |              Description               |
| --------------- | ----------------------------------------------------------------------- | -------------------------------------- |
| namespaceURI    | [Schema namespace string constants](#schema-namespace-string-constants) | The namespace URI string.              |
| suggestedPrefix | String                                                                  | The suggested namespace prefix string. |

##### Returns

A String containing the actual registered prefix. This is the `suggestedPrefix`, unless that one is already assigned to another namespace.

---

#### XMPMeta.resolveAlias()

`XMPMeta.resolveAlias(aliasNS, aliasProp)`

##### Description

Retrieves information about the actual property to which an alias is mapped.

##### Parameters

| Parameter |                                  Type                                   |           Description           |
| --------- | ----------------------------------------------------------------------- | ------------------------------- |
| schemaNS  | [Schema namespace string constants](#schema-namespace-string-constants) | The alias namespace URI string. |
| aliasProp | The alias property string.                                              |                                 |


#### Returns

An [XMPAliasInfo object](#xmpaliasinfo-object).

---

### XMPMeta object functions

#### XMPMeta.appendArrayItem()

`XMPMetaObj.appendArrayItem(schemaNS, arrayName[, itemOptions], itemValue[, arrayOptions])`

##### Description

Appends an item to an existing array, or creates a new array-type property if the named array does not exist.

##### Parameters

+----------------+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
|   Parameter    |                                   Type                                   |                                                                  Description                                                                   |
+================+==========================================================================+================================================================================================================================================+
| `schemaNS`     | [Schema namespace string constants](#schema-namespace-string-constants). | The namespace URI string.                                                                                                                      |
+----------------+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| `arrayName`    | String                                                                   | The array-type property name string. Can be a general path expression.                                                                         |
+----------------+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| `itemOptions`  | Number                                                                   | Optional. A flag that describes the new item, if it is being created. One of:                                                                  |
|                |                                                                          |                                                                                                                                                |
|                |                                                                          | - `0`: The default. A simple item, or the type implied by the arrayOptions value.                                                              |
|                |                                                                          | - `XMPConst.PROP_IS_ARRAY`: The item is an array (of type alt, bag, or seq).                                                                   |
|                |                                                                          | - `XMPConst.PROP_IS_STRUCT`: The item is a structure with nested fields.                                                                       |
+----------------+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| `itemValue`    | String                                                                   | The new item value string. Pass `null` for array items that do not have values.                                                                |
+----------------+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| `arrayOptions` | Number                                                                   | Optional. A flag that describes the array form. Must be provided if the array is being created; ignored if the array already exists. One of:   |
|                |                                                                          |                                                                                                                                                |
|                |                                                                          | - `XMPConst.ARRAY_IS_ORDERED` - Item order is significant. Implies `XMPConst.PROP_IS_ARRAY`.                                                   |
|                |                                                                          | - `XMPConst.ARRAY_IS_ALTERNATIVE` - Items are mutually exclusive alternates. Implies `XMPConst.PROP_IS_ARRAY` and `XMPConst.ARRAY_IS_ORDERED`. |
+----------------+--------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+

##### Returns

Nothing

---

#### XMPMeta.countArrayItems()

`XMPMetaObj.countArrayItems(schemaNS, arrayName)`

##### Description

Reports the number of items in an array-type metadata property.

##### Parameters

|  Parameter  |                                  Type                                   |                              Description                               |
| ----------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `schemaNS`  | [Schema namespace string constants](#schema-namespace-string-constants) | The namespace URI string.                                              |
| `arrayName` | String                                                                  | The array-type property name string. Can be a general path expression. |

##### Returns

Number

---

#### XMPMeta.deleteArrayItem()

`XMPMetaObj.deleteArrayItem(schemaNS, arrayName, itemIndex)`

##### Description

Deletes the metadata tree that has the given array item as its root.

##### Parameters

|  Parameter  |                                  Type                                   |                                                       Description                                                        |
| ----------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `schemaNS`  | [Schema namespace string constants](#schema-namespace-string-constants) | The namespace URI string.                                                                                                |
| `arrayName` | String                                                                  | The array-type property name string. Can be a general path expression.                                                   |
| `itemIndex` | Number                                                                  | The 1-based position index of the item. Use `XMPConst.ARRAY_LAST_ITEM` to reference the last existing item in the array. |

##### Returns

Nothing

---

#### XMPMeta.deleteProperty()

`XMPMetaObj.deleteProperty(schemaNS, propName)`

##### Description

Deletes the metadata tree that has the given property as its root. If the property does not exist, does nothing.

##### Parameters

| Parameter  |                                  Type                                   |                         Description                         |
| ---------- | ----------------------------------------------------------------------- | ----------------------------------------------------------- |
| `schemaNS` | [Schema namespace string constants](#schema-namespace-string-constants) | The namespace URI string.                                   |
| `propName` | String                                                                  | The property name string. Can be a general path expression. |


##### Returns

Nothing

---

#### XMPMeta.deleteStructField()

`XMPMetaObj.deleteStructField(schemaNS, structName, fieldNS, fieldName)`

##### Description

Deletes the metadata tree that has the given structure field as its root.

##### Parameters

|  Parameter   |                                  Type                                   |                         Description                          |
| ------------ | ----------------------------------------------------------------------- | ------------------------------------------------------------ |
| `schemaNS`   | [Schema namespace string constants](#schema-namespace-string-constants) | The namespace URI string.                                    |
| `structName` | String                                                                  | The structure name string. Can be a general path expression. |
| `fieldNS`    | [Schema namespace string constants](#schema-namespace-string-constants) | The field type namespace string.                             |
| `fieldName`  | String                                                                  | The field name string. Must be a simple XML name.            |

##### Returns

Nothing

---

#### XMPMeta.deleteQualifier()

`XMPMetaObj.deleteQualifier(schemaNS, structName, qualNS, qualName)`

##### Description

Deletes the metadata tree that has the given qualifier as its root. If the qualifier does not exist, does nothing.

##### Parameters

| Parameter  |                                  Type                                   |                         Description                          |
| ---------- | ----------------------------------------------------------------------- | ------------------------------------------------------------ |
| `schemaNS` | [Schema namespace string constants](#schema-namespace-string-constants) | The namespace URI string.                                    |
| structName | String                                                                  | The structure name string. Can be a general path expression. |
| qualNS     | String                                                                  | The URI string of the qualifier namespace.                   |
| qualName   | String                                                                  | The qualifier name string. Must be a simple XML name.        |

##### Returns

Nothing

---

#### XMPMeta.doesArrayItemExist()

`XMPMetaObj.doesArrayItemExist(schemaNS, arrayName, itemIndex)`

##### Description

Reports whether an array item with a given index currently exists in an existing array in the metadata.

##### Parameters

|  Parameter  |                                  Type                                   |                       Description                        |
| ----------- | ----------------------------------------------------------------------- | -------------------------------------------------------- |
| `schemaNS`  | [Schema namespace string constants](#schema-namespace-string-constants) | The namespace URI string.                                |
| `arrayName` | String                                                                  | The array name string. Can be a general path expression. |
| `itemIndex` | Number                                                                  | The 1-based position index of the item.                  |

##### Returns

Boolean. `true` if the array and item exist.

---

#### XMPMeta.doesPropertyExist()

`XMPMetaObj.doesPropertyExist(schemaNS, propName)`

##### Description

Reports whether a property with a given name currently exists in the metadata.

##### Parameters

| Parameter  |                                  Type                                   |                         Description                         |
| ---------- | ----------------------------------------------------------------------- | ----------------------------------------------------------- |
| `schemaNS` | [Schema namespace string constants](#schema-namespace-string-constants) | The namespace URI string.                                   |
| `propName` | String                                                                  | The property name string. Can be a general path expression. |

##### Returns

Boolean. `true` if the property exists.

---

#### XMPMeta.doesStructFieldExist()

`XMPMetaObj.deleteStructField(schemaNS, structName, fieldNS, fieldName)`

##### Description

Reports whether a structure field with a given name currently exists in the metadata.

##### Parameters

| Parameter  |                                  Type                                   |                         Description                          |
| ---------- | ----------------------------------------------------------------------- | ------------------------------------------------------------ |
| schemaNS   | [Schema namespace string constants](#schema-namespace-string-constants) | The namespace URI string.                                    |
| structName | String                                                                  | The structure name string. Can be a general path expression. |
| fieldNS    | [Schema namespace string constants](#schema-namespace-string-constants) | The field type namespace string.                             |
| fieldName  | String                                                                  | The field name string. Must be a simple XML name.            |

##### Returns

Boolean. `true` if the structure and field exist.

---

#### XMPMeta.doesQualifierExist()

`XMPMetaObj.doesQualifierExist(schemaNS, structName, qualNS, qualName)`

##### Description

Reports whether a qualifier with a given name currently exists for a given property.

##### Parameters

| Parameter  |                                  Type                                   |                         Description                          |
| ---------- | ----------------------------------------------------------------------- | ------------------------------------------------------------ |
| `schemaNS` | [Schema namespace string constants](#schema-namespace-string-constants) | The namespace URI string.                                    |
| structName | String                                                                  | The structure name string. Can be a general path expression. |
| qualNS     | String                                                                  | The URI string of the qualifier namespace.                   |
| qualName   | String                                                                  | The qualifier name string. Must be a simple XML name.        |

##### Returns

Boolean. `true` if the property and qualifier exist.

---

#### XMPMeta.dumpObject()

`XMPMetaObj.dumpObject()`

##### Description

Creates and returns a string containing the metadata content of this object as RDF.

##### Returns

String

---

#### XMPMeta.getArrayItem()

`XMPMetaObj.getArrayItem(schemaNS, arrayName, itemIndex)`

##### Description

Retrieves an item from an array-type metadata property.

##### Parameters

|  Parameter  |                                  Type                                   |                                                       Description                                                        |
| ----------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `schemaNS`  | [Schema namespace string constants](#schema-namespace-string-constants) | The namespace URI string.                                                                                                |
| `arrayName` | String                                                                  | The array name string. Can be a general path expression.                                                                 |
| `itemIndex` | Number                                                                  | The 1-based position index of the item. Use `XMPConst.ARRAY_LAST_ITEM` to reference the last existing item in the array. |

##### Returns

An [XMPProperty object](#xmpproperty-object), or `undefined` if the property is not found.

---

#### XMPMeta.getLocalizedText()

`XMPMetaObj.getLocalizedText(schemaNS, altTextName, genericLang, specificLang)`

##### Description

Retrieves the text value for a specific language from an alternate-text array. First tries to match the specific language. If not found, tries to match the generic language, if specified. If not found, gets the x-default item, if any. Otherwise, gets the first item.

##### Parameters

|   Parameter    |                                  Type                                   |                                               Description                                               |
| -------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `schemaNS`     | [Schema namespace string constants](#schema-namespace-string-constants) | The namespace URI string.                                                                               |
| `altTextName`  | String                                                                  | The alternate-text array name string. Can be a general path expression.                                 |
| `genericLang`  | String                                                                  | The name of the generic language as an RFC 3066 primary subtag. Can be `null` or the empty string.      |
| `specificLang` | String                                                                  | The name of the specific language as an RFC 3066 primary subtag; for example, en-US. Must be specified. |

##### Returns

String, or `undefined` if no matching value is not found.

---

#### XMPMeta.getProperty()

`XMPMetaObj.getProperty(schemaNS, propName[, valueType])`

##### Description

Retrieves the value and options of a metadata property. Use for top-level, simple properties, or after using the path-composition functions in the XMPUtils object.

##### Parameters

+-------------+-------------------------------------------------------------------------+-------------------------------------------------------------+
|  Parameter  |                                  Type                                   |                         Description                         |
+=============+=========================================================================+=============================================================+
| `schemaNS`  | [Schema namespace string constants](#schema-namespace-string-constants) | The namespace URI string.                                   |
+-------------+-------------------------------------------------------------------------+-------------------------------------------------------------+
| `propName`  | String                                                                  | The property name string. Can be a general path expression. |
+-------------+-------------------------------------------------------------------------+-------------------------------------------------------------+
| `valueType` | String                                                                  | Optional. The property data type, one of:                   |
|             |                                                                         |                                                             |
|             |                                                                         | - `XMPConst.STRING`                                         |
|             |                                                                         | - `XMPConst.INTEGER`                                        |
|             |                                                                         | - `XMPConst.NUMBER`                                         |
|             |                                                                         | - `XMPConst.BOOLEAN`                                        |
|             |                                                                         | - `XMPConst.XMPDATE`                                        |
+-------------+-------------------------------------------------------------------------+-------------------------------------------------------------+

##### Returns

An [XMPProperty object](#xmpproperty-object), or `undefined` if the property is not found.

---

#### XMPMeta.getStructField()

`XMPMetaObj.getStructField(schemaNS, structName, fieldNS, fieldName)`

##### Description

Retrieves a field value from within a nested structure in metadata.

##### Parameters

|  Parameter   |                                  Type                                   |                         Description                          |
| ------------ | ----------------------------------------------------------------------- | ------------------------------------------------------------ |
| `schemaNS`   | [Schema namespace string constants](#schema-namespace-string-constants) | The namespace URI string.                                    |
| `structName` | String                                                                  | The structure name string. Can be a general path expression. |
| `fieldNS`    | [Schema namespace string constants](#schema-namespace-string-constants) | The field type namespace string.                             |
| `fieldName`  | String                                                                  | The field name string. Must be a simple XML name.            |

##### Returns

An [XMPProperty object](#xmpproperty-object), or `undefined` if the property is not found.

---

#### XMPMeta.getQualifier()

`XMPMetaObj.getQualifier(schemaNS, structName, qualNS, qualName)`

##### Description

Retrieves a qualifier attached to a metadata property.

##### Parameters

|  Parameter   |                                  Type                                   |                         Description                          |
| ------------ | ----------------------------------------------------------------------- | ------------------------------------------------------------ |
| `schemaNS`   | [Schema namespace string constants](#schema-namespace-string-constants) | The namespace URI string.                                    |
| `structName` | String                                                                  | The structure name string. Can be a general path expression. |
| `qualNS`     | String                                                                  | The URI string of the qualifier namespace.                   |
| `qualName`   | String                                                                  | The qualifier name string. Must be a simple XML name.        |

##### Returns

An [XMPProperty object](#xmpproperty-object), or `undefined` if the property is not found.

---

#### XMPMeta.insertArrayItem()

`XMPMetaObj.insertArrayItem(schemaNS, arrayName, itemIndex, itemValue[, itemOptions])`

##### Description

Inserts an item into an array, before an existing item. The index positions of all later items are incremented. The array must exist.

##### Parameters

+---------------+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
|   Parameter   |                                                  Type                                                  |                                                                 Description                                                                  |
+===============+========================================================================================================+==============================================================================================================================================+
| `schemaNS`    | The namespace URI string. See [Schema namespace string constants](#schema-namespace-string-constants). |                                                                                                                                              |
+---------------+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| `arrayName`   | String                                                                                                 | The array-type property name string. Can be a general path expression.                                                                       |
+---------------+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| `itemIndex`   | Number                                                                                                 | The 1-based position index at which to insert the new item. Use `XMPConst.ARRAY_LAST_ITEM` to reference the last existing item in the array. |
+---------------+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| `itemValue`   | String                                                                                                 | The new item value. Pass `null` for array items that do not have values.                                                                     |
+---------------+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| `itemOptions` | Number                                                                                                 | Optional. A flag that describes the new item, if it is being created. One of:                                                                |
|               |                                                                                                        |                                                                                                                                              |
|               |                                                                                                        | - `0`: A simple item, the default.                                                                                                           |
|               |                                                                                                        | - `XMPConst.PROP_IS_ARRAY`: The item is an array (of type alt, bag, or seq).                                                                 |
|               |                                                                                                        | - `XMPConst.PROP_IS_STRUCT`: The item is a structure with nested fields.                                                                     |
+---------------+--------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

##### Returns

Nothing

---

#### XMPMeta.iterator()

`XMPMetaObj.iterator(options, schemaNS, propName)`

##### Description

Creates an iteration object that can iterate over the properties, arrays, and qualifiers within this metadata. Specify options, a namespace, and a property to limit the range and granularity of the resulting items.

##### Parameters

+------------+---------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Parameter  |                                                                 Type                                                                  |                                         Description                                          |
+============+=======================================================================================================================================+==============================================================================================+
| `options`  | A logical OR of these bit-flag constants:                                                                                             | The set of options that control how the iteration is performed, and how values are returned. |
|            |                                                                                                                                       |                                                                                              |
|            | - `XMPConst.ITERATOR_JUST_CHILDREN` - Limit iteration to immediate children of the root property. By default, iterates into subtrees. |                                                                                              |
|            | - `XMPConst.ITERATOR_JUST_LEAFNODES` - Limit iteration to leaf nodes. By default, iterates into all nodes of a subtree.               |                                                                                              |
|            | - `XMPConst.ITERATOR_JUST_LEAFNAMES` - Return only the leaf part of the path. By default, returns a full path.                        |                                                                                              |
|            | - `XMPConst.ITERATOR_INCLUDE_ALIASES` - Include aliases. By default, considers only actual properties.                                |                                                                                              |
|            | - `XMPConst.ITERATOR_OMIT_QUALIFIERS` - Omit qualifiers from iteration.                                                               |                                                                                              |
+------------+---------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| `schemaNS` | [Schema namespace string constants](#schema-namespace-string-constants)                                                               | The namespace URI string.                                                                    |
+------------+---------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| `propName` | String                                                                                                                                | The array-type property name string. Can be a general path expression.                       |
+------------+---------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+

##### Returns

An [XMPIterator object](#xmpiterator-object) for this metadata object.

---

#### XMPMeta.serialize()

`XMPMetaObj.serialize([options, padding, indent, newline, baseIndent])`

##### Description

Serializes this XMP metadata into a string as RDF.

##### Parameters

+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  Parameter   |                                                                                               Type                                                                                                |                                                                            Description                                                                            |
+==============+===================================================================================================================================================================================================+===================================================================================================================================================================+
| `options`    | Optional. A logical OR of these bit-flag constants:                                                                                                                                               | The set of options that control how the serialization is performed. The options must be logically consistent; if they conflict, the function throws an exception. |
|              |                                                                                                                                                                                                   |                                                                                                                                                                   |
|              | - `XMPConst.SERIALIZE_OMIT_PACKET_WRAPPER` - Do not include an XML packet wrapper.                                                                                                                |                                                                                                                                                                   |
|              | - `XMPConst.SERIALIZE_READ_ONLY_PACKET` - Create a read-only XML packet wrapper.                                                                                                                  |                                                                                                                                                                   |
|              | - `XMPConst.SERIALIZE_USE_COMPACT_FORMAT` - Use a highly compact RDF syntax and layout.                                                                                                           |                                                                                                                                                                   |
|              | - `XMPConst.SERIALIZE_USE_PLAIN_XMP` - Serialize a plain XMP (not currently supported).                                                                                                           |                                                                                                                                                                   |
|              | - `XMPConst.SERIALIZE_INCLUDE_THUMBNAIL_PAD` - Include typical space for a JPEG thumbnail in the padding if no xmp:Thumbnail property is present.                                                 |                                                                                                                                                                   |
|              | - `XMPConst.SERIALIZE_EXACT_PACKET_LENGTH` - Compute padding to meet the overall packet length provided by the padding parameter. Throws an exception if the unpadded packet exceeds this length. |                                                                                                                                                                   |
|              | - `XMPConst.SERIALIZE_WRITE_ALIAS_COMMENTS` - Include XML comments for aliases.                                                                                                                   |                                                                                                                                                                   |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `padding`    | Number                                                                                                                                                                                            | Optional.                                                                                                                                                         |
|              |                                                                                                                                                                                                   |                                                                                                                                                                   |
|              |                                                                                                                                                                                                   | - If the options value is `SERIALIZE_EXACT_PACKET_LENGTH`, this the exact length of the packet, including padding characters that are added to meet this length.  |
|              |                                                                                                                                                                                                   | - If the options value is not `SERIALIZE_EXACT_PACKET_LENGTH`, this is a number of padding characters to add.                                                     |
|              |                                                                                                                                                                                                   | - Default is `0`, meaning to use the appropriate amount of padding.                                                                                               |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `indent`     | String                                                                                                                                                                                            | Optional. The string to use as an indent. Default is two spaces.                                                                                                  |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `newline`    | String                                                                                                                                                                                            | Optional. The newline character to use. Default is `U+000A`.                                                                                                      |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `baseIndent` | Number                                                                                                                                                                                            | Optional. The level of indentation of the outermost XML element. Default is `0`.                                                                                  |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

##### Returns

String

---

#### XMPMeta.serializeToArray()

`XMPMetaObj.serializeToArray([options, padding, indent, newline, baseIndent])`

##### Description

Serializes this XMP metadata into a string as RDF, then converts that to an array of one-byte numeric values, the UTF-8 or UTF-16 encoded characters.

##### Parameters

+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  Parameter   |                                                                                               Type                                                                                                |                                                                                 Description                                                                                 |
+==============+===================================================================================================================================================================================================+=============================================================================================================================================================================+
| `options`    | A logical OR of these bit-flag constants:                                                                                                                                                         | Optional. The set of options that control how the serialization is performed. The options must be logically consistent; if they conflict, the function throws an exception. |
|              |                                                                                                                                                                                                   |                                                                                                                                                                             |
|              | - `XMPConst.SERIALIZE_OMIT_PACKET_WRAPPER` - Do not include an XML packet wrapper.                                                                                                                |                                                                                                                                                                             |
|              | - `XMPConst.SERIALIZE_READ_ONLY_PACKET` - Create a read-only XML packet wrapper.                                                                                                                  |                                                                                                                                                                             |
|              | - `XMPConst.SERIALIZE_USE_COMPACT_FORMAT` - Use a highly compact RDF syntax and layout.                                                                                                           |                                                                                                                                                                             |
|              | - `XMPConst.SERIALIZE_USE_PLAIN_XMP` - Serialize a plain XMP (not currently supported).                                                                                                           |                                                                                                                                                                             |
|              | - `XMPConst.SERIALIZE_INCLUDE_THUMBNAIL_PAD` - Include typical space for a JPEG thumbnail in the padding if no xmp:Thumbnail property is present.                                                 |                                                                                                                                                                             |
|              | - `XMPConst.SERIALIZE_EXACT_PACKET_LENGTH` - Compute padding to meet the overall packet length provided by the padding parameter. Throws an exception if the unpadded packet exceeds this length. |                                                                                                                                                                             |
|              | - `XMPConst.SERIALIZE_WRITE_ALIAS_COMMENTS` - Include XML comments for aliases.                                                                                                                   |                                                                                                                                                                             |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `padding`    | Number                                                                                                                                                                                            | Optional.                                                                                                                                                                   |
|              |                                                                                                                                                                                                   |                                                                                                                                                                             |
|              |                                                                                                                                                                                                   | - If the options value is `SERIALIZE_EXACT_PACKET_LENGTH`, this the exact length of the packet, including padding characters that are added to meet this length.            |
|              |                                                                                                                                                                                                   | - If the options value is not `SERIALIZE_EXACT_PACKET_LENGTH`, this is a number of padding characters to add.                                                               |
|              |                                                                                                                                                                                                   | - Default is `0`, meaning to use the appropriate amount of padding.                                                                                                         |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `indent`     | String                                                                                                                                                                                            | Optional. The string to use as an indent. Default is two spaces.                                                                                                            |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `newline`    | String                                                                                                                                                                                            | Optional. The newline character to use. Default is `U+000A`.                                                                                                                |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `baseIndent` | Number                                                                                                                                                                                            | Optional. The level of indentation of the outermost XML element. Default is `0`.                                                                                            |
+--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

##### Returns

An Array of Numbers.

---

#### XMPMeta.setArrayItem()

`XMPMetaObj.setArrayItem(schemaNS, arrayName, itemIndex, itemValue[, itemOptions])`

##### Description

Replaces an item within an array, or appends an item. The array must exist. To create an item, [appendArrayItem()](#xmpmetaobj-appendarrayitem) and [insertArrayItem()](#xmpmetaobj-insertarrayitem) are preferred.

##### Parameters

+---------------+------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
|   Parameter   |                                     Type                                     |                                                                Description                                                                 |
+===============+==============================================================================+============================================================================================================================================+
| `schemaNS`    | [Schema namespace string constants](#schema-namespace-string-constants)      | The namespace URI string.                                                                                                                  |
+---------------+------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| `arrayName`   | String                                                                       | The array-type property name string. Can be a general path expression.                                                                     |
+---------------+------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| `itemIndex`   | Number                                                                       | The 1-based position index at which to insert the new item. Use `XMPConst.ARRAY_LAST_ITEM` to replace the last existing item in the array. |
+---------------+------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| `itemValue`   | String                                                                       | The new item value string. Pass `null` for array items that do not have values.                                                            |
+---------------+------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
| `itemOptions` | A flag that describes the new item, if it is being created. One of:          | Optional                                                                                                                                   |
|               |                                                                              |                                                                                                                                            |
|               | - `0`: A simple item, the default.                                           |                                                                                                                                            |
|               | - `XMPConst.PROP_IS_ARRAY`: The item is an array (of type alt, bag, or seq). |                                                                                                                                            |
|               | - `XMPConst.PROP_IS_STRUCT`: The item is a structure with nested fields.     |                                                                                                                                            |
+---------------+------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+

##### Returns

Nothing

---

#### XMPMeta.setLocalizedText()

`XMPMetaObj.setLocalizedText(schemaNS, altTextName, genericLang, specificLang, itemValue, setOptions)`

##### Description

Sets the text value for a specific language in an alternate-text array. Handles special cases for the x-default item.

##### Parameters

|   Parameter    |                                  Type                                   |                                               Description                                               |
| -------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `schemaNS`     | [Schema namespace string constants](#schema-namespace-string-constants) | The namespace URI string.                                                                               |
| `altTextName`  | String                                                                  | The name string of the alternate-text array. Can be a general path expression.                          |
| `genericLang`  | String                                                                  | The name of the generic language as an RFC 3066 primary subtag. Can be null or the empty string.        |
| `specificLang` | String                                                                  | The name of the specific language as an RFC 3066 primary subtag; for example, en-US. Must be specified. |
| `itemValue`    | String                                                                  | The new string value.                                                                                   |
| `setOptions`   | Unknown                                                                 | Not used.                                                                                               |

##### Returns

Nothing

---

#### XMPMeta.setStructField()

`XMPMetaObj.setStructField(schemaNS, structName, fieldNS, fieldName, fieldValue[, options])`

##### Description

Sets the value of a field within a structure-type property, or creates a new field if the named field does not exist in the structure, or creates a new structure containing the named field if the named structure does not exist.

##### Parameters

+--------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
|  Parameter   |                                     Type                                      |                                 Description                                 |
+==============+===============================================================================+=============================================================================+
| `schemaNS`   | [Schema namespace string constants](#schema-namespace-string-constants)       | The namespace URI string.                                                   |
+--------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| `structName` | String                                                                        | The name string of an existing structure. Can be a general path expression. |
+--------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| `fieldNS`    | [Schema namespace string constants](#schema-namespace-string-constants)       | The field type namespace string.                                            |
+--------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| `fieldName`  | String                                                                        | The field name string. Must be a simple XML name.                           |
+--------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| `fieldValue` | String                                                                        | The new field value string. Pass null for fields that do not have values.   |
+--------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------+
| `options`    | Option flags that describe a new structure. One of:                           | Optional. Used only if the structure is being created.                      |
|              |                                                                               |                                                                             |
|              | - `0` - A simple item, the default.                                           |                                                                             |
|              | - `XMPConst.PROP_IS_ARRAY` - The item is an array (of type alt, bag, or seq). |                                                                             |
|              | - `XMPConst.PROP_IS_STRUCT` - The item is a structure with nested fields.     |                                                                             |
+--------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------+

##### Returns

Nothing

---

#### XMPMeta.setQualifier()

`XMPMetaObj.setQualifier(schemaNS, propName, qualNS, qualName, qualValue[, options])`

##### Description

Attaches a new qualifier to a metadata property. A qualifier can be added to a simple property, an array item, a struct field, or another qualifier.

##### Parameters

+-------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
|  Parameter  |                                     Type                                      |                                             Description                                             |
+=============+===============================================================================+=====================================================================================================+
| `schemaNS`  | [Schema namespace string constants](#schema-namespace-string-constants)       | The namespace URI string.                                                                           |
+-------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| `propName`  | String                                                                        | The name string of an existing property. Can be a general path expression.                          |
+-------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| `qualNS`    | String                                                                        | The URI of the qualifier namespace. Has the same URI and prefix usage as a schema namespace.        |
+-------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| `qualName`  | String                                                                        | The name of the qualifier. Must be a simple XML name. Has the same prefix usage as a property name. |
+-------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| `qualValue` | String                                                                        | The new qualifier value string. Pass null for qualifiers that do not have values.                   |
+-------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| `options`   | Option flags that describe the qualifier. One of:                             | Optional. Used only if the qualifier is being created.                                              |
|             |                                                                               |                                                                                                     |
|             | - `0` - A simple item, the default.                                           |                                                                                                     |
|             | - `XMPConst.PROP_IS_ARRAY` - The item is an array (of type alt, bag, or seq). |                                                                                                     |
|             | - `XMPConst.PROP_IS_STRUCT` - The item is a structure with nested fields.     |                                                                                                     |
+-------------+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+

##### Returns

Nothing

---

#### XMPMeta.setProperty()

`XMPMetaObj.setProperty(schemaNS, propName, propValue[, setOptions, valueType])`

##### Description

Sets the value of a simple metadata property, creating the property if necessary, or creates a new array or structure property. For creating array and structure properties, [setArrayItem()](#xmpmetaobj-setarrayitem) and [setStructField()](#xmpmetaobj-setstructfield) are preferred. Use this call to create or set top-level, simple properties, or after using the path-composition functions in the [XMPUtils object](#xmputils-object).

##### Parameters

+--------------+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
|  Parameter   |                                     Type                                      |                                            Description                                            |
+==============+===============================================================================+===================================================================================================+
| `schemaNS`   | [Schema namespace string constants](#schema-namespace-string-constants)       | The namespace URI string.                                                                         |
+--------------+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| `propName`   | String                                                                        | The property name string. Can be a general path expression.                                       |
+--------------+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| `propValue`  | String                                                                        | The new property value string. Pass null to create an array or non-leaf level structure property. |
+--------------+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| `setOptions` | A simple-valued property. Other constant values are:                          | Optional. The type of property to create, if the named property does not exist. Default is `0`.   |
|              |                                                                               |                                                                                                   |
|              | - `0` - A simple item, the default.                                           |                                                                                                   |
|              | - `XMPConst.PROP_IS_ARRAY` - The item is an array (of type alt, bag, or seq). |                                                                                                   |
|              | - `XMPConst.PROP_IS_STRUCT` - The item is a structure with nested fields.     |                                                                                                   |
+--------------+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| `valueType`  | The property data type. One of:                                               | Optional. If supplied, the value is converted to this type.                                       |
|              |                                                                               |                                                                                                   |
|              | - `XMPConst.STRING`                                                           |                                                                                                   |
|              | - `XMPConst.INTEGER`                                                          |                                                                                                   |
|              | - `XMPConst.NUMBER`                                                           |                                                                                                   |
|              | - `XMPConst.BOOLEAN`                                                          |                                                                                                   |
|              | - `XMPConst.XMPDATE`                                                          |                                                                                                   |
+--------------+-------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+

##### Returns

Nothing

---

#### XMPMeta.sort()

`XMPMetaObj.sort()`

##### Description

Sorts the XMP contents alphabetically.

- At the top level, sorts namespaces by their prefixes.
- Within a namespace, sorts top-level properties are sorted by name.
- Within a struct, sorts fields by their qualified name (that is, the XML `prefix:local` form.)
- Sorts unordered arrays of simple items by value.
- Sorts language alternative arrays by the `xml:lang` qualifiers, with the `"x-default"` item placed first.

##### Returns

Nothing

---

## XMPPacketInfo object

This object is returned by [XMPFile.getPacketInfo()](#getpacketinfo). The read-only properties describe the XMP packet for the file represented by the [XMPFile object](#xmpfile-object).

---

### XMPPacketInfo object properties

+-------------+---------+---------------------------------------------------------------------+
|  Parameter  |  Type   |                             Description                             |
+=============+=========+=====================================================================+
| `charForm`  | Number  | The character encoding in the packet, one of:                       |
|             |         | - `0` - UTF8                                                        |
|             |         | - `2` - UTF-16, MSB-first (big-endian)                              |
|             |         | - `3` - UTF-16, LSB-first (little-endian)                           |
|             |         | - `4` - UTF 32, MSB-first (big-endian)                              |
|             |         | - `5` - UTF 32, LSB-first (little-endian)                           |
+-------------+---------+---------------------------------------------------------------------+
| `length`    | Number  | The length of the packet in bytes.                                  |
+-------------+---------+---------------------------------------------------------------------+
| `offset`    | Number  | The byte-offset from the start of the file where the packet begins. |
+-------------+---------+---------------------------------------------------------------------+
| `packet`    | String  | The raw packet data.                                                |
+-------------+---------+---------------------------------------------------------------------+
| `padSize`   | Number  | The packet's padding size in bytes, 0 if unknown.                   |
+-------------+---------+---------------------------------------------------------------------+
| `writeable` | Boolean | If `true`, the packet is writeable.                                 |
+-------------+---------+---------------------------------------------------------------------+

---

## XMPProperty object

This object is returned by various property accessor functions of the [XMPMeta object](#xmpmeta-object), such as
[getProperty](#getproperty). The read-only properties describe a metadata property.

---

### XMPProperty object properties

+-----------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter |  Type   |                                                                                                       Description                                                                                                        |
+===========+=========+==========================================================================================================================================================================================================================+
| locale    | String  | The language of the property value. This value is set by calls to [getLocalizedText()](#xmpmetaobj-getlocalizedtext), which assigns the language of the selected alternative text item, if an appropriate item is found. |
+-----------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| namespace | String  | The namespace of the property; see [Schema namespace string constants](#schema-namespace-string-constants). Typically used when browsing metadata with an [XMPIterator object](#xmpiterator-object).                     |
+-----------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| options   | Number  | A constant that describes the property type, 0 for a simple property. Constants are:                                                                                                                                     |
|           |         |                                                                                                                                                                                                                          |
|           |         | - `XMPConst.PROP_IS_ARRAY` - The property is an array (of type alt, bag, or seq).                                                                                                                                        |
|           |         | - `XMPConst.PROP_IS_STRUCT` - The property is a structure with nested fields.                                                                                                                                            |
+-----------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| path      | String  | The property path, including the property name. For a simple property, the entire path is the property name.                                                                                                             |
+-----------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| value     | Variant | The value of the property, if any. Arrays and non-leaf levels of structures do not have values.                                                                                                                          |
+-----------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

---

## XMPUtils object

This class provides additional utility functions for the XMP Toolkit, layered upon the functionality of the [XMPMeta object](#xmpmeta-object). It has only static functions, you cannot create an instance.

Path-composition functions such as [composeArrayItemPath()](#xmputils-composearrayitempath), provide support for composing path expressions to deeply nested properties, which you can then pass to the accessor functions in XMPMeta object, such as xmpmetaobj-getProperty.

Higher-level functions such as xmputils-duplicateSubtree allow you to manipulate the metadata tree in an XMPMeta object.

---

### XMPUtils class functions

#### XMPUtils.appendProperties()

`XMPUtils.appendProperties(source, dest, options)`

##### Description

Copies properties from a source XMPMeta object and appends them to a destination XMPMeta object.

##### Parameters

+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| Parameter |                                                                                                            Type                                                                                                            |                           Description                            |
+===========+============================================================================================================================================================================================================================+==================================================================+
| `source`  | [XMPMeta Object](#xmpmeta-object)                                                                                                                                                                                          | The source XMPMeta object.                                       |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| `dest`    | [XMPMeta Object](#xmpmeta-object)                                                                                                                                                                                          | The destination XMPMeta object.                                  |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+
| `options` | A logical OR of these bit-flag constants:                                                                                                                                                                                  | Option flags that control the copying operation. Default is `0`. |
|           |                                                                                                                                                                                                                            |                                                                  |
|           | - `XMPConst.APPEND_ALL_PROPERTIES` - Include both internal and external properties. By default, copies only external properties. This applies only to top-level properties.                                                |                                                                  |
|           | - `XMPConst.APPEND_REPLACE_OLD_VALUES` - Replace the values of existing properties with the value from the source object. By default, existing values are retained. This applies to properties at all levels of hierarchy. |                                                                  |
|           | - `XMPConst.APPEND_DELETE_EMPTY_VALUES` - Delete properties if the new value is empty.                                                                                                                                     |                                                                  |
+-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------+

##### Returns

Nothing

---

#### XMPUtils.catenateArrayItems()

`XMPUtils.catenateArrayItems(xmpObj, schemaNS, arrayName, separator, quotes, options)`

##### Description

Concatenates a set of array item values into a single string. The resulting string can be separated back out into array items using [separateArrayItems()](#xmputils-separatearrayitems).

##### Parameters

|  Parameter  |                                  Type                                   |                                                                                                                                                              Description                                                                                                                                                              |
| ----------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `xmpObj`    | [XMPMeta Object](#xmpmeta-object)                                       | The XMPMeta object containing the array.                                                                                                                                                                                                                                                                                              |
| `schemaNS`  | [Schema namespace string constants](#schema-namespace-string-constants) | The namespace URI string.                                                                                                                                                                                                                                                                                                             |
| `arrayName` | String                                                                  | The array property name string. Can be a general path expression. Each item in the array must be a simple string value.                                                                                                                                                                                                               |
| `separator` | String                                                                  | The string used to separate the items in the result string. Default is '; ', an ASCII semicolon and space (U+003B,U+0020).                                                                                                                                                                                                            |
| `quotes`    | String                                                                  | The character used to quote items that contain a separator. Default is '"', an ASCII double quote (U+0022).                                                                                                                                                                                                                           |
| `options`   | Constant value                                                          | Option flag that controls the concatenation. The constant value `XMPConst.SEPARATE_ALLOW_COMMAS` - Allow commas in item values (such as "LastName, FirstName"). This option must be set the same way in this function and in [separateArrayItems()](#xmputils-separatearrayitems) to reconstruct the items correctly. Default is `0`. |

##### Returns

String

---

#### XMPUtils.composeArrayItemPath()

`XMPUtils.composeArrayItemPath(schemaNS, arrayName, itemIndex)`

##### Description

Creates and returns a string containing the path expression for an item in an array, using the registered prefix for the namespace, in the form:

```javascript
schemaNS:arrayName[itemIndex]
```

##### Parameters

|  Parameter  |                                  Type                                   |                                                                                     Description                                                                                      |
| ----------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `schemaNS`  | [Schema namespace string constants](#schema-namespace-string-constants) | The namespace URI string.                                                                                                                                                            |
| `arrayName` | String                                                                  | The array property name string. Can be a general path expression.                                                                                                                    |
| `itemIndex` | Number                                                                  | The 1-based position index of the item. Use `XMPConst.ARRAY_LAST_ITEM` to reference the last existing item in the array. In this case, the resulting path is `ns:arrayName[last()]`. |

##### Returns

String

---

#### XMPUtils.composeFieldSelector()

`XMPUtils.composeFieldSelector(schemaNS, arrayName, fieldNS, fieldName, fieldValue)`

##### Description

Creates and returns a string containing the path expression to select an alternate item by a field's value, using the registered prefixes for the namespaces, in the form:

```javascript
schemaNS:arrayName[fieldNS:fieldName='fieldValue']
```

##### Parameters

|  Parameter   |                                  Type                                   |                            Description                            |
| ------------ | ----------------------------------------------------------------------- | ----------------------------------------------------------------- |
| `schemaNS`   | [Schema namespace string constants](#schema-namespace-string-constants) | The namespace URI string.                                         |
| `arrayName`  | String                                                                  | The array property name string. Can be a general path expression. |
| `fieldNS`    | String                                                                  | The field namespace URI string.                                   |
| `fieldName`  | String                                                                  | The field name. Must be a simple XML name.                        |
| `fieldValue` | Any                                                                     | The desired field value.                                          |

##### Returns

String

---

#### XMPUtils.composeLanguageSelector()

`XMPUtils.composeLanguageSelector(schemaNS, arrayName, locale)`

##### Description

Creates and returns a string containing the path expression to select an alternate item in an alt text array by language, using the registered prefix for the namespace, in the form:

```javascript
schemaNS:arrayName[@xml:lang='langName']
```

!!! note
    Do not use this in place of getLocalizedText() or setLocalizedText().

    Those functions provide extra logic to choose the appropriate language and maintain consistency with the x-default value. This function provides a path expression for an explicit language, and only for that language.

##### Parameters

|  Parameter  |                                  Type                                   |                            Description                            |
| ----------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------- |
| `schemaNS`  | [Schema namespace string constants](#schema-namespace-string-constants) | The namespace URI string.                                         |
| `arrayName` | String                                                                  | The array property name string. Can be a general path expression. |
| `locale`    | String                                                                  | The RFC3066 locale code string for the desired language.          |

##### Returns

String

---

#### XMPUtils.composeStructFieldPath()

`XMPUtils.composeStructFieldPath(schemaNS, structName, fieldNS, fieldName)`

##### Description

Creates and returns a string containing the path expression for a field in a structure, using the registered prefixes for the namespaces, in the form:

```javascript
schemaNS:structName/fieldNS:fieldName
```

##### Parameters

|  Parameter   |                                  Type                                   |                              Description                              |
| ------------ | ----------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `schemaNS`   | [Schema namespace string constants](#schema-namespace-string-constants) | The namespace URI string.                                             |
| `structName` | String                                                                  | The structure property name string. Can be a general path expression. |
| `fieldNS`    | String                                                                  | The field namespace URI string.                                       |
| `fieldName`  | String                                                                  | The field name. Must be a simple XML name.                            |

##### Returns

String

---

#### XMPUtils.composeQualifierPath()

`XMPUtils.composeQualifierPath(schemaNS, propName, qualNS, qualName)`

##### Description

Creates and returns a string containing the path expression for a qualifier attached to a property, using the registered prefix for the namespace, in the form:

```javascript
schemaNS:propName/?qualNS:qualName
```

##### Parameters

| Parameter  |                                  Type                                   |                         Description                         |
| ---------- | ----------------------------------------------------------------------- | ----------------------------------------------------------- |
| `schemaNS` | [Schema namespace string constants](#schema-namespace-string-constants) | The namespace URI string.                                   |
| `propName` | String                                                                  | The property name string. Can be a general path expression. |
| `qualNS`   | String                                                                  | The qualifier namespace URI string.                         |
| `qualName` | String                                                                  | The qualifier name. Must be a simple XML name.              |

##### Returns

String

---

#### XMPUtils.duplicateSubtree()

`XMPUtils.duplicateSubtree(source, dest, sourceNS, sourceRoot, destNS, destRoot, options)`

##### Description

Copies properties in the specified subtree from a source [XMPMeta object](#xmpmeta-object) and adds them into a destination [XMPMeta object](#xmpmeta-object).

##### Parameters

+--------------+-------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  Parameter   |                                  Type                                   |                                                                                                        Description                                                                                                         |
+==============+=========================================================================+============================================================================================================================================================================================================================+
| `source`     | [XMPMeta Object](#xmpmeta-object)                                       | The source XMPMeta object.                                                                                                                                                                                                 |
+--------------+-------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `dest`       | [XMPMeta Object](#xmpmeta-object)                                       | The destination XMPMeta object.                                                                                                                                                                                            |
+--------------+-------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `sourceNS`   | [Schema namespace string constants](#schema-namespace-string-constants) | The source namespace URI string.                                                                                                                                                                                           |
+--------------+-------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `sourceRoot` | String                                                                  | The property name string for the root location of the source subtree. Can be a general path expression.                                                                                                                    |
+--------------+-------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `destNS`     | [Schema namespace string constants](#schema-namespace-string-constants) | The destination namespace URI string.                                                                                                                                                                                      |
+--------------+-------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `destRoot`   | String                                                                  | Optional. The property name string for the root location of the destination subtree. Can be a general path expression. Default is the source root location.                                                                |
+--------------+-------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `options`    | A logical OR of these bit-flag constants:                               | Option flags that control the copying operation. Default is `0`.                                                                                                                                                           |
|              |                                                                         |                                                                                                                                                                                                                            |
|              |                                                                         | - `XMPConst.APPEND_ALL_PROPERTIES` - Include both internal and external properties. By default, copies only external properties. This applies only to top-level properties.                                                |
|              |                                                                         | - `XMPConst.APPEND_REPLACE_OLD_VALUES` - Replace the values of existing properties with the value from the source object. By default, existing values are retained. This applies to properties at all levels of hierarchy. |
|              |                                                                         | - `XMPConst.APPEND_DELETE_EMPTY_VALUES` - Delete properties if the new value is empty.                                                                                                                                     |
+--------------+-------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

##### Returns

Nothing

---

#### XMPUtils.removeProperties()

`XMPUtils.removeProperties(xmpObj, schemaNS, propName, options)`

##### Description

Removes multiple properties from an [XMPMeta object](#xmpmeta-object).

If both the namespace and property name are supplied, removes the property if it is external, even if it is an alias. If it is internal, removes it if the option `XMPConst.REMOVE_ALL_PROPERTIES` is specified.

If the namespace is supplied and the property name is not, removes all external properties in the namespace, and optionally all internal properties. Removes aliases only if the option `XMPConst.REMOVE_INCLUDE_ALIASES` is specified.

If neither the namespace nor the property name are supplied, removes all external properties, and optionally all internal properties. Aliases are handled implicitly, because the associated actual is removed.

##### Parameters

+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter  |                                                                             Type                                                                              |                                                                            Description                                                                            |
+============+===============================================================================================================================================================+===================================================================================================================================================================+
| `xmpObj`   | [XMPMeta Object](#xmpmeta-object)                                                                                                                             | The object to remove properties from                                                                                                                              |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `schemaNS` | [Schema namespace string constants](#schema-namespace-string-constants). Optional. The namespace URI string. Must be supplied if a property name is supplied. |                                                                                                                                                                   |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `propName` | String                                                                                                                                                        | Optional. The property name string. Can be a general path expression.                                                                                             |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `options`  | A logical OR of these bit-flag constants:                                                                                                                     | Option flags that control the deletion operation. Default is `0`.                                                                                                 |
|            |                                                                                                                                                               |                                                                                                                                                                   |
|            |                                                                                                                                                               | - `XMPConst.REMOVE_ALL_PROPERTIES` - Remove internal and external properties. By default, removes only external properties. Applies only to top-level properties. |
|            |                                                                                                                                                               | - `XMPConst.REMOVE_INCLUDE_ALIASES` - Remove aliases defined in the namespace. If the property name is supplied, removes it regardless of this option.            |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

##### Returns

Nothing

---

#### XMPUtils.separateArrayItems()

`XMPUtils.separateArrayItems(xmpObj, schemaNS, arrayName, arrayOptions, concatString)`

##### Description

Updates individual array item strings in the XMPMeta object from a concatenated string returned by [catenateArrayItems()](#xmputils-catenatearrayitems). Recognizes a large set of separator characters, including semicolons, commas, tab, return, linefeed, and multiple spaces.

##### Parameters

+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
|   Parameter    |                                                                                                            Type                                                                                                            |                                                        Description                                                        |
+================+============================================================================================================================================================================================================================+===========================================================================================================================+
| `xmpObj`       | [XMPMeta Object](#xmpmeta-object)                                                                                                                                                                                          | The object to separate items from                                                                                         |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| `schemaNS`     | The namespace URI string. See [Schema namespace string constants](#schema-namespace-string-constants).                                                                                                                     |                                                                                                                           |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| `arrayName`    | String                                                                                                                                                                                                                     | The array property name string. Can be a general path expression. Each item in the array must be a simple string value.   |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| `arrayOptions` | A logical OR of these bit-flag constants:                                                                                                                                                                                  | Option flags that control how the array property is updated from the separated string. Default is `0`.                    |
|                |                                                                                                                                                                                                                            |                                                                                                                           |
|                | - `XMPConst.APPEND_ALL_PROPERTIES` - Include both internal and external properties. By default, copies only external properties. This applies only to top-level properties.                                                |                                                                                                                           |
|                | - `XMPConst.APPEND_REPLACE_OLD_VALUES` - Replace the values of existing properties with the value from the source object. By default, existing values are retained. This applies to properties at all levels of hierarchy. |                                                                                                                           |
|                | - `XMPConst.APPEND_DELETE_EMPTY_VALUES` - Delete properties if the new value is empty.                                                                                                                                     |                                                                                                                           |
|                | - `XMPConst.SEPARATE_ALLOW_COMMAS` - Allow commas in item values. If not specified, an item containing a comma (such as "LastName, FirstName") is separated into two array items.                                          |                                                                                                                           |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| `concatString` | String                                                                                                                                                                                                                     | The string containing the concatenated array values, as returned by [catenateArrayItems()](#xmputils-catenatearrayitems). |
+----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+

##### Returns

Nothing
