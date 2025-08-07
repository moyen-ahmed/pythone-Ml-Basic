

## 🧠 Table of Contents

1. [What is OOP?](#what-is-oop)
2. [Class and Object](#class-and-object)
3. [`__init__` Constructor](#init-constructor)
4. [Instance Variables vs Class Variables](#instance-vs-class-variables)
5. [Methods in Class](#methods-in-class)
6. [Encapsulation](#encapsulation)
7. [Inheritance](#inheritance)
8. [Polymorphism](#polymorphism)
9. [Abstraction](#abstraction)
10. [Magic/Dunder Methods](#magic-dunder-methods)
11. [Classmethod & Staticmethod](#classmethod-vs-staticmethod)
12. [Property Decorator (`@property`)](#property-decorator)
13. [OOP Best Practices](#oop-best-practices)

---

## 🧱 What is OOP?
Object-Oriented Programming is a programming paradigm based on the concept of **objects**, which contain **data (attributes)** and **code (methods)**.

**Benefits:**
- Reusability
- Modularity
- Scalability
- DRY (Don't Repeat Yourself)

---

## 🧩 Class and Object
A **class** is a blueprint, and an **object** is an instance of the class.

```python
class Car:
    pass

my_car = Car()  # object of class Car
```

---

## 🔨 `__init__` Constructor
Used to initialize the object's attributes.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Corolla")
```

---

## ⚖ Instance vs Class Variables

```python
class Dog:
    species = "Canine"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable
```

- `species` is shared by all instances.
- `name` is unique to each instance.

---

## 🛠 Methods in Class

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
```

---

## 🔒 Encapsulation
Hides internal details, exposing only what’s necessary.

```python
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
```

Use `__` (double underscore) for private variables.

---

## 👨‍👩‍👧 Inheritance
Allows a class to inherit attributes and methods from another class.

```python
class Animal:
    def speak(self):
        return "I make sound"

class Dog(Animal):
    def speak(self):
        return "Bark"
```

---

## 🎭 Polymorphism
Same method name but behaves differently depending on the object.

```python
def animal_sound(animal):
    print(animal.speak())

animal_sound(Dog())  # Bark
```

---

## 🧼 Abstraction
Hiding complex implementation using abstract base classes.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Engine started")
```

---

## ✨ Magic/Dunder Methods

These start and end with double underscores `__`.

```python
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"
```

Common dunder methods:
- `__init__`
- `__str__`
- `__len__`
- `__repr__`

---

## 🧭 `@classmethod` vs `@staticmethod`

```python
class MyClass:
    @classmethod
    def from_string(cls, string):
        return cls(string)

    @staticmethod
    def add(a, b):
        return a + b
```

- `@classmethod`: Receives class `cls` as first argument.
- `@staticmethod`: Doesn’t receive `self` or `cls`.

---

## 🧵 Property Decorator
Used to make method act like an attribute.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
```

---

## 🧙‍♂️ OOP Best Practices

- Keep classes **small** and **focused**
- Follow **Single Responsibility Principle**
- Prefer **composition** over inheritance when possible
- Use **descriptive** names for methods and variables
- Write **docstrings**

---

## 📚 Summary
Object-Oriented Programming makes your code reusable, scalable, and clean. Mastering OOP in Python opens the door to writing professional-grade software.

Stay curious, keep coding! 💻✨

---

