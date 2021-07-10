from django.shortcuts import render
from django.http import HttpResponse
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

# Home Page
# Processing CRUD Requests & routing
def index(request):
    if request.method == 'GET':
        # artist_name = []
        # track_name = []
        # popularity = []
        # track_id = []
        # for i in range(0,10000,50):
        #     track_results = sp.search(q='year:2018', type='track', limit=50,offset=i)
        #     for i, t in enumerate(track_results['tracks']['items']):
        #         artist_name.append(t['artists'][0]['name'])
        #         track_name.append(t['name'])
        #         track_id.append(t['id'])
        #         popularity.append(t['popularity'])
        # print(artist_name)

        return render(request, 'recommender/index.html', 
            # {
            #     'data': data
            # }
        
        )
    elif request.method == 'POST':
        return render(request, 'recommender/index.html', 
            # {
            #     'data': data
            # }
        
        )

# Final Recommendation Pages
# Front end rendering with result data
def detail(request):
    return render(request, 'recommender/index.html', 
        # {
        #     'data': data
        # }
    
    )