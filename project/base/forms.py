from django import forms
from .models import (
  Lagu,
  Genre,
  Album,
  Playlist,
)

class LaguForm(forms.ModelForm):
  class Meta:
    model = Lagu
    fields = '__all__'

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
    fields = '__all__'

class AlbumForm(forms.ModelForm):
  class Meta:
    model = Album
    fields = '__all__'

class GenreForm(forms.ModelForm):
  class Meta:
    model = Genre
    fields = '__all__'