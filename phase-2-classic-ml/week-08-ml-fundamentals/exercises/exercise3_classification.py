from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import json
import os

# 1. Load data
base_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(base_dir,"..","data","raw","tmdb_popular_shows.json")

with open(filepath,'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# 2. Create is_high_quality column based on median threshold
df['is_high_quality'] = df ['vote_average'] >= 7.6

# 3. Define X (features) and y (target)
y = df['is_high_quality']

X = df [['popularity','vote_count']]

# 4. Train / Test split
X_train, X_test, y_train, y_test = train_test_split(
X, y, 
test_size=0.2, 
random_state=42
)

# 5. Initialize and Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 6. Make predictions on test set
predictions = model.predict(X_test)

# 7. Calculate Confusion Matrix
c_matrix = confusion_matrix(y_test, predictions)
print(f"Confusion Matrix score: {c_matrix}")

# 8. Calculate Classification Report
c_report = classification_report(y_test, predictions)
print(f"Classification Report: {c_report}")

# 9. Calculate ROC Curve
y_proba = model.predict_proba(X_test)[:, 1]
r_curve = roc_curve(y_test, y_proba)

# 10. Plotting ROC
fpr, tpr, thresholds = roc_curve(y_test, y_proba)
auc_score = auc(fpr, tpr)

plt.plot(fpr, tpr, label=f'AUC = {auc_score:.2f}')
plt.plot([0, 1], [0, 1], 'k--')  # random baseline
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.savefig(os.path.join(base_dir, '..', 'results', 'roc_curve.png'))
plt.show()