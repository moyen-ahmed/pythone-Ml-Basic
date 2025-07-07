

# 🐍 Python Strings Cheat Sheet


## 📌 What is a String?

A **string** is a sequence of characters enclosed in single `'` or double `"` quotes.

```python
s1 = 'Hello'
s2 = "World"
````

---

## 🔤 String Basics

```python
text = "Python"
print(len(text))     # 6
print(text[0])       # 'P'
print(text[-1])      # 'n'
```

---

## 🪓 String Slicing

```python
text = "programming"

print(text[0:4])     # 'prog'
print(text[4:])      # 'ramming'
print(text[:4])      # 'prog'
print(text[-3:])     # 'ing'
print(text[::-1])    # 'gnimmargorp' (reversed)
```

---

## 🔁 Looping Through Strings

```python
for char in "abc":
    print(char)
```

---

## 🎯 String Methods (Most Common)

| Method         | Description              | Example                         |
| -------------- | ------------------------ | ------------------------------- |
| `lower()`      | Lowercase all letters    | `'PYTHON'.lower()` → `'python'` |
| `upper()`      | Uppercase all letters    | `'python'.upper()` → `'PYTHON'` |
| `title()`      | Capitalize each word     | `'hello world'.title()`         |
| `strip()`      | Remove whitespace        | `'  hi  '.strip()`              |
| `replace()`    | Replace substring        | `'bad'.replace('b', 'g')`       |
| `find()`       | First index of substring | `'apple'.find('p')` → `1`       |
| `count()`      | Count occurrences        | `'banana'.count('a')` → `3`     |
| `startswith()` | Check start              | `'hello'.startswith('h')`       |
| `endswith()`   | Check end                | `'hello'.endswith('o')`         |

---

## 🧪 String Checks

```python
text = "Hello123"

print(text.isalpha())     # False (has numbers)
print(text.isdigit())     # False
print("123".isdigit())    # True
print(text.isalnum())     # True (alpha + num)
print(text.islower())     # False
print("hello".islower())  # True
```

---

## 🧩 f-Strings (Formatted Strings)

```python
name = "Alice"
age = 25

print(f"My name is {name} and I am {age} years old.")
```

You can also use expressions inside:

```python
print(f"2 + 2 = {2 + 2}")
```

---

## 🔗 String Concatenation and Repetition

```python
a = "Hello"
b = "World"

print(a + " " + b)     # 'Hello World'
print(a * 3)           # 'HelloHelloHello'
```

---

## 🧠 String Formatting (Old Style)

```python
name = "John"
print("Hello, %s!" % name)

age = 30
print("Age: %d" % age)
```

---

## ⚙️ Advanced Formatting

```python
pi = 3.1415926

print(f"{pi:.2f}")         # 3.14
print(f"{1000:,}")         # 1,000
print(f"{25:>5}")          # '   25' (right-aligned)
print(f"{25:<5}")          # '25   ' (left-aligned)
print(f"{25:^5}")          # ' 25  ' (centered)
```

---

## 🔒 String Immutability

Strings in Python are **immutable**, which means they can’t be changed after creation.

```python
text = "hello"
# text[0] = 'H'  # ❌ Error
text = "Hello"   # ✅ Reassign new string
```

---

## 🧵 Multiline Strings

```python
msg = """This is
a multiline
string"""
```

---

## 🧨 Escape Characters

| Escape | Meaning      |
| ------ | ------------ |
| `\n`   | New line     |
| `\t`   | Tab          |
| `\\`   | Backslash    |
| `\"`   | Double quote |
| `\'`   | Single quote |

```python
print("Hello\nWorld")
print("She said: \"Yes!\"")
```

---

## 🧰 String to List (Split) & List to String (Join)

```python
text = "a,b,c"
lst = text.split(",")     # ['a', 'b', 'c']

new_text = "-".join(lst)  # 'a-b-c'
```

---

## 🔍 String Searching

```python
"apple" in "pineapple"         # True
"banana" not in "pineapple"    # True
```

---

## 📘 Practice Example

```python
quote = "  The quick brown fox  "
result = quote.strip().upper().replace("FOX", "DOG")

print(result)  # 'THE QUICK BROWN DOG'
```

---

## 📎 Reference

* [Python Docs: Strings](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)


