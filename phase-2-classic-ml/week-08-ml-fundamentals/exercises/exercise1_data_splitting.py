import json
import os
import pandas as pd
from sklearn.model_selection import train_test_split

base_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(base_dir,"..","data","raw","tmdb_popular_shows.json")

with open(filepath,'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
y = df['vote_average']

first_air_date_modified = pd.to_datetime(df['first_air_date'])
unix_first_air_date = first_air_date_modified.astype(int) // 10**9

df['unix_first_air_date'] = unix_first_air_date

X = df [['popularity','vote_count','unix_first_air_date']]

X_train, X_test, y_train, y_test = train_test_split(
X, y, 
test_size=0.2, 
random_state=42
)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)