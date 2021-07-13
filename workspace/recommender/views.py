from django.shortcuts import render
from django.http import HttpResponse
import requests
import sys
import os
import base64
import json
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
import config

### Credentials for spotify api request
client_id = config.cid
client_secret = config.secret

def get_headers(client_id, client_secret):
    """Authorization for Spotify API request"""

    endpoint = "https://accounts.spotify.com/api/token"
    encoded = base64.b64encode("{}:{}".format(client_id, client_secret).encode('utf-8')).decode('ascii')

    headers = {
        "Authorization": "Basic {}".format(encoded)
    }

    payload = {
        "grant_type": "client_credentials"
    }

    r = requests.post(endpoint, data=payload, headers=headers)

    access_token = json.loads(r.text)['access_token']

    headers = {
        "Authorization": "Bearer {}".format(access_token)
    }
    return headers

# Get playlist Id's of a genre
def getGenrePlaylist(genre):
    url = "https://api.spotify.com/v1/browse/categories/{}/playlists?limit=10".format(genre)
    headers = get_headers(client_id, client_secret)
    r = requests.get(url, headers=headers)
    raw = json.loads(r.text)
    playlistId = raw['playlists']['items'][0]['id']
    return playlistId

# Get tracks of a playlist
def getPlaylist(genre):
    playListId = getGenrePlaylist(genre)
    url = "https://api.spotify.com/v1/playlists/{}".format(playListId)
    headers = get_headers(client_id, client_secret)
    r = requests.get(url, headers=headers)
    raw = json.loads(r.text)
    data = []
    # Get 9 tracks
    for i in range(9):
        songLink = raw['tracks']['items'][i]['track']['external_urls']['spotify']
        songImage = raw['tracks']['items'][i]['track']['album']['images'][0]['url']
        songName = raw['tracks']['items'][i]['track']['name']
        albumName = raw['tracks']['items'][i]['track']['album']['name']
        artistName = raw['tracks']['items'][i]['track']['artists'][0]['name']
        songLength = raw['tracks']['items'][i]['track']['duration_ms'] / 60000
        data.append({'songName': songName, 'albumName': albumName, 'artistName': artistName, 'image': songImage, 'link': songLink, 'duration': songLength})
    return data

genre = ['chill', 'pop', 'sleep', 'workout', "study", "summer", 'rainyday', "classical", "dance"]
genre_kind = {'Driving song': genre[0]}

# Home Page
def index(request):
    if request.method == 'GET':
        return render(request, 'recommender/index.html', 
            {
                'genre': genre
            }
        )
    elif request.method == 'POST':
        return render(request, 'recommender/index.html', 
        )

# Result Page
def result(request):
    if request.method == 'GET':
        data = getPlaylist(genre[0])
        return render(request, 'recommender/result.html', 
            {
                'data': data
            }
        
        )