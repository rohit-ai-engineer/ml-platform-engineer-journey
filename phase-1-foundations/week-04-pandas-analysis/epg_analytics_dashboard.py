import pandas as pd 
import json
import os

# Global variable to store report
report = ""

def log(text):
    """log to screen AND add to report"""
    global report
    print(text)  # ← Use log(), not log()!
    report += str(text) + "\n"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(BASE_DIR, 'epg_schedule_20260311_041046.json')

with open(filepath,'r') as f:
    data = json.load(f)

df = pd.DataFrame(data['valid'])
df_copy = df.copy()

print(df_copy.head())

print(df_copy.columns.tolist())

net_count = df_copy['network'].value_counts().head(10)
log(net_count)

big_networks = df_copy['network'].value_counts()
big_networks = big_networks[big_networks >= 5].index

avg = df_copy[df_copy['network'].isin(big_networks)].groupby('network')['runtime'].agg(['mean','min','max'])
log (avg)

show_count = df_copy['type'].value_counts(normalize=True) * 100 
log(show_count)

print(df_copy['airdate'].head(10))

print(df_copy['airdate'].dtype)

df_copy['airdate'] = pd.to_datetime(df_copy['airdate'])

log(df_copy['airdate'].dtype)

airdate_log = df_copy.groupby('airdate')['show_name'].count()
log(airdate_log)

netwok_log = df_copy.groupby(['airdate','network'])['show_name'].count().sort_values(ascending=False)
log(netwok_log)


missing = pd.DataFrame({
    'missing_count' : df_copy.isna().sum(),
    'missing_pct' : df_copy.isna().mean() * 100
})

log(missing)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(BASE_DIR, 'epg_quality_report.txt')

with open(filepath, 'w') as f:
    f.write(report)
