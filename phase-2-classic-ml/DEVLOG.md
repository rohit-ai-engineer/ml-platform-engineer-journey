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
**Hours logged:** ~6-7 hours

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

### Weeks 9-10 - Entry 9 | [DATE]

**Theme:** ML Fundamentals continued + Feature Engineering Toolkit  
**Hours logged:** ___ hours

**What I actually learned:**

**The hardest thing this week:**

**What I built:**

**Moment I'm most proud of:**

**Plan for next week:**

**Weeks 9-10 complete? (Y/N):**

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