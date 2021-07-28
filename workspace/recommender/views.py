from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import sys
import os
import json
import re
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
import spotify

# Genre kinds
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


# Song Page Auto Completion Reload
def reload(request):
    if request.method == 'POST':
        # keyword for search
        keyword = request.body.decode("UTF-8")
        emptyList = [{}]
        searchedTracks = json.dumps(spotify.searchTrack(
            keyword)) if keyword != "" else emptyList

        return HttpResponse(searchedTracks)

# Result Page


def result(request):
    if request.method == 'POST':
        recType = request.POST.get('rec-kind')  # 'by-genre' or 'by-song'

        if recType == "by-genre":  # came from 'recommender/by-genre/'
            tile = request.POST.get('genre').lower()
            data = spotify.getPlaylist(tile)
            return render(request, 'recommender/result.html', 
                {
                    'recType': recType,
                    'title': tile,
                    'data': data,
                }
            )
          
        if recType == "by-song":
            rawUserSongs = request.POST.get('trackToSend')
            userSongs = re.sub("},{", "}~{", rawUserSongs).split("~")
            for i in range(len(userSongs)):
                userSongs[i] = json.loads(userSongs[i])

            # access to the data like
            track_ids = [userSongs[0]['songId'], userSongs[1]['songId'], userSongs[2]['songId']]
            data = spotify.getRecommendation(track_ids)
            return render(request, 'recommender/result.html', 
                {
                    'recType': recType,
                    'title' : 'Recommendations',
                    'data': data, 
                }
            )
        
        
        
