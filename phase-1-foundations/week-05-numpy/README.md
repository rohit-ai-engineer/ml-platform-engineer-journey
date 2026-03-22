# Week 5 - NumPy & Statistical Foundations

> Phase 1: Foundations · ML Platform Engineer Journey

---

## 🎯 What I Learned

- ndarray vs Python list: type enforcement plus contiguous memory gives you 15x speed on 1M elements
- Array creation: `zeros`, `ones`, `arange`, `linspace` and when to use each
- 2D matrices: `shape`, comma notation `[row, col]`, `np.column_stack()`
- Vectorization: operations on entire arrays at once, no loops
- Broadcasting: scalar operations on arrays just work, NumPy handles the shape
- Statistics: mean, median, std, percentile, corrcoef
- Linear algebra: dot product, matrix multiplication, `np.linalg.norm()`
- Cosine similarity: `dot(A,B) / (norm(A) * norm(B))` - direction not magnitude
- Categorical encoding: `.astype('category').cat.codes` for ML-ready features
- `lambda` functions: mini one-line functions, used in sorting and filtering

---

## 🔨 What I Built

| File | Description |
|------|-------------|
| `numpy_fundamentals.py` | Core NumPy - arrays, vectorization, stats, linear algebra, correlation |
| `exercise1_runtime_analysis.py` | Stats on EPG runtime data - mean/std/percentile, boolean filtering, normalization |
| `exercise2_epg_calculator.py` | Vectorized EPG calculator - end times, gap detection, scheduling holes. No loops. |
| `exercise3_epg_stats_dashboard.py` | Stats dashboard - runtime by type, airtime distribution, genre variance, correlation |
| `exercise4_cosine_similarity_engine.py` | Cosine similarity from scratch - dot product, norm, lambda sorting |
| `mini_project_content_similarity_engine.py` | `find_similar_shows()` on real TVmaze data - 3-feature matrix, normalization, edge cases |

---

## 💡 Key Concepts

**Vectorization vs loops:**
```python
# Python list - loop required
doubled = [x * 2 for x in numbers]

# NumPy - entire array at once
doubled = np_array * 2  # 15x faster on 1M elements
```

**Cosine similarity:**
```python
similarity = np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))
```
Measures direction not magnitude. Two shows with the same runtime/airtime/type = score of 1.0. Will be used in Project 1 for semantic title matching.

**Every ML prediction:**
```python
prediction = np.dot(features, weights)
```
That's it. Every linear model, every neural network layer - dot products all the way down.

**`axis=0` vs `axis=1`:**
- `axis=0` - calculate per column (down the rows)
- `axis=1` - calculate per row (across the columns)

---

## 🚀 Run It

```bash
python mini_project_content_similarity_engine.py
```

Expected output:
```
Top 3 shows similar to 'Way Too Early':
1. Early Start with Rahel Solomon - 1.000
2. CNN This Morning - 0.999
3. ...
Report saved to content_similarity_report.txt
```

---

## ➡️ Next

Week 6: SQL, Testing & Version Control - SQLite with real EPG data, pytest for production-quality test suites, Python logging module.