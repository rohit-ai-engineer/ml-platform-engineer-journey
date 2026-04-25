# 📓 Devlog - AI Engineer Journey

> An honest, weekly log of my learning. The wins, the confusion, the breakthroughs.  
> Updated every Saturday.

---

## How I Use This Log

Every Saturday I answer these 5 questions:
1. What did I actually learn this week (not just watch)?
2. What was the hardest thing?
3. What am I most proud of building?
4. How many hours did I put in?
5. What's my plan for next week?

---

### Week 8 - Entry 8 | March 30 - APril 5, 2026

**Theme:** ML Fundamentals & Feature Engineering
**Hours logged:** ~11-12 hours

**What I actually learned:**

ML Concepts:
- Overfitting vs underfitting: memorising training data vs learning actual patterns. Getting the balance right is the core challenge.
- Train/validation/test splits: two splits aren't enough. Every time we need to adjust based on test results, that set stops being honest. Three splits always, test set touched once at the very end.
- Cross-validation: a single 80/20 split can get lucky and K-fold runs 5 splits and averages. The single split gave R² = 0.1092 whereas Cross-validation gave 0.0866. The single split got lucky this time.
- Bias-variance tradeoff: simpler models underfit, complex models overfit, can't minimise both at the same time.
- Linear regression end to end: trained, evaluated the dataset with MSE/RMSE/R², cross-validated and read the coefficients.
- Random Forest classification: built 'is_high_quality' target from median vote_average, trained and evaluated it with confusion matrix, classification report, ROC curve and lastly AUC came 0.73.
- Feature engineering: one-hot encoding for language and genres, interaction features (popularity x vote_count), date features (year, month, days_since_aired), scaling with StandardScaler.
- predict_proba vs predict: hard predictions vs probability scores. ROC curve needs probabilities and not True/False.

The thing that stuck most: R² = 0.087 wasn't a surprise. Before building the model I said "ratings depend on content quality, cast, direction - none of which I have." The model confirmed exactly that. Knowing your features before training is more valuable than any algorithm.

**The hardest thing this week:**

Faced two major things this week. First, the TMDB detail endpoint kept dropping with Windows SSL ConnectionResetError(10054). I had spent a couple of hours debugging, tries retries, sessions, different sleep timers - nothing worked. Moved on with the popular endpoint data. The fetcher works, just without runtime and seasons for now.

Second, 'predict_proba'. I had to ask for proper coverage before I could write it - the syntax wasn't obvious from the concept alone. That led to a bigger conversation about how theory without syntax coverage is half a lesson.

**What I built:**
- `src/fetch_tmdb.py` - TMDB popular shows fetcher with incremental saves and deduplication across runs. 940 unique shows.
- `exercises/exercise1_data_splitting.py` - data loading, X/y definition, 80/20 split
- `exercises/exercise2_regression.py` - linear regression, MSE/RMSE/R², cross-validation, coefficient analysis
- `exercises/exercise3_classification.py` - Random Forest, confusion matrix, classification report, ROC curve plot
- `exercises/exercise4_feature_engineering.py` - full feature engineering pipeline: language encoding, genre mapping + one-hot, interaction features, date features, scaling

**Moment I'm most proud of:**

Noticed mid-week that half the roadmap topics hadn't been covered. I was building the exercises while skipping many important concepts like polynomial regression, regularization, logistic regression, decision trees, target encoding, feature leakage, and the entire Applied ML Decision Framework. None of that would have come up without checking the roadmap against what I'd actually done. It's now a rule: after every section, check what's covered and what isn't before moving on.

**Honest self-assessment:**
> ML concepts: 7/10 - solid foundation, gaps in polynomial regression and regularization (will cover next week)
> Linear regression: 7/10 - built it, evaluated it, read the coefficients but need more reps.
> Classification: 7/10 - Random Forest working, ROC curve plotted with matplotlib, confusion matrix readable.
> Feature engineering: 7/10 - covered the main techniques, target encoding and text features still ahead.
> Syntax building: improving. Still need theory + syntax before writing, but getting faster once I have both.

**Aha moments:**

The negative popularity coefficient. The model said more popular shows rate slightly lower. Counterintuitive at first but then it clicked - mainstream popularity and critical quality are different things. Viral shows and critically acclaimed shows are not the same audience. The model found a real statistical pattern, whether it's a useful one is a different question and that's a domain judgment the model can't make.

Also, the roadmap review moment. I knew something felt thin, upon checking the roadmap showed exactly what was missing.

**Plan for next week:**

Week 9 closes every gap before the mini-project:
- Polynomial regression
- Regularization L1, L2
- Logistic regression + decision trees (built, not just theory)
- Target encoding
- Text features TF-IDF, n-grams
- Feature leakage prevention in code
- Feature selection techniques
- Applied ML Decision Framework - full coverage

Mini-project: Reusable Feature Engineering Toolkit comes after all of that. Not before.

**Week 8 complete? Y** but with known gaps. Week 9 closes them.

---

### Weeks 9 | April 06 - April 25 2026

**Theme:** ML Fundamentals continued + Feature Engineering Toolkit  
**Hours logged:** ~34-36 hours

**What I actually learned:**

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

**The hardest thing this week:**

Variable naming across exercises. Reusing `X, X_train, X_test` in different setups caused silent bugs that took longer to trace than they should have. Also the alpha tuning for regularization — `alpha=1.0` on Lasso eliminated every feature, looked completely broken until I realized the penalty was just too aggressive.

