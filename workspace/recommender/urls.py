from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('by-genre/', views.byGenre, name='genre'),
    path('by-song/', views.bySong, name='song'),
    path('result/', views.result, name='result'),
    path('reload/', views.reload, name='reload'),
]
