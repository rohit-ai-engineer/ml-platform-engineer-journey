import pandas as pd
import json

print("=== My First Pandas DataFrame ===\n")

# Step 1: Load your EPG JSON from Week 3
# (Update the filename to match yours)
with open('C:/Users/Rohit Jadiya/Downloads/data/Claude/ai-engineer-journey/epg_schedule_20260311_041046.json', 'r') as f:
    data = json.load(f)

# Step 2: Extract just the valid shows
shows = data['valid']

# Step 3: Create a DataFrame
df = pd.DataFrame(shows)

# Step 4: Basic exploration
print(f"📊 Loaded {len(df)} shows into DataFrame\n")

# Show first 5 rows
print("--- First 5 Shows ---")
print(df.head())

# Show column names
print(f"\n--- Columns ({len(df.columns)}) ---")
print(df.columns.tolist())

# Show basic stats
print("\n--- DataFrame Info ---")
print(df.info())

print("\n" + "="*50)
print("ANALYSIS 1: Shows Per Network")
print("="*50)

network_counts = df['network'].value_counts()
print(network_counts)

print("\n" + "="*50)
print("ANALYSIS 2: Runtime Statistics")
print("="*50)

avg_runtime = df['runtime'].mean()
min_runtime = df['runtime'].min()
max_runtime = df['runtime'].max()

print(f"Average runtime: {avg_runtime:.1f} minutes")
print(f"Shortest show: {min_runtime} minutes")
print(f"Longest show: {max_runtime} minutes")


print("\n" + "="*50)
print("ANALYSIS 3: Find the Longest Show")
print("="*50)

longest_show = df[df['runtime'] == 300]
print(longest_show[['show_name', 'network', 'runtime', 'airtime']])


print("\n" + "="*50)
print("ANALYSIS 4: Shows Missing Network Info")
print("="*50)

missing_network = df[df['network'].isna()]
print(f"Found {len(missing_network)} shows with missing network:\n")
print(missing_network[['show_name', 'network', 'airtime']])

print("\n" + "="*50)
print("PREVIEW: Grouping & Aggregation")
print("="*50)

# Group by network and calculate stats
network_stats = df.groupby('network').agg({
    'runtime': ['mean', 'min', 'max', 'count']
})

print("\nNetwork Stats (Top 10 by show count):")
print(network_stats.sort_values(('runtime', 'count'), ascending=False).head(10))