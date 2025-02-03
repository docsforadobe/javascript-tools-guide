# Specifying measurement values

ExtendScript provides the UnitValue object to represent measurement values. The properties and methods of the UnitValue object make it easy to change the value, the unit, or both, or to perform conversions from one unit to another.

## UnitValue object

Represents measurement values that contain both the numeric magnitude and the unit of measurement.

### UnitValue object constructor

The UnitValue constructor creates a new UnitValue object. The keyword new is optional:

```javascript
myVal = new UnitValue (value, unit);
myVal = new UnitValue ("value unit");
myVal = new UnitValue (value, "unit");
```

The value is a number, and the unit is specified with a string in abbreviated, singular, or plural form, as shown in the following table.

| Abbreviation |       Singular        |         Plural         |       Comments       |
| ------------ | --------------------- | ---------------------- | -------------------- |
| `"in"`       | `"inch"`              | `"inches"`             | 2.54 cm              |
| `"ft"`       | `"foot"`              | `"feet"`               | 30.48 cm             |
| `"yd"`       | `"yard"`              | `"yards"`              | 91.44 cm             |
| `"mi"`       | `"mile"`              | `"miles"`              | 1609.344 m           |
| `"mm"`       | `"millimeter"`        | `"millimeters"`        |                      |
| `"cm"`       | `"centintimeter"`     | `"centimeters"`        |                      |
| `"m"`        | `"meter"`             | `"meters"`             |                      |
| `"km"`       | `"kilometer"`         | `"kilometers"`         |                      |
| `"pt"`       | `"point"`             | `"points"`             | inches / 72          |
| `"pc"`       | `"pica"`              | `"picas"`              | points \* 12         |
| `"tpt"`      | `"traditional point"` | `"traditional points"` | inches / 72.27       |
| `"tpc"`      | `"traditional pica"`  | `"traditional picas"`  | 12 tpt               |
| `"ci"`       | `"cicero"`            | `"ciceros"`            | 12.7872 pt           |
| `"px"`       | `"pixel"`             | `"pixels"`             | baseless (see below) |
| `"%" `       | `"percent"`           | `"percent"`            | baseless (see below) |

If an unknown unit type is supplied, the type is set to `"?"`, and the `UnitValue` object prints as "UnitValue 0.00000".

For example, all the following formats are equivalent:

```javascript
myVal = new UnitValue (12, "cm");
myVal = new UnitValue ("12 cm");
myVal = UnitValue ("12 centimeters");
```

---

## Attributes

### UnitValue.baseUnit

`unitValueObj.baseUnit`

#### Description

