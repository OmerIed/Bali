from django.contrib import admin
from playlist.models import AccountSong, Song, Genre, AccountGenre

admin.site.register(Song)
admin.site.register(Genre)
admin.site.register(AccountSong)
admin.site.register(AccountGenre)
