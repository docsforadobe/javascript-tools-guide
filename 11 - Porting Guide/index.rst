.. _porting-guide:
Porting Guide
=============

This chapter briefly describes changes between this release and the previous release of ExtendScript, to
aid you in porting applications to current versions.

- ExtendScript Toolkit
    - This version of ExtendScript Toolkit comes with a number of improvements related to its usability. For complete details, see the README file.

- ScriptUI
    - User interface elements in the ScriptUI version used by Photoshop and After Effects are created and managed by the Adobe Flash player; a ScriptUI Button created by a script run in Photoshop or After Effects has the same appearance on both platforms, rather than a platform-specific appearance, as it would in other applications or in the ExtendScript Toolkit. For details, see the scripting documentation distributed with the Photoshop and After Effects applications.
    - For certain elements, the title layout feature allows you to easily define an element's title and its spacial relationship with the graphic representation of the object it identifies. (This feature was present in previous versions, but undocumented.) See :ref:`Managing-control-titles`.

- Interapplication messaging
    - This is the complete list of identifying names for applications that can use interapplication messaging in Creative Suite 5::
        aftereffects
        ame
        audition
        bridge
        contribute
        devicecentral
        dreamweaver
        encore
        estoolkit
        exman
        fireworks
        flash
        flashbuilder
        flashcatalyst
        illustrator
        incopy
        indesign
        indesignserver
        photoshop
        premierepro
        soundbooth
