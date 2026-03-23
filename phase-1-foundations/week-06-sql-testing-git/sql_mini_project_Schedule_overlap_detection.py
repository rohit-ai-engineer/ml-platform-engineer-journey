import sqlite3
import pandas as pd
import json
import os

# global variable to store output
report = ""

def log(text):
    global report
    print (text)
    report += str(text) + "\n"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(BASE_DIR, '..', 'week-04-pandas-analysis', 'epg_schedule_20260311_041046.json')

with open(filepath, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data['valid'])

# Create SQLite database and load EPG data
conn = sqlite3.connect(':memory:')
df['genres'] = df['genres'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
df.to_sql('shows', conn, if_exists='replace', index=False)


result = pd.read_sql("""WITH airtime_calc AS (
    -- Step 1: convert airtime to minutes
    SELECT show_name,  network, runtime,airtime,
        CAST(SUBSTR(airtime, 1, 2) AS INTEGER) * 60 + 
        CAST(SUBSTR(airtime, 4, 2) AS INTEGER) AS airtime_minutes 
    FROM SHOWS
),
overlap_calc AS ( 
    -- Step 2: calculate end_time and next_start using 
    SELECT *, 
        airtime_minutes + runtime AS end_time,
        LEAD(airtime_minutes) OVER (PARTITION BY network 
        order by airtime_minutes ASC) AS next_start 
    FROM airtime_calc
)
-- Step 3: filter where overlap exists
SELECT * FROM overlap_calc WHERE end_time > next_start""",conn
)

log(result)

filepath = os.path.join(BASE_DIR, "detected_overlaps.txt")

with open (filepath,'w') as f:
    f.write(report)