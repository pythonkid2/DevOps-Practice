# Python Learning Notes

## Day 1 - Basics

### 1. Taking User Input and Printing Output

```python
print("Hello, " + input("What is your name? ") + "!")
```

**Explanation:**

* `input()` takes input from the user.
* `print()` displays output.
* `+` is used for string concatenation.

**Example Output:**

```text
What is your name? Mathew
Hello, Mathew!
```

---

### 2. Store Input in a Variable

```python
name = input("What's your name? ")
print(name)
```

**Explanation:**

* Variables are used to store values.
* Here, the variable `name` stores the user's input.

---

### 3. Find Length of User Input

```python
print(len(input("Tell me your name: ")))
```

**Explanation:**

* `len()` returns the number of characters.
* The input is passed directly into `len()`.

---

### 4. Using Variables with `len()`

```python
username = input("What is your name? ")
length = len(username)

print("Your name has " + str(length) + " characters")
```

**Explanation:**

* `len()` returns an integer.
* Integers must be converted to strings using `str()` before concatenation.

---

### 5. Variable Swapping Exercise

**Question:**
We have two variables:

```python
glass1 = "milk"
glass2 = "juice"
```

Swap the contents without typing `"milk"` or `"juice"`.

**Solution:**

```python
temp = glass1
glass1 = glass2
glass2 = temp
```

**Result:**

```text
glass1 = juice
glass2 = milk
```

---

### 6. Band Name Generator Project

```python
username = input("What is your name? ")
petname = input("What is your pet name? ")

print("Hello, " + username + "!")
print("Your band name is " + username + " " + petname)
```

**Example Output:**

```text
What is your name? Mathew
What is your pet name? Bruno

Hello, Mathew!
Your band name is Mathew Bruno
```

---

# Day 2 - Data Types

## 1. Python Data Types

### String (`str`)

```python
name = "Mathew"
```

Stores text data.

---

### Integer (`int`)

```python
age = 25
```

Stores whole numbers.

---

### Float (`float`)

```python
salary = 25000.50
```

Stores decimal numbers.

---

### Boolean (`bool`)

```python
is_active = True
```

Stores either `True` or `False`.

---

## 2. String Indexing (Subscripting)

```python
print("Hello"[0])
```

Output:

```text
H
```

**Explanation:**

* Strings are sequences of characters.
* Index starts from `0`.

| Character | H | e | l | l | o |
| --------- | - | - | - | - | - |
| Index     | 0 | 1 | 2 | 3 | 4 |

Examples:

```python
print("Hello"[1])  # e
print("Hello"[4])  # o
```

---

## 3. Checking Data Types

```python
print(type(1234))
print(type(12.34))
print(type("Hello, World!"))
print(type([1, 2, 3, 4, 5]))
print(type((1, 2, 3, 4, 5)))
print(type({1, 2, 3, 4, 5}))
print(type({"a": 1, "b": 2, "c": 3}))
print(type(True))
print(type(None))
print(type(1 + 2j))
print(type(len))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'list'>
<class 'tuple'>
<class 'set'>
<class 'dict'>
<class 'bool'>
<class 'NoneType'>
<class 'complex'>
<class 'builtin_function_or_method'>
```

---

## 4. Type Conversion (Type Casting)

### Convert Integer to String

```python
length = 10

print("Length is " + str(length))
```

---

### Convert String to Integer

```python
num = "100"

print(int(num) + 50)
```

Output:

```text
150
```

---

### Example Program

```python
user = input("Enter your name: ")

print(f"Hello, {user}!")

length = len(user)

print(f"Your name has {length} characters.")

print("Number converted to string: " + str(length))

print("Goodbye!")
```

**Example Output:**

```text
Enter your name: Mathew

Hello, Mathew!
Your name has 6 characters.
Number converted to string: 6
Goodbye!
```

---

## 5. Implicit Type Casting

Python automatically converts some data types when needed.

```python
num1 = 10
num2 = 5.5

result = num1 + num2

print(result)
print(type(result))
```

Output:

```text
15.5
<class 'float'>
```

**Explanation:**

* Integer (`10`) is automatically converted to float (`10.0`).
* Result becomes a float.

---

# Key Concepts Learned So Far

✅ `print()`
✅ `input()`
✅ Variables
✅ `len()` function
✅ String concatenation
✅ f-Strings
✅ Data Types (`str`, `int`, `float`, `bool`)
✅ String indexing
✅ `type()` function
✅ Type Casting (`str()`, `int()`, `float()`)
✅ Implicit Type Conversion
✅ Variable Swapping
✅ Mini Project - Band Name Generator

---

# Python Learning Notes

# Day 2 (Continued) - Operators and Conditional Statements

## 1. Tip Calculator Project

### Program

