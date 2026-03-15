# ML Platform Engineer Journey — Rohit Jadiya

**Never coded before. Building in public until I land an ML Platform Engineer role at a top streaming platform.**

---

## 👤 About Me

**Name:** Rohit Jadiya  
**Current Role:** Manager – Ingest Operations @ Simply.TV  
**Background:** 8+ years in OTT/streaming metadata operations (Nielsen, Simply.TV)  
**Target Role:** ML Platform Engineer at tier-1 streaming platforms and tech companies  
**Timeline:** 14-16 months with extensive practice (started March 2026)  

**Why ML Platform Engineering?** I've spent 8 years manually solving problems that AI should automate. I'm building the tools I wish I had at Simply.TV — then using them to get hired by the companies that need them most.

---

## 🎯 Mission

Build 3 production-grade ML systems that solve real streaming/OTT problems:

1. **The Metadata Conflict Resolver** — Multi-source truth reconciliation using ML
2. **The Content Velocity Predictor** — Forecast content popularity trajectories  
3. **The Live Event Anomaly Guardian** — Real-time anomaly detection for live events

**End Goal:** Portfolio that proves I can ship ML systems, not just train models.

---

## 📍 Current Status

**Phase 1 — Foundations (7 weeks)** `[Week 4 of 7 — COMPLETE]`
```
Phase 1: Foundations           ██████████████░░░░░░  Week 4 of 7
Phase 2: Classical ML + P1     ░░░░░░░░░░░░░░░░░░░░  Locked
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
**Week 5:** NumPy, linear algebra, stats fundamentals ⏳  
**Week 6:** SQL, Testing & Version Control  
**Week 7:** Advanced Python + System Design Thinking (basics)  

---

### Phase 2: Classical ML + Project 1 (Weeks 8-14)
**Goal:** Build the Metadata Conflict Resolver

**Skills:**
- scikit-learn (Random Forest, XGBoost)
- Multi-class classification
- Confidence scoring
- Model evaluation (precision, recall, F1)
- MLflow experiment tracking
- pytest (production-quality test suites)

**Capstone: PROJECT 1 — The Metadata Conflict Resolver**
- Ingest EPG data from multiple providers
- ML model assigns confidence scores to each source
- Auto-resolves conflicts using weighted voting
- **GenAI Addition:** LLM embeddings for semantic title matching
- HITL approval dashboard — flags low-confidence predictions (<0.7) for human review
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

**Capstone: PROJECT 2 — The Content Velocity Predictor**
- Predict content popularity trajectories (fast burn vs slow build)
- Uses metadata + social sentiment + historical patterns
- **Cold Start Engine:** Hybrid approach for new content with zero history — uses OpenAI embeddings to find similar shows, averages their performance with wide confidence intervals
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

**Skills:**
- Docker containerization
- Kafka (real-time streaming)
- Model deployment (FastAPI)
- Airflow orchestration (DAGs, scheduling, pipeline automation)
- Monitoring (Prometheus, Grafana)
- Model drift detection (EvidentlyAI)
- Alerting & incident response
- CI/CD for ML models (GitHub Actions)
- Kubernetes fundamentals (conceptual — pods, deployments, services)

**Capstone: PROJECT 3 — The Live Event Anomaly Guardian**
- Real-time monitoring of live event metadata feeds
- Anomaly detection using Isolation Forest (classical ML — speed matters)
- Schema drift detection with EvidentlyAI — catches provider format changes before they break pipelines
- **GenAI Addition (minimal):** LLM generates human-readable incident summaries
- Auto-failover + alerting with 5-min SLA
- Zero outages goal
- Tech: Python, Kafka, Docker, Prometheus, Grafana, PagerDuty, EvidentlyAI, GitHub Actions

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
- FastAPI
- Airflow (pipeline orchestration)
- Prometheus, Grafana
- EvidentlyAI (drift detection)
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

---

## 📊 Learning Log

**Latest:** Week 4 complete! Mastered Pandas through 4 analytical tools. Breakthrough moment: wrote Exercise 4 entirely from my own logic (no step-by-step guidance). Going from "copying syntax" to "thinking in code patterns." Next: NumPy for numerical computing.

**Week 3 Reflection:** Built production-quality EPG data pipeline that fetches live schedule data, extracts clean fields from nested JSON, validates quality, and exports to timestamped files. 115 shows processed with 100% success rate. Foundation for Project 1.

**Week 2 Reflection:** Built my first OOP system (Catalog Manager). Struggled with understanding where code belongs (Content class vs Catalog class) but got it eventually. Realized I'm doing OOP without solid fundamentals — need more practice with basics.

**Week 1 Reflection:** Started from zero. Built 4 tools including a real EPG validator that handles Virgin Media XML feeds. Learned XML parsing, caught a bug in the instructor's code using my domain knowledge. Feels good to apply my Simply.TV experience.

---

## 🔗 Connect

- **GitHub:** [rohit-ai-engineer](https://github.com/rohit-ai-engineer/ml-platform-engineer-journey)
- **LinkedIn:** [Rohit Jadiya](https://www.linkedin.com/in/rohit-jadiya-47a42443)

---

## 📝 Philosophy

**Deep understanding > speed.** I'm 35 with bills to pay — no time for shallow learning. Every project must be production-ready and portfolio-worthy.

**Right tool for the job.** I use classical ML where it's best (speed, reliability, cost) and GenAI where it adds unique value (semantic understanding, text analysis). Production systems need both.

---

_Last updated: March 16, 2026_