from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pandas as pd
import json
import numpy as np
import os
import matplotlib.pyplot as plt

# 1. Load data
base_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(base_dir,"..","data","raw","tmdb_popular_shows.json")

with open (filepath,'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# 2. Defining variables
X = df['vote_count'].values.reshape(-1,1)
y = df['vote_average']
X_plot = np.linspace(X.min(), X.max(), 300).reshape(-1, 1)

# 3. Train/Test split 80/20
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size = 0.2,
    random_state = 42)

# 4. Train a plain LinearRegression
model = LinearRegression()
model.fit (X_train,y_train)

# generating prediction on test set
predictions = model.predict(X_test)
predictions_plot = model.predict(X_plot)

# calculate  R² on y_tet & predictions
r_square = r2_score(y_test,predictions)

# 5. Creat Polynomial Features and get R²
poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)
X_plot_poly = poly.transform(X_plot)

# 6. Linear Regression on polynomial features
model = LinearRegression()
model.fit(X_train_poly,y_train)

prediction_linear = model.predict(X_test_poly)
prediction_linear_plot = model.predict(X_plot_poly) 

r_square_lin = r2_score(y_test,prediction_linear)
print(r_square_lin)

# 6. Plotting both R2 results on charts

# Create a figure
plt.figure(figsize=(10, 6))

# Scatter plot - raw data points
plt.scatter(X, y, alpha=0.3, color='gray', label='actual shows')

# Line plot - model predictions
plt.plot(X_plot, predictions_plot, color='blue', label='linear')

# Curve plot - model predictions
plt.plot(X_plot, prediction_linear_plot, color='red', label='polynomial (degree=2)')

# Labels and legend
plt.xlabel('Vote Count')
plt.ylabel('Vote Average')
plt.title(f'Linear (R²={r_square:.3f}) vs Polynomial (R²={r_square_lin:.3f})')
plt.legend()

# Save it
plt.savefig(os.path.join(base_dir, '..', 'results', 'Linear_vs_Polynomial_Regression.png'))

# Show it
plt.show()
