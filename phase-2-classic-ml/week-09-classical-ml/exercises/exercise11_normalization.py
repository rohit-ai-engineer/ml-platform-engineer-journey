import json
import pandas as pd 
import numpy as np
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

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

# 2. Define X (features) and y (target)
X = df[['popularity','vote_count']]
y = df['vote_average']

# 3. Train / Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
test_size=0.2, 
random_state=42
)

# 4. calculate Scalers
scalers = {
    'StandardScaler': StandardScaler(),
    'MinMaxScaler': MinMaxScaler(),
    'RobustScaler': RobustScaler()
}

for name, scaler in scalers.items():
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)
    predict = model.predict(X_test_scaled)
    r_square = r2_score(y_test, predict)
    
    print(f"{name}: R² = {r_square:.4f}")
