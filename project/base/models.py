from django.db import models

class Album(models.Model):
  album_img = models.ImageField(upload_to="gambar_album/")
  nama = models.CharField(max_length=100)
  artis = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = "Album"
    verbose_name_plural = "Album"

  def __str__(self):
    return f'{self.nama} - {self.artis}'

class Playlist(models.Model):
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
  artis = models.CharField(max_length=100)
  genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

  audio_img = models.ImageField(upload_to="gambar_audio")
  audio_file = models.FileField(upload_to="file_audio")

  album = models.ForeignKey(Album, on_delete=models.CASCADE)
  playlist = models.ManyToManyField(Playlist, blank=True, null=True)

  class Meta:
    verbose_name = "Lagu"
    verbose_name_plural = "Lagu"

  def __str__(self):
    return f'{self.judul} - {self.artis}- {self.album}'