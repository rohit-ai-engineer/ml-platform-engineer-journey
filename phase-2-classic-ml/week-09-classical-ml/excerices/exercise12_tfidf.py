import json
import pandas as pd 
import numpy as np
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.feature_extraction.text import TfidfVectorizer

# 1. Load data

BASEDIR = os.path.dirname(os.path.abspath(__file__))
filpath = os.path.join(BASEDIR,"..","data","raw","tmdb_popular_shows.json")

with open (filpath,'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# 2. Data Preprocessing
df = df.dropna(subset=['overview'])

# 3. Define X (features) and y (target)
X = df['overview']
y = df['vote_average']

# 4. Train / Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
test_size=0.2, 
random_state=42
)

# 5. calculate TF-IDF
vectorizer = TfidfVectorizer(max_features=100)
X_tfidf_train = vectorizer.fit_transform(X_train)
X_tfidf_test = vectorizer.transform(X_test)

# 6. Linear Regression
model = LinearRegression()
model.fit(X_tfidf_train,y_train)

predict = model.predict(X_tfidf_test)

# 7. Calculate R²
r_sqaure = r2_score(y_test,predict)
print(f"R2 score of TF-IDF = {r_sqaure}")

