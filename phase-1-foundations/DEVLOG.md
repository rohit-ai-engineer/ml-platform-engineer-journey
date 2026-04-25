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

## 🗓️ Phase 1 · Foundations (Weeks 1-7)

---

### Week 1 - Entry 1 | March 2-3, 2026

**Theme:** Python fundamentals - accelerated track  
**Hours logged:** ~6 hours across 3 days

**What I actually learned:**
- Variables, print(), input() - the basics
- Working with the datetime module (strptime, strftime)
- How to format time strings properly
- CSV parsing with csv.DictReader
- **XML parsing with ElementTree** - tags vs attributes, finding elements
- The importance of actually saving files before running them (lol)
- f-strings for cleaner output
- try/except for error handling
- File paths and working directories in terminal

**The hardest thing this week:**
> Understanding XML structure - especially the difference between tags and attributes. At first I thought `announcedTime` was a tag, but it's actually an attribute on the `<slot>` tag. Also caught a bug in the validator where it was checking for date on every slot when date is actually stored once at the `<schedule>` level. Used my domain knowledge from Nielsen and Simply.TV to spot that!

**What I built:**
- `calculator.py` - basic calculator with 4 operations (addition, subtraction, multiplication, division)
- `epg_time_calculator.py` - calculates show end time from start time + duration (actually useful for my job!)
- `metadata_validator.py` - validates CSV metadata, checks for missing fields and invalid values
- `epg_flexible_validator.py` - **validates real real life EPG XML feeds** - this is production-level stuff! Checks 137+ programs for missing announcedTime, date, and title

**Moment I'm most proud of:**
> Building the XML EPG validator. It works on REAL provider feeds - the exact kind of data I work with at Simply.TV. When it validated all 137 programs successfully, that felt incredible. First time I built something that could legitimately be used in my actual job.

**Honest self-assessment:**
> Variables: 9/10, print/input: 9/10, datetime: 7/10, CSV parsing: 8/10, XML parsing: 6/10 (still learning), error handling: 7/10, control flow (loops/conditions): 8/10

**Plan for next week:**
- Start Week 2: OOP (classes, objects, methods)
- Build the Streaming Catalog Manager using proper OOP
- Maybe tackle the optional Content Duration Aggregator if time allows

**Week 1 complete? Almost - 4 out of 5 projects done. Moving to Week 2.**

---

### Week 2 - Entry 2 | March 3-4, 2026

**Theme:** OOP, File I/O & Error Handling  
**Hours logged:** ~5 hours across 2 days

**What I actually learned:**
- Classes vs objects - the blueprint vs the actual thing built from it
- `__init__` method - the constructor that runs when you create an object
- `self` - refers to the specific instance (THIS object)
- Methods - functions that belong to a class
- When to put code in Content class vs Catalog class (single item vs collection)
- JSON persistence - saving/loading data so it survives between runs
- Dictionary counting pattern - checking if key exists, then add 1 or create new
- `**kwargs` - passing flexible named arguments to functions
- try/except for handling missing files gracefully

**The hardest thing this week:**
> Understanding WHERE code should go. I tried to put a counting method in the Content class when it should've been in Catalog. It clicked when I realized: Content = ONE show, Catalog = MANY shows. Also struggled with the genre counting logic at first - had to really think through the if/else pattern for dictionaries. But once I got it, it made total sense.

**What I built:**
- `content.py` - Content class with is_movie(), matches_genre(), get_type() methods
- `catalog.py` - Catalog class that manages a collection of Content objects
- Features: add, remove, search (with multiple filters), save to JSON, load from JSON, duplicate prevention, statistics dashboard
- The stats dashboard was mostly me - wrote the movie/episode counting and genre dict logic myself with guidance

**Moment I'm most proud of:**
> Writing the genre counting logic myself. Even though I referenced the explanation, I understood WHY each line worked. When I saw the output with the genre breakdown, that felt like a real accomplishment. Also realizing I had built something that actually persists data - that's not a toy anymore.

**Honest self-assessment:**
> OOP concepts: 6/10 (understand basics but still building intuition), loops: 8/10, dictionaries: 7/10, file I/O: 8/10, knowing where code belongs: 5/10 (need more practice)

