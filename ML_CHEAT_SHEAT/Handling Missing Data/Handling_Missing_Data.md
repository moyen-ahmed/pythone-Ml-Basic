# Handling Missing Data: A Practical, End‑to‑End Guide

**Audience:** data analysts, ML practitioners, researchers  
**Goal:** understand types of missingness, choose the right strategy, and implement robust pipelines (with reproducible Python code).

---

## 1) Why Missing Data Matters

Missing values distort distributions, bias parameter estimates, and silently break models. A good workflow: **detect → diagnose → decide → implement → validate**.

---

## 2) Taxonomy: Types of Missingness (Mechanism ≠ Amount)

1. **MCAR (Missing Completely At Random).**  
   Probability of missingness is independent of observed and unobserved data.  
   *Impact:* listwise deletion is unbiased but less efficient.

2. **MAR (Missing At Random).**  
   Missingness depends only on **observed** variables (e.g., income missing more often for younger people, but we know age).  
   *Impact:* model‑based/multiple imputation can be unbiased if the imputation model includes the predictors of missingness.

3. **MNAR (Missing Not At Random).**  
   Missingness depends on the **unobserved** value itself (e.g., people with very high income don’t report it).  
   *Impact:* requires sensitivity analyses, explicit modeling of the missingness process, or external data/assumptions.

> **Rule of thumb:** treat data as MAR unless domain knowledge suggests MNAR; then perform sensitivity checks.

---

## 3) Quick Audit: How Much Is Missing and Where?

```python
import pandas as pd

df = pd.read_csv("your_data.csv")

# basic counts
missing_per_col = df.isna().sum().sort_values(ascending=False)
missing_rate_per_col = df.isna().mean().sort_values(ascending=False)

# row-level missingness
rows_any_missing = df.isna().any(axis=1).mean()

# pairwise missing overlap
overlap = df.isna().T.dot(df.isna())  # square matrix of co-missing counts

print(missing_per_col.head(10))
print(missing_rate_per_col.head(10))
print(f"% rows with any missing: {rows_any_missing:.1%}")
print(overlap)
```

**What to look for:**  
- variables with >30% missing → consider removal or specialized methods  
- structured patterns (all missing when another field has a value) → data quality rule or conditional imputation  
- time‑dependent gaps → use time‑series methods

---

## 4) Strategy Map — “How Many Ways?” (by Category)

**A. Elimination**
- A1. **Listwise deletion** (drop rows with any NA).  
- A2. **Pairwise deletion** (use available cases per analysis).  
- A3. **Drop variables** with too much missingness.

**B. Simple Deterministic Imputation**
- B1. **Constant imputation** (e.g., 0, “Unknown”).  
- B2. **Mean/median** (numeric).  
- B3. **Mode/most frequent** (categorical).  
- B4. **Group‑wise imputation** (impute within strata, e.g., by gender or region).

**C. Model‑Based Single Imputation**
- C1. **k‑Nearest Neighbors (KNN)** imputation.  
- C2. **Regression imputation** (predict missing from other features).  
- C3. **Iterative multivariate imputation (MICE‑style)** — chained equations.

**D. Multiple Imputation (MI)**
- D1. **Generate M>1 imputed datasets**, analyze each, then **pool** estimates (Rubin’s rules).

**E. Time‑Series Specific**
- E1. **Forward/Backward fill** (carry last/next observation).  
- E2. **Interpolation** (linear, spline, polynomial).  
- E3. **State‑space/ARIMA/Kalman smoothing**.

**F. Algorithm‑Aware Handling**
- F1. **Tree ensembles with built‑in missing handling** (e.g., LightGBM, CatBoost).  
- F2. **Create missingness indicators** (flags) + impute, then let the model learn the signal.

**G. Domain/Rule‑Based**
- G1. **Business rules** (e.g., if “units_sold=0” then “revenue=0”).  
- G2. **External data linkage** to fill gaps (geocoding, lookups).

**H. MNAR & Sensitivity**
- H1. **Selection/Pattern‑mixture models.**  
- H2. **Delta adjustments** and **tipping‑point** analyses.

> In practice: start with B+F (simple + indicator flags) as a baseline; escalate to C/D/E for performance and bias control.

---

## 5) Practical Recipes with Python

### 5.1 Baseline: Simple Imputation + Flags in a Pipeline