A [UnitValue object](#unitvalue-object) that defines the size of one pixel, or a total size to use as a base for percentage values.

This is used as the base conversion unit for pixels and percentages; see [Converting pixel and percentage values](#converting-pixel-and-percentage-values).

Default is 0.013889 inches (1/72 in), which is the base conversion unit for pixels at 72 dpi. Set to null to restore the default.

#### Type

UnitValue

---

### UnitValue.type

`unitValueObj.type`

#### Description

The unit type in abbreviated form; for example, "cm" or "in".

#### Type

String

---

### UnitValue.value

`unitValueObj.value`

#### Description

The numeric measurement value.

#### Type

Number

---


---

## Methods

### UnitValue.as()

`unitValueObj.as(unit)`

#### Description

Returns the numeric value of this object in the given unit. If the unit is unknown or cannot be computed, generates a run-time error.

#### Parameter

| Parameter |  Type  |                            Description                            |
| --------- | ------ | ----------------------------------------------------------------- |
| `unit`    | String | The unit type in abbreviated form; for example, `"cm"` or `"in"`. |

#### Returns

Number

---

### UnitValue.convert()

`unitValueObj.convert(unit)`

#### Description

Converts this object to the given unit, resetting the type and value accordingly.

Returns `true` if the conversion is successful. If the unit is unknown or the object cannot be converted, generates a run-time error and returns `false`.

#### Parameter

| Parameter |  Type  |                            Description                            |
| --------- | ------ | ----------------------------------------------------------------- |
| `unit`    | String | The unit type in abbreviated form; for example, `"cm"` or `"in"`. |

#### Returns

Boolean

---

## Converting pixel and percentage values

Converting measurements among different units requires a common base unit. For example, for length, the meter is the base unit. All length units can be converted into meters, which makes it possible to convert any length unit into any other length unit.

Pixels and percentages do not have a standard common base unit. Pixel measurements are relative to display resolution, and percentages are relative to an absolute total size.

- To convert pixels into length units, you must know the size of a single pixel. The size of a pixel depends on the display resolution. A common resolution measurement is 72 dpi, which means that there are 72 pixels to the inch. The conversion base for pixels at 72 dpi is 0.013889 inches (1/72 inch).
- Percentage values are relative to a total measurement. For example, 10% of 100 inches is 10 inches, while 10% of 1 meter is 0.1 meters. The conversion base of a percentage is the unit value corresponding to 100%.

The default `baseUnit` of a `unitValue` object is 0.013889 inches, the base for pixels at 72 dpi. If the `unitValue` is for pixels at any other dpi, or for a percentage value, you must set the `baseUnit` value accordingly. The `baseUnit` value is itself a `unitValue` object, containing both a magnitude and a unit.

For a system using a different DPI, you can change the `baseUnit` value in the `UnitValue` class, thus changing the default for all new `unitValue` objects. For example, to double the resolution of pixels:

```javascript
UnitValue.baseUnit = UnitValue (1/144, "in"); //144 dpi
```

To restore the default, assign null to the class property:

```javascript
UnitValue.baseUnit = null; //restore default
```

You can override the default value for any particular unitValue object by setting the property in that object. For example, to create a unitValue object for pixels with 96 dpi:

```javascript
pixels = UnitValue (10, "px");
myPixBase = UnitValue (1/96, "in");
pixels.baseUnit = myPixBase;
```

For percentage measurements, set the baseUnit property to the measurement value for 100%. For example, to create a unitValue object for 40% of 10 feet:

```javascript
myPctVal = UnitValue (40, "%");
myBase = UnitValue (10, "ft")
myPctVal.baseUnit = myBase;
```

Use the [as()](#unitvalue-object-as) method to get to a percentage value as a unit value:

```javascript
myFootVal = myPctVal.as ("ft"); // => 4
myInchVal = myPctVal.as ("in"); // => 36
```

You can convert a unitValue from an absolute measurement to pixels or percents in the same way:

```javascript
myMeterVal = UnitValue (10, "m"); // 10 meters
myBase = UnitValue (1, "km");
myMeterVal.baseUnit = myBase; //as a percentage of 1 kilometer
pctOfKm = myMeterVal.as ('%'); // => 1
myVal = UnitValue ("1 in"); // Define measurement in inches
// convert to pixels using default base
myVal.convert ("px"); // => value=72 type=px
```

---

## Computing with unit values

UnitValue objects can be used in computational JavaScript expressions. The way the value is used depends on the type of operator.

### Unary operators `(~, !, +, -)`

|   Operator   |                                Behaviour                                |
| ------------ | ----------------------------------------------------------------------- |
| `~unitValue` | The numeric value is converted to a 32-bit integer with inverted bits.  |
| `!unitValue` | Result is `true` if the numeric value is nonzero, `false` if it is not. |
| `+unitValue` | Result is the numeric value.                                            |
| `-unitValue` | Result is the negated numeric value.                                    |

### Binary operators `(+, -, *, /, %)`

If one operand is unitValue object and the other is a number, the operation is applied to the number and the numeric value of the object. The expression returns a new unitValue object with the result as its value.

For example:

```javascript
val = new UnitValue ("10 cm");
res = val * 20;
// res is a UnitValue (200, "cm");
```

If both operands are unitValue objects, JavaScript converts the right operand to the same unit as the left operand and applies the operation to the resulting values. The expression returns a new unitValue object with the unit of the left operand, and the result value.

For example:

```javascript
a = new UnitValue ("1 m");
b = new UnitValue ("10 cm");
a + b;
// res is a UnitValue (1.1, "m");
b + a;
// res is a UnitValue (110, "cm");
```

### Comparisons (=, ==, <, >, <=, >=)

If one operand is a unitValue object and the other is a number, JavaScript compares the number with the unitValue's numeric value.

If both operands are unitValue objects, JavaScript converts both objects to the same unit, and compares the converted numeric values.

For example:

```javascript
a = new UnitValue ("98 cm");
b = new UnitValue ("1 m");
a < b;   // => true
a < 1;   // => false
a == 98; // => true
```
