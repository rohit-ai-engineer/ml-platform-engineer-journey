import pandas as pd
import numpy as np


shows = {
    'Breaking Bad':     [60, 1260],  # 60 min, 9PM
    'Better Call Saul': [60, 1260],
    'The Voice':        [120, 1200],
    'News Tonight':     [30, 1320],
    'Late Night Show':  [60, 1380],
    'Morning News':     [30, 360],
    'Documentary Now':  [60, 1260],
    'Sports Center':    [30, 660],
}

# Q1. Normalize the features (subtract mean, divide by std)


names  = list(shows.keys())
features = np.array(list(shows.values()))
mean = np.mean(features, axis=0)
std = np.std(features, axis=0)
features = (features - mean)/std
#print(features)

# Q2. Calculate cosine similarity between "Breaking Bad" and every other show

breaking_bad = features[0]
norm_bb = np.linalg.norm(breaking_bad)
norm_features = np.linalg.norm(features, axis=1)

similarity = np.dot(features, breaking_bad) / (norm_features * norm_bb)
print (similarity)


# Q3. Return Top 3 most similar shows

top_3 = list(zip(names,similarity))
top_3_sorted = sorted(top_3, key=lambda x:x[1], reverse=True)
top_3_sliced = top_3_sorted[1:4]
print(top_3_sliced)