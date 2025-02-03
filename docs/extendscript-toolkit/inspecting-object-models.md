# Inspecting object models

The ExtendScript Toolkit offers the ability to inspect the object model of any loaded dictionary, using the Object Model Viewer that you invoke from the Help menu.

![Help Menu](extendscript-toolkit/_static/02_the-extendscript-toolkit_inspecting-object-models_help-menu.jpg)

The Object Model Viewer (OMV) comes up as a separate, floating window. The OMV allows you to browse through the object hierarchy and inspect the type and description of each property, and the description and parameters for each method.

![Object Model Viewer](extendscript-toolkit/_static/02_the-extendscript-toolkit_inspecting-object-models_omv.jpg)

The drop-down menu in the Browser section at the top left allows you to choose from any loaded dictionary of objects. A dictionary provides access to the object model for one application or subsystem.

- The **Core JavaScript Classes** dictionary includes Adobe tools and utilities such as File and Folder.
- The **ScriptUI Classes** dictionary shows the interface elements defined in the ScriptUI JavaScript module.
- Each Adobe application defines a dictionary for that application's Document Object Model (DOM). The dictionary for a particular application may not be available until you launch that application, or until you select it as a target in the Toolkit.

![Object Model Viewer Dictionary](extendscript-toolkit/_static/02_the-extendscript-toolkit_inspecting-object-models_omv-dictionary.jpg)

To inspect an object model, select the appropriate dictionary from the Browser menu. The classes defined in that model appear in the Classes panel. Select a class to populate the Types panel with the available element types (Constructor, Class, Instance, Event). Select the type to populate the Properties and Methods panel with elements of that type.

Each time you select a class or element, its description appears on the right; descriptions are stacked, remaining in view until you close them. You can close each description individually, using the mouse-over menu that appears in the lower right of the description itself, or you can close all open descriptions using the Close All button at the top left of the OMV window.

![Object Model Viewer](extendscript-toolkit/_static/02_the-extendscript-toolkit_inspecting-object-models_omv-details.png)

The mouse-over menu also allows you to bookmark an element for easy access, or copy text from the description. Live links in the descriptions take you to related objects and elements, and you can search for text in names or descriptions.
