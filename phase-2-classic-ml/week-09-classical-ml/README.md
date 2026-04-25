# Week 9 — ML Fundamentals Continued & Feature Engineering

Phase 2: Classical ML + Project 1 · ML Platform Engineer Journey
 
---
 
## What I Learned

Polynomial regression - Linear draws a straight line, polynomial bends it. The curve comes from the features and not the algorithm. PolynomialFeatures generates x², x³ columns and feeds them to the same LinearRegression. degree=2 R² = 0.124 vs linear 0.089. Small improvement on the same weak features.

Regularization - Penalizes the model for overcomplicating things. Lasso (L1) zeros out useless coefficients entirely. Ridge (L2) shrinks them but never all the way. Lasso won at `R² = 0.169` vs Ridge and Linear both at `~0.150`. The interesting part was though alpha=1.0 killed everything. Lasso with `alpha=1.0` zeroed out every single feature - looked broken until dropping to 0.01. Ridge barely moved from plain linear regardless of alpha, which actually tells you something - the features aren't overfitting, they're just weak. Same stable signals across all three models: vote_count, lang_cn, Animation, Drama.

Logistic Regression - Classification model despite the name. Same linear math as LinearRegression, but the output gets squashed through a sigmoid into a probability between 0 and 1. `AUC = 0.81` vs `Random Forest's 0.73`. Simpler model won on simple data. Precision improved 0.82 → 0.89, Recall dropped slightly 0.63 → 0.60. The ops insight that came out of this one: in conflict detection, optimize for Recall. False Negatives reach the client and False Positives just waste review time.

Decision Tree - Single tree of yes/no questions the model learns from data. Fully explainable - you can literally draw why it made any decision. `AUC = 0.79`, sitting between Random Forest (0.73) and Logistic Regression (0.81). Root split landed on `vote_count <= 663.5`. plot_tree made the internal logic visible for the first time, which was genuinely interesting to see.

Target Encoding - Replaces each category with the average target value for that category. `CV R² = 0.208` vs `baseline 0.089` - more than doubled with one column and the genre coefficient was 1.55, dwarfing popularity and vote_count. The model basically said genre is the strongest predictor of rating. Hard to argue with that from a domain perspective.

Frequency Encoding - Replaces each category with how often it appears in the dataset. CV `R² = 0.096` - barely above baseline. Target encoding won by a mile. Frequency tells the model how popular a genre is in the data, not what rating it gets. Wrong signal for this problem.

Normalization strategies - `StandardScaler (mean=0, std=1)`,` MinMaxScaler (0-1 range)`, `RobustScaler (uses median and IQR, ignores outliers)`. All three gave identical R² = 0.0935 on LinearRegression. Scaling doesn't move R² for plain linear regression - it changes coefficient values, not predictive power. Matters for Lasso/Ridge, KNN, SVM, neural networks. RobustScaler is the safe default when data is messy.

TF-IDF - Words common across all documents get penalized, rare words that appear often in one specific document get boosted. R² = 0.083 on TMDB overviews - worse than target encoding, barely above baseline. Short descriptions plus words that don't actually predict ratings = weak signal. TF-IDF works when words carry real signal. For conflict detection in EPG metadata it would be useful but for predicting ratings 
from one-sentence summaries, it isn't.

Feature leakage in code - `Built check_leakage()` - loops through feature columns, calculates absolute correlation with target, flags anything above 0.95. Tested it:vote_average as a feature returned [('vote_average', 1.0)]. Clean features returned []. In a real pipeline this runs as a gate before training - stops cold if anything looks suspicious.

Feature selection - After spending weeks building and transforming features, this week was about cutting them down. The question isn't which features feel relevant but gut feel breaks down fast when you have 20+ columns. You need a systematic method.
 
Three approaches - 
Filter methods score each feature using statistics before the model gets involved - fast, works fine, blind to how features interact. 
Wrapper methods train the model repeatedly with different subsets and see what performs best - accurate but slow, and can overfit to training data. 
Embedded methods let the model figure it out during training and report back - `SelectFromModel` with a Random Forest. No separate step needed.
 
Built a synthetic EPG conflict dataset to test all three. 500 rows, five real signal features, three pure noise columns. Defined `is_conflict` using actual ops logic: low title similarity AND high duration difference between two providers. Filter and Embedded both picked exactly those two features. Wrapper went slightly off and grabbed `provider_frequency` instead of `duration_diff_minutes`. The noise columns got dropped by all three. Satisfying to watch.
 
The lesson that stuck: `title_similarity_score` was unanimous across all three methods because its threshold sits right in the middle of its 0–1 range. Cleanest signal possible. The model couldn't miss it.
 
Applied ML Decision Framework - No coding, just six questions to ask before writing any ML code. 
1. Can rules solve this? 
2. Do you have enough quality data? 
3. What's the acceptable error rate? 
4. How will failures be detected? 
5. What does ML cost vs the alternative? 
6. Classical ML or GenAI?
 
