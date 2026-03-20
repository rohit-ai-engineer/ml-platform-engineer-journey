import pandas as pd
import numpy as np
import json
import os

# Global variable to store output
report = ""

def log(text):
    global report
    print(text)
    report += str(text) + "\n"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(BASE_DIR, '..','week-04-pandas-analysis','epg_schedule_20260311_041046.json')

with open (filepath,'r') as f:
    data = json.load(f)

df = pd.DataFrame(data['valid'])

df_copy = df.copy()

# Building feature matrix

# Converting airtime to minutes
airtime_split = df_copy['airtime'].str.split((':'),expand=True)
airtime_split.columns = ['HR','Min']
airtime_split = airtime_split.astype(int)

hours = (airtime_split['HR']*60)
Total_time = hours + airtime_split['Min']


# Extracted runtime from df
runtime_stack = df_copy['runtime']

# Encoding type as integers
type_cat = df_copy['type'].astype('category').cat.codes

# Stacking all 3 into one 2D NumPy array
new_arr = np.column_stack((Total_time,runtime_stack,type_cat))

# Normalizing the matrix
mean = np.mean(new_arr,axis=0)
std = np.std(new_arr,axis=0)
features_normalized = (new_arr - mean) / std

# Building the function
def find_similar_show(show_name, df_copy, features_normalized, top_n=3):
    # condition if the show name is user input show name which isn't present in dataset
    if show_name not in df_copy['show_name'].values:
        return f"Show '{show_name}' not found in dataset"

    # finding index of show_name
    name = df_copy['show_name'].tolist().index(show_name)
    #Extrcating the row
    norm = features_normalized[name]
    # Calculating cosine similarity
    sim_target = np.linalg.norm(norm)
    sim_all = np.linalg.norm(features_normalized, axis=1)
    cosine_simi = np.dot(features_normalized, norm) / (sim_target * sim_all)
    # sorting
    top_shows = list(zip(df_copy['show_name'],cosine_simi))
    top_shows_sorted = sorted(top_shows, key=lambda x:x[1],reverse=True)
    top_shows_sliced = top_shows_sorted[1:top_n+1]
    return top_shows_sliced


log(find_similar_show('SEC Now',df_copy,features_normalized ))

filepath = os.path.join(BASE_DIR,'content_similarity_report.txt')

with open(filepath,'w') as f:
    f.write(report)



