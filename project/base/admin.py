from django.contrib import admin
from .models import (
  Lagu,
  Genre,
  Album,
  Playlist,
)

@admin.register(Lagu)
class LaguAdmin(admin.ModelAdmin):
  list_display = ('judul', 'artis', 'album',)
  list_filter = ('artis', 'album',)
  exclude = ('playlist',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
  list_display = ('nama',)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
  list_display = ('nama', 'artis',)
  list_filter = ('artis',)

@admin.register(Playlist)
class Playlist(admin.ModelAdmin):
  list_display = ('nama',)