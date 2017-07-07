# README #

### What is this repository for? ###

This is the repo for converting The Javascript Tools Guide pdf into a readthedocs.io doc.

[WIP can be seen here](http://javascript-tools-guide.readthedocs.io/en/latest/)

### Contributing ###

Contributions are very appreciated! Just pick any of the uncompleted todos below. If you start working on a todo, edit this file and put your name beside the todo so people know what is being worked on, and don't do unnecessary work.
This project uses reStructuredText for a reference on how to write reStructuredText check out this [quickref](http://docutils.sourceforge.net/docs/user/rst/quickref.html).

### To do ###

- ~~pdf to text~~
- ~~Split into sections~~
- ~~Remove page headers~~
    - There might be some left over, so if you see something seems like it shouldn't be there, it probably shouldn't
- ~~Format h1 and h2 headers in each section~~
- ~~Split each section into files~~
- ~~Convert 'see something on page' to links~~
- Format text into **bold**, *italics*, `code`, headers, bullet lists, and paragraphs.
    - ~~1 - Introduction~~
    - ~~2 - ExtendScript Toolkit~~
    - ~~3 - File System Access~~
    - 4 - User-Interface Tools
        - Common Properties
        - Graphic Customization Objects
    - 5 - Interapplication Communictation with Scripts
    - 6 - External Communication Tools
    - 7 - Intergrating External Libraries
    - 8 - ExtendScript Tools and Features
    - 9 - Intergrating XML into JavaScript
    - 10 - Scripting Access to XMP Metadata
- Format code examples
    - 2 - ExtendScript Toolkit
    - 3 - File System Access
    - 4 - User-Interface Tools
    - 5 - Interapplication Communictation with Scripts
    ~~6 - External Communication Tools~~
    ~~7 - Intergrating External Libraries~~
    - 8 - ExtendScript Tools and Features
    - 9 - Intergrating XML into JavaScript
    - 10 - Scripting Access to XMP Metadata
- Format tables
    ~~2 - ExtendScript Toolkit~~
    ~~3 - File System Access~~
    ~~4 - User-Interface Tools~~
    ~~5 - Interapplication Communication with Scripts~~
    ~~6 - External Communication Tools~~
    ~~7 - Intergrating External Libraries~~
    - 8 - ExtendScript Tools and Features
    - 9 - Intergrating XML into JavaScript
    - 10 - Scripting Access to XMP Metadata
- ~~Format notes, warnings and tips~~
- Extract images from the pdf and put into the text files
    - 2 - ExtendScript Toolkit
    - 4 - User-Interface Tools
    - 8 - ExtendScript Tools and Features

### How to ###

#### Text

```
**bold**, *italics*, ``code``
```

#### Headers

```
H1. line must be at least as long as text
=========================================

h2
--

h3
**

h4
++
```

#### Bullet lists

```
- Bullet point lists must start with one empty line above
  - Indented bullet points are indented with 2 spaces
  - very long bullet point that goes over multiple lines
    have the additional lines indented one more level
- Bullet point
```

#### Paragraphs

```

New paragraphs starts with an empty line above.
If there are no empty line above. The line will be added to the end of the previous line.

Correct way to start a new paragraph.

Header
======
Paragraphs can start directly underneath headers, an empty line is not needed in that case.
```
