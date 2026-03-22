# Week 2 - Object-Oriented Programming

> Phase 1: Foundations · ML Platform Engineer Journey

---

## 🎯 What I Learned

- Classes vs objects: I think of it like the difference between a recipe and the actual cake you bake from it
- `__init__`, `self`, methods: the weird Python stuff that makes OOP work (still feels backwards to me sometimes)
- When to put code in `Content` (single item) vs `Catalog` (collection): honestly this took me a while to get right
- JSON persistence: saving and loading data so it survives between runs
- Dictionary counting pattern: checking if key exists, then increment or create
- `**kwargs` - passing flexible named arguments to functions
- Duplicate prevention logic: checking if something's already there before adding it again

---

## 🔨 What I Built

| File | Description |
|------|-------------|
| `content.py` | Content class - single show with is_movie(), matches_genre(), get_type() |
| `catalog.py` | Catalog class - manages a collection, add/remove/search/save/load/stats |

---

## 💡 Key Concepts

**Content vs Catalog:** Content = ONE show. Catalog = MANY shows. I spent way too long putting collection logic on Content before I realized that was backwards. Once I moved it to Catalog, everything clicked.

**JSON persistence:** `json.dump()` to save, `json.load()` to restore. The data survives after the script ends. Not a toy anymore and felt like magic the first time it worked.

**Dictionary counting:**
```python
if genre in counts:
    counts[genre] += 1
else:
    counts[genre] = 1
```
This pattern is everywhere once you start looking for it.

---

## 🚀 Run It

```bash
python catalog.py
```

---

## ➡️ Next

Week 3: APIs & Data Pipelines - fetching real data from OMDB and TVmaze, building a production-quality EPG pipeline.