# Week 3 - APIs & Data Pipelines

> Phase 1: Foundations · ML Platform Engineer Journey

---

## 🎯 What I Learned

- REST APIs: `requests.get()`, status codes, query parameters
- JSON parsing: navigating nested structures, extracting specific fields you actually need
- None handling: `.get('key') or {}` vs `.get('key', {})` (these behave differently, matters more than you would think)
- Data validation with business logic: required fields, format checks, values that actually make sense
- End-to-end pipeline pattern: fetch → extract → validate → save
- Timestamped file output for traceability, so you can trace what happened when

---

## 🔨 What I Built

| File | Description |
|------|-------------|
| `first_api_call.py` | First ever API request - proof of concept |
| `movie_fetcher.py` | Movie collector with OMDB API - search, filter by rating, export |
| `epg_pipeline.py` | Production EPG pipeline - 115 shows, 100% success rate |

---

## 💡 Key Concepts

**The `or {}` pattern:**
```python
network = show.get('network') or {}  # replaces None with empty dict
name = network.get('name', 'Unknown')  # safe to chain now
```
Without this, a None return anywhere in the chain crashes everything.

**Pipeline architecture:** Fetch → Extract → Validate → Save. Each step is separate, each step can fail gracefully. This is how production data pipelines are structured and run reliably.

**100% success rate:** 115 shows fetched from TVmaze API, all validated, all saved. The same pattern used here is the foundation for Project 1 (Metadata Conflict Resolver).

---

## 🚀 Run It

```bash
python epg_pipeline.py
```

Expected output:
```
Fetched: 115 shows
Valid: 115 (100.0%)
Saved to epg_schedule_[timestamp].json
```

---

## ➡️ Next

Week 4: Pandas & Data Analysis - loading that EPG JSON into DataFrames and asking real business questions.