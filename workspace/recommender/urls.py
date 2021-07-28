from . import views
from django.urls import path
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


urlpatterns = [
    path('', views.index, name='index'),
    path('by-genre/', views.byGenre, name='genre'),
    path('by-song/', views.bySong, name='song'),
    path('result/', views.result, name='result'),
    path('reload/', views.reload, name='reload'),
]
