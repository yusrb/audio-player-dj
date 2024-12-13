from django.db import models
from django.contrib.auth.models import User

class ProfilArtis(models.Model):
  nama = models.CharField(max_length=100)
  sampul_foto = models.ImageField(upload_to="sampul_foto")

  class Meta:
    verbose_name = "Profil Artis"
    verbose_name_plural = "Profil Artis"

  def __str__(self):
    return self.nama

class Album(models.Model):
  album_img = models.ImageField(upload_to="gambar_album/")
  nama = models.CharField(max_length=100)
  artis = models.ForeignKey(ProfilArtis, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = "Album"
    verbose_name_plural = "Album"

  def __str__(self):
    return self.nama

class Playlist(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  playlist_img = models.ImageField(upload_to="gambar_playlist")
  nama = models.CharField(max_length=100)

  class Meta:
    verbose_name= "Playlist Musik"
    verbose_name_plural = "Playlist Musik"

  def __str__(self):
    return f'{self.nama}'

class Genre(models.Model):
  nama = models.CharField(max_length=50)

  class Meta:
    verbose_name="Genre"
    verbose_name_plural="Genre"

  def __str__(self):
    return self.nama

class Lagu(models.Model):
  judul = models.CharField(max_length=150)
  artis = models.ForeignKey(ProfilArtis, on_delete=models.CASCADE)
  genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

  audio_img = models.ImageField(upload_to="gambar_audio")
  audio_file = models.FileField(upload_to="file_audio")

  album = models.ForeignKey(Album, on_delete=models.CASCADE)
  playlist = models.ManyToManyField(Playlist, blank=True)

  class Meta:
    verbose_name = "Lagu"
    verbose_name_plural = "Lagu"

  def __str__(self):
    return f'{self.judul} - {self.artis}- {self.album}'