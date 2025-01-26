## **Python Notes**

#### What will come from this course

* Write Your Notes
* Practice Daily 
* Assignments
* Projects

#### Intro To Python

* Managing Data is More Complex
* Python is very useful in data science
* Python is using each and every industry

#### Print Function + String Manipulation

* If you just print it will give simple cursor line
* String Manipulation: + symbol is used to concatenation
* New lines can be added using backslash

#### Input Function in python

* syntax: `input(prompt)`
* by default input function value is string
* mention int , float to changes

#### Variables in Python

* Variable Naming Conventions:
  * a-z,A-Z,0-9 only characters
  * Spaces & Special Characters are not allowed
  * Variable should start with Letter or Underscore
  * Multi-word name is allowed 
  * camelCase is allowed (myName)
  * PascalCase is allowed(MyName)
  * snake case is allowed(My_Name)
  * class not allowed to use as variable
  * python is case-sensitive

#### Data Types:

* Data Types are actually classes in python
* Build-in data types
  * int(-ve +ve),float(.-ve .+ve),string,boolean
* 0B12,0b12 --> Binary Numbers
* 0o12,0O12 --> Octal Numbers
* 0x12,0X12 --> Hexa-Decimal Numbers
* **Type Error**
  * int does not contain any length function

#### Operators

* Operators are used to perform operations
* Arithmatic --> + - % / // 
* Comparison(Relational) --> == >= <= != --> returns true or false
* Logical --> and or nor  ---> returns true or false
* Bitwise --> 
* Assignment
* Identity
* Membership
* Precedence of operators (BOD MAS)
* BOD MAS-Bracket-Division-Multiplication-Addition-Subtraction

#### Bitwise Operators

Bitwise operators perform operations on bits and are commonly used for efficient low-level programming. Below is a summary of the bitwise operators:

- **`&`** → **AND**  
  Performs a bitwise AND operation.

- **`|`** → **OR**  
  Performs a bitwise OR operation.

- **`^`** → **XOR**  
  Performs a bitwise XOR (exclusive OR) operation.

- **`~`** → **NOT** (Complement)  
  Inverts all bits (complements the number).  
  Example:  
  `a = 10` → `~a = -11` (The value is negated with one value higher).

- **`<<`** → **Left Shift**  
  Shifts bits to the left, which effectively increases the value.

- **`>>`** → **Right Shift**  
  Shifts bits to the right, which effectively decreases the value.

#### Identity Operators

Identity operators are used to compare the memory locations of two objects. They are:

- **`is`**  
  Returns `True` if both variables refer to the same object in memory.

- **`is not`**  
  Returns `True` if both variables do not refer to the same object in memory.

#### Membership Operators

Membership operators are used to test if a value is found within a sequence (such as a list, tuple, or string). They are:

- **`in`**  
  Returns `True` if the value is found in the specified sequence.

- **`not in`**  
  Returns `True` if the value is not found in the specified sequence.

#### Relational Operators

Relational operators are used to compare the values of two operands. They return a boolean value (`True` or `False`). The following are relational operators:

- **`==`**  
  Returns `True` if the values of two operands are equal.

- **`!=`**  
  Returns `True` if the values of two operands are not equal.

- **`>`**  
  Returns `True` if the left operand is greater than the right operand.

- **`<`**  
  Returns `True` if the left operand is less than the right operand.

- **`>=`**  
  Returns `True` if the left operand is greater than or equal to the right operand.

- **`<=`**  
  Returns `True` if the left operand is less than or equal to the right operand.

#### Assignment Operators

Assignment operators are used to assign values to variables. They can also combine assignment with another operation:

- **`=`**  
  Assigns the value of the right-hand operand to the left-hand operand.

- **`+=`**  
  Adds the right operand to the left operand and assigns the result to the left operand.  
  `a += b` is equivalent to `a = a + b`.

- **`-=`**  
  Subtracts the right operand from the left operand and assigns the result to the left operand.  
  `a -= b` is equivalent to `a = a - b`.

- **`*=`**  
  Multiplies the left operand by the right operand and assigns the result to the left operand.  
  `a *= b` is equivalent to `a = a * b`.

- **`/=`**  
  Divides the left operand by the right operand and assigns the result to the left operand.  
  `a /= b` is equivalent to `a = a / b`.

- **`%=`**  
  Takes the modulus of the left operand by the right operand and assigns the result to the left operand.  
  `a %= b` is equivalent to `a = a % b`.

- **`//=`**  
  Performs floor division and assigns the result to the left operand.  
  `a //= b` is equivalent to `a = a // b`.

- **`**=`**  
  Raises the left operand to the power of the right operand and assigns the result to the left operand.  
  `a **= b` is equivalent to `a = a ** b`.

---

#### Logical Operators

Logical operators are used to combine conditional statements. They operate on boolean values and return `True` or `False`.

- **`and`**  
  Returns `True` if both operands are `True`.

- **`or`**  
  Returns `True` if at least one of the operands is `True`.

- **`not`**  
  Returns `True` if the operand is `False` and `False` if the operand is `True`.

#### Python `round()` Function

The `round()` function in Python is used to round a floating-point number to a specified number of decimal places. It can also round to the nearest integer if no decimal places are specified.

#### Syntax: ```round(number, ndigits)```
#### F-Strings in Python

F-Strings, short for **formatted string literals**, were introduced in Python 3.6. They provide a concise and readable way to embed expressions inside string literals using curly braces `{}`. The `f` prefix in an f-string's name refers to this feature.

#### Why Use F-Strings?

- **Readability**: F-Strings make it easy to embed variables and expressions directly into strings without using concatenation or older formatting methods like `.format()` or `%`.
- **Performance**: They are faster than `.format()` and `%` formatting because expressions are evaluated at runtime and directly embedded into the string.
- **Flexibility**: They allow embedding any valid Python expression.

#### Syntax

To use an f-string, prefix the string with the letter `f` or `F`, and place expressions inside curly braces `{}`.

```python
name = "Alice"
age = 30

# Basic usage
message = f"My name is {name} and I am {age} years old."
print(message)  # Output: My name is Alice and I am 30 years old.

# Inline expressions
square = f"The square of 5 is {5**2}."
print(square)  # Output: The square of 5 is 25.

# Function calls
import math
pi_value = f"The value of pi is approximately {math.pi:.2f}."
print(pi_value)  # Output: The value of pi is approximately 3.14.
```

#### Conditional Statements

* if
* else
* else-if
* nested if else
* 
