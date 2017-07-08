.. _scripting-access-to-xmp-metadata:

Scripting Access to XMP Metadata
================================
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
using the Adobe Bridge DOM's ``Thumbnail`` object.

.. note:: Adobe Bridge provides a means of embedding metadata values in a script (to describe the script file
  itself) using XML delimited by special tags within a comment block. This is not related to metadata access
  for files and thumbnails. For details, see the *Adobe Bridge JavaScript Guide*.
