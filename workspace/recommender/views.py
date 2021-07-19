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
    for i in range(13):
        songLink = raw['tracks']['items'][i]['track']['external_urls']['spotify']
        songImage = raw['tracks']['items'][i]['track']['album']['images'][0]['url']
        songName = raw['tracks']['items'][i]['track']['name']
        albumName = raw['tracks']['items'][i]['track']['album']['name']
        artistName = raw['tracks']['items'][i]['track']['artists'][0]['name']
        songLength = raw['tracks']['items'][i]['track']['duration_ms'] / 60000
        data.append({'songName': songName, 'albumName': albumName, 'artistName': artistName, 'image': songImage, 'link': songLink, 'duration': songLength})
    return data

genre = ['chill', 'pop', 'sleep', 'workout', 'party', 'summer', 'holidays', 'classical', 'ambient']
genre_dict = {}
for i in genre:
    genre_dict[i] = 'web/images/{}.jpg'.format(i)


# Home Page
def index(request):
    if request.method == 'GET':
        return render(request, 'recommender/index.html',
            {
            }
        )

# Genre Page
def byGenre(request):
    if request.method == 'GET':
        return render(request, 'recommender/genre.html', 
            {
                'genre_dict': genre_dict,
                'genre': genre,
            }
        )

# Song Page
def bySong(request):
    if request.method == 'GET':
        return render(request, 'recommender/song.html')
    if request.method == 'POST':
        # keyword for search
        test = request.POST.get('search') 

        return render(request, 'recommender/song.html',
            {
                # return search auto completion playlist, 
                # just like genre json structure
                'autocompletionList': test,
            }
        )

# Result Page
def result(request):
    if request.method == 'POST':
        #if(request.POST.get('rec-kind')){
        recType = request.POST.get('rec-kind') # 'by-genre' or 'by-song'
        tile = request.POST.get('genre').lower()
        data = getPlaylist(tile)
        return render(request, 'recommender/result.html', 
            {
                'recType': recType,
                'genre': tile,
                'data': data,
            }
        )
