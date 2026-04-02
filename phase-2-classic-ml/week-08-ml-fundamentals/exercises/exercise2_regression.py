from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import json
import os
from sklearn.model_selection import cross_val_score

# 1. Load data
base_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(base_dir,"..","data","raw","tmdb_popular_shows.json")

with open(filepath,'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# 2. Define X (features) and y (target)
y = df['vote_average']

first_air_date_modified = pd.to_datetime(df['first_air_date'])
unix_first_air_date = first_air_date_modified.astype(int) // 10**9

df['unix_first_air_date'] = unix_first_air_date

X = df [['popularity','vote_count','unix_first_air_date']]

# 3. Train / Test split
X_train, X_test, y_train, y_test = train_test_split(
X, y, 
test_size=0.2, 
random_state=42
)

# 4. Initialize and Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Make predictions on test set
predictions = model.predict(X_test)

# 6. Calculate MSE
mse = mean_squared_error(y_test, predictions)

# 7. Calculate RMSE from RMSE
rmse = np.sqrt(mse)

# 8. Calculate R²
r_square = r2_score(y_test, predictions)

# 9. Calcuate Cross Validation score
cv_score_r2 = cross_val_score(model, X, y, cv =5, scoring='r2')
cv_score_mse = cross_val_score(model, X, y, cv =5, scoring='neg_mean_squared_error')

# 10. Checking the outcomes
# print(f"CV R² scores: {cv_score_r2}")
# print(f"CV R² mean: {cv_score_r2.mean():.4f}")
# print(f"CV MSE scores: {-cv_score_mse}")
# print(f"CV MSE mean: {(-cv_score_mse).mean():.4f}")

# 11. Checking what did the model actually learn
print(f"Coefficients: {model.coef_}")
print(f"Feature names: {X.columns.tolist()}")
print(f"Intercept: {model.intercept_:.4f}")