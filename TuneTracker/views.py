
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Song,Artist
from .forms import SongForm

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song.html', {'songs': songs})

def song_detail(request, song_id):
    song = Song.objects.get(pk=song_id)
    return render(request, 'song_detail.html', {'song': song})

def artist_song_count(request):
    artists = Artist.objects.all()
    return render(request, 'song_count.html', {'artists': artists})

@login_required
def favorite_songs(request):
    user = request.user
    songs = Song.objects.filter(user=user)
    return render(request, 'fav_song.html', {'songs': songs})

@login_required
def add_favorite_song(request, song_id):
    user = request.user
    song = Song.objects.get(pk=song_id)

    
    if not user.song_set.filter(pk=song.id).exists():
        user.song_set.add(song)

    return redirect('all_songs')  

def all_songs(request):
    songs = Song.objects.all()
    return render(request, 'all_songs.html', {'songs': songs})
