
# 🐍 Python Variables Cheat Sheet


## 📌 What is a Variable?

A **variable** is a named container to store data.

```python
x = 10
name = "Alice"
pi = 3.14
````

---

## 🧠 Variable Naming Rules

✅ Valid:

* Must start with a letter (a–z, A–Z) or underscore (`_`)
* Can contain letters, digits, and underscores
* Case-sensitive (`age` and `Age` are different)

❌ Invalid:

* Cannot start with a digit
* Cannot contain spaces or special characters like `@`, `#`, `$`

```python
valid_name = "OK"
_valid = 123
2cool = "Nope"    # ❌ Starts with digit
my-name = "Nope"  # ❌ Contains hyphen
```

---

## 📚 Variable Types (Dynamic Typing)

Python is **dynamically typed** – you don’t need to declare the type.

```python
age = 25               # int
price = 19.99          # float
name = "Bob"           # str
is_active = True       # bool
items = [1, 2, 3]      # list
info = {"key": "val"}  # dict
```

---

## 🔄 Type Casting (Conversion)

```python
int("10")      # 10
str(10)        # "10"
float("3.14")  # 3.14
bool(1)        # True
```

---

## 🛠️ Multiple Assignment

```python
a, b, c = 1, 2, 3
x = y = z = 0
```

---

## 📏 Checking Variable Type

```python
type(123)        # <class 'int'>
type("hello")    # <class 'str'>
```

---

## 🗑️ Deleting Variables

```python
del x
```

---

## 🧪 Useful Built-in Functions

```python
id(x)              # Memory address of x
type(x)            # Type of x
isinstance(x, int) # Checks if x is an integer
```

---

## 🚨 Reserved Keywords (Can’t Use as Variable Names)

```
False, None, True, and, as, assert, async, await,
break, class, continue, def, del, elif, else, except,
finally, for, from, global, if, import, in, is, lambda,
nonlocal, not, or, pass, raise, return, try, while, with, yield
```

---

## 💡 Tips

* Use lowercase + underscores for variable names: `user_name`
* Constants: use all caps: `PI = 3.1416`
* Use meaningful names: `count` is better than `c`

---

## 📘 Example Practice

```python
name = "John"
age = 21
height = 5.9
is_student = True

print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")
```

---

## 📎 Reference

* [Python Official Docs - Variables](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator)
