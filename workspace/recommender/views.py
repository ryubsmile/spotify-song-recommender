from django.shortcuts import render
from django.http import HttpResponse
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))
import spotify

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
    return render(request, 'recommender/song.html')

# Result Page
def result(request):
    if request.method == 'POST':
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
