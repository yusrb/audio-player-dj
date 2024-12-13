from django.urls import path
from .views import (
  daftar_lagu,
  detail_lagu,
  tambah_lagu,
  edit_lagu,
  hapus_lagu,

  daftar_album,
  detail_album,
  tambah_album,
  edit_album,
  hapus_album,

  tambah_genre,
)

urlpatterns = [
  path('', daftar_lagu, name="daftar_lagu"),
  path('lagu/detail/<int:pk>', detail_lagu, name="detail_lagu"),
  path('lagu/tambah', tambah_lagu, name="tambah_lagu"),
  path('lagu/edit/<int:pk>', edit_lagu, name="edit_lagu"),
  path('lagu/hapus/<int:pk>', hapus_lagu, name="hapus_lagu"),

  path('album/', daftar_album, name="daftar_album"),
  path('album/detail/<int:pk>', detail_album, name="detail_album"),
  path('album/tambah', tambah_album, name="tambah_album"),
  path('album/edit/<int:pk>', edit_album, name="edit_album"),
  path('album/hapus/<int:pk>', hapus_album, name="hapus_album"),

  path('genre/tambah', tambah_genre, name="tambah_genre"),
]