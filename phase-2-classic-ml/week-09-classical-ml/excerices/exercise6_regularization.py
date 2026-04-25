import numpy as np
import pandas as pd
import json
import os
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, Lasso, LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


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

# 5. Return final engineered DataFrame

final_feature = pd.concat([df_encoded,combine,df[['popularity','vote_count','days_since_aired','air_year','air_month','popularity_x_votes']]],axis=1)

final_feature = final_feature.fillna(0)

# 7. Regularization
X = final_feature
y = df['vote_average']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()

# fit_transform on training data - learns mean and std, then transforms
X_train_scaled = scaler.fit_transform(X_train)

# transform only on test data - uses mean/std learned from training
X_test_scaled = scaler.transform(X_test)

# 6. Reorganization Lasso model
lasso = Lasso(alpha=0.01)
lasso.fit(X_train_scaled, y_train)
predictions = lasso.predict(X_test_scaled)

# get feature names
feature_names = X.columns

# pair each feature name with its coefficient
coef_pairs = zip(feature_names, lasso.coef_)

# sort by absolute value, take top 5
top5 = sorted(coef_pairs, key=lambda x: abs(x[1]), reverse=True)[:5]

r_square = r2_score(y_test,predictions)
print(f"R2 of lasso {r_square}")

for feature, coef_pairs in top5:
    print(f"{feature:15} → {coef_pairs:.4f}")

# 7. Reorganization Ridge model
ridge = Ridge(alpha=0.01)
ridge.fit(X_train_scaled, y_train)
predictions = ridge.predict(X_test_scaled)

# get feature names
feature_names = X.columns

# pair each feature name with its coefficient
coef_pairs = zip(feature_names, ridge.coef_)

# sort by absolute value, take top 5
top5 = sorted(coef_pairs, key=lambda x: abs(x[1]), reverse=True)[:5]

r_square = r2_score(y_test,predictions)
print(f"R2 of Ridge {r_square}")

for feature, coef_pairs in top5:
    print(f"{feature:15} → {coef_pairs:.4f}")


# 8. Linear Regression model
model = LinearRegression()
model.fit(X_train_scaled, y_train)
predictions = model.predict(X_test_scaled)

# get feature names
feature_names = X.columns

# pair each feature name with its coefficient
coef_pairs = zip(feature_names, model.coef_)

# sort by absolute value, take top 5
top5 = sorted(coef_pairs, key=lambda x: abs(x[1]), reverse=True)[:5]

r_square = r2_score(y_test,predictions)
print(f"R2 of Linear {r_square}")

for feature, coef_pairs in top5:
    print(f"{feature:15} → {coef_pairs:.4f}")
