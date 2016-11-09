.. _file-and-folder-supported-encoding-names:

File- and Folder-supported encoding names
=========================================
The following list of names is a basic set of encoding names supported by the File object. Some of the
character encoders are built in, while the operating system is queried for most of the other encoders.
Depending on the language packs installed, some of the encodings may not be available. Names that refer
to the same encoding are listed in one line. Underlines are replaced with dashes before matching an
encoding name.

The File object processes an extended Unicode character with a value greater that 65535 as a Unicode
surrogate pair (two characters in the range between 0xD700-0xDFFF).

Built-in encodings are:

US-ASCII, ASCII,ISO646-US,I SO-646.IRV:1991, ISO-IR-6,
ANSI-X3.4-1968,CP367,IBM367,US,ISO646.1991-IRV
UCS-2,UCS2, ISO-10646-UCS-2
UCS2LE,UCS-2LE,ISO-10646-UCS-2LE
UCS2BE,UCS-2BE,ISO-10646-UCS-2BE
UCS-4,UCS4, ISO-10646-UCS-4
UCS4LE,UCS-4LE,ISO-10646-UCS-4LE
UCS4BE,UCS-4BE,ISO-10646-UCS-4BE
UTF-8,UTF8,UNICODE-1-1-UTF-8,UNICODE-2-0-UTF-8,X-UNICODE-2-0-UTF-8
UTF16,UTF-16,ISO-10646-UTF-16
UTF16LE,UTF-16LE,ISO-10646-UTF-16LE
UTF16BE,UTF-16BE,ISO-10646-UTF-16BE
CP1252,WINDOWS-1252,MS-ANSI
ISO-8859-1,ISO-8859-1,ISO-8859-1:1987,ISO-IR-100,LATIN1
MACINTOSH,X-MAC-ROMAN
BINARY

The ASCII encoder raises errors for characters greater than 127, and the BINARY encoder simply converts
between bytes and Unicode characters by using the lower 8 bits. The latter encoder is convenient for
reading and writing binary data.

.. _additional-encodings:

Additional encodings
--------------------
In Windows, all encodings use code pages, which are assigned numeric values. The usual Western
character set that Windows uses, for example, is the code page 1252. You can select Windows code pages
by prepending the number of the code page with "CP" or "WINDOWS": for example, "CP1252" for the code
page 1252. The File object has many other built-in encoding names that match predefined code page
numbers. If a code page is not present, the encoding cannot be selected.

In Mac OS, you can select encoders by name rather than by code page number. The File object queries
Mac OS directly for an encoder. As far as Mac OS character sets are identical with Windows code pages,
Mac OS also knows the Windows code page numbers.

In UNIX, the number of available encoders depends on the installation of the ``iconv`` library.

Common encoding names
*********************
The following encoding names are implemented both in Windows and in Mac OS::

    UTF-7,UTF7,UNICODE-1-1-UTF-7,X-UNICODE-2-0-UTF-7
    ISO-8859-2,ISO-8859-2,ISO-8859-2:1987,ISO-IR-101,LATIN2
    ISO-8859-3,ISO-8859-3,ISO-8859-3:1988,ISO-IR-109,LATIN3
    ISO-8859-4,ISO-8859-4,ISO-8859-4:1988,ISO-IR-110,LATIN4,BALTIC
    ISO-8859-5,ISO-8859-5,ISO-8859-5:1988,ISO-IR-144,CYRILLIC
    ISO-8859-6,ISO-8859-6,ISO-8859-6:1987,ISO-IR-127,ECMA-114,ASMO-708,ARABIC
    ISO-8859-7,ISO-8859-7,ISO-8859-7:1987,ISO-IR-126,ECMA-118,ELOT-928,GREEK8,GREEK
    ISO-8859-8,ISO-8859-8,ISO-8859-8:1988,ISO-IR-138,HEBREW
    ISO-8859-9,ISO-8859-9,ISO-8859-9:1989,ISO-IR-148,LATIN5,TURKISH
    ISO-8859-10,ISO-8859-10,ISO-8859-10:1992,ISO-IR-157,LATIN6
    ISO-8859-13,ISO-8859-13,ISO-IR-179,LATIN7
    ISO-8859-14,ISO-8859-14,ISO-8859-14,ISO-8859-14:1998,ISO-IR-199,LATIN8
    ISO-8859-15,ISO-8859-15,ISO-8859-15:1998,ISO-IR-203
    ISO-8859-16,ISO-885,ISO-885,MS-EE
    CP850,WINDOWS-850,IBM850
    CP866,WINDOWS-866,IBM866
    CP932,WINDOWS-932,SJIS,SHIFT-JIS,X-SJIS,X-MS-SJIS,MS-SJIS,MS-KANJI
    CP936,WINDOWS-936,GBK,WINDOWS-936,GB2312,GB-2312-80,ISO-IR-58,CHINESE
    CP949,WINDOWS-949,UHC,KSC-5601,KS-C-5601-1987,KS-C-5601-1989,ISO-IR-149,KOREAN
    CP950,WINDOWS-950,BIG5,BIG-5,BIG-FIVE,BIGFIVE,CN-BIG5,X-X-BIG5
    CP1251,WINDOWS-1251,MS-CYRL
    CP1252,WINDOWS-1252,MS-ANSI
    CP1253,WINDOWS-1253,MS-GREEK
    CP1254,WINDOWS-1254,MS-TURK
    CP1255,WINDOWS-1255,MS-HEBR
    CP1256,WINDOWS-1256,MS-ARAB
    CP1257,WINDOWS-1257,WINBALTRIM
    CP1258,WINDOWS-1258
    CP1361,WINDOWS-1361,JOHAB
    EUC-JP,EUCJP,X-EUC-JP
    EUC-KR,EUCKR,X-EUC-KR
    HZ,HZ-GB-2312
    X-MAC-JAPANESE
    X-MAC-GREEK
    X-MAC-CYRILLIC
    X-MAC-LATIN
    X-MAC-ICELANDIC
    X-MAC-TURKISH

Additional Windows encoding names:
***********************************
::

    CP437,IBM850,WINDOWS-437
    CP709,WINDOWS-709,ASMO-449,BCONV4
    EBCDIC
    KOI-8R
    KOI-8U
    ISO-2022-JP
    ISO-2022-KR


Additional Mac OS encoding names
***********************************
These names are alias names for encodings that Mac OS might know::

    TIS-620,TIS620,TIS620-0,TIS620.2529-1,TIS620.2533-0,TIS620.2533-1,ISO-IR-166
    CP874,WINDOWS-874
    JP,JIS-C6220-1969-RO,ISO646-JP,ISO-IR-14
    JIS-X0201,JISX0201-1976,X0201
    JIS-X0208,JIS-X0208-1983,JIS-X0208-1990,JIS0208,X0208,ISO-IR-87
    JIS-X0212,JIS-X0212.1990-0,JIS-X0212-1990,X0212,ISO-IR-159
    CN,GB-1988-80,ISO646-CN,ISO-IR-57
    ISO-IR-16,CN-GB-ISOIR165
    KSC-5601,KS-C-5601-1987,KS-C-5601-1989,ISO-IR-149
    EUC-CN,EUCCN,GB2312,CN-GB
    EUC-TW,EUCTW,X-EUC-TW

UNIX encodings
In UNIX, the File object looks for the presence of the iconv library, and uses whatever encoding it finds
there. If you need a special encoding in UNIX, make sure that there is an iconv encoding module installed
that converts between UTF-16 (the internal format that the File object uses) and the desired encoding.
