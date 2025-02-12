# Window class

The Window class defines these static properties and functions. Window instances created with new `Window()` do not have these properties and functions defined.

---

## Window Class Attributes

### Window.frameworkName

`Window.frameworkName`

#### Description

!!! danger
    Deprecated. Use [ScriptUI.frameworkName](./scriptui-class.md#scriptuiframeworkname) instead.

#### Type

String

---

### Window.version

`Window.version`

#### Description

!!! danger
    Deprecated. Use [ScriptUI.version](./scriptui-class.md#scriptuiversion) instead.

#### Type

String

---

## Window Class Methods

Access these function through the class. For example:

```javascript
Window.alert("Notification to user");
```

---

### alert()

`Window.alert(message[, title="Script Alert", errorIcon=false]);`

#### Description

Displays a platform-standard dialog containing a short message and an OK button.

#### Parameters

|  Parameter  |  Type   |                                                                                        Description                                                                                        |
| ----------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `message`   | String  | The string for the displayed message.                                                                                                                                                     |
| `title`     | String  | Optional. A string to appear as the title of the dialog, if the platform supports a title. Mac OS does not support titles for alert dialogs. The default title string is `"Script Alert"` |
| `errorIcon` | Boolean | Optional. When `true`, the platform-standard alert icon is replaced by the platform-standard error icon in the dialog. Default is `false`.                                                |

#### Returns

Nothing

---

### confirm()

`Window.confirm(message[, noAsDflt=false, title="Script Alert"]);`


#### Description

Displays a platform-standard dialog containing a short message and two buttons labeled "Yes" and "No".

#### Parameters

| Parameter  |  Type   |                                                                                           Description                                                                                            |
| ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `message`  | String  | The string for the displayed message.                                                                                                                                                            |
| `noAsDflt` | Boolean | Optional. When `true`, the No button is the default choice, selected when the user types ENTER. Default is `false`, meaning that Yes is the default choice.                                      |
| `title`    | String  | Optional. A string to appear as the title of the dialog, if the platform supports a title. Mac OS does not support titles for confirmation dialogs. The default title string is `"Script Alert"` |

#### Returns

Boolean. `true` if the user clicked "Yes", `false` if the user clicked "No".

---

### find()

`Window.find(resourceName)`

`Window.find(type, title)`

#### Description

Use this method to find an existing window. This includes windows already created by a script, and windows created by the application (if the application supports this case).

!!! warning
    Not supported in all ScriptUI implementations.

#### Parameters

|   Parameter    |  Type  |                                                                                              Description                                                                                              |
| -------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `resourceName` | String | The name of a predefined resource available to JavaScript in the current application.                                                                                                                 |
| `type`         | String | Optional. The window type (see [Window object constructor](window-object.md#window-object-constructor)) used if there is more than one window with the same title. Can be `null` or the empty string. |
| `title`        | Strign | The window title.                                                                                                                                                                                     |

#### Returns

[Window object](./window-object.md) found or generated from the resource, or `null` if no such window or resource exists.

---

### prompt()

`Window.prompt(message, preset[, title="Script Prompt"]);`


#### Description

Displays a modal dialog that returns the user's text input.

#### Parameters

| Parameter |  Type  |                                                                                           Description                                                                                           |
| --------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `message` | String | The string for the displayed message.                                                                                                                                                           |
| `preset`  | String | The initial value to be displayed in the text edit field.                                                                                                                                       |
| `title`   | String | Optional. A string to appear as the title of the dialog. In Windows, this appears in the window's frame; in Mac OS it appears above the message. The default title string is `"Script Prompt"`. |

#### Returns

Returns the value of the text edit field if the user clicked OK, `null` if the user clicked Cancel.
