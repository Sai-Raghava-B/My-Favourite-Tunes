from django.urls import path
from .views import song_list, song_detail,artist_song_count,favorite_songs,add_favorite_song,all_songs

urlpatterns = [
    path('songs/', song_list, name='song_list'),
    path('songs/<int:song_id>/', song_detail, name='song_detail'),
    path('artist-song-count/', artist_song_count, name='artist_song_count'),
    path('favorite-songs/', favorite_songs, name='favorite_songs'),
    path('add-favorite-song/<int:song_id>/', add_favorite_song, name='add_favorite_song'),
    path('all-songs/', all_songs, name='all_songs'),
]
