from . import config
import sys
import os
import base64
import json
import requests
from recommendation import Recommendation
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

# Credentials for spotify api request
client_id = config.cid
client_secret = config.secret


def get_headers(client_id, client_secret):
    """Authorization for Spotify API request"""

    endpoint = "https://accounts.spotify.com/api/token"
    encoded = base64.b64encode("{}:{}".format(
        client_id, client_secret).encode('utf-8')).decode('ascii')

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
    url = "https://api.spotify.com/v1/browse/categories/{}/playlists?limit=10".format(
        genre)
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
    # Get 13 tracks
    for i in range(13):
        songLink = raw['tracks']['items'][i]['track']['external_urls']['spotify']
        songImage = raw['tracks']['items'][i]['track']['album']['images'][0]['url']
        songName = raw['tracks']['items'][i]['track']['name']
        albumName = raw['tracks']['items'][i]['track']['album']['name']
        artistName = raw['tracks']['items'][i]['track']['artists'][0]['name']
        songLength = raw['tracks']['items'][i]['track']['duration_ms'] / 60000
        data.append({'songName': songName, 'albumName': albumName, 'artistName': artistName,
                    'image': songImage, 'link': songLink, 'duration': songLength})
    return data

# Search a song by title


def searchTrack(search):
    url = "https://api.spotify.com/v1/search?q={}&type=track&limit=5".format(
        search)
    headers = get_headers(client_id, client_secret)
    r = requests.get(url, headers=headers)
    raw = json.loads(r.text)
    data = []
    # Get 5 tracks per search
    for i in range(5):
        songLink = raw['tracks']['items'][i]['external_urls']['spotify']
        songImage = raw['tracks']['items'][i]['album']['images'][0]['url']
        songName = raw['tracks']['items'][i]['name']
        songId = raw['tracks']['items'][i]['id']
        albumName = raw['tracks']['items'][i]['album']['name']
        artistName = raw['tracks']['items'][i]['artists'][0]['name']
        artistId = raw['tracks']['items'][i]['artists'][0]['id']
        songLength = raw['tracks']['items'][i]['duration_ms'] / 60000
        data.append({'songName': songName, 'songId': songId, 'albumName': albumName, 'artistName': artistName,
                    'artistId': artistId, 'image': songImage, 'link': songLink, 'duration': songLength})
    return data


"""
Butter
artist_id : 3Nrfpe0tUJi4K4DXYWgMUX
track_id: 2bgTY4UwhfBYhGT4HUYStN
"""

# Get Audio Features of a track


def getAudioFeatures(trackId):
    url = "https://api.spotify.com/v1/audio-features/{}".format(trackId)
    headers = get_headers(client_id, client_secret)
    r = requests.get(url, headers=headers)
    raw = json.loads(r.text)


# Get recommendation based on three songs
def getRecommendation():
    songs_data = ['2bgTY4UwhfBYhGT4HUYStN',
                  '0LThjFY2iTtNdd4wviwVV2', '7iAgNZdotu40NwtoIWJHFe']
    rec = Recommendation()
    return rec.recommend_songs(songs_data)
