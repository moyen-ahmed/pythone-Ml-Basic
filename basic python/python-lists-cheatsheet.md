
# 📋 Python Lists Cheat Sheet


## 🔰 What is a List?

A **list** is an ordered, mutable (changeable) collection of items.

```python
fruits = ["apple", "banana", "cherry"]
````

---

## ✅ List Features

* Ordered
* Mutable (can change items)
* Allow duplicates
* Can contain **mixed data types**: numbers, strings, even other lists

```python
mixed = [1, "hello", 3.14, [1, 2]]
```

---

## 🎯 Creating Lists

```python
empty = []
numbers = list(range(5))      # [0, 1, 2, 3, 4]
chars = list("hello")         # ['h', 'e', 'l', 'l', 'o']
```

---

## 🔍 Accessing Items

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])      # 'apple'
print(fruits[-1])     # 'cherry'
```

---

## ✂️ Slicing Lists

```python
fruits = ["apple", "banana", "cherry", "date", "fig"]

print(fruits[1:4])    # ['banana', 'cherry', 'date']
print(fruits[:2])     # ['apple', 'banana']
print(fruits[::2])    # ['apple', 'cherry', 'fig']
print(fruits[::-1])   # reversed list
```

---

## 🔁 Looping Through a List

```python
for fruit in fruits:
    print(fruit)

# With index
for i, val in enumerate(fruits):
    print(i, val)
```

---

## ➕ List Operations

| Operation     | Example             | Result            |
| ------------- | ------------------- | ----------------- |
| Concatenation | `[1, 2] + [3, 4]`   | `[1, 2, 3, 4]`    |
| Repetition    | `['a'] * 3`         | `['a', 'a', 'a']` |
| Membership    | `'apple' in fruits` | `True/False`      |

---

## 🛠️ Modifying Lists

```python
fruits[1] = "blueberry"        # Change value
fruits.append("grape")         # Add at end
fruits.insert(1, "kiwi")       # Insert at index
fruits.extend(["pear", "plum"]) # Add multiple
```

---

## ❌ Removing Items

```python
fruits.remove("banana")       # Remove by value
fruits.pop()                  # Remove last
fruits.pop(1)                 # Remove by index
del fruits[0]                 # Delete by index
fruits.clear()                # Remove all
```

---

## 📋 List Methods Overview

| Method      | Description                     |
| ----------- | ------------------------------- |
| `append()`  | Add item to the end             |
| `insert()`  | Insert at a specific index      |
| `extend()`  | Add multiple items              |
| `remove()`  | Remove first matching item      |
| `pop()`     | Remove and return item by index |
| `clear()`   | Remove all items                |
| `index()`   | Find index of value             |
| `count()`   | Count occurrences               |
| `sort()`    | Sort list in-place              |
| `reverse()` | Reverse list in-place           |
| `copy()`    | Shallow copy of list            |

---

## 🔍 Searching and Counting

```python
fruits = ["apple", "banana", "apple", "cherry"]

fruits.index("banana")     # 1
fruits.count("apple")      # 2
```

---

## 📊 Sorting Lists

```python
nums = [5, 2, 9, 1]

nums.sort()                # Ascending: [1, 2, 5, 9]
nums.sort(reverse=True)    # Descending

words = ["apple", "Banana", "cherry"]
words.sort(key=str.lower)  # Case-insensitive sort
```

---

## 📚 Copying Lists (Don’t Do This 👇)

```python
wrong = list1 = list2      # both point to same memory ❌
```

✅ Correct Ways to Copy:

```python
copy1 = list1.copy()
copy2 = list(list1)
copy3 = list1[:]
```

---

## 🧠 List Comprehensions (Advanced 🔥)

```python
squares = [x**2 for x in range(5)]      # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x%2==0] # [0, 2, 4, 6, 8]
```

---

## 🧩 Nested Lists

```python
matrix = [[1, 2], [3, 4]]

print(matrix[0][1])    # 2
```

---

## 🧪 Other Tricks

```python
max([1, 2, 3])        # 3
min([1, 2, 3])        # 1
sum([1, 2, 3])        # 6
list("hello")         # ['h', 'e', 'l', 'l', 'o']
```

---

## 🧼 Clean List (Remove Duplicates)

```python
unique = list(set([1, 2, 2, 3, 3]))   # [1, 2, 3]
```

---

## 📘 Practice Example

```python
nums = [1, 2, 3, 4, 5]

squared_even = [x**2 for x in nums if x % 2 == 0]
print(squared_even)  # [4, 16]
```

---

## 📎 Reference

* [Python Official Docs - Lists](https://docs.python.org/3/tutorial/datastructures.html)

