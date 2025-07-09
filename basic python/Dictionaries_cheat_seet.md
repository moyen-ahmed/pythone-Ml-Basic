
## 🧩 What is a Dictionary?

A **dictionary** is an unordered, mutable, and indexed collection of key-value pairs.

```python
person = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}
````

---

## 🔑 Dictionary Syntax

```python
my_dict = {
    "key1": "value1",
    "key2": "value2"
}
```

✅ Keys must be **unique** and **immutable** (like strings, numbers, tuples).

---

## 🧠 Accessing Values

```python
person["name"]       # 'Alice'
person.get("age")    # 25
person.get("email", "Not found")  # Returns default if not exists
```

---

## 📝 Modifying Dictionary

```python
person["age"] = 30
person["email"] = "alice@example.com"
```

---

## ❌ Removing Items

```python
del person["age"]           # Removes key "age"
person.pop("email")         # Removes and returns value
person.clear()              # Empties the dictionary
```

---

## ✅ Checking Existence

```python
"name" in person         # True
"salary" not in person   # True
```

---

## 🔁 Looping Through Dictionary

```python
for key in person:
    print(key, person[key])

# OR
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## 📋 Dictionary Methods

| Method            | Description                         |
| ----------------- | ----------------------------------- |
| `.get(k)`         | Get value of key `k`                |
| `.keys()`         | Returns all keys                    |
| `.values()`       | Returns all values                  |
| `.items()`        | Returns key-value pairs             |
| `.update(dict)`   | Merge another dict                  |
| `.pop(k)`         | Remove key `k` and return its value |
| `.clear()`        | Remove all items                    |
| `.copy()`         | Shallow copy of dict                |
| `dict.fromkeys()` | Create dict from list of keys       |

---

## 🛠️ Dictionary Comprehension

```python
squares = {x: x*x for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

## 🔀 Merging Dictionaries

```python
a = {"x": 1}
b = {"y": 2}
merged = {**a, **b}
```

Or in Python 3.9+:

```python
merged = a | b
```

---

## 📦 Nested Dictionaries

```python
student = {
    "name": "Bob",
    "grades": {
        "math": 90,
        "science": 85
    }
}

student["grades"]["math"]  # 90
```

---

## 🧪 Advanced Tricks

### ✔ Create dict from two lists

```python
keys = ["a", "b", "c"]
values = [1, 2, 3]
zipped = dict(zip(keys, values))
```

### ✔ Count frequency of items

```python
from collections import Counter

data = ["apple", "banana", "apple"]
counts = Counter(data)
# {'apple': 2, 'banana': 1}
```

### ✔ Default value with defaultdict

```python
from collections import defaultdict

d = defaultdict(int)
d["a"] += 1
# d = {'a': 1}
```

---

## 🧵 Dictionary vs List

| Feature    | Dictionary          | List              |
| ---------- | ------------------- | ----------------- |
| Access     | By key              | By index          |
| Uniqueness | Keys must be unique | Values can repeat |
| Ordering   | Ordered (since 3.7) | Ordered           |
| Use Case   | Mapping             | Sequencing        |

---

## 📘 Practice Example

```python
user = {
    "username": "admin",
    "permissions": ["read", "write", "delete"]
}

if "write" in user["permissions"]:
    print(f"{user['username']} can write.")
```

---

## 📎 Reference

* [Python Official Docs – `dict`](https://docs.python.org/3/library/stdtypes.html#dict)

