
# 🔀 Python `if` Statements Cheat Sheet


## 🧠 What is an `if` Statement?

It allows you to execute certain blocks of code **only if a condition is true**.

```python
if condition:
    # Code block runs only if condition is True
````

---

## ✅ Basic `if` Statement

```python
x = 10

if x > 5:
    print("x is greater than 5")
```

---

## ➕ `if-else` Statement

```python
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## 🔗 `if-elif-else` Chain

```python
score = 75

if score >= 90:
    print("A grade")
elif score >= 80:
    print("B grade")
elif score >= 70:
    print("C grade")
else:
    print("Fail")
```

---

## 🎯 Comparison Operators

| Operator | Meaning          | Example  |
| -------- | ---------------- | -------- |
| `==`     | Equal to         | `x == 5` |
| `!=`     | Not equal to     | `x != 5` |
| `>`      | Greater than     | `x > 5`  |
| `<`      | Less than        | `x < 5`  |
| `>=`     | Greater or equal | `x >= 5` |
| `<=`     | Less or equal    | `x <= 5` |

---

## 🔗 Logical Operators

| Operator | Description               | Example            |
| -------- | ------------------------- | ------------------ |
| `and`    | True if both are true     | `x > 5 and x < 10` |
| `or`     | True if at least one true | `x < 5 or x > 10`  |
| `not`    | Inverts the result        | `not(x > 10)`      |

---

## 🧩 Nested `if` Statements

```python
num = 10

if num > 0:
    if num % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")
```

---

## 🪓 Short-Hand (Ternary) `if` Expression

```python
x = 10
result = "Even" if x % 2 == 0 else "Odd"
print(result)
```

---

## 🧪 `if` with Booleans and Truthy Values

```python
if "hello":
    print("This will run")  # Non-empty string is truthy

if 0:
    print("This won’t run")  # 0 is falsy

if []:
    print("Empty list is falsy")
```

📌 Falsy values: `0`, `None`, `''`, `[]`, `{}`, `set()`, `False`

---

## 🛠️ `pass` in `if`

Used as a placeholder to avoid errors when you have no code yet.

```python
x = 5

if x > 0:
    pass  # TODO: Add logic later
```

---

## 📏 Match Multiple Conditions

```python
if name == "Alice" or name == "Bob":
    print("Welcome!")
```

✅ You can also use `in`:

```python
if name in ["Alice", "Bob"]:
    print("Welcome!")
```

---

## 🧠 Combining `if` with Functions

```python
def check_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
```

Shorthand:

```python
def check_even(num):
    return num % 2 == 0
```

---

## 📘 Practice Example

```python
temperature = 35

if temperature > 40:
    print("It's too hot!")
elif temperature > 30:
    print("It's warm.")
elif temperature > 20:
    print("Perfect weather.")
else:
    print("It's cold.")
```

---

## 📎 Reference

* [Python `if` Statement Docs](https://docs.python.org/3/tutorial/controlflow.html#if-statements)