```python
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

# Example schema
num_features = ["age", "income", "balance"]
cat_features = ["segment", "region"]

numeric_transformer = Pipeline(steps=[
    ("flag_missing", SimpleImputer(strategy="constant", fill_value=np.nan)),  # placeholder
    # add a missingness flag by comparing to initial nulls
])

# Better: create flags before imputation
class MissingFlagger:
    def __init__(self, features):
        self.features = features
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        X = X.copy()
        for f in self.features:
            X[f + "_is_missing"] = X[f].isna().astype(int)
        return X

from sklearn.base import BaseEstimator, TransformerMixin
class ColumnSelector(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.columns]

# Build preprocessing
pre_flags = Pipeline(steps=[
    ("flags", MissingFlagger(num_features))
])

numeric_impute = Pipeline(steps=[
    ("select", ColumnSelector(num_features)),
    ("imputer", SimpleImputer(strategy="median"))
])

categorical_impute = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocess = ColumnTransformer(
    transformers=[
        ("num", numeric_impute, num_features),
        ("cat", categorical_impute, cat_features),
    ],
    remainder="drop",
)

clf = Pipeline(steps=[
    ("add_flags", pre_flags),
    ("preprocess", preprocess),
    ("model", LogisticRegression(max_iter=200))
])
```

**Notes**
- Add *_is_missing flags **before** imputation so the signal is not lost.  
- Fit imputers **on training data only**, then transform validation/test to prevent leakage.

---

### 5.2 k‑NN Imputation

```python
from sklearn.impute import KNNImputer

knn_imputer = KNNImputer(n_neighbors=5, weights="distance")
X_num = df[num_features]
X_num_imputed = knn_imputer.fit_transform(X_num)  # fit on train only in real projects
```

**When to use:** non‑linear relations, moderate missingness, features on similar scales (consider StandardScaler first).  
**Caveats:** expensive for large N, sensitive to irrelevant features and scale.

---

### 5.3 Iterative (MICE‑style) Imputation

```python
from sklearn.experimental import enable_iterative_imputer  # noqa
from sklearn.impute import IterativeImputer
from sklearn.ensemble import RandomForestRegressor

mice = IterativeImputer(
    estimator=RandomForestRegressor(n_estimators=200, n_jobs=-1, random_state=42),
    max_iter=10,
    sample_posterior=True,   # adds uncertainty
    random_state=42
)
X_num = df[num_features]
X_num_mice = mice.fit_transform(X_num)
```

**Pros:** captures multivariate structure; with `sample_posterior=True` approximates MI draws.  
**Cons:** slower; ensure convergence; set sensible `max_iter` and monitor imputation diagnostics.

---

### 5.4 Multiple Imputation Proper (Analysis + Pooling)

```python
import numpy as np
from sklearn.linear_model import LinearRegression

M = 5  # number of imputations
fits = []
preds = []

for m in range(M):
    imp = IterativeImputer(sample_posterior=True, random_state=42 + m, max_iter=10)
    X_imp = imp.fit_transform(df[num_features])
    y = df["target"].values
    mask = ~np.isnan(y)
    model = LinearRegression().fit(X_imp[mask], y[mask])
    fits.append(model)
    preds.append(model.predict(X_imp))

# pool predictions as simple average (for metrics); for inference, use Rubin's rules for parameters/SEs
pooled_pred = np.mean(np.column_stack(preds), axis=1)
```

**Key idea:** reflect imputation **uncertainty** by analyzing multiple imputed datasets and pooling. For classical statistical inference, apply **Rubin’s rules** to coefficients and variances.

---

### 5.5 Time‑Series Imputation

```python
# Assume df is indexed by a DateTimeIndex and has a numeric column 'y'
# Forward/Backward fill
df["y_ffill"] = df["y"].ffill()
df["y_bfill"] = df["y"].bfill()

# Linear interpolation
df["y_interp"] = df["y"].interpolate(method="time")

# Spline interpolation (needs SciPy)
# df["y_spline"] = df["y"].interpolate(method="spline", order=3)
```

**Tips:**  
- Forward fill is reasonable for **stock-like** level variables; avoid for cumulative metrics.  
- Always validate by backtesting models trained on imputed series.

---

### 5.6 Categorical “Missing as Category”

```python
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.impute import SimpleImputer

cat = ["color", "segment"]
pre_cat = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="constant", fill_value="__MISSING__")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])
```

**When useful:** genuine absence contains signal (e.g., “no response”).  
**When risky:** when “missing” has no semantic meaning (measurement error).

---

