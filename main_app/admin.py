from django.contrib import admin
from .models import User, Song, ProfileSong, Genre, ProfileGenre


admin.site.register(User)
admin.site.register(Song)
admin.site.register(ProfileSong)
admin.site.register(Genre)
admin.site.register(ProfileGenre)

