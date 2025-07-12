

## 🧑‍💻 User Input (`input()`)

### 📌 Basic Input
```python
name = input("What is your name? ")
print("Hello,", name)
````

* Returns a **string** by default.

### 🔄 Type Casting

```python
age = int(input("Enter your age: "))   # Convert to int
price = float(input("Enter price: "))  # Convert to float
```

### ✅ Input Validation Example

```python
age = input("Enter your age: ")

if age.isdigit():
    age = int(age)
    print("You are", age, "years old")
else:
    print("Invalid age!")
```

---

## 🔁 While Loops

### 📌 Basic Syntax

```python
while condition:
    # code block
```

### 🔁 Example: Counting

```python
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1
```

---

## ❗ Infinite Loops (Be Careful!)

```python
while True:
    print("I will run forever... unless you stop me!")
```

✅ Stop using `break`, or `Ctrl+C` in terminal.

---

## 🛑 Using `break` and `continue`

### 🔚 `break` — Exit the loop early

```python
while True:
    user_input = input("Type 'exit' to stop: ")
    if user_input == "exit":
        break
```

### ⏭️ `continue` — Skip current iteration

```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
```

---

## ⛓️ While Loop with Else

```python
x = 0
while x < 3:
    print("x =", x)
    x += 1
else:
    print("Loop finished!")
```

✅ The `else` block runs **only if loop didn’t break**.

---

## 🎯 Real-World Examples

### ✅ 1. Login Attempt Limit

```python
attempts = 0
while attempts < 3:
    password = input("Enter password: ")
    if password == "admin123":
        print("Access granted!")
        break
    else:
        print("Wrong password!")
        attempts += 1
else:
    print("Too many failed attempts.")
```

---

### ✅ 2. Menu System

```python
while True:
    print("\nMenu:\n1. Add\n2. Subtract\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        print("Addition selected")
    elif choice == "2":
        print("Subtraction selected")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
```

---

## ✅ Good Practices

| Bad Practice      | Good Practice                |
| ----------------- | ---------------------------- |
| Infinite loops    | Use `break` wisely           |
| Raw input strings | Typecast using `int()`, etc. |
| No input check    | Validate using `.isdigit()`  |
| Hard exit logic   | Use `while True` + `break`   |

---

## 💡 Quick Recap

* `input()` always returns a **string**
* Use `int()`, `float()` to convert input
* `while` keeps running while condition is `True`
* Use `break` to stop, `continue` to skip
* `while...else` runs else when loop ends **naturally**

---

## 📎 References

* [Python `input()` Docs](https://docs.python.org/3/library/functions.html#input)
* [Python `while` Loop Docs](https://docs.python.org/3/reference/compound_stmts.html#while)

---
