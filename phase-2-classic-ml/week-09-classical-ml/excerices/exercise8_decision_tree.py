import pandas as pd
import json
import os
from sklearn.metrics import confusion_matrix, classification_report, auc, roc_curve
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree, DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# 1. Load data
BASEDIR = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(BASEDIR,"..","data","raw","tmdb_popular_shows.json")

with open (filepath,'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# 2. Creat high_quality  
df['is_high_quality'] = df['vote_average'] >= 7.6

# 3. Define X (features) and y (target)
X = df[['popularity','vote_count']]
y = df['is_high_quality']

# 4. Train / Test split
X_train, X_test, y_train, y_test = train_test_split (
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 5. Initialize and Train the model
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train,y_train)

# 6. Make predictions on test set
prediction = model.predict(X_test)

# 7. Calculate Probability
probability = model.predict_proba(X_test)[:,1] # type: ignore

# 8. Calculate Confusion Matrix
c_matrix = confusion_matrix(y_test,prediction)
print (f"Confusion matrix: {c_matrix}")

# 9. Calculate Classification Report
c_report = classification_report(y_test,prediction)
print (f"Classification Report: {c_report}")

# 10. Calculate ROC Curve
r_curve = roc_curve(y_test,prediction)

# 11. Calculate AUC
fpr, tpr, thresholds = roc_curve(y_test, probability)
auc_score = auc(fpr, tpr)
print(f"AUC Score {auc_score}")

# 12. Plotting ROC
plt.plot(fpr, tpr, label=f'AUC = {auc_score:.2f}')
plt.plot([0, 1], [0, 1], 'k--')  # random baseline
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.savefig(os.path.join(BASEDIR, '..', 'results', 'roc_curve_decision_tree.png'))
# plt.show()

# 13. Plot the tree
plt.figure(figsize=(15, 8))
plot_tree(model, feature_names=X.columns , 
          class_names=['Low', 'High'], filled=True) # type: ignore
plt.savefig(os.path.join(BASEDIR, '..', 'results', 'decision_tree.png')) 
plt.show()