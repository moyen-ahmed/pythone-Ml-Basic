

## 📌 What is a Function?

A **function** is a reusable block of code that performs a specific task.

```python
def greet():
    print("Hello, World!")
````

To **call** a function:

```python
greet()  # Output: Hello, World!
```

---

## 🧠 Why Use Functions?

✅ Reusable code
✅ Cleaner and easier to manage
✅ Avoids repetition (DRY principle)
✅ Makes code more readable

---

## 🧾 Function Syntax

```python
def function_name(parameters):
    """Docstring (optional)"""
    # Code block
    return result (optional)
```

---

## 🎯 Passing Arguments

You can pass values (arguments) into a function:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
```

---

### 🏋️‍♂️ Exercise 1: Passing Arguments

```python
# Write a function that greets the user by their age
def greet_by_age(name, age):
    print(f"{name}, you are {age} years old!")

greet_by_age("Bob", 30)
```

---

## 🎁 Return Values

Functions can return data using `return`:

```python
def square(x):
    return x * x

result = square(4)
print(result)  # Output: 16
```

---

### 🏋️‍♀️ Exercise 2: Return Values

```python
# Create a function that returns the sum of two numbers
def add(a, b):
    return a + b

print(add(10, 5))  # Output: 15
```

---

## 📦 Passing a List

```python
def print_items(items):
    for item in items:
        print(item)

print_items(["apple", "banana", "mango"])
```

✅ Lists are passed **by reference**, so changes affect the original list unless copied.

---

## 🌟 Arbitrary Number of Arguments

### `*args` — Non-keyword variable arguments:

```python
def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3, 4))  # Output: 10
```

### `**kwargs` — Keyworded variable arguments:

```python
def print_user(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_user(name="Alice", age=25)
```

---

## 🔄 Default Parameter Values

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()         # Hello, Guest
greet("Moyen")  # Hello, Moyen
```

---

## ⚠️ Positional vs Keyword Arguments

```python
def person(name, age):
    print(f"{name} is {age} years old.")

person("Sam", 22)              # Positional
person(age=22, name="Sam")     # Keyword
```

---

## 🧠 Lambda (Anonymous Functions)

```python
square = lambda x: x * x
print(square(5))  # Output: 25
```

Short but powerful — often used in `map()`, `filter()`, etc.

---

## 🚀 Advanced Topics

### 1. **Nested Functions**

```python
def outer():
    def inner():
        print("Inner function")
    inner()
outer()
```

---

### 2. **Functions as Arguments**

```python
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    print(func("Hello"))

greet(shout)  # Output: HELLO
greet(whisper)  # Output: hello
```

---

### 3. **Returning Functions**

```python
def multiplier(x):
    def multiply(y):
        return x * y
    return multiply

double = multiplier(2)
print(double(10))  # Output: 20
```

---

### 4. **Decorators (💎 Pro-level)**

```python
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
```

---

## 📘 Mini Summary Table

| Concept                  | Syntax / Example              |
| ------------------------ | ----------------------------- |
| Define Function          | `def func():`                 |
| With Parameters          | `def func(x):`                |
| Return Value             | `return x + y`                |
| Default Arguments        | `def func(x=5):`              |
| `*args` (tuple)          | `def func(*args):`            |
| `**kwargs` (dict)        | `def func(**kwargs):`         |
| Lambda                   | `lambda x: x*x`               |
| Function inside Function | `def outer(): def inner():`   |
| Function as Argument     | `def greet(func): func("hi")` |
| Decorators               | `@decorator`                  |

---

## 🧪 Practice Challenge

Create a function that takes any number of numbers and returns the average:

```python
def average(*nums):
    return sum(nums) / len(nums)

print(average(10, 20, 30))  # Output: 20.0
```

---

## 📎 References

* [Python Docs – Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
* [W3Schools – Python Functions](https://www.w3schools.com/python/python_functions.asp)

