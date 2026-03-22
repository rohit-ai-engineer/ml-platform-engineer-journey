import sqlite3
import pandas as pd
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(BASE_DIR, '..', 'week-04-pandas-analysis', 'epg_schedule_20260311_041046.json')

with open(filepath, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data['valid'])

# Create SQLite database and load EPG data
conn = sqlite3.connect(':memory:')
df['genres'] = df['genres'].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
df.to_sql('shows', conn, if_exists='replace', index=False)



# result =  ("first sqlite query in Python", pd.read_sql("select network, count(*) AS show_count from shows where  runtime > 30 AND network IS NOT NULL group by network HAVING count(*) > 3 ORDER BY COUNT(*) DESC;", conn))
           
# print(result)


# result = pd.read_sql("""
#     SELECT 
#         show_name,
#         airtime,
#         airtime - LAG(airtime) OVER (PARTITION BY network ORDER BY airtime) AS gap_from_previous
#     FROM shows
#     ORDER BY airtime
# """, conn)
# print(print(result[['show_name', 'airtime', 'gap_from_previous']].head()))


result = pd.read_sql("""SELECT 
    show_name,
    network,
    runtime,
    RANK() OVER (PARTITION BY network ORDER BY runtime DESC) AS runtime_rank
FROM shows where network = 'Fox News Channel' ORDER BY runtime DESC""", conn)

