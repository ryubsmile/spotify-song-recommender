from django.db import models

"""
Spotify Tracks data
"""
class Tracks(models.Model):
    app_label  = 'tracks'

    # Get Track info API
    track_id = models.IntegerField(default=0)
    #artist_id = models.IntegerField(default=0)
    artists = models.CharField(default = '', max_length = 200)
    year = models.IntegerField(default=0)
    popularity = models.IntegerField(default=0)
    release_date = models.IntegerField(default=0)
    
    # Get audio_features API
    acousticness = models.FloatField(default=0)
    danceability = models.FloatField(default=0)
    duration_ms = models.FloatField(default=0)
    energy = models.FloatField(default=0)
    instrumentalness = models.FloatField(default=0)
    liveness = models.FloatField(default=0)
    loudness = models.FloatField(default=0)
    valence = models.FloatField(default=0)
    speechiness = models.FloatField(default=0)
    tempo = models.FloatField(default=0)
    key = models.IntegerField(default=0)
    mode = models.IntegerField(default=0)

