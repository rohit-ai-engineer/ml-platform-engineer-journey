import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Build synthetic dataset

runtime_variance = np.random.randint(0,101,200)
title_match_score = np.random.uniform(0,10,200)
provider_reliability = np.random.randint(0,11,200)
data_freshness_days = np.random.randint(0,31,200)
conflict_resolved = np.where((provider_reliability > 7) & (title_match_score > 6) & (runtime_variance < 5), 1, 0)

df = pd.DataFrame({
    "runtime_variance":runtime_variance,
    "title_match_score":title_match_score,
    "provider_reliability":provider_reliability,
    "data_freshness_days":data_freshness_days,
    "conflict_resolved":conflict_resolved
})

X = df.drop('conflict_resolved',axis =1)
y = df['conflict_resolved']

# Train / Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train a RandomForest Classifier
model = RandomForestClassifier(
    n_estimators=100,
    max_features='sqrt',
    random_state=42
)

model.fit(X_train,y_train)
model.predict(X_train)
y_pred = model.predict(X_test)

# Calculate accurace scroe 
y_accuracy = accuracy_score(y_test,y_pred)
print(y_accuracy)

# Calculate Feature importances
for feature, importance in zip(X.columns, model.feature_importances_):
    print(f"{feature}:{importance}")

print(model.feature_importances_)

