
## 📦 Importing

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
````

---

## 🧾 Type of Data You Can Plot

* Lists or NumPy arrays
* Pandas Series/DataFrame
* Mathematical functions

---

## 📈 2-D Line Plot

### ✅ Plotting a Simple Function

```python
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()
```

---

### ✅ From a Pandas DataFrame

```python
df = pd.DataFrame({
    'x': [1, 2, 3, 4],
    'y': [2, 4, 6, 8]
})

plt.plot(df['x'], df['y'])
plt.title("Line Plot from DataFrame")
plt.show()
```

---

## 📉 Multiple Plots, Labels, Title

```python
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), label='sin(x)')
plt.plot(x, np.cos(x), label='cos(x)')
plt.title("Sin and Cos Functions")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.grid(True)
plt.show()
```

---

## 🎨 Colors, Line Style, Marker

```python
plt.plot(x, np.sin(x), color="#1f77b4", linewidth=2, linestyle='--', marker='o', markersize=5)
plt.title("Custom Line Style & Marker")
plt.show()
```

---

## 🧭 Legend Location

```python
plt.plot(x, np.sin(x), label="sin(x)")
plt.legend(loc='upper right')  # Locations: 'best', 'upper left', etc.
plt.show()
```

---

## 📐 Limiting Axes

```python
plt.plot(x, np.sin(x))
plt.xlim(0, 5)
plt.ylim(-1, 1)
plt.show()
```

---

## ✅ Grid and Show

```python
plt.plot(x, np.sin(x))
plt.grid(True)
plt.show()
```

---

# 🔵 Scatter Plots

### ✅ Simple Function

```python
x = np.linspace(0, 10, 50)
y = np.sin(x)
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()
```

---

### ✅ Scatter on Pandas Data

```python
df = pd.DataFrame({
    'height': [150, 160, 170],
    'weight': [50, 60, 70]
})

plt.scatter(df['height'], df['weight'])
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()
```

---

### ✅ Labeling, Marker, Size

```python
plt.scatter(x, y, color='red', s=100, marker='*', label="points")
plt.legend()
plt.show()
```

---

### ✅ Scatterplot Using `plt.plot`

```python
plt.plot(x, y, 'o')  # 'o' means dot marker
plt.show()
```

---

### 🤔 plt.plot vs plt.scatter

| Feature      | `plt.plot()`     | `plt.scatter()`           |
| ------------ | ---------------- | ------------------------- |
| Use          | Line/Marker      | Dot clouds only           |
| Performance  | Faster for lines | Better for scattered data |
| Size Control | Less direct      | `s=` controls marker size |

---

# 📊 Bar Charts

### ✅ Simple Bar Chart

```python
categories = ['A', 'B', 'C']
values = [3, 7, 5]

plt.bar(categories, values)
plt.title("Simple Bar Chart")
plt.show()
```

---

### ✅ Horizontal Bar Chart

```python
plt.barh(categories, values)
plt.title("Horizontal Bar Chart")
plt.show()
```

---

### ✅ Multiple Bar Charts

```python
labels = ['A', 'B', 'C']
men = [20, 35, 30]
women = [25, 32, 34]

x = np.arange(len(labels))
width = 0.35

plt.bar(x - width/2, men, width, label='Men')
plt.bar(x + width/2, women, width, label='Women')

plt.xticks(x, labels)
plt.legend()
plt.title("Grouped Bar Chart")
plt.show()
```

---

### ❗ Problem - Label Overlapping

```python
plt.xticks(rotation=45)
```

---

### ✅ Stacked Bar Chart

```python
plt.bar(labels, men, label='Men')
plt.bar(labels, women, bottom=men, label='Women')
plt.legend()
plt.title("Stacked Bar Chart")
plt.show()
```

---

## ❓ Bar Chart Doubts

* Use `plt.bar()` for vertical bars
* Use `plt.barh()` for horizontal
* Adjust `width`, `label`, and `bottom` for grouped/stacked charts

---

# 📊 Histogram

### ✅ Simple Data - Histogram

```python
data = np.random.randn(1000)
plt.hist(data, bins=30, color='skyblue')
plt.title("Histogram")
plt.show()
```

---

### ✅ Histogram on Dataset

```python
df = pd.read_csv("data.csv")
plt.hist(df['age'], bins=10)
plt.title("Age Distribution")
plt.show()
```

---

### ✅ Logarithmic Scale

```python
plt.hist(data, bins=30, log=True)
plt.title("Log-Scaled Histogram")
plt.show()
```

---

# 🥧 Pie Chart

### ✅ Simple Data Pie Chart

```python
sizes = [25, 35, 40]
labels = ['A', 'B', 'C']

plt.pie(sizes, labels=labels)
plt.title("Simple Pie Chart")
plt.show()
```

---

### ✅ Pie Chart with Dataset

```python
df = pd.DataFrame({
    'labels': ['Apple', 'Banana', 'Cherry'],
    'values': [30, 40, 30]
})

plt.pie(df['values'], labels=df['labels'])
plt.show()
```

---

### ✅ Percentages, Colors, Explode, Shadow

```python
sizes = [40, 35, 25]
labels = ['Python', 'C++', 'Java']
colors = ['#ff9999','#66b3ff','#99ff99']
explode = (0.1, 0, 0)  # explode 1st slice

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140,
        colors=colors, explode=explode, shadow=True)

plt.title("Pie Chart with Style")
plt.show()
```

---

# 🧠 Summary

* Use **`plt.plot`** for lines, **`plt.scatter`** for points
* Use **`plt.bar`**/`barh` for vertical/horizontal bars
* Use **`plt.hist`** for distributions
* Use **`plt.pie`** for proportions
* Always remember `plt.title`, `plt.xlabel`, `plt.ylabel`, and `plt.legend`

---

## 📎 Reference

* [Matplotlib Official Docs](https://matplotlib.org/stable/contents.html)