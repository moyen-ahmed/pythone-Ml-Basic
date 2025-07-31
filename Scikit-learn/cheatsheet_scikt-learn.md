

## Table of Contents
1. [Getting Started](#getting-started)  
2. [Supervised Learning](#supervised-learning)  
   - [Regression](#regression)  
     - [Linear Regression](#linear-regression)  
     - [Multiple Linear Regression](#multiple-linear-regression)  
     - [Ridge & Lasso Regression](#ridge--lasso-regression)  
   - [Classification](#classification)  
     - [Logistic Regression](#logistic-regression)  
     - [Support Vector Machines (SVM)](#support-vector-machines-svm)  
     - [k-Nearest Neighbors (KNN)](#k-nearest-neighbors-knn)  
     - [Decision Trees & Random Forests](#decision-trees--random-forests)  
3. [Unsupervised Learning](#unsupervised-learning)  
   - [Clustering](#clustering)  
   - [Dimensionality Reduction](#dimensionality-reduction)  
4. [Model Evaluation & Selection](#model-evaluation--selection)  
   - [Metrics](#metrics)  
   - [Cross-Validation](#cross-validation)  
   - [Hyperparameter Tuning](#hyperparameter-tuning)  
5. [Pipelines & Feature Engineering](#pipelines--feature-engineering)  
6. [Advanced Topics](#advanced-topics)  
   - [Custom Transformers](#custom-transformers)  
   - [Ensemble Methods](#ensemble-methods)  
   - [Model Persistence](#model-persistence)  
   - [Out-of-Core Learning](#out-of-core-learning)  
7. [Tips & Best Practices](#tips--best-practices)

---

## Getting Started
```bash
pip install scikit-learn
```
```python
from sklearn import datasets
from sklearn.model_selection import train_test_split

# Load example dataset
data = datasets.load_boston()
X, y = data.data, data.target

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
```

---

## Supervised Learning

### Regression

#### Linear Regression
```python
from sklearn.linear_model import LinearRegression

model = LinearRegression(
    fit_intercept=True,  # whether to calculate the intercept for this model
    normalize=False      # whether to normalize the regressors
)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

#### Multiple Linear Regression
*Same `LinearRegression` class, just with multiple features.*

#### Ridge & Lasso Regression
```python
from sklearn.linear_model import Ridge, Lasso

ridge = Ridge(alpha=1.0)   # L2 regularization strength
lasso = Lasso(alpha=0.1)   # L1 regularization strength

ridge.fit(X_train, y_train)
lasso.fit(X_train, y_train)
```

---

### Classification

#### Logistic Regression
```python
from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(
    penalty='l2',    # norm used in the penalization
    C=1.0,           # inverse of regularization strength
    solver='lbfgs'   # algorithm to use in the optimization problem
)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
```

#### Support Vector Machines (SVM)
```python
from sklearn.svm import SVR, SVC

# Regression
svr = SVR(kernel='rbf', C=1.0, epsilon=0.1)
svr.fit(X_train, y_train)

# Classification
svc = SVC(kernel='linear', C=1.0)
svc.fit(X_train, y_train)
```

#### k-Nearest Neighbors (KNN)
```python
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor

# Classification
knn_clf = KNeighborsClassifier(n_neighbors=5)
knn_clf.fit(X_train, y_train)

# Regression
knn_reg = KNeighborsRegressor(n_neighbors=5)
knn_reg.fit(X_train, y_train)
```

#### Decision Trees & Random Forests
```python
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

# Decision Tree
dt_reg = DecisionTreeRegressor(max_depth=5, random_state=42)
dt_reg.fit(X_train, y_train)

# Random Forest
rf_reg = RandomForestRegressor(n_estimators=100, max_depth=7, random_state=42)
rf_reg.fit(X_train, y_train)
```

---

## Unsupervised Learning

### Clustering
```python
from sklearn.cluster import KMeans, DBSCAN

kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X)

dbscan = DBSCAN(eps=0.5, min_samples=5)
labels_db = dbscan.fit_predict(X)
```

### Dimensionality Reduction
```python
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X)
```

---

## Model Evaluation & Selection

### Metrics
- **Regression**: MAE, MSE, RMSE, R², Adjusted R²  
- **Classification**: Accuracy, Precision, Recall, F1-score, ROC-AUC

```python
from sklearn.metrics import (
    mean_absolute_error, mean_squared_error, r2_score,
    accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
)
```

### Cross-Validation
```python
from sklearn.model_selection import cross_val_score, KFold

cv = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=cv, scoring='r2')
```

### Hyperparameter Tuning
```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

param_grid = {'n_estimators': [50, 100, 200], 'max_depth': [5, 10, None]}
grid = GridSearchCV(rf_reg, param_grid, cv=3, scoring='r2')
grid.fit(X_train, y_train)
print(grid.best_params_, grid.best_score_)
```

---

## Pipelines & Feature Engineering
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

numeric_features = ['age', 'fare']
numeric_transformer = Pipeline([
    ('scaler', StandardScaler())
])

categorical_features = ['embarked', 'sex']
categorical_transformer = Pipeline([
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer([
    ('num', numeric_transformer, numeric_features),
    ('cat', categorical_transformer, categorical_features)
])

pipe = Pipeline([
    ('pre', preprocessor),
    ('model', RandomForestRegressor())
])

pipe.fit(X_train, y_train)
```

---

## Advanced Topics

### Custom Transformers
```python
from sklearn.base import TransformerMixin, BaseEstimator

class CustomAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_value=1):
        self.add_value = add_value
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X + self.add_value

# Usage in pipeline:
pipe = Pipeline([
    ('adder', CustomAdder(add_value=10)),
    ('model', LinearRegression())
])
```

### Ensemble Methods
- **Bagging**: `BaggingClassifier`, `BaggingRegressor`  
- **Boosting**: `GradientBoostingRegressor`, `AdaBoostClassifier`

### Model Persistence
```python
import joblib

# Save
joblib.dump(model, 'model.pkl')

# Load
loaded = joblib.load('model.pkl')
```

### Out-of-Core Learning
```python
from sklearn.linear_model import SGDRegressor

sgd = SGDRegressor()
sgd.partial_fit(X_batch, y_batch)
```

---

## Tips & Best Practices
- **Always** split data before preprocessing.
- **Scale** features for distance-based algorithms.
- **Use** pipelines to avoid data leakage.
- **Evaluate** multiple metrics.
- **Visualize** data distributions and relationships.
- **Document** experiments and random seeds.

---

*Cheat Sheet created for quick reference of Scikit-Learn workflows, from basic to advanced.*