import sys
import os
import pandas as pd
import numpy as np
from collections import defaultdict
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config
import sqlite3

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
        # Read in data from sqlite3 database
        self.df = self.connection()
        # Columns to use for clustering
        self.number_cols = ['valence', 'year', 'acousticness', 'danceability', 'duration_ms', 'energy', 'explicit', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'popularity', 'speechiness', 'tempo']
        # Spotify credentials request
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= config.cid,
                                                  client_secret=config.secret))

    def connection(self):
        """
        Connects to database and retrieves the data in a dataframe format
        """
        con = sqlite3.connect("db.sqlite3")
        df = pd.read_sql_query("SELECT * from recommender_tracks", con)
        df = df.drop(['id'], axis = 1)
        con.close()
        return df

    def cluster(self):
        """
        Performs cluster of the tracks data with Kmeans
        - Divide the dataset into 20 clusters based on the tracks' features
        """
        song_cluster_pipeline = Pipeline([('scaler', StandardScaler()), 
                                  ('kmeans', KMeans(n_clusters=20, 
                                   verbose=2, n_jobs=4))], verbose=True)
        # Select numerical features for training
        X = self.df.select_dtypes(np.number)
        self.number_cols = list(X.columns)
        song_cluster_pipeline.fit(X)
        song_cluster_labels = song_cluster_pipeline.predict(X)
        # Label each data with clustered result
        self.df['cluster_label'] = song_cluster_labels
        return song_cluster_pipeline

    
    def find_song(self, track_id):
        """
        Finds tracks that are not in the database and return it as a dataframe form
        """
        song_data = defaultdict()
        results = self.sp.track(track_id)
        audio_features = self.sp.audio_features(track_id)
        song_data['name'] = [results['name']]
        song_data['year'] = [int(results['album']['release_date'][0:4])]
        song_data['explicit'] = [int(results['explicit'])]
        song_data['duration_ms'] = [results['duration_ms']]
        song_data['popularity'] = [results['popularity']]
        for key, value in audio_features[0].items():
            song_data[key] = value

        # Need to add to the database as well
        
        return pd.DataFrame(song_data)

    
    def get_song_data(self, track_id, track_data):
        """
        Get the tracks' audio feature meta data from the dataframe
        """
        try:
            song_data = track_data[(track_data['track_id'] == track_id)].iloc[0]
            return song_data
        # If the track data does not exist, search from spotify
        except IndexError:
            return self.find_song(track_id)

    def get_mean_vector(self, song_list, track_data):
        """
        Calculates the mean vectors of every track
        """
        song_vectors = []
        for track_id in song_list:
            # Retrieve aduio features of the input track
            song_data = self.get_song_data(track_id, track_data)
            song_vector = song_data[self.number_cols].values
            song_vectors.append(song_vector)  
        
        song_matrix = np.array(list(song_vectors))
        return np.mean(song_matrix, axis=0)

    def song_features(self, track_id):
        data = []
        for id in track_id:
            results = self.sp.track(id)
            songName = results['name']
            songLink = results['external_urls']['spotify']
            songImage = results['images'][0]['url']
            albumName = results['album']['name']
            artistName = results['artists'][0]['name']
            artistId = results['artists'][0]['id']
            songLength = results['duration_ms'] / 60000
            data.append({'songName': songName, 'songId': songId, 'albumName': albumName, 'artistName': artistName, 'artistId': artistId, 'image': songImage, 'link': songLink, 'duration': songLength})
        return data

    def recommend_songs(self, song_list, n_songs=10):
        """
        Executes recommendation engine
        Call this function to get recommendation
        """
        # Return data features
        metadata_cols = ['name', 'year', 'artists']
        song_center = self.get_mean_vector(song_list, self.df)
        scaler = self.cluster().steps[0][1]     # song cluster pipeline
        scaled_data = scaler.transform(self.df[self.number_cols])
        scaled_song_center = scaler.transform(song_center.reshape(1, -1))
        distances = cdist(scaled_song_center, scaled_data, 'cosine')
        index = list(np.argsort(distances)[:, :n_songs][0])
        
        rec_songs = self.df.iloc[index]
        # Exclude tracks data in input
        rec_songs = rec_songs[~rec_songs['track_id'].isin(song_list)]
        return rec_songs[metadata_cols].to_dict(orient='records')
        