```python
a = float(input("What's the bill amount? "))
b = float(input("What's the tip percentage? "))
c = int(input("How many people are splitting the bill? "))

tip = a * (b / 100)
total = a + tip
per_person = total / c

print(f"Each person should pay: ${per_person:.2f}")
```

### Concepts Used

#### float()

Converts input into a decimal number.

```python
price = float("150.75")
```

#### int()

Converts input into a whole number.

```python
people = int("5")
```

#### Arithmetic Operators

| Operator | Meaning        | Example |
| -------- | -------------- | ------- |
| +        | Addition       | 10 + 5  |
| -        | Subtraction    | 10 - 5  |
| *        | Multiplication | 10 * 5  |
| /        | Division       | 10 / 5  |
| //       | Floor Division | 10 // 3 |
| %        | Modulus        | 10 % 3  |
| **       | Power          | 2 ** 3  |

#### f-Strings

```python
name = "Mathew"
print(f"Hello {name}")
```

#### Formatting Decimal Places

```python
price = 25.6789
print(f"{price:.2f}")
```

Output:

```text
25.68
```

---

# Conditional Statements

Conditional statements allow a program to make decisions.

## Basic Syntax

```python
if condition:
    # code
else:
    # code
```

### Example

```python
print("Welcome to the roller coaster!")

height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the roller coaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")
```

### Flow

```text
Condition True  -> Execute IF block
Condition False -> Execute ELSE block
```

---

# Comparison Operators

Comparison operators compare two values and return either True or False.

| Operator | Meaning                  |
| -------- | ------------------------ |
| >        | Greater than             |
| <        | Less than                |
| >=       | Greater than or equal to |
| <=       | Less than or equal to    |
| ==       | Equal to                 |
| !=       | Not equal to             |

### Examples

```python
print(10 > 5)
```

Output:

```text
True
```

```python
print(10 == 5)
```

Output:

```text
False
```

### Important

```python
=
```

Assignment operator

```python
==
```

Comparison operator

Example:

```python
age = 25
```

Assigns 25 to age.

```python
age == 25
```

Checks if age equals 25.

---

# Modulus Operator (%)

The modulus operator returns the remainder after division.

```python
10 % 2
```

Output:

```text
0
```

```python
10 % 3
```

Output:

```text
1
```

---

# Even or Odd Number Program

```python
a = int(input("Enter a number: "))

if a % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
```

### Logic

```text
Number % 2 = 0  -> Even
Number % 2 = 1  -> Odd
```

---

# Nested If Statements

An if statement inside another if statement.

### Example

```python
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))

if height >= 120:
    print("You can ride the rollercoaster!")

    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
```

### Flow

```text
Height Check
    |
    ├── False → Not allowed
    |
    └── True
            |
            Age Check
                |
                ├── <=18 → $7
                └── >18  → $12
```

---

# Multiple Conditions (if - elif - else)

Used when there are multiple possible outcomes.

### Syntax

```python
if condition1:
    code
elif condition2:
    code
elif condition3:
    code
else:
    code
```

### Example

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Fail")
```

Output:

```text
Grade B
```

---

# BMI Calculator Project

BMI (Body Mass Index) measures body weight relative to height.

### Formula

BMI = \frac{weight}{height^2}

### Program

```python
weight = int(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
```

### BMI Categories

| BMI Range    | Category    |
| ------------ | ----------- |
| Below 18.5   | Underweight |
| 18.5 - 24.9  | Normal      |
| 25 - 29.9    | Overweight  |
| 30 and above | Obese       |

### Concepts Used

#### Exponent Operator (**)

```python
2 ** 3
```

Output:

```text
8
```

Used in BMI calculation:

```python
height ** 2
```

means:

```python
height × height
```

---

# Logical Operators (Important Missing Concept)

Used to combine multiple conditions.

| Operator | Meaning                             |
| -------- | ----------------------------------- |
| and      | Both conditions must be True        |
| or       | At least one condition must be True |
| not      | Reverses the result                 |

### AND

```python
age = 20
height = 170

if age >= 18 and height >= 150:
    print("Allowed")
```

### OR

```python
if age >= 18 or height >= 150:
    print("Allowed")
```

### NOT

```python
is_banned = False

if not is_banned:
    print("Access Granted")
```

---

# Key Concepts Learned So Far

✅ print()

✅ input()

✅ Variables

✅ len()

✅ Strings

✅ Integers

✅ Floats

✅ Booleans

✅ String Indexing

✅ type()

✅ Type Casting

✅ Arithmetic Operators

✅ Comparison Operators

✅ Modulus Operator

✅ Exponent Operator

✅ Conditional Statements

✅ if

✅ else

✅ elif

✅ Nested if

✅ Logical Operators (and, or, not)

✅ f-Strings

✅ Tip Calculator Project

✅ BMI Calculator Project

✅ Even/Odd Checker Project

✅ Roller Coaster Project


