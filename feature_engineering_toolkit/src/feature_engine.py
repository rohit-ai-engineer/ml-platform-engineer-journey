import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import RobustScaler
from sklearn.feature_selection import SelectFromModel

class FeatureEngine:
    def __init__(self):
        self.target_encoding_map = {} # filled during fit_target_encoder()
        self.freq_encoding_map = {} # filled during fit_frequency_encoder()
        self.scalers = {} # filled during fit_normalization()
        self.selected_features = []  # filled during select_features()
        self.tfidf_vectorizer = None  # filled during fit_tfidf()

    def fit_target_encoder (self,X_train, y_train):
        """Fit a TargetEncoder on the training data"""
        y_mean = y_train.mean()
        t_encoding = y_train.groupby(X_train).mean()
        self.target_encoding_map = {
            'global_mean': y_mean,
            'encoding': t_encoding
            } 

    def transform_target_encoder(self,X_train):
        """Transform data using the fitted TargetEncoder"""
        category_mapping = X_train.map(self.target_encoding_map['encoding'])
        encoded_column = category_mapping.fillna(self.target_encoding_map['global_mean'])
        return encoded_column
    
    def fit_frequency_encoder(self,X_train):
        """Fit a FrequencyEncoder on the training data"""
        self.freq_encoding_map = X_train.value_counts()/ len(X_train)

    def transform_frequency_encoder(self,X_train):
        """Transform data using the fitted FrequencyEncoder"""
        freq_encoding = X_train.map(self.freq_encoding_map)
        freq_encoded_column = freq_encoding.fillna(0)
        return freq_encoded_column

    def fit_normalization(self,X_train):
        """ Fit normalization on on the training data"""
        self.scalers = RobustScaler()
        self.scalers.fit(X_train)

    def transform_normalization(self,X_train_scaled):
        """Transform data using the fitted normalization"""
        return self.scalers.transform(X_train_scaled) #type: ignore

    def detect_leakage(self,X,y, threshold=0.95):
        """Detect leakage in test data"""
        leaky = []
        for col in X.columns:
            corr = abs(X[col].corr(y))
            if corr > threshold:
                leaky.append((col, round(corr,4)))
        return leaky

    def select_features(self,X_train,y_train):
        """ Select best feature when compared columns of feature and target  """
        rf = RandomForestClassifier(n_estimators=100,random_state=42)
        selector_embedded = SelectFromModel(estimator=rf,threshold='mean')
        selector_embedded.fit(X_train,y_train)
        self.selected_features = X_train.columns[selector_embedded.get_support()]
        return self.selected_features