I'd already applied this without knowing it. When asked if I'd use ML to validate a new provider's file format - one provider, 10 files, known structure - the answer was no. Rules work. Twenty providers with volume climbing and edge cases multiplying - that's when ML starts making sense. The framework just gives that instinct a name.
 
Feature Engineering Toolkit - Built a proper production-structured Python package. `FeatureEngine` class with eight methods. Fit/transform pattern throughout - fits on training data, stores the learned mapping, applies it to any new data later. Unknown category handling in every encoder: target encoding falls back to global mean, frequency encoding falls back to zero.
 
Five pytest tests - All five passing. The unknown provider test was the one worth building - fit on Netflix, HBO, Disney, then transform a Series containing "Unknown_Provider." Got zero back, no crash. A new provider showing up at 2 AM shouldn't take the pipeline down. Now it doesn't.

---

## What I Built

| Exercise | Description | Key Result |
|----------|-------------|------------|
| exercise5_polynomial_regression.py | Linear vs polynomial degree=2 with matplotlib plot | Poly R² 0.124 vs Linear 0.089 |
| exercise6_regularization.py | Lasso vs Ridge vs Linear on full feature set | Lasso 0.169 wins |
| exercise7_logistic_regression.py | Logistic regression on is_high_quality | AUC 0.81 |
| exercise8_decision_tree.py | Decision tree with plot_tree visualization | AUC 0.79 |
| exercise9_target_encoding.py | Target encoding on genre column | R² 0.208 - best this week |
| exercise10_frequency_encoding.py | Frequency encoding comparison | R² 0.096 |
| exercise11_normalization.py | Three scalers compared | All identical R² 0.0935 |
| exercise12_tfidf.py | TF-IDF on TMDB overviews | R² 0.083 |
| exercise13_leakage_detection.py | Feature leakage detector | Catches vote_average at 1.0 |
| exercise14_feature_selection.py | SelectKBest, RFE, SelectFromModel on synthetic EPG data | Filter + Embedded agreed on true signals, noise dropped |
| feature_engineering_toolkit/src/feature_engine.py | FeatureEngine class - 8 methods, fit/transform pattern | Unknown category handling, leakage detection, feature selection |
| feature_engineering_toolkit/tests/test_feature_engine.py | pytest suite | 5/5 passing |

## Results

```
Polynomial Regression (vote_count only)
Linear R²:     0.089
Polynomial R²: 0.124
 
Regularization (full feature set)
Lasso R²:  0.169  ← winner
Ridge R²:  0.150
Linear R²: 0.150
 
Classification (is_high_quality)
Logistic Regression AUC: 0.81  ← best this week
Decision Tree AUC:       0.79
Random Forest AUC:       0.73  ← Week 8 baseline
 
Encoding comparison (genre → vote_average)
Target Encoding CV R²:    0.208  ← best result this week
Frequency Encoding CV R²: 0.096
Baseline (no genre) R²:   0.089
 
TF-IDF (overview text → vote_average)
R²: 0.083

Feature Selection — Synthetic EPG Dataset (500 rows, 8 features)
Filter  (SelectKBest):     duration_diff_minutes, title_similarity_score
Wrapper (RFE):             title_similarity_score, provider_frequency
Embedded (SelectFromModel):duration_diff_minutes, title_similarity_score
 
Noise features dropped by all three:
  show_title_length, random_noise_1, random_noise_2
 
pytest — feature_engineering_toolkit
5 passed in 12.22s
```
 
---

## Key Lessons

Right feature beats right algorithm. Target encoding on one column doubled R². No model change, no tuning — just the right signal.
 
Perfect score means check for leakage first. Decision Tree AUC = 1.0 was the first number that came back. Took about 30 seconds to trace it to vote_average in the feature set. Fixed, retested, got honest results.
 
Simpler model on simple data. Logistic Regression beat Random Forest on the same dataset. Complexity needs a reason.
 
alpha matters more than you'd expect. Lasso at alpha=1.0 zeroed out every feature and looked completely broken. alpha=0.01 gave the best results in the week. The right setting matters as much as the right algorithm.

Filter and Embedded are more reliable than Wrapper on small datasets. Wrapper found a slightly noisier path and missed one of the two real signals. Filter and Embedded didn't.
 
Unknown category handling is not optional. A new provider in production at 2 AM shouldn't crash the pipeline. Global mean fallback for target encoding, zero for frequency encoding — both sensible, both tested.
 
Fit on training data, transform everywhere else. The class stores what it learned during fit. Transform just applies it. That separation is what makes a reusable tool instead of a one-time script.
 
The Decision Framework is just making the implicit explicit. The instinct to not use ML for single-provider file validation was already there. The framework gives it structure you can explain in an interview.
 
---

### Week 9 Complete
 
All topics closed. PR merged.
