from django.shortcuts import render
from django.http import HttpResponse
import spotipy
import sys
sys.path.append('../../')
# from config import *
#from spotipy.oauth2 import SpotifyClientCredentials

#client_credentials_manager = SpotifyClientCredentials(client_id = Credentials.cid, client_secret = Credentials.secret)
#sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

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