**Brutal honesty moment:**
> Realized halfway through that I'm doing OOP without solid fundamentals. It's like learning Formula 1 racing before learning to drive. I can follow along and build things with guidance, but I couldn't write this from scratch yet. Need to go back and drill the basics more.

**Plan for this week:**
- Do fundamentals practice exercises (loops, dicts, functions - no OOP)
- Solidify the concepts before Week 3
- Make sure I can write basic programs WITHOUT looking anything up
- Then start Week 3: APIs & Data Pipelines

**Week 2 complete? (Y/N):** Y - but with the understanding that I need fundamentals practice before moving forward

---

### Week 3 - Entry 3 | March 10-11, 2026

**Theme:** APIs, Data Pipelines & Real-Time Data  
**Hours logged:** ~4 hours across 2 days

**What I actually learned:**
- API requests with requests.get() - talking to external services
- JSON parsing and manipulation - converting API responses to Python objects
- Error handling - try/except blocks and None checks (the `or {}` pattern)
- Data extraction from deeply nested structures
- Data validation with business logic (required fields, format checking, reasonable values)
- File I/O with timestamps - saving processed data
- Building end-to-end pipelines (fetch → extract → validate → save)
- Debugging NoneType errors - learned to handle when API returns None values

**The hardest thing this week:**
> The NoneType error in the extraction function. I thought I fixed it with `show_data = raw_show.get('show') or {}` but kept getting errors. Turned out ANOTHER field (`network`) was also returning None. Learned that you have to check for None at EVERY level of nested data, not just the first one. This is exactly the kind of messy data I deal with at my current job - different providers return None in different places.

**What I built:**
- `movie_fetcher.py` - Full-featured movie collector with OMDB API integration
  - Search and add movies
  - Filter by rating
  - Remove from collection
  - Export reports
  - Save/load JSON persistence
- `epg_pipeline.py` - Production-quality EPG data pipeline
  - Fetches live schedule from TVmaze API (115 shows)
  - Extracts 10 clean fields from 15+ messy nested fields
  - Validates required fields and data quality
  - 100% success rate on real data
  - Saves to timestamped JSON files

**Moment I'm most proud of:**
> Building the EPG pipeline and seeing "Valid: 115 (100.0%)". This is a mini version of what I'll build for Project 1 (Metadata Conflict Resolver). I took messy, nested API data and normalized it into clean, validated records. That's literally my job at Simply.TV, except now I can code it myself.

**Honest self-assessment:**
> API requests: 8/10, JSON handling: 8/10, Error handling: 7/10 (getting better at defensive coding), Data validation: 9/10 (this felt natural from my ops background), Nested data extraction: 7/10 (still learning the patterns)

