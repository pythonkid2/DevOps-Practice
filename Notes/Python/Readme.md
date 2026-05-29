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

