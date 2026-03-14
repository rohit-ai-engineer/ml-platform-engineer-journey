import pandas as pd
import json

# Load data
with open(r'C:/Users/Rohit Jadiya/Downloads/data/Claude/ai-engineer-journey/epg_schedule_20260311_041046.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data['valid'])

df_copy = df.copy()

df_exploded = df_copy.explode('genres')

# print(f"Original rows: {len(df)}")
# print(f"After explode: {len(df_exploded)}")
# print("\n--- First 10 rows ---")
# print(df_exploded[['show_name', 'genres', 'runtime']].head(10))


df_clean = df_exploded[df_exploded['genres'].notna()]
# print(f"After removing NaN: {len(df_clean)} rows")
# print(df_clean[['show_name', 'genres', 'runtime']].head(10))


# df_count = df_exploded.groupby('genres')['show_name'].count()
# print(df_count.head(10))


# df_avg = df_exploded.groupby('genres')['runtime'].mean().sort_values(ascending=False)

# print(df_avg.head(10))

df_spl = df_clean.groupby(['network', 'genres']).size().sort_values(ascending=False).head(10)
print(df_spl.head(10))