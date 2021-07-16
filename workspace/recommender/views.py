from django.shortcuts import render
from django.http import HttpResponse
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
import spotify

genre = ['chill', 'pop', 'sleep', 'workout', 'party', 'summer', 'holidays', 'classical', 'ambient']
genre_dict = {}
for i in genre:
    genre_dict[i] = 'workspace/recommender/images/{}.jpg'.format(i)

# Home Page
def index(request):
    if request.method == 'GET':
        data = spotify.getPlaylist('chill')
        print(data)
        return render(request, 'recommender/index.html', 
            {
                'genre': genre_dict
            }
        )

# Result Page
def result(request):
    if request.method == 'POST':
        tile = request.POST.get('choice').lower()
        data = spotify.getPlaylist(tile)
        return render(request, 'recommender/result.html', 
            {
                'genre': tile,
                'data': data,
                
            }
        )