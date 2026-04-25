import json
import pandas as pd 
import numpy as np
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 1. Load data

BASEDIR = os.path.dirname(os.path.abspath(__file__))
filpath = os.path.join(BASEDIR,"..","data","raw","tmdb_popular_shows.json")

with open (filpath,'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# 3. Define X (features) and y (target)
X = df[['popularity','vote_count']]
y = df['vote_average']


# 4. Train / Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
test_size=0.2, 
random_state=42
)
# 5. Feature Leakage Detector
def check_leakage(X,y, threshold=0.95):
    leaky = []
    for col in X.columns:
        corr = abs(X[col].corr(y))
        if corr > threshold:
            leaky.append((col, round(corr,4)))
    return leaky

leaky = check_leakage(X, y)
print(leaky)