**Aha moment:**
> Understanding the difference between `.get('key', {})` and `.get('key') or {}`. The first one returns the ACTUAL value (even if it's None). The second one replaces None with {}. This tiny difference caused a 2-hour debugging session, but now I get it completely.

**Plan for next week:**
- Week 4: Pandas and data analysis
- Learn to manipulate tabular data (CSVs, DataFrames)
- Feature engineering prep for Project 1
- Start thinking about multi-source data reconciliation

**Week 3 complete? (Y/N):** Y - built 2 real pipelines, ready for data analysis!

---

### Week 4 - Entry 4 | March 13-14, 2026

**Theme:** Pandas & Data Analysis Mastery  
**Hours logged:** ~6 hours across 2 days

**What I actually learned:**
- DataFrames - loading, exploring, filtering at scale
- Grouping & aggregation (`.groupby().agg()`)
- Boolean filtering with complex conditions
- Creating new columns based on conditions
- Data validation (missing data, suspicious values)
- File I/O (reading JSON, writing formatted reports)
- Error handling with try/except

**The hardest thing this week:**
> Learning to THINK in code logic, not just copy syntax. Exercise 3 was brutal - I struggled to write code independently. But then Exercise 4 happened: I wrote the entire script from scratch based on MY OWN LOGIC. That was the breakthrough.

**What I built:**
- Network Analysis Dashboard (groupby/agg mastery)
- Primetime Analyzer (boolean filtering, new columns)
- Data Quality Report Tool (automated validation, dual output)
- Morning Programming Analyzer (self-written from logic!)
- EPG Analytics Dashboard - 5 business questions on real TVmaze data:
  1. Network Dominance (Top 10 by show count)
  2. Runtime Analysis (avg/min/max for networks with 5+ shows)
  3. Show Type Breakdown (% of schedule per type)
  4. Schedule Activity (shows per date per network)
  5. Missing Data Audit (field-level null counts + %)
  - Output saved to epg_quality_report.txt using log() pattern

**Moment I'm most proud of:**
> Writing Exercise 4 from scratch. Thought through the logic BEFORE coding, mapped it to patterns, and it worked on first try.

**Honest self-assessment:**
> DataFrames: 8/10, Groupby/agg: 7/10, Boolean logic: 8/10, Code logic: 6/10, File I/O: 9/10

**Aha moment:**
> Understanding the difference between `print()` and `return`, and between `print()` and `f.write()`. The `log()` function pattern clicked: same data, three destinations (screen, memory, file).
> Debugged 3 errors independently in the dashboard - recursion error (function calling itself), type error (Series can't concatenate with string, fixed with str()), and path error. Each one solved without being given the answer.

**Plan for next week:**
- NumPy fundamentals
- More practice exercises (5-7) for muscle memory
- Continue building portfolio depth

**Week 4 complete? ✅** Y - 5 tools built including self-written Exercise 4 and EPG Analytics Dashboard. Solid Pandas foundation, starting to think in code patterns not just syntax.

---

### Week 5 - Entry 5 | March 18-21, 2026

**Theme:** NumPy & Statistical Foundations  
**Hours logged:** ~8 hours across 3 sessions

**What I actually learned:**
- ndarray vs Python list - type enforcement + contiguous memory = 15x speed improvement, measured it myself
- Array creation: zeros, ones, arange, linspace - and the difference between them (step size vs number of points)
- 2D matrices - shape, comma notation indexing `[row, col]`, why it beats `[row][col]`
- Vectorization - entire array operations at once, no loops. Ran the benchmark, saw the difference: 0.04s vs 0.003s on 1 million elements
- Broadcasting - scalar operations on arrays just work, NumPy figures out the shape automatically
- Statistics - mean, median, std, percentile, corrcoef - and when median matters more than mean (outliers)
- Linear algebra - dot product, matrix multiplication, `np.linalg.norm()`
- Cosine similarity - `dot(A,B) / (norm(A) * norm(B))` - measuring direction not magnitude
- Categorical encoding - `.astype('category').cat.codes` to make string columns ML-ready
- `np.column_stack()` vs `np.vstack()` - got this wrong first, figured it out
- `lambda` functions - finally clicked when I saw them in `sorted(key=lambda x: x[1])`

**The hardest thing this week:**
> Cosine similarity. Not the formula - I could read the formula. The concept. Why are we dividing by the norm? What does "direction not magnitude" actually mean in practice? It only clicked when I drew two arrows and asked - do they point the same way? The math is just answering that question precisely. Once that landed, the rest followed naturally. Before that moment I was just copying the formula without understanding it.

**What I built:**
- Exercise 1: NumPy runtime analysis - arrays, vectorization, stats, value_counts on EPG data
- Exercise 2: Vectorized EPG runtime calculator - end times, gap detection, scheduling holes, time conversion. No loops anywhere.
- Exercise 3: EPG stats dashboard - runtime stats by type, airtime distribution, genre variance, network correlation. Pandas + NumPy working together.
- Exercise 4: Cosine similarity engine - dot product, linalg.norm, lambda sorting on a sample dataset
- Mini-project: `find_similar_shows()` - production function on real TVmaze data. 3-feature matrix (runtime, airtime, type encoded), normalization, cosine similarity, edge case handling. Saves output to file.

**Moment I'm most proud of:**
> I ran `find_similar_shows('Way Too Early')` and got Early Start with Rahel Solomon and CNN This Morning at the top. Here's the thing - I never told the algorithm anything about morning news. It just figured that out from runtime, airtime, and show type. I've been working with EPG data for 8 years, and when I saw those results, I knew the math was actually right. That moment felt like watching two parts of my brain finally talk to each other.

**Honest self-assessment:**
> NumPy arrays: 8/10 - solid, can write without looking things up. Vectorization: 9/10 - internalized, not just syntax. Statistics: 7/10 - know the operations, still building intuition for interpretation. Linear algebra: 6/10 - concept is clear, matrix operations still need practice. Cosine similarity: 7/10 - understand it, need to use it more to own it. Code cleanliness: 8/10 - catching variable naming issues before committing now.

**Aha moments:**
> Every ML prediction is `np.dot(features, weights)`. That's the whole thing. Dot products all the way down. I've been using scikit-learn as a black box for years in my head - now I know what's actually happening inside.

> `axis=0` vs `axis=1` didn't click from reading about it. Took 3 exercises of getting it wrong before it stuck. That's just how it goes sometimes.

> Also learned the hard way that variable names matter. Named two completely different things `norm` in the same script - one was the full normalized matrix, one was a single show's vector. Worked fine until it didn't. Caught it before committing, which is the point.

**Things I figured out on my own / Googled:**
- `np.column_stack()` - stacks arrays as columns side by side (vs vstack which stacks as rows on top of each other)
- `idxmax()` - returns the INDEX label at the maximum value, not the value itself. Subtle but important difference.

**Plan for next week:**
- SQL refresher: WHERE vs HAVING, window functions, schedule overlap detection
- Python `logging` module: proper production logging, not just print()
- pytest: full depth, this is the main event of Week 6
- Git advanced - conflict resolution

**Week 5 complete? ✅** Y - 4 exercises + mini-project done. NumPy internalized, cosine similarity understood, first taste of ML math under the hood.

---

### Week 6 - Entry 6 | March 22-23, 2026

**Theme:** SQL, Testing & Version Control  
**Hours logged:** ~6 hours across 2 sessions

**What I actually learned:**
- SQL execution order - why WHERE runs before SELECT, why HAVING runs after GROUP BY
- Window functions: RANK(), LEAD(), LAG() - querying rows relative to other rows without collapsing the dataset
- CTEs - breaking complex queries into named steps instead of one unreadable block
- Schedule overlap detection in SQL using LAG() to compare each show's start time against the previous show's end time
- pytest fundamentals - unit tests, fixtures, parametrize, data validation tests
- Python logging module - replacing print() with proper log levels (DEBUG, INFO, WARNING, ERROR)
- Git conflict resolution - what a merge conflict actually looks like, how to resolve it manually

**The hardest thing this week:**
> Window functions, the concept of operating on a row while still seeing the full dataset felt backwards at first. LAG() specifically - understanding that it's pulling the previous row's value into the current row clicked once I applied it to schedule overlap detection. 
Once that landed it made total sense: I'm not grouping, I'm sliding.

**What I built:**
- EPG SQLite database - normalized the Week 3 pipeline output into a real relational schema
- Schedule overlap detector - LAG() query that flags shows where start time < previous end time
- pytest test suite - 7 tests covering validate_show(), extract_show_info(), data quality checks, fixtures for reusable test data
- Production logging - replaced all print() calls in pipeline with structured log levels

**Moment I'm most proud of:**
> The overlap detection query. Wrote it myself using LAG() after understanding the concept. It found 3 real scheduling conflicts in the TVmaze data. That's the kind of thing I check manually at work every week and I just automated it in 8 lines of SQL.

**Honest self-assessment:**
> SQL basics: 9/10, Window functions: 7/10 (understand, need more reps), CTEs: 8/10, pytest: 7/10, Logging: 8/10, Git conflicts: 7/10

**Aha moment:**
> pytest fixtures. Writing the test data once and reusing it across 7 tests instead of copy-pasting the same dict. That's the first time testing felt like it had actual structure rather than just checking things.

**Plan for next week:**
- Week 7: Advanced Python + System Design Thinking
- Encapsulation, serialization (deferred from Week 2)
- Decorators, generators, context managers, type hints
- Architecture diagrams, trade-off thinking, ETL patterns

**Week 6 complete? ✅** Y - SQL, testing, and Git done. Window functions and pytest were the highlights. Phase 1 one week from done.

---

### Week 7 - Entry 7 | March 27-28, 2026

**Theme:** Advanced Python & System Design Thinking  
**Hours logged:** ~2 hours

**What I actually learned:**

Advanced Python
- Encapsulation: private attributes with `__double_underscore`, getters to read them, setters to update them with validation rules
- Serialization: converting Python objects to JSON and back. Turns out I've been doing this since Week 3 with `json.dump()` and `json.load()`. Just didn't have a name for it.
- Context managers: same story. `with open()` has been a context manager this whole time. `__enter__` runs at the start, `__exit__` runs at the end no matter what.
- Decorators: a function that wraps another function. `@log_stage` adds logging without touching the original function. The `wrapper` layer was the hardest part to visualise.
- Generators: `yield` instead of `return`. One item at a time, memory stays flat, use when the dataset is too large to load all at once.
- Type hints: `def fetch_schedule(country_code: str, date: str) -> list[dict]:` tells the next engineer exactly what goes in and comes out. `mypy` checks them before runtime.
- Advanced error handling: specific except blocks per error type, `finally` for cleanup that always runs, `raise` to pass errors up the chain.

System Design Thinking
- Architecture diagrams: drew the Metadata Conflict Resolver architecture on paper twice (really on paper). First attempt was missing the Normalize step before the ML model. Once I understood why the model needs all providers in the same format before it can compare anything, the diagram fixed itself.
- Trade-off thinking: there's no universally right answer, just the right answer for the situation. A live schedule update hitting every 15 minutes needs a fast model even if it's slightly less accurate, wrong metadata gets corrected next cycle anyway. A $2 million content licensing call that happens once a month? Take the time, run the complex model, get it right. Same pipeline, completely different priorities. The decision changes based on what failure actually costs.
- Latency vs throughput: independent metrics. More workers raises throughput but doesn't make each item process faster. like for live sports metadata, latency is everything. A score update that arrives 10 minutes late is useless. For overnight batch runs, throughput wins - get through 50,000 shows before morning.
- Single point of failure: one component that takes everything down if it fails. Fix it with redundancy and failover. if source API goes down and the entire pipeline stops, that's a single point of failure. The fix is redundancy: a backup source that kicks in automatically when the primary fails. At work we don't rely on one EPG provider for exactly this reason.If one drops, the others cover. I've been building around single points of failure for years without calling it that.
- ETL pipeline architecture: Extract, Transform, Load. Turns out I've been building ETL pipelines since Week 3 and calling them "the pipeline". The naming isn't the insight though. The insight is why the order is non-negotiable: bad data caught at validation is an internal problem. Bad data that makes it through validation, gets transformed, gets loaded into the database and ends up in a client feed is a customer escalation. Fail fast, fail early. Catch it at the gate.
Also learned that production pipelines don't live in one giant file like ingest.py, validate.py, transform.py, load.py, each with one job. When something breaks at 3am, you go to one file, not 800 lines of spaghetti.

**The hardest thing this week:**
> Decorators. Specifically the layering: `log_stage` returns `wrapper`, `wrapper` calls `func`, and `func.__name__` is the original function being wrapped - not the decorator. Took several passes before I stopped reading it backwards.

**What I built:**
> Theory-only week. No code projects. Drew the Metadata Conflict Resolver architecture on paper: Providers → Validate → Normalize → ML Model → confidence diamond → HITL or Transform → PostgreSQL. 
Drew it twice: once wrong (missing Normalize), once right after understanding why normalization has to happen before the ML model sees the data.

**Moment I'm most proud of:**
> The System Design session. Almost everything covered - staging environments, schema validation on onboarding, provider isolation, failover which I already do at work. I've been doing system design for last 8 years, I just didn't have the vocabulary for it until now.

**Honest self-assessment:**
> Encapsulation: 8/10, Serialization: 9/10 (was already doing it), Context managers: 8/10 (was already using them), Decorators: 6/10 (concept clear, need reps), Generators: 7/10, Type hints: 8/10, System design principles: 8/10 (domain knowledge helps a lot here)

**Aha moments:**
> Decorators and context managers both clicked the same way: I'd been using the patterns without knowing their names. `with open()` every week since Week 3. `json.dump()` since Week 3, named things now. That changes how I read other people's code.

> System design isn't a new skill. It's the same decisions I make at work, just with different names and drawn on a whiteboard instead of written in an SOP.

**Plan for next week:**
- Phase 2 kickoff - Week 8: ML Fundamentals & Feature Engineering
- Supervised vs unsupervised, overfitting, bias-variance tradeoff
- Decision trees, Random Forest, classification metrics
- Feature engineering masterclass

**Week 7 complete? ✅** Y - Advanced Python and System Design Thinking done. Phase 1 complete. 7 weeks, 17 projects, ~75 commits. Phase 2 starts now.

---