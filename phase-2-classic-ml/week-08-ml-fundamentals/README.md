# Week 8 - ML Fundamentals & Feature Engineering

> Phase 2: Classical ML + Project 1 · ML Platform Engineer Journey

---

## What I Learned

- Overfitting vs underfitting: a model that scores perfectly on training data and falls apart on new data has memorised the noise, not learned the pattern. Getting the balance right is the core challenge of ML.
- Train/validation/test splits: two splits aren't enough. Every time you peek at test results and adjust the model, that set stops being honest. Three splits - test set touched once, at the very end.
- Data leakage: when information the model shouldn't have seen sneaks into training. Subtle, hard to catch, and it destroys any honest measure of performance.
- Cross-validation: a single 80/20 split can get lucky or unlucky depending on which rows end up where. K-fold runs 5 splits and averages the scores. Our single split gave R² = 0.1092. Cross-validation gave 0.0866. The single split got lucky.
- Bias-variance tradeoff: simpler models underfit (high bias), complex models overfit (high variance). Can't minimise both at once.
- Linear regression: slope × feature + intercept = prediction. Trained on 752 shows, evaluated on 188. MSE, RMSE, R² all calculated and interpreted.
- Random Forest classification: created is_high_quality target from median vote_average, trained, evaluated with confusion matrix, classification report, ROC curve. AUC = 0.73.
- Feature engineering pipeline: one-hot encoding for language and genres (multi-label), interaction features (popularity × vote_count), date features (year, month, days_since_aired), scaling with StandardScaler.
- predict_proba vs predict: predict gives hard True/False. predict_proba gives probability scores. ROC curve needs probabilities, not hard decisions - you need to vary the threshold to draw the curve.
- Feature selection matters more than the algorithm: same weak features, Linear Regression R² = 0.087, Random Forest AUC = 0.73. Better problem framing beats a better model.

---

## What I Built

| File | Description |
|------|-------------|
| `src/fetch_tmdb.py` | TMDB popular shows fetcher - incremental saves, deduplication by ID across runs. 940 unique shows collected. |
| `exercises/exercise1_data_splitting.py` | Load TMDB data, define X and y, train/test split 80/20, verify shapes |
| `exercises/exercise2_regression.py` | Linear regression on vote_average, MSE/RMSE/R² evaluation, cross-validation, coefficient analysis |
| `exercises/exercise3_classification.py` | Random Forest on is_high_quality, confusion matrix, classification report, ROC curve AUC=0.73 |
| `exercises/exercise4_feature_engineering.py` | One-hot encoding, genre mapping + multi-label encoding, interaction features, date features, StandardScaler |

---

## Why These Features - And Why They Performed Poorly (Intentionally)

Features used: `popularity`, `vote_count`, `first_air_date`. Model scored R² = 0.087 on vote_average.

This was deliberate. Before building with good features, it's worth seeing what a model with weak features actually looks like. The results made the point:

- `popularity` had a negative coefficient. More popular shows rated slightly lower. Statistically real, practically counterintuitive. Mainstream popularity and critical quality pull in different directions.
- `vote_count` had a small positive effect. More votes means a more established signal, not necessarily a better show.
- `first_air_date` contributed almost nothing. A show from 1985 and one from 2024 can both score 8.5. Air date tells you when something was made, not how good it is.

R² = 0.087 means the model is barely better than just predicting the average for every show. That's the baseline to beat before anything is worth deploying.

What would actually predict vote_average? Genre, cast, production budget, critic reviews, word-of-mouth sentiment and none of which exist in this dataset. The lesson: "know your features before you train anything."

---

## Key Concepts

**The three-split rule:**
```
Train (64%)      - model learns from this
Validation (16%) - you tune against this
Test (20%)       - touched once, at the very end
```

**Cross-validation - 5-fold:**
```python
cv_scores = cross_val_score(model, X, y, cv=5, scoring='r2')
print(cv_scores.mean())  # honest average across 5 splits
```
Single split R²: 0.1092. Cross-validated R²: 0.0866. The single split got lucky. Cross-validation doesn't.

**Reading model coefficients:**
```python
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef:.6f}")
```
Always check coefficients. A negative where you expect positive is a signal something is off - either the features or the assumptions.

**predict vs predict_proba:**
```python
predictions = model.predict(X_test)          # True / False
y_proba = model.predict_proba(X_test)[:, 1]  # probability of True
```
ROC curve needs probabilities. `[:, 1]` gets the positive class probability.

**Multi-label genre encoding:**
```python
# Map IDs to names
df['genre_names'] = df['genre_ids'].apply(lambda x: [GENRE_MAP.get(id) for id in x])
# Explode lists into rows
genre_exploded = df['genre_names'].explode()
# One-hot encode
genre_encoded = pd.get_dummies(genre_exploded, prefix='genre')
# Group back - one row per show
genre_final = genre_encoded.groupby(level=0).max()
```

---

## Results

```
Linear Regression on vote_average
MSE:  1.8584
RMSE: 1.3632
R²:   0.1092  (single split)
R²:   0.0866  (5-fold cross-validation mean)

Random Forest on is_high_quality (threshold: vote_average >= 7.6)
Accuracy:  0.71
Precision: 0.82 (True class)
Recall:    0.63 (True class)
F1:        0.71
AUC:       0.73
```

---

## Run It

```bash
# Fetch TMDB data (run multiple times to accumulate shows)
python src/fetch_tmdb.py

# Exercises
python exercises/exercise1_data_splitting.py
python exercises/exercise2_regression.py
python exercises/exercise3_classification.py
python exercises/exercise4_feature_engineering.py
```

---

## Next

Week 9: Closes all uncovered gaps - polynomial regression, regularization, logistic regression, decision trees, target encoding, frequency encoding, normalization strategies, TF-IDF, feature leakage in code, feature selection, Applied ML Decision Framework. Then the mini-project: Reusable Feature Engineering Toolkit.