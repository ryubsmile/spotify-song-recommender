import sys
import os
import pandas as pd
import numpy as np
from collections import defaultdict
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config

# Libraries for recommendation
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import euclidean_distances
from scipy.spatial.distance import cdist
import difflib

"""
Recommendation algorithm based on the three tracks user requested
- Content-based filtering
"""

class Recommendation:
    def __init__(self):
        # Read in data for test
        self.df = pd.read_csv('/Users/sehwaryu/Documents/spotify-song-recommender/workspace/recommender/data.csv')
        self.number_cols = ['valence', 'year', 'acousticness', 'danceability', 'duration_ms', 'energy', 'explicit',
 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'popularity', 'speechiness', 'tempo']
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= config.cid,
                                                           client_secret=config.secret))

    def test(self):
        # print(self.df.head())
        # print(self.find_song('BTS', 2021))
        print(self.recommend_songs([{'name': 'Butter', 'year': 2021},
                {'name': 'Permission to Dance', 'year': 2021},
                {'name': 'Dynamite', 'year': 2020}],  self.df))
        
                                                
    """
    Perform cluster of the tracks data with Kmeans
    - Divide the dataset into 20 clusters based on the tracks' features
    """
    def cluster(self):
        song_cluster_pipeline = Pipeline([('scaler', StandardScaler()), 
                                  ('kmeans', KMeans(n_clusters=20, 
                                   verbose=2, n_jobs=4))], verbose=True)
        X = self.df.select_dtypes(np.number)
        self.number_cols = list(X.columns)
        song_cluster_pipeline.fit(X)

        song_cluster_labels = song_cluster_pipeline.predict(X)
        self.df['cluster_label'] = song_cluster_labels
        return song_cluster_pipeline

    """
    Find songs that are not in the dataset and return it as a dataframe form
    """
    def find_song(self, name, year):
    
        song_data = defaultdict()
        results = self.sp.search(q= 'track: {} year: {}'.format(name,
                                                        year), limit=1)
        if results['tracks']['items'] == []:
            return None
        
        results = results['tracks']['items'][0]

        track_id = results['id']
        audio_features = self.sp.audio_features(track_id)[0]
        
        song_data['name'] = [name]
        song_data['year'] = [year]
        song_data['explicit'] = [int(results['explicit'])]
        song_data['duration_ms'] = [results['duration_ms']]
        song_data['popularity'] = [results['popularity']]
        
        for key, value in audio_features.items():
            song_data[key] = value
        
        return pd.DataFrame(song_data)

    """
    Get the tracks' audio feature meta data from the dataframe
    """
    def get_song_data(self, song, track_data):
        # Get the audio feature meta data from the dataframe
        try:
            song_data = track_data[(track_data['name'] == song['name']) 
                                    & (track_data['year'] == song['year'])].iloc[0]
            return song_data
        # If the track data does not exist, search from spotify
        except IndexError:
            return self.find_song(song['name'], song['year'])

    """
    Calculate the average vectors of each track
    """
    def get_mean_vector(self, song_list, track_data):
        song_vectors = []
        for song in song_list:
            # Retrieve aduio features of the input track
            song_data = self.get_song_data(song, track_data)
            if song_data is None:
                print('Warning: {} does not exist in Spotify or in database'.format(song['name']))
                continue
            song_vector = song_data[self.number_cols].values
            song_vectors.append(song_vector)  
        
        song_matrix = np.array(list(song_vectors))
        return np.mean(song_matrix, axis=0)
    
    def flatten_dict_list(self, dict_list):
    
        flattened_dict = defaultdict()
        for key in dict_list[0].keys():
            flattened_dict[key] = []
        
        for dictionary in dict_list:
            for key, value in dictionary.items():
                flattened_dict[key].append(value)
                
        return flattened_dict

    def recommend_songs(self, song_list, track_data, n_songs=10):
    
        metadata_cols = ['name', 'year', 'artists']
        song_dict = self.flatten_dict_list(song_list)        
        song_center = self.get_mean_vector(song_list, track_data)
        scaler = self.cluster().steps[0][1]     # song cluster pipeline
        scaled_data = scaler.transform(track_data[self.number_cols])
        scaled_song_center = scaler.transform(song_center.reshape(1, -1))
        distances = cdist(scaled_song_center, scaled_data, 'cosine')
        index = list(np.argsort(distances)[:, :n_songs][0])
        
        rec_songs = track_data.iloc[index]
        rec_songs = rec_songs[~rec_songs['name'].isin(song_dict['name'])]
        return rec_songs[metadata_cols].to_dict(orient='records')
        

