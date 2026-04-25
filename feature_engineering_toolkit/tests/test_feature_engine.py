import pandas as pd
import numpy as np
from src.feature_engine import FeatureEngine


X_train = pd.Series(['Netflix', 'HBO', 'Netflix', 'Disney', 'HBO'])
y_train = pd.Series([1, 0, 1, 0, 1])

def test_fit_feature_encoder():
    fe = FeatureEngine()
    fe.fit_target_encoder(X_train, y_train)

    assert 'global_mean' in fe.target_encoding_map
    assert 'encoding' in fe.target_encoding_map
    assert not fe.target_encoding_map['encoding'].empty
    assert 'Netflix' in fe.target_encoding_map['encoding'].index


def test_fit_frequency_encoder():
    fe = FeatureEngine()
    fe.fit_frequency_encoder(X_train)

    assert not fe.freq_encoding_map.empty #type: ignore
    assert fe.freq_encoding_map.between(0,1).all() #type: ignore

def test_transform_frequency_encoder():
    X_unknown = pd.Series(['Netflix', 'Unknown_Provider'])
    fe = FeatureEngine()
    fe.fit_frequency_encoder(X_train)
    result = fe.transform_frequency_encoder(X_unknown)

    assert result.iloc[1] == 0

def test_detect_leakage():
    X = pd.DataFrame({
    'leaky_feature': [1, 0, 1, 0, 1],
    'clean_feature': [0.5, 0.3, 0.8, 0.1, 0.6]})
    y = pd.Series([1, 0, 1, 0, 1])
    fe = FeatureEngine()
    result = fe.detect_leakage(X,y,threshold=0.95)
    features = [f[0] for f in result]

    assert 'leaky_feature' in features


def test_select_features ():
    duration_diff = np.random.randint(0,60,100)
    star_diff = np.random.randint(0,1000,100)
    title_uni = np.random.uniform(0,1,100)
    genre_match = np.random.choice([0,1],100)

    test_binary = np.random.choice([0,1],100)

    df_1 = pd.DataFrame({
        "duration_diff":duration_diff,
        "star_diff":star_diff,
        "title_uni":title_uni,
        "genre_match":genre_match
        })
    df_test = pd.Series(test_binary)
    
    X_train = df_1
    y_train = df_test
    
    fe = FeatureEngine()
    result = fe.select_features(X_train,y_train)

    assert set(result).issubset(set(X_train.columns))