Writing the class from scratch without copy-pasting from previous exercises. The logic was clear. The syntax kept lagging behind. Every method meant going back to basics — what does this take, what does it store, what does it return. Slow going at first. By `detect_leakage` it was starting to feel less like translating and more like writing.
 
The pytest import error also ate more time than it deserved. `ModuleNotFoundError: No module named 'src'` — tried `__init__.py`, wrong directory, wrong flags, accidentally ran the terminal command inside the Python file at one point. `conftest.py` with `sys.path.insert` in the right place fixed it. Classic.


**What I built:**

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

**Moment I'm most proud of:**

Catching the data leakage in Exercise 8 without being told — AUC of 1.0 triggered the instinct immediately. Traced it back to vote_average being used to create is_high_quality and then accidentally included as a feature. That reflex is now permanent.

The unknown provider test. Didn't just build the happy path — built the fallback and tested it explicitly. Tutorial code handles the known case. Production code handles the one you didn't plan for.
 
Close second: catching that copy-paste was slowing down syntax recall and stopping it mid-session. Uncomfortable in the short run. The only fix that actually works.

**Honest self-assessment:**

- Feature engineering: 8/10 — covered all major techniques with real numbers to back them up. The R² comparisons tell an honest story about what actually matters.
- Model variety: 8/10 — five model types built and compared across Weeks 8-9.
- Production thinking: 9/10 — leakage detector, alpha tuning, domain reasoning on encoding choice. The ops background keeps paying off.
- Still to go: feature selection, Applied ML Decision Framework, mini-project.
- Feature selection: 8/10. Understood all three methods, built the exercise, interpreted the results correctly. The part I want to get sharper on is knowing upfront which method to reach for rather than running all three.
- Applied ML Decision Framework: 7/10. The concepts landed. Applying it consistently to every problem before jumping to code,that's the habit still forming.
- Syntax recall: 6/10. Logic is there. Syntax still needs the training wheels off. Stopped copy-pasting this week. That's the only fix and it's uncomfortable. Good sign.
- Toolkit / class design: 8/10. Fit/transform pattern correct, unknown handling tested, pytest suite clean. First time building a proper Python package structure from scratch. Didn't feel like guessing by the end.


**Plan for next week:**

Week 10–11: Ensemble methods — Random Forest deep dive, XGBoost. Clustering — K-Means, DBSCAN, elbow method. Hyperparameter tuning — GridSearch, RandomSearch. Design Exercise 1 — Metadata Ingestion Architecture.
 
Also: repo refactor. Proper directory structure before Week 10 work starts.

**Weeks 9-10 complete? (Y/N):** Y

PR merged and closed

---

### Weeks 10-11 - Entry 10 | [DATE]

**Theme:** Advanced ML, Ensemble Methods & Design Exercise 1  
**Hours logged:** ___ hours

**Design Exercise 1 - Metadata Ingestion Architecture:**
> [Describe your architecture diagram. What trade-offs did you make? What feedback did you get?]

**Weeks 10-11 complete? (Y/N):**

---

### Weeks 12-14 - Entry 11 | [DATE]

**Theme:** PROJECT 1 - Metadata Conflict Resolver  
**Hours logged:** ___ hours

**Project status:**
> [Where are you with the build? What's working, what broke, what surprised you?]

**MLflow experiment results:**
> [Which model won - Logistic Regression, Random Forest, or XGBoost? Why?]

**HITL dashboard:**
> [How did the human-in-the-loop approval flow work?]

**Phase 2 complete reflection:**
> [Look back at Week 7 you. What changed?]

**Phase 2 complete? (Y/N):**  
**Ready for Phase 3? (Y/N):**

---

## 🗓️ Phase 3 · Time-Series + Project 2 (Weeks 15-19)

---

### Weeks 15-16 - Entry 12 | [DATE]

**Theme:** Time-Series Analysis & System Design 2  
**Hours logged:** ___ hours

**Weeks 15-16 complete? (Y/N):**

---

### Weeks 17-19 - Entry 13 | [DATE]

**Theme:** PROJECT 2 - Content Velocity Predictor  
**Hours logged:** ___ hours

**Phase 3 complete? (Y/N):**

---

## 🗓️ Phase 4 · Deep Learning Foundations (Weeks 20-21)

---

### Weeks 20-21 - Entry 14 | [DATE]

**Theme:** PyTorch, Neural Networks, LLMs & Embeddings  
**Hours logged:** ___ hours

**Phase 4 complete? (Y/N):**

---

## 🗓️ Phase 5 · MLOps + Project 3 (Weeks 22-28)

---

### Weeks 22-24 - Entry 15 | [DATE]

**Theme:** Docker, Kubernetes, Kafka, FastAPI  
**Hours logged:** ___ hours

**Weeks 22-24 complete? (Y/N):**

---

### Weeks 25-28 - Entry 16 | [DATE]

**Theme:** PROJECT 3 - Live Event Anomaly Guardian  
**Hours logged:** ___ hours

**Project status:**

**Phase 5 complete reflection:**
> [This is your most important devlog entry. Look back at Week 1 you. What changed? Write freely - minimum 100 words.]

**Phase 5 complete? (Y/N):**  
**Ready to apply? (Y/N):**

---

## 📊 Phase 1 Stats Summary

| Metric | Value |
|--------|-------|
| Total weeks | 7 |
| Total hours logged | ~37 |
| Projects built | 17 |
| GitHub commits | ~75 |
| Toughest concept | Cosine similarity (Week 5) / Decorators (Week 7) |
| Most fun project | find_similar_shows() mini-project (Week 5) |

---