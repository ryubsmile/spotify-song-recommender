import sys
import os
import pandas as pd
import numpy as np

# Libraries for recommendation
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

class Recommendation:
    def __init__(self):
        # Read in data for test
        self.df = pd.read_csv('/Users/sehwaryu/Documents/spotify-song-recommender/workspace/recommender/data.csv')

    def test(self):
        print(self.df.head())

        
    # Takes about 18s for cluster
    def cluster(self):
        song_cluster_pipeline = Pipeline([('scaler', StandardScaler()), 
                                  ('kmeans', KMeans(n_clusters=20, 
                                   verbose=2, n_jobs=4))], verbose=True)
        X = self.df.select_dtypes(np.number)
        number_cols = list(X.columns)
        song_cluster_pipeline.fit(X)

        song_cluster_labels = song_cluster_pipeline.predict(X)
        self.df['cluster_label'] = song_cluster_labels




    
