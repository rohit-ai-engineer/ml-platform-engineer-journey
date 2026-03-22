# Week 4 - Pandas & Data Analysis

> Phase 1: Foundations · ML Platform Engineer Journey

---

## 🎯 What I Learned

- DataFrames: loading JSON/CSV, exploring shape, dtypes, head/info/describe
- Boolean filtering: `df[df['runtime'] > 60]` - works like NumPy masks but for DataFrames
- `.groupby().agg()`: group your data and run multiple aggregations at once instead of doing them one by one
- `.loc[]`: to create new columns based on conditions
- `.isna()` / `.notna()`: for missing data detection
- `.explode()`: when you have list columns, it turns one row with multiple genres into separate rows
- `value_counts()`: idiomatic or the Pandas way to count how often things appear
- `pd.concat()`: for merging multiple sources
- The `log()` pattern: write to screen and file at the same time with one function call
- `.str.split(expand=True)`: split string column into multiple columns

---

## 🔨 What I Built

| File | Description |
|------|-------------|
| `pandas_intro.py` | First DataFrame operations - loading, exploring, filtering |
| `practice_1_network_analysis.py` | Network-level groupby/agg - runtime stats per network |
| `practice_2_primetime.py` | Boolean filtering - 8PM-10PM shows, new boolean columns |
| `practice_3_data_quality_report.py` | Automated validation - dual output (screen + file) |
| `practice_4_morning_shows_analysis.py` | Self-written from scratch - no step-by-step guidance |
| `practice_5_genre_analysis.py` | `.explode()` + multi-column groupby - written independently |
| `epg_analytics_dashboard.py` | 5 business questions on real TVmaze data - mini-project |
| `data_cleaning.py` | Data cleaning patterns on EPG data |

---

## 💡 Key Concepts

**Boolean masking:**
```python
big_networks = counts[counts >= 5].index  # filter Series using itself
df[df['network'].isin(big_networks)]       # filter DataFrame using the result
```
Same pattern repeated everywhere - understand it once, use it forever.

**`value_counts()` vs `groupby().count()`:** Same result, `value_counts()` is one line and already sorted. Use it when you just need counts.

**The `log()` pattern:**
```python
def log(text):
    global report
    print(text)
    report += str(text) + "\n"
```
Every `log()` call goes to screen AND accumulates in memory. One `f.write(report)` at the end saves everything. Clean separation of concerns.

---

## 🚀 Run It

```bash
python epg_analytics_dashboard.py
```

Expected output:
```
[Network dominance top 10]
[Runtime stats for networks with 5+ shows]
[Show type breakdown %]
[Schedule activity by date/network]
[Missing data audit]
Report saved to epg_quality_report.txt
```

---

## ➡️ Next

Week 5: NumPy & Statistical Foundations - the math layer under Pandas, vectorization, dot products, and a content similarity engine.