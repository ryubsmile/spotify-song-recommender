from django.shortcuts import render
from django.http import HttpResponse
import requests
import sys
import os
import base64
import json
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
import config

"""
Credentials for spotify api request
"""
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

def getArtistId (artist):
    """ Get ArtistId by name"""

    url = "https://api.spotify.com/v1/search?q=artist:{}&type=artist".format(artist)
    headers = get_headers(client_id, client_secret)

    r = requests.get(url, headers=headers)
    raw = json.loads(r.text)
    items = raw['artists']['items']
    artistId = items[0]['id']

    return artistId

def getArtistTopTracks(artist, country):
    artistId = getArtistId(artist)
    url = "https://api.spotify.com/v1/artists/{}/top-tracks?country={}".format(artistId, country)
    headers = get_headers(client_id, client_secret)
    r = requests.get(url, headers=headers)
    raw = json.loads(r.text)
    total = raw['tracks'][:5]
    data = []
    for i in total:
        data.append({i['name']: [{'artist': i['album']['artists'][0]['name']}, {'link': i['album']['external_urls']['spotify']}, {'image': i['album']['images'][0]['url']}]})
    return data

def getGenrePlaylist(genre):
    url = "https://api.spotify.com/v1/browse/categories/{}/playlists?limit=10".format(genre)
    headers = get_headers(client_id, client_secret)
    r = requests.get(url, headers=headers)
    raw = json.loads(r.text)
    playlistId = raw['playlists']['items'][0]['id']
    
    return playlistId

def getPlaylist(genre):
    playListId = getGenrePlaylist(genre)
    url = "https://api.spotify.com/v1/playlists/{}".format(playListId)
    headers = get_headers(client_id, client_secret)
    r = requests.get(url, headers=headers)
    raw = json.loads(r.text)
    data = []
    for i in range(9):
        songLink = raw['tracks']['items'][i]['track']['external_urls']['spotify']
        songImage = raw['tracks']['items'][i]['track']['album']['images'][0]['url']
        #songId = raw['tracks']['items'][i]['track']['album']['id']
        songName = raw['tracks']['items'][i]['track']['name']
        artistName = raw['tracks']['items'][i]['track']['artists'][0]['name']
        data.append({'songName': songName, 'artistName': artistName, 'image': songImage, 'link': songLink})
    return data

# Home Page
# Processing CRUD Requests & routing
def index(request):
    if request.method == 'GET':
        # Return categories
        genre = ['chill', 'pop', 'sleep', 'workout', "study", "summer", 'rainyday', "classical", "dance"]
        genre_kind = {'Driving song': genre[0]}
        data = getPlaylist("acoustic")
        print(data)
        return render(request, 'recommender/index.html', 
            {
                'genre': genre_kind
            }
        )
    elif request.method == 'POST':
        # Receive genre type
        return render(request, 'recommender/index.html', 
        )

# Final Recommendation Pages
# Front end rendering with result data
def result(request):
    if request.method == 'GET':
        data = getPlaylist('chill')
        return render(request, 'recommender/result.html', 
            {
                'data': data
            }
        
        )