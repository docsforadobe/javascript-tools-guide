.. _common-properties:

Common properties
=================

All types of user-interface elements, including windows, containers, and controls, share many of the same
properties, although some have slightly different meanings for different types of objects. The following
table summarizes which properties are used in which object types.

==============  ======  =====  ===========  ===  =====  ======  ========  ============  ========  ===========  ==========  =====  =======  ========  ===========  ===========  =========  ======  ==========  ========
Property        Window  Panel  TabbedPanel  Tab  Group  Button  Checkbox  DropDownList  EditText  FlashPlayer  IconButton  Image  ListBox  ListItem  ProgressBar  RadioButton  Scrollbar  Slider  StaticText  TreeView
==============  ======  =====  ===========  ===  =====  ======  ========  ============  ========  ===========  ==========  =====  =======  ========  ===========  ===========  =========  ======  ==========  ========
active          x                                       x       x         x             x         x            x           x      x                               x            x          x       x           x
alignChildren   x       x      x            x    x
alignment       x       x      x            x    x      x       x         x             x         x            x           x      x                  x            x            x          x       x           x
bounds          x       x      x            x    x      x       x         x             x         x            x           x      x                  x            x            x          x       x           x
cancelElement   x
characters              x      x            x    x
checked                                                                                                                                    x
children        x       x      x            x    x      x       x         x             x         x            x           x      x                  x            x            x          x       x           x
columns                                                                                                                           x
defaultElement  x
enabled         x       x      x            x    x      x       x         x             x         x            x           x      x        x         x            x            x          x       x           x
expanded                                                                                                                                   x
frameBounds     x
frameLocation   x
frameSize       x
graphics        x       x      x            x    x      x       x         x             x         x            x           x      x                  x            x            x          x       x           x
helpTip         x       x      x            x    x      x       x         x             x         x            x           x      x                  x            x            x          x       x           x
icon                                                                                                           x           x               x
image                                                                                                          x           x               x
index                                                                                                                                      x
items                                                                     x                                                       x                                                                           x
itemSize                                                                  x                                                       x                                                                           x
jumpdelta                                                                                                                                                                      x
justify                                                 x       x                       x                                                                         x                               x
layout          x       x      x            x    x
location        x       x      x            x    x      x       x         x             x         x            x           x      x                  x            x            x          x       x           x
margins         x       x      x            x    x
maximumSize     x       x      x            x    x      x       x         x             x         x            x           x      x                  x            x            x          x       x           x
maxvalue                                                                                                                                             x                         x          x
minimumSize     x       x      x            x    x      x       x         x             x         x            x           x      x                  x            x            x          x       x           x
minvalue                                                                                                                                             x                         x          x
orientation     x       x      x            x    x
parent          x       x      x            x    x      x       x         x             x         x            x           x      x        x         x            x            x          x       x           x
preferredSize   x       x      x            x    x      x       x         x             x         x            x           x      x                  x            x            x          x       x           x
properties      x       x      x            x    x      x       x         x             x         x            x           x      x        x         x            x            x          x       x           x
resizeable      x
selected                                                                                                                                   x
selection                      x                                          x                                                       x                                                                           x
shortcutKey     x                                       x       x         x             x         x            x           x      x                               x            x          x       x           x
size            x       x      x            x    x      x       x         x             x         x            x           x      x                  x            x            x          x       x           x
spacing         x       x      x            x    x
stepdelta                                                                                                                                                                      x
subitems                                                                                                                                   x
text            x       x      x            x           x       x         x             x                      x                           x         x            x                       x       x
textselection                                                             x             x
title                                                                                                          x
titleLayout                    x                                          x                       x            x           x
type            x       x      x            x    x      x       x         x             x         x            x           x      x        x         x            x            x          x       x           x
value                                                           x                                              x                                     x            x            x          x
visible         x       x      x            x    x      x       x         x             x         x            x           x      x                  x            x            x          x       x           x
window          x       x      x            x    x      x       x         x             x         x            x           x      x                  x            x            x          x       x           x
windowBounds    x       x      x            x    x      x       x         x             x         x            x           x      x                  x            x            x          x       x           x
==============  ======  =====  ===========  ===  =====  ======  ========  ============  ========  ===========  ==========  =====  =======  ========  ===========  ===========  =========  ======  ==========  ========
