# Week 6 - SQL, Testing & Version Control

> Phase 1: Foundations · ML Platform Engineer Journey

---

## What I Learned

- SQL execution order: WHERE runs before SELECT, HAVING runs after GROUP BY. Once you know the order, the logic stops feeling arbitrary.
- Window functions: RANK(), LEAD(), LAG() let you query rows relative to other rows without collapsing the dataset. LAG() took the longest to click.
- CTEs: break a complex query into named steps instead of one unreadable nested block.
- Schedule overlap detection using LAG(): compare each show's start time against the previous show's end time in a single query, found 4 real overlaps in live TVmaze data.
- pytest fixtures: define test data once, share it across every test. Stopped copy-pasting the same dict into 10 different test functions.
- Python logging module: replaced print() with DEBUG, INFO, WARNING, ERROR levels. Matters when something breaks at 3am and you need to know at a glance what kind of event you're looking at.
- Git conflict resolution: what a merge conflict actually looks like in the file, how to pick a side, how to commit the resolution.

---

## What I Built

| File | Description |
|------|-------------|
| `sql_refresher.py` | SQL basics in SQLite - SELECT, WHERE, GROUP BY, HAVING, JOINs, window functions on real EPG data |
| `sql_mini_project_Schedule_overlaps.py` | LAG() query that detects schedule overlaps - found 4 real conflicts in TVmaze feed |
| `epg_pipeline_logged.py` | Week 3 pipeline rebuilt with Python logging module - print() replaced with structured log levels |
| `fixtures_testing.py` | Shared pytest fixtures - test data defined once, reused across the full test suite |
| `test_epg_pipeline.py` | 7 unit tests covering validate_show(), extract_show_info(), required fields, runtime edge cases |
| `test_similarity_engine.py` | 3 tests on find_similar_show() - result count, not-found handling, similarity score range |
| `detected_overlaps.txt` | Output file from the overlap detector - 4 flagged conflicts with show names and times |

---

## Key Concepts

**Why LAG() matters for EPG:**
```sql
SELECT
    show_name,
    airtime,
    LAG(end_time) OVER (ORDER BY airtime) AS prev_end_time
FROM schedule
WHERE airtime < prev_end_time  -- overlap detected
```
This is something I check manually every week at Simply.TV. Eight lines of SQL automated it.

**pytest fixture - define once, use everywhere:**
```python
@pytest.fixture
def epg_data():
    with open(filepath, 'r') as f:
        data = json.load(f)
    return pd.DataFrame(data['valid'])

def test_returns_three_results(epg_data):
    result = find_similar_show('Way Too Early', epg_data, features_normalized)
    assert len(result) == 3
```

**Logging levels - not all messages are equal:**
```python
import logging

logging.debug("Fetching schedule...")      # dev only
logging.info("115 shows fetched")         # normal ops
logging.warning("Runtime > 300 mins")     # worth watching
logging.error("API returned 404")         # something broke
```

**CTE - readable SQL:**
```sql
WITH valid_shows AS (
    SELECT * FROM schedule WHERE runtime > 0
),
long_shows AS (
    SELECT * FROM valid_shows WHERE runtime > 60
)
SELECT * FROM long_shows;
```
Same result as a nested subquery. Easier to read, easier to fix when something goes wrong.

---

## Test Results

```
10 tests ran - 10 passed
7 tests (test_epg_pipeline.py) - validate_show(), extract_show_info(), field checks, runtime edge cases
3 tests (test_similarity_engine.py) - result count, not-found handling, score range validation

```

---

## Run It

```bash
# Run the overlap detector
python sql_mini_project_Schedule_overlaps.py

# Run the full test suite
pytest -v
```

Expected overlap detector output:
```
4 scheduling conflicts detected
Results saved to detected_overlaps.txt
```

---

## Next

Week 7: Advanced Python + System Design Thinking - decorators, generators, context managers, type hints, and how to think in systems before Phase 2 begins.