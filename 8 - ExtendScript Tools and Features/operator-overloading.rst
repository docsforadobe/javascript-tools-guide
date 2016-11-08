.. _operator-overloading:

Operator overloading
====================
ExtendScript allows you to extend or override the behavior of a math or a Boolean operator for a specific
class by defining a method in that class with same name as the operator. For example, this code defines
the addition (+) operator for the class MyClass. In this case, the addition operator simply adds the operand
to the property value:
// define the constructor method
function MyClass (initialValue) {
this.value = initialValue;
}
// define the addition operator
MyClass.prototype ["+"] = function (operand) {
return this.value + operand;
}

This allows you to perform the "+" operation with any object of this class:
var obj = new MyClass (5);
Result: [object Object]
obj + 10;
Result: 15

You can override the following operators:
Unary

+, ~

Binary

+, *, /, %, ^
<, <=, ==
<<, >>, >>>
&, |, ===

The operators > and >= are implemented by executing NOT operator <= and NOT operator <.
Combined assignment operators such as *= are not supported.
All operator overload implementations must return the result of the operation. To perform the default
operation, return undefined.
Unary operator functions work on the this object, while binary operators work on the this object and
the first argument. The + and - operators have both unary and binary implementations. If the first
argument is undefined, the operator is unary; if it is supplied, the operator is binary.
For binary operators, a second argument indicates the order of operands. For noncommutative operators,
either implement both order variants in your function or return undefined for combinations that you do
not support. For example:
this ["/"] = function (operand, rev) {
if (rev) {
// do not resolve operand / this
return;
} else {
// resolve this / operand
return this.value / operand;
}
