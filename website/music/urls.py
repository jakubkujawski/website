from django.urls import path

from music import views

urlpatterns = [
    path('', views.music_home, name='music_home'),
    path('download', views.music_download, name='music_download'),
    path('favourite', views.music_favourite, name='music_favourite'),
]