### 5.7 Algorithm‑Native Missing Handling

- **CatBoost**: handles missing values natively with ordered statistics.  
- **LightGBM**: learns default directions for missing values at splits.  
- **XGBoost**: supports a default branch for missing.

```python
from lightgbm import LGBMClassifier

lgbm = LGBMClassifier(n_estimators=500)
lgbm.fit(X_train, y_train)  # can pass NaNs without pre-imputing numeric features
```

**Still recommended:** keep **missingness flags**; they can boost performance.

---

## 6) Choosing a Method — A Decision Checklist

1. **Mechanism?** Assume MAR unless MNAR is plausible → consider sensitivity.  
2. **Amount?** Low (<5%): simple imputation is often fine. Moderate (5–30%): consider KNN/MICE. High (>30%): re‑think feature, external data, or MI.  
3. **Data type & structure?** Time‑series vs. cross‑sectional; numeric vs. categorical.  
4. **Scale & compute?** KNN/MICE may be slow on very wide or tall data.  
5. **Model compatibility?** Tree‑based vs. linear models; native handling available?  
6. **Evaluation?** Use a **held‑out** set and compare pipelines end‑to‑end.

---

## 7) Leakage‑Safe Training/Validation Split

```python
from sklearn.model_selection import train_test_split

X = df.drop(columns=["target"])
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Fit imputers only on training data inside a Pipeline, then transform test automatically.
```

---

## 8) Diagnostics & Validation

- **Distributional checks:** compare original vs. imputed distributions (KDE/ECDF).  
- **Downstream metrics:** accuracy/AUC/RMSE comparing pipelines.  
- **Convergence (MICE):** monitor changes across iterations.  
- **Sensitivity (MNAR):** shift imputed values by a delta and observe impact (tipping‑point analysis).

```python
import numpy as np

def tipping_point(y_pred_base, y_pred_imputed, deltas=np.linspace(-1,1,9)):
    impacts = []
    for d in deltas:
        impacts.append(((y_pred_imputed + d) - y_pred_base).mean())
    return np.array(impacts)
```

---

## 9) Common Pitfalls (and Fixes)

- **Imputing target variable.** Avoid; if necessary, use MI with caution and report sensitivity.  
- **Imputing before split.** Causes leakage. Always fit imputers on train only.  
- **Dropping rows blindly.** MCAR rarely holds; check patterns first.  
- **Ignoring categorical missingness.** Often predictive; use flags or “missing” category.  
- **Forgetting uncertainty.** Prefer MI for inference; report limitations.  
- **Scaling after KNN imputation.** Scale **before** KNN, or include scaling in the pipeline.

---

## 10) Minimal, Reusable Template

```python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer, KNNImputer

num = ["x1","x2","x3"]
cat = ["c1","c2"]

numeric_pipe = Pipeline([
    ("scale", StandardScaler(with_mean=False)),  # if sparse; else with_mean=True
    ("impute", KNNImputer(n_neighbors=5))
])

categorical_pipe = Pipeline([
    ("impute", SimpleImputer(strategy="constant", fill_value="__MISSING__")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

pre = ColumnTransformer([
    ("num", numeric_pipe, num),
    ("cat", categorical_pipe, cat)
])
```

---

## 11) Reporting: What to Document in Papers/Reports

- Missingness per variable and overall rate  
- Assumed mechanism (MCAR/MAR/MNAR) and justification  
- Chosen imputation strategy and hyperparameters  
- Leakage controls (train/test protocol)  
- Diagnostics, sensitivity analyses, and limitations

---

## 12) Quick Reference (Cheat Sheet)

| Situation | Good First Choice | Alternatives | Notes |
|---|---|---|---|
| Low missing (<5%), numeric | Median + flag | Mean, constant | Robust, simple |
| Categorical with “meaningful missing” | Missing-as-category | Mode | Keep a flag too |
| Moderate missing (5–30%), multivariate | MICE | KNN, regression | Add predictors of missingness |
| Time series gaps | Interpolation | FFill/BFill, Kalman | Validate via backtests |
| Tree models (LightGBM/CatBoost) | Native handling + flags | Simple impute | Often strongest baseline |
| Inference required | Multiple imputation | Sensitivity analysis | Report pooling rules |

---

### Final Take

Start pragmatic: **flags + simple imputation** in a pipeline. If bias/performance concerns remain, escalate to **MICE or model‑native handling**, and always validate with **sensitivity** and **out‑of‑sample** checks.
