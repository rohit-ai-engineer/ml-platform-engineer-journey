# ML Platform Engineer Journey - Rohit Jadiya

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Status](https://img.shields.io/badge/Status-Active-green)
![Phase](https://img.shields.io/badge/Phase-1%20Foundations%20Complete-purple)
![Phase](https://img.shields.io/badge/Phase_2-Week_9_Complete-turquoise)

**Never coded before. Building in public until I land an ML Platform Engineer role at a top streaming platform.**

---

## 👤 About Me

**Name:** Rohit Jadiya  
**Current Role:** Manager – Ingest Operations @ Simply.TV  
**Background:** 8+ years in OTT/streaming metadata operations (Nielsen, Simply.TV)  
**Target Role:** ML Platform Engineer at tier-1 streaming platforms and tech companies  
**Timeline:** 14-16 months with extensive practice (started March 2026)  

**Why ML Platform Engineering?** I've spent 8 years manually solving problems that AI should automate. I'm building the tools I wish I had at Simply.TV - then using them to get hired by the companies that need them most.

---

## 🎯 Mission

Build 3 production-grade ML systems that solve real streaming/OTT problems:

1. **The Metadata Conflict Resolver** - Multi-source truth reconciliation using ML
2. **The Content Velocity Predictor** - Forecast content popularity trajectories  
3. **The Live Event Anomaly Guardian** - Real-time anomaly detection for live events

**End Goal:** Portfolio that proves I can ship ML systems, not just train models.

---

## 📍 Current Status

**Phase 1 - Foundations (7 weeks)** `[Week 6 of 7 - IN PROGRESS]`
```
Phase 1: Foundations           ████████████████████  Week 7 ✅ COMPLETE
Phase 2: Classical ML + P1     ████████░░░░░░░░░░░░  Week 9 ✅
Phase 3: Time-Series + P2      ░░░░░░░░░░░░░░░░░░░░  Locked
Phase 4: Deep Learning         ░░░░░░░░░░░░░░░░░░░░  Locked
Phase 5: MLOps + P3            ░░░░░░░░░░░░░░░░░░░░  Locked
```

---

## 🗺️ The Roadmap

### Phase 1: Foundations (Weeks 1-7)
**Goal:** Python, data manipulation, APIs, and production engineering basics

**Week 1:** Python basics + OTT-focused projects ✅  
**Week 2:** OOP, file I/O, JSON persistence ✅  
**Week 3:** APIs, data pipelines, real-time data fetching ✅  
**Week 4:** Pandas, data analysis, feature engineering ✅  
**Week 5:** NumPy, linear algebra, stats fundamentals ✅  
**Week 6:** SQL, Testing & Version Control ✅  
**Week 7:** Advanced Python + System Design Thinking (basics) ✅  

---

### Phase 2: Classical ML + Project 1 (Weeks 8-14)
**Goal:** Build the Metadata Conflict Resolver  

**Week 8:** ML Fundamentals + Feature Engineering ✅  
**Week 9:** Feature selection, Applied ML Decision Framework, Feature Engineering Toolkit ✅  
**Weeks 10-11:** Advanced ML + Design Exercise 1  
**Weeks 12-14:** PROJECT 1 - Metadata Conflict Resolver  

**Skills:**
- scikit-learn (Random Forest, XGBoost)
- Multi-class classification
- Confidence scoring
- Model evaluation (precision, recall, F1)
- MLflow experiment tracking
- pytest (production-quality test suites)

**Capstone: PROJECT 1 - The Metadata Conflict Resolver**
- Ingest EPG data from multiple providers
- ML model assigns confidence scores to each source
- Auto-resolves conflicts using weighted voting
- **GenAI Addition:** LLM embeddings for semantic title matching
- HITL approval dashboard - flags low-confidence predictions (<0.7) for human review
- MLflow experiment tracking (Logistic Regression vs Random Forest vs XGBoost)
- Tech: Python, Pandas, scikit-learn, PostgreSQL, OpenAI API, MLflow, pytest

---

### Phase 3: Time-Series ML + Project 2 (Weeks 15-19)
**Goal:** Build the Content Velocity Predictor

**Skills:**
- Time-series forecasting (ARIMA, Prophet, LSTM)
- Feature engineering from metadata
- Social media sentiment analysis
- Web scraping for trend data

**Capstone: PROJECT 2 - The Content Velocity Predictor**
- Predict content popularity trajectories (fast burn vs slow build)
- Uses metadata + social sentiment + historical patterns
- **Cold Start Engine:** Hybrid approach for new content with zero history - uses OpenAI embeddings to find similar shows, averages their performance with wide confidence intervals
- **GenAI Addition:** LLM analyzes social media sentiment for buzz detection
- Helps platforms make multi-million dollar licensing decisions
- Tech: Python, scikit-learn, BeautifulSoup, TMDB API, Plotly, OpenAI API, MLflow

---

### Phase 4: Deep Learning Foundations (Weeks 20-21)
**Goal:** PyTorch, neural networks, embeddings

**Skills:**
- PyTorch basics
- Neural network architectures
- Transfer learning
- LLMs & embeddings (Hugging Face)
- Vector databases (Pinecone)
- RAG architecture
- Prompt engineering

*(Applied in Projects 1 & 2, minimal use in Project 3)*

---

### Phase 5: MLOps + Project 3 (Weeks 22-29)
**Goal:** Build the Live Event Anomaly Guardian

> **I don't build models. I build platforms for other engineers to build models on.**

**Skills:**
- Docker containerization
- Kubernetes (hands-on - pods, deployments, services, Minikube deployment)
- Kafka (real-time streaming)
- Model deployment (FastAPI + auth + rate limiting)
- Airflow orchestration (DAGs, scheduling, pipeline automation)
- Monitoring (Prometheus, Grafana)
- Model drift detection (EvidentlyAI)
- Alerting & incident response
- CI/CD for ML models (GitHub Actions)
- Terraform (IaC basics - deploy AWS resources)
- AWS SageMaker (train + deploy ML endpoints)
- IAM (roles, policies, least privilege)

**Capstone: PROJECT 3 - The Live Event Anomaly Guardian**
- Real-time monitoring of live event metadata feeds
- Anomaly detection using Isolation Forest (classical ML - speed matters)
- Schema drift detection with EvidentlyAI - catches provider format changes before they break pipelines
- **GenAI Addition (minimal):** LLM generates human-readable incident summaries
- Auto-failover + alerting with 5-min SLA
- Zero outages goal
- Tech: Python, Kafka, Docker, Kubernetes, Prometheus, Grafana, PagerDuty, EvidentlyAI, GitHub Actions, Terraform

---

## 🤖 My Approach to GenAI

**Philosophy:** Use GenAI where it adds UNIQUE value. Skip it where classical ML is better.

**I use GenAI for:**
- ✅ Unstructured text analysis (sentiment, semantic matching)
- ✅ Content generation (descriptions, tags)
- ✅ Fuzzy matching (multilingual, typos)

**I DON'T use GenAI for:**
- ❌ Real-time systems (too slow)
- ❌ High-stakes decisions (hallucination risk)
- ❌ When classical ML is faster/cheaper

**Why this matters:** Most bootcamp grads use LLMs for everything. I use the right tool for the job. That's what production engineers do.

---

## 🛠️ Tech Stack (By End of Journey)

**Languages:** Python (advanced), SQL (MySQL, PostgreSQL)

**ML/AI:**
- scikit-learn (classical ML)
- PyTorch (deep learning)
- Hugging Face (LLMs, embeddings)
- OpenAI/Anthropic APIs (strategic GenAI use)

**Data Engineering:**
- Pandas, NumPy
- Kafka (streaming)
- PostgreSQL (relational)
- Pinecone (vector DB)

**MLOps & Production:**
- Docker
- Kubernetes (hands-on)
- FastAPI (+ auth + rate limiting)
- Airflow (pipeline orchestration)
- Prometheus, Grafana
- EvidentlyAI (drift detection)
- Terraform (IaC basics)
- AWS SageMaker
- IAM
- CI/CD (GitHub Actions)
- Git

**Data Sources:**
- XML/JSON parsing
- REST APIs
- Web scraping (BeautifulSoup)

---

## 📁 Projects Built So Far

| Project | Week | Stack | Status | Description |
|---------|------|-------|--------|-------------|
| Calculator | W1 | Python | ✅ Done | Basic arithmetic operations |
| EPG Time Calculator | W1 | Python, datetime | ✅ Done | Calculate show end times from EPG data |
| CSV Metadata Validator | W1 | Python, CSV | ✅ Done | Quality checks on metadata records |
| XML EPG Validator | W1 | Python, XML | ✅ Done | Validates real Virgin Media EPG feeds |
| Streaming Catalog Manager | W2 | Python, OOP, JSON | ✅ Done | Full-featured catalog with persistence |
| Movie Collector | W3 | Python, APIs, JSON | ✅ Done | OMDB API integration with search, filter, export |
| EPG Data Pipeline | W3 | Python, APIs, JSON | ✅ Done | Production pipeline: fetch → extract → validate → save |
| Network Analysis Dashboard | W4 | Python, Pandas | ✅ Done | Grouped EPG data by network with runtime stats |
| Primetime Analyzer | W4 | Python, Pandas | ✅ Done | Filtered 8pm-10pm shows, created boolean columns |
| Data Quality Report Tool | W4 | Python, Pandas, File I/O | ✅ Done | Automated validation with dual output (screen + file) |
| Morning Shows Analyzer | W4 | Python, Pandas | ✅ Done | Self-written analysis of 6am-12pm programming |
| EPG Analytics Dashboard | W4 | Python, Pandas, JSON, File I/O | ✅ Done | 5-question business analysis dashboard with file output |
| NumPy Runtime Analysis | W5 | Python, NumPy | ✅ Done | Array operations, vectorization, stats on runtime data |
| Vectorized EPG Calculator | W5 | Python, NumPy | ✅ Done | End times, gap detection, scheduling holes - no loops |
| EPG Stats Dashboard | W5 | Python, NumPy, Pandas | ✅ Done | Runtime stats, airtime distribution, genre variance, correlation |
| Cosine Similarity Engine | W5 | Python, NumPy | ✅ Done | Show similarity using dot product and vector normalization |
| Content Similarity Engine | W5 | Python, NumPy, Pandas | ✅ Done | find_similar_shows() on real EPG data - mini-project capstone |
| TMDB Fetcher | W8 | Python, requests | ✅ Done | Popular shows API fetcher with incremental saves and dedup. 940 shows. |
| Data Splitting | W8 | Python, scikit-learn | ✅ Done | X/y definition, 80/20 train/test split |
| Linear Regression | W8 | scikit-learn, NumPy | ✅ Done | Regression on vote_average, MSE/RMSE/R², cross-validation |
| Classification | W8 | scikit-learn, matplotlib | ✅ Done | Random Forest, confusion matrix, ROC curve AUC=0.73 |
| Feature Engineering | W8 | Pandas, scikit-learn | ✅ Done | One-hot, genre mapping, interaction features, date features, scaling |
| Polynomial Regression | W9 | scikit-learn | ✅ Done | Linear vs polynomial degree=2, R² 0.089 → 0.124 |
| Regularization | W9 | scikit-learn | ✅ Done | Lasso vs Ridge vs Linear, Lasso R² 0.169 wins |
| Logistic Regression | W9 | scikit-learn | ✅ Done | Classification on is_high_quality, AUC 0.81 |
| Decision Tree | W9 | scikit-learn | ✅ Done | plot_tree visualization, AUC 0.79 |
| Target Encoding | W9 | Pandas, scikit-learn | ✅ Done | CV R² 0.208 - best result of the week |
| Frequency Encoding | W9 | Pandas | ✅ Done | CV R² 0.096 vs target encoding 0.208 |
| Normalization | W9 | scikit-learn | ✅ Done | StandardScaler, MinMaxScaler, RobustScaler compared |
| TF-IDF | W9 | scikit-learn | ✅ Done | Text features on TMDB overviews, R² 0.083 |
| Leakage Detection | W9 | Pandas | ✅ Done | check_leakage() - catches vote_average at 1.0 |
| Feature Selection | W9 | scikit-learn | ✅ Done | SelectKBest, RFE, SelectFromModel - noise dropped by all three |
| Feature Engineering Toolkit | W9 | Python, scikit-learn, pytest | ✅ Done | FeatureEngine class, fit/transform pattern, 5/5 tests passing |


---

## 📊 Learning Log

**Week 9 Reflection**

Week 9 was closing gaps. Everything skipped in Week 8 got proper coverage - polynomial regression, regularization, logistic regression, decision trees, four encoding strategies, normalization, TF-IDF, and a feature leakage detector built from scratch.

The result that surprised me most: target encoding on a single genre column doubled R² from 0.089 to 0.208. No model change, no tuning. Just the right signal. That's the kind of thing you can only learn by running the experiment.

Logistic Regression beat Random Forest on the same dataset - AUC 0.81 vs 0.73. Simpler model, simpler data. Complexity needs a reason.

The leakage detector was the moment that felt most production-ready. AUC of 1.0 on the Decision Tree triggered the instinct immediately and traced it back to vote_average leaking into features inside a minute. That reflex is now permanent.

Feature selection landed differently than expected. The question isn't which features feel relevant but gut feel breaks down past 20 columns. Built a synthetic EPG conflict dataset, defined is_conflict using actual ops logic, ran all three methods. Filter and Embedded both found the exact two features used to define the target. Wrapper drifted slightly. Noise columns dropped by all three. 
The takeaway: when Filter and Embedded agree, trust them over Wrapper.

The Applied ML Decision Framework had no code. Just six questions to ask before writing any. The one that stuck - acceptable error rate is a business question, not a technical one. A recommendation model wrong 20% of the time is fine. A metadata conflict detector wrong 5% of the time means 5% of the schedule is broken on air. Different answer, same math.

The Toolkit was the hardest part of the week. Not the logic - the discipline. No copy-pasting from previous exercises. Every method written from memory. Slow at first. The fit/transform pattern started feeling natural around detect_leakage. First proper Python package built from scratch - src/, tests/, data/, results/. Five pytest tests, five passing. Unknown provider handled without a crash. That last part mattered more than the passing tests.


**Week 8 Reflection**
First real ML week done. 

Built linear regression, Random Forest classification and a full feature engineering pipeline on 940 TMDB shows.
 
The R² of 0.087 on vote_average didn't surprise me, I'd already figured out it would be low. Ratings come from content quality, cast, direction and none of that's in the dataset. The model just confirmed what I already suspected, which is actually the point - "Know your features before you train."
 
Switching to classification: "is_high_quality" or not and the same weak features suddenly gave AUC = 0.73. Same data but better problem framing which resulted in much more usable output. 
That gap between 0.087 and 0.73 is almost entirely about how you set up the question.
 
The unexpected part came at the end of the week when I checked the roadmap and realized how much got skipped. Polynomial regression, regularization, logistic regression, decision trees, target encoding, feature leakage, the whole Applied ML Decision Framework all skipped but nevertheless in Week 9 I am going to be catching up on all of that before the mini-project.

I'm not sure if that's a curriculum problem or just how learning actually goes. well either way the habit of checking is now part of the process.

**Week 7 Reflection** Pure theory week. No projects, but probably the most dense session of Phase 1.

Advanced Python covered encapsulation, serialization, context managers, decorators, generators, type hints, and advanced error handling. Half of these turned out to be things I'd been using since Week 3 without knowing the names like serialization with json.dump, context managers with `with open()`. The other half was genuinely new, decorators especially.

System Design Thinking was the surprise. Architecture diagrams, trade-off thinking, latency vs throughput, single points of failure, ETL patterns - I kept recognising things I do at work. Different vocabulary, same decisions. 
Eight years of operations work turns out to map directly onto system design principles.

One lesson going into Phase 2: theory gets equal weight. Not after the code. Before it.

Phase 2 starts now. Metadata Conflict Resolver. The problem I've been solving manually for 8 years, now in code.

**Week 6 Reflection:** Spent yesterday going through SQL basics again. WHERE vs HAVING, PRIMARY/FOREIGN keys, JOINs, execution order, window functions. Got SQLite running with actual EPG data and wrote my first query that doesn't look like noob writing. 
Today: LAG/RANK exercises, figuring out schedule overlap detection, then pytest + Git - which is apparently the whole point of Week 6.

**Week 5 Reflection:** Toughest week conceptually - NumPy, linear algebra, statistics, and cosine similarity all in one week. The dot product clicked when I realised every ML prediction is `np.dot(features, weights)`. Built 4 exercises and a mini-project similarity engine on real EPG data. Breakthrough: understood WHY vectorization is faster, not just that it is.

**Week 4 Reflection:** Learned Pandas through 4 different analysis tools. 
The moment it clicked: Exercise 4, I wrote the whole thing myself,No looking at examples, just worked through the logic. I'm finally starting to see the patterns instead of just copying what works. Also managed to fix 3 bugs in the dashboard on my own, which felt good.


**Week 3 Reflection:** I built a pipeline this week that pulls live TV schedule data and actually cleans it up properly. Takes the messy nested JSON, pulls out what matters, checks if it's any good, then dumps everything to files with timestamps. Ran it on 115 shows without a single failure, which honestly surprised me.


**Week 2 Reflection:** Built first OOP system (Catalog Manager). Struggled with understanding where code belongs but got it eventually. Realized I'm doing OOP without solid fundamentals - needed more basics practice.

**Week 1 Reflection:** I started with nothing and built 4 tools so far. One of them is an actual EPG validator that can process Virgin Media's XML feeds, which was harder than it sounds. The weirdest part? I caught a bug in the instructor's code because I actually understood the domain well enough to spot it.


---

## 🔗 Connect

- **GitHub:** [rohit-ai-engineer](https://github.com/rohit-ai-engineer/ml-platform-engineer-journey)
- **LinkedIn:** [Rohit Jadiya](https://www.linkedin.com/in/rohit-jadiya-47a42443)

---

## 📝 Philosophy

**Deep understanding > speed.** I'm 35 with bills to pay - no time for shallow learning. Every project must be production-ready and portfolio-worthy.

**Right tool for the job.** I use classical ML where it's best (speed, reliability, cost) and GenAI where it adds unique value (semantic understanding, text analysis). Production systems need both.

---

_Last updated: April 25, 2026_
