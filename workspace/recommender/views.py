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
        data.append({i['name']: i['album']['external_urls']['spotify']})
    return data

# Home Page
# Processing CRUD Requests & routing
def index(request):
    if request.method == 'GET':
        data = getArtistTopTracks('BTS', 'KR')
        return render(request, 'recommender/index.html', 
            {
                'data': data
            }
        )
    elif request.method == 'POST':
        return render(request, 'recommender/index.html', 
        
        )

# Final Recommendation Pages
# Front end rendering with result data
def detail(request):
    return render(request, 'recommender/index.html', 
        # {
        #     'data': data
        # }
    
    )