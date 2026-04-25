import pandas as pd 
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.feature_selection import RFE
from sklearn.feature_selection import SelectFromModel

# 1. Creating synthetic DataFrame - 500 rows
# numeric, random 0-60
duration_diff_minutes = np.random.randint(0, 60, 500) 
# numeric, random 0-3600
start_time_diff_seconds = np. random.randint(0,3600,500) 
# float, random 0.0-1.0
title_similarity_score = np.random.uniform(0.0,1.0,500)
# binary, 0 or 1
genre_match = np.random.choice([0,1],500)
# float, random 0.0-1.0
provider_frequency = np.random.uniform(0.0,1.0,500)
# numeric, random 10-100
show_title_length = np.random.randint(10,100,500)
# pure random float
random_noise_1 = np.random.uniform(0,1200,500)
# pure random float
random_noise_2 = np.random.uniform(0,3200,500)

# 2. create PD Dataframe out of synthetic DataFrame
df = pd.DataFrame({
    "duration_diff_minutes": duration_diff_minutes,
    "start_time_diff_seconds": start_time_diff_seconds,
    "title_similarity_score": title_similarity_score,
    "genre_match":genre_match,
    "provider_frequency": provider_frequency,
    "show_title_length": show_title_length,
    "random_noise_1": random_noise_1,
    "random_noise_2": random_noise_2
})

# 3. Create is_conflict (target) column
df['is_conflict'] = ((df['title_similarity_score'] < 0.5) & (df['duration_diff_minutes'] > 30)).astype(int)

# 4. Define X (features) and y (target
X = df.drop('is_conflict',axis=1)
y = df['is_conflict']

# 5. Train / Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 6. Filter method
selector_filter = SelectKBest(score_func=f_classif, k=2)
X_selected_filter = selector_filter.fit_transform(X_train, y_train)
selcted_features_filter = X.columns[selector_filter.get_support()]
print("Filter selected:", selcted_features_filter)

# 7. Wrapper method
rfe = RFE(estimator=LogisticRegression(max_iter=1000), n_features_to_select=2)
X_selected_wrapper = rfe.fit_transform(X_train, y_train)
selcted_features_wrapper = X.columns[rfe.support_]
print("Wrapper selected:", selcted_features_wrapper)

# 8. Embedded method
rf = RandomForestClassifier(n_estimators=100, random_state=42)
selector_embedded = SelectFromModel(estimator=rf, threshold="mean")
X_selected_embedded = selector_embedded.fit_transform(X_train, y_train)
selcted_features_embedded = X.columns[selector_embedded.get_support()]
print("Embedded selected:", selcted_features_embedded)



