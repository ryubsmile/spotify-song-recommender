from django.db import models

"""
Spotify Tracks data
valence,year,acousticness,artists,danceability,duration_ms,energy,explicit,id,instrumentalness,key,liveness,loudness,mode,name,popularity,release_date,speechiness,tempo

"""
class Tracks(models.Model):
    #app_label  = 'tracks'

    valence = models.FloatField(default=0)
    year = models.IntegerField(default=0)
    acousticness = models.FloatField(default=0)
    artists = models.CharField(default = '', max_length = 200)
    danceability = models.FloatField(default=0)
    duration_ms = models.FloatField(default=0)
    energy = models.FloatField(default=0)
    explicit = models.IntegerField(default=0)
    track_id = models.CharField(default = '', max_length = 200)
    instrumentalness = models.FloatField(default=0)
    key = models.IntegerField(default=0)
    liveness = models.FloatField(default=0)
    loudness = models.FloatField(default=0)
    mode = models.IntegerField(default=0)
    name = models.CharField(default = '', max_length = 200)
    popularity = models.IntegerField(default=0)
    release_date = models.IntegerField(default=0)
    speechiness = models.FloatField(default=0)
    tempo = models.FloatField(default=0)

    # # Get Track info API
    # track_id = models.CharField(default = '', max_length = 200)
    # artists = models.CharField(default = '', max_length = 200)
    # year = models.IntegerField(default=0)
    # popularity = models.IntegerField(default=0)
    # release_date = models.IntegerField(default=0)
    
    # # Get audio_features API
    # acousticness = models.FloatField(default=0)
    # danceability = models.FloatField(default=0)
    # duration_ms = models.FloatField(default=0)
    # energy = models.FloatField(default=0)
    # instrumentalness = models.FloatField(default=0)
    # liveness = models.FloatField(default=0)
    # loudness = models.FloatField(default=0)
    # valence = models.FloatField(default=0)
    # speechiness = models.FloatField(default=0)
    # tempo = models.FloatField(default=0)
    # key = models.IntegerField(default=0)
    # mode = models.IntegerField(default=0)
    # # Added
    # explicit = models.IntegerField(default=0)
    # track_name = models.CharField(default = '', max_length = 200)