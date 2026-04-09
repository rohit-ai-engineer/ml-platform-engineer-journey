import json
import pandas as pd 
import numpy as np
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

# 1. Load data

BASEDIR = os.path.dirname(os.path.abspath(__file__))
filpath = os.path.join(BASEDIR,"..","data","raw","tmdb_popular_shows.json")

with open (filpath,'r') as f:
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

# 2. Create Genre column
df['genre'] = df['genre_ids'].apply(lambda x: GENRE_MAP.get(x[0]) if x else None)

# 3. calculate Freq encoding of genre 
freq_map = df['genre'].value_counts()
df['genre_freq'] = df['genre'].map(freq_map)
df['genre_freq'] = df['genre_freq'].fillna(0)

# 4. Define X (features) and y (target)
X = df[['genre_freq','popularity','vote_count']]
y = df['vote_average']

# 5. Train / Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
test_size=0.2, 
random_state=42
)

# 6. Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

predict = model.predict(X_test)

# 7. Calculate MSE
mse = mean_squared_error(y_test, predict)

# 8. Calculate RMSE from RMSE
rmse = np.sqrt(mse)

# 9. Calculate R²
r_square = r2_score(y_test, predict)

# 10. Calcuate Cross Validation score
cv_score_r2 = cross_val_score(model, X_train, y_train, cv =5, scoring='r2')
cv_score_mse = cross_val_score(model, X_train, y_train, cv =5, scoring='neg_mean_squared_error')

# 11. checking the outcomes
print(f"CV R² scores: {cv_score_r2}")
print(f"CV R² mean: {cv_score_r2.mean():.4f}")
print(f"CV MSE scores: {-cv_score_mse}")
print(f"CV MSE mean: {(-cv_score_mse).mean():.4f}")

# 12. checking What did the model actually learn
print(f"Coefficients: {model.coef_}")
print(f"Feature names: {X.columns.tolist()}") # type: ignore
print(f"Intercept: {model.intercept_:.4f}")