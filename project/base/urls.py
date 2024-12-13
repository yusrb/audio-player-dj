from django.urls import path
from .views import (
  UserLoginView,
  UserRegisterView,
  UserLogoutView,

  daftar_artis,
  profil_artis,
  tambah_artis,
  edit_artis,
  hapus_artis,

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

  daftar_genre,
  detail_genre,
  tambah_genre,
  edit_genre,
  hapus_genre,

  daftar_playlist,
  detail_playlist,
  tambah_playlist,
  edit_playlist,
  hapus_playlist,
  tambah_lagu_on_playlist,
  hapus_lagu_on_playlist,
)

urlpatterns = [
  path('auth/login', UserLoginView.as_view(), name="user_login"),
  path('auth/register', UserRegisterView.as_view(), name="user_register"),
  path('auth/logout', UserLogoutView.as_view(), name="user_logout"),

  path('profil', daftar_artis, name="daftar_artis"),
  path('profil/<int:pk>', profil_artis, name="profil_artis"),
  path('profil/tambah', tambah_artis, name="tambah_artis"),
  path('profil/edit/<int:pk>', edit_artis, name="edit_artis"),
  path('profil/hapus/<int:pk>', hapus_artis, name="hapus_artis"),

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

  path('genre', daftar_genre, name="daftar_genre"),
  path('genre/detail/<int:pk>', detail_genre, name="detail_genre"),
  path('genre/tambah', tambah_genre, name="tambah_genre"),
  path('genre/edit/<int:pk>', edit_genre, name="edit_genre"),
  path('genre/hapus/<int:pk>', hapus_genre, name="hapus_genre"),

  path('playlist/', daftar_playlist, name="daftar_playlist"),
  path('playlist/detail/<int:pk>', detail_playlist, name="detail_playlist"),
  path('playlist/tambah', tambah_playlist, name="tambah_playlist"),
  path('playlist/edit/<int:pk>' , edit_playlist, name="edit_playlist"),
  path('playlist/hapus/<int:pk>' , hapus_playlist, name="hapus_playlist"),
  path('playlist/<int:playlist_id>/tambah/', tambah_lagu_on_playlist, name="tambah_lagu_on_playlist"),
  path('playlist/<int:playlist_id>/hapus/<int:lagu_id>/', hapus_lagu_on_playlist, name="hapus_lagu_on_playlist"),
]