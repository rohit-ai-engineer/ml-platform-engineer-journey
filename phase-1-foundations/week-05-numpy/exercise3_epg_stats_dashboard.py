import pandas as pd
import numpy as np
import json
import os

# Global variable to store report
report = ""

def log(text):
    """log to screen AND add to report"""
    global report
    print(text) 
    report += str(text) + "\n"


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(BASE_DIR,'..','week-04-pandas-analysis','epg_schedule_20260311_041046.json')

with open (filepath,'r') as f:
    data = json.load(f)

df = pd.DataFrame(data['valid'])

df_copy = df.copy()

# Q1 — Runtime stats by show type

runtime_stat = df_copy.groupby('type').agg({'runtime' : ['mean','std']
})

log(runtime_stat)
log(runtime_stat.values)

# Q2 — Airtime distribution

airtime_split = df_copy['airtime'].str.split((':'),expand=True)
airtime_split.columns = ['HR', 'Min']
airtime_split = airtime_split.astype(int)


hours = (airtime_split['HR']*60)
total_time = hours + airtime_split['Min'] 

log(np.mean(total_time))
log(np.median(total_time))
log(np.std(total_time))

# Q3 — Genre variance

df_explode = df_copy.explode('genres')
genre_std = df_explode.groupby('genres')['runtime'].std()
log(genre_std)

log(np.max((genre_std)))
log(genre_std.idxmax())

# Q4 — Airtime vs runtime correlation

log(np.corrcoef(total_time,df['runtime']))

filepath = os.path.join(BASE_DIR, 'epg_stats.txt')

with open (filepath,'w') as f:
    f.write(report)