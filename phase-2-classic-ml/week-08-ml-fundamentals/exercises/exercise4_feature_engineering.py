import numpy as np
import pandas as pd
import json
import os
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
# 1. Load data
base_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(base_dir,"..","data","raw","tmdb_popular_shows.json")

with open(filepath,'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

GENRE_MAP = {
    10759: "Action & Adventure",
    35: "Comedy",
    80: "Crime",
    99: "Documentary",
    18: "Drama",
    10751: "Family",
    10762: "Kids",
    9648: "Mystery",
    10763: "News",
    10764: "Reality",
    10765: "Sci-Fi & Fantasy",
    10766: "Soap",
    10767: "Talk",
    10768: "War & Politics",
    37: "Western",
    16: "Animation"
}

# 1. One-hot encode on original_language (Single value column)
df_encoded = pd.get_dummies(df['original_language'], prefix='lang')

# 2A. Map genre IDs to genre names
df['genre_names'] = df['genre_ids'].apply(lambda x:[GENRE_MAP.get(id) for id in x])

# 2B. Explode genre lists into separate rows
genre_explode = df["genre_names"].explode()

# 2C. One-hot encode the exploded genre column
genre_encode = pd.get_dummies(genre_explode, prefix='gen_expl')

# 2D. Group back to one row per show
combine = (genre_encode.groupby(level=0)).max()

# 3. Interaction feature: popularity × vote_count
df['popularity_x_votes'] = df['popularity'] * df['vote_count']


# 4. Create date features from first_air_date
# First convert to datetime
df['first_air_date'] = pd.to_datetime(df['first_air_date'])

# Then extract
df['air_year'] = df['first_air_date'].dt.year
df['air_month'] = df['first_air_date'].dt.month

# Days since aired
df['days_since_aired'] = (pd.Timestamp.now() - df['first_air_date']).dt.days

# 5. Scale numerical columns
# defining features
X = df[['popularity','vote_count','days_since_aired','air_year','air_month','popularity_x_votes']]

# Train / Test split
X_train, X_test = train_test_split(
X,
test_size=0.2, 
random_state=42
)

# Train / Test split
scaler = StandardScaler()

# fit_transform on training data - learns mean and std, then transforms
X_train_scaled = scaler.fit_transform(X_train)

# transform only on test data - uses mean/std learned from training
X_test_scaled = scaler.transform(X_test)

# 6. Return final engineered DataFrame

final_feature = pd.concat([df_encoded,combine,df[['popularity','vote_count','days_since_aired','air_year','air_month','popularity_x_votes']]],axis=1)

print(final_feature.shape)