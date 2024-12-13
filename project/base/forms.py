from django import forms
from .models import (
  ProfilArtis,
  Lagu,
  Genre,
  Album,
  Playlist,
)

class ArtisProfilForm(forms.ModelForm):
  class Meta:
    model = ProfilArtis
    fields = '__all__'

class LaguForm(forms.ModelForm):
  class Meta:
    model = Lagu
    fields = ('judul','artis','album','genre','audio_img','audio_file',)

class GenreForm(forms.ModelForm):
  class Meta:
    model = Genre
    fields = '__all__'

class AlbumForm(forms.ModelForm):
  class Meta:
    model = Album
    fields = '__all__'

class PlaylistForm(forms.ModelForm):
  class Meta:
    model = Playlist
    fields = ['playlist_img','nama']

class AlbumForm(forms.ModelForm):
  class Meta:
    model = Album
    fields = '__all__'

class GenreForm(forms.ModelForm):
  class Meta:
    model = Genre
    fields = '__all__'