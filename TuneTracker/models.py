from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def song_count(self):
        return Song.objects.filter(artist=self).count()

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def artist_song_count(self):
        return self.artist.song_count()