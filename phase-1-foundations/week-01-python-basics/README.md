# Week 1 - Python Fundamentals

> Phase 1: Foundations · ML Platform Engineer Journey

---

## 🎯 What I Learned

- Python basics - variables, loops, conditionals, functions, f-strings
- `datetime` module - parsing and formatting time strings (strptime, strftime)
- CSV parsing with `csv.DictReader`
- XML parsing with `ElementTree` - tags vs attributes, navigating real provider feeds
- Error handling with try/except
- File paths and working directories

---

## 🔨 What I Built

| File | Description |
|------|-------------|
| `calculator.py` | Basic arithmetic calculator - 4 operations |
| `epg_time_calculator.py` | Calculates show end time from start + duration |
| `metadata_validator.py` | Validates CSV metadata - checks for missing fields and invalid values |
| `epg_flexible_validator.py` | Validates real EPG XML feeds - checks 137+ programs across providers |

---

## 💡 Key Concepts

**Tags vs Attributes in XML:** `announcedTime` is an attribute on the `<slot>` tag, not a child tag. i got this wrong at first - domain knowledge from Simply.TV helped catch it.

**Date stored at schedule level:** In EPG XML, `date` lives on the `<schedule>` element, not on every `<slot>`. This actually caught a bug in the validator.

**try/except:** Don't let one bad record crash the whole pipeline. Validate, catch, log, keep going.

---

## 🚀 Run It

```bash
python epg_flexible_validator.py
```

Expected output:
```
✓ Valid: 137 programs
✗ Invalid: 0 programs
```

---

## ➡️ Next

Week 2: Object-Oriented Programming - building a Streaming Catalog Manager with classes, JSON persistence, and a stats dashboard.