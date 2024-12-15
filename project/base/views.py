import os
import random
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import (
  ProfilArtis,
  Lagu,
  Genre,
  Album,
  Playlist,
)
from .forms import (
  ArtisProfilForm,
  LaguForm,
  GenreForm,
  AlbumForm,
  PlaylistForm,
  AlbumForm,
  GenreForm,
)

class UserLoginView(LoginView):
  model = User
  template_name = "base/Auth/user_login.html"

  def get_success_url(self):
    return reverse_lazy('base:daftar_lagu')

class UserRegisterView(CreateView):
  model = User
  template_name = "base/Auth/user_register.html"
  form_class = UserCreationForm

  def get_success_url(self):
    return reverse_lazy('base:user_login')

class UserLogoutView(LogoutView):
  model = User

  def get_success_url(self):
    return reverse_lazy('base:user_login')

@login_required
def daftar_artis(request):
    all_artis = ProfilArtis.objects.all()

    search_query = request.GET.get('q')

    if search_query:
        all_artis = all_artis.filter(Q(nama__icontains=search_query))

    paginator = Paginator(all_artis, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if not search_query:
        all_artis = random.sample(list(page_obj.object_list), min(len(page_obj.object_list), 10))
        page_obj.object_list = all_artis

    context = {
        'artists': page_obj.object_list,
        'page_obj': page_obj,
    }

    return render(request, 'base/Artis/daftar_artis.html', context)

@login_required
def profil_artis(request, pk):
  get_artis = ProfilArtis.objects.get(pk=pk)
  all_lagu = get_artis.lagu_set.all()
  all_album = get_artis.album_set.all()

  context = {
    'artis': get_artis,
    'all_lagu': all_lagu,
    'all_album': all_album,
  }

  return render(request, 'base/Artis/detail_artis.html', context)

@login_required
def tambah_artis(request):
  if request.method == 'POST':
    form = ArtisProfilForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('base:daftar_lagu')
  else:
    form = ArtisProfilForm()

  context = {
    'form': form
  }

  return render(request, 'base/Artis/tambah_artis.html', context)

@login_required
def edit_artis(request, pk):
  edit_artis = ProfilArtis.objects.get(pk=pk)
  if request.method == 'POST':
    form = ArtisProfilForm(request.POST, request.FILES, instance=edit_artis)
    if form.is_valid():
      form.save()
      return redirect('base:daftar_lagu')
  else:
    form = ArtisProfilForm(instance=edit_artis)

  context = {
    'form': form,
  }

  return render(request, 'base/Artis/edit_artis.html', context)

@login_required
def hapus_artis(request, pk):
  get_artis = ProfilArtis.objects.get(pk=pk)

  if request.method == 'POST':
    get_artis.delete()
    return redirect('base:daftar_lagu')

  return render(request, 'base/Artis/daftar_artis.html')

@login_required
def daftar_lagu(request):
    all_lagu = Lagu.objects.all()
    search_query = request.GET.get('q')

    if search_query:
        all_lagu = all_lagu.filter(Q(judul__icontains=search_query))

    paginator = Paginator(all_lagu, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if not search_query:
        all_lagu = random.sample(list(page_obj.object_list), min(len(page_obj.object_list), 10))
        page_obj.object_list = all_lagu

    context = {
        'lagus': page_obj.object_list,
        'page_obj': page_obj,
        'search_query': search_query,
    }

    return render(request, 'base/Lagu/daftar_lagu.html', context)

@login_required
def detail_lagu(request, pk):
    get_lagu = Lagu.objects.get(pk=pk)
    another_lagu = Lagu.objects.exclude(pk=get_lagu.pk).filter(genre=get_lagu.genre)

    another_lagu = random.sample(list(another_lagu), min(len(another_lagu), 20))

    lirik = None

    try:
        lagu = Lagu.objects.get(id=get_lagu.id)

        lirik = None
        if lagu.lirik_file:
            with open(lagu.lirik_file.path, 'r', encoding='utf-8') as file:
                lirik = []
                for line in file:
                    if ']' in line:

                        timestamp = line.split(']')[0][1:]
                        lyric_text = line.split(']')[1].strip()
                        lirik.append({
                            'timestamp': timestamp,
                            'text': lyric_text
                        })

        return render(request, 'base/Lagu/detail_lagu.html', {
            'lagu': lagu,
            'lirik': lirik,
            'another_lagus': another_lagu
        })
    except Lagu.DoesNotExist:
        raise Http404("Lagu tidak ditemukan")

    context = {
        'lagu': get_lagu,
        'another_lagus': another_lagu,
        'lirik': lirik,
    }

    return render(request, 'base/Lagu/detail_lagu.html', context)

@login_required
def tambah_lagu(request):
  if request.method == 'POST':
    form = LaguForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('base:daftar_lagu')
  else:
    form = LaguForm()

  context = {
    'form': form,
  }

  return render(request, 'base/Lagu/tambah_lagu.html', context)

@login_required
def edit_lagu(request, pk):
    get_lagu = Lagu.objects.get(pk=pk)

    if request.method == 'POST':
        form = LaguForm(request.POST, request.FILES, instance=get_lagu)
        if form.is_valid():
            if 'audio_file' in request.FILES:
                if get_lagu.audio_file:
                    old_file_path = get_lagu.audio_file.path
                    if os.path.isfile(old_file_path):
                        os.remove(old_file_path)
            form.save()
            return redirect('base:daftar_lagu')
    else:
        form = LaguForm(instance=get_lagu)

    context = {
        'form': form,
        'lagu': get_lagu,
    }

    return render(request, 'base/Lagu/edit_lagu.html', context)

@login_required
def hapus_lagu(request,pk):
  get_lagu = Lagu.objects.get(pk=pk)
  if request.method == 'POST':
    get_lagu.delete()
    return redirect('base:daftar_lagu')

  return render(request, 'base/Lagu/daftar_lagu.html')

@login_required
def daftar_album(request):
  get_album = Album.objects.all()
  search_query = request.GET.get('q')

  if search_query:
      get_album = get_album.filter(
          Q(nama__icontains=search_query) |
          Q(artis__icontains=search_query)
      )
  else :
    get_album = random.sample(list(get_album), min(len(get_album), 10))

  context = {
    'albums': get_album,
  }

  return render(request, 'base/Album/daftar_album.html', context)

@login_required
def detail_album(request, pk):
  get_album = Album.objects.get(pk=pk)
  all_lagu_in_album = get_album.lagu_set.all()

  context = {
    'album': get_album,
    'all_lagu': all_lagu_in_album,
  }

  return render(request, 'base/Album/detail_album.html', context)

@login_required
def edit_album(request, pk):
  get_album = Album.objects.get(pk=pk)

  if request.method == 'POST':
    form = AlbumForm(request.POST, request.FILES, instance=get_album)
    if form.is_valid:
      form.save()
      return redirect('base:daftar_album')
  else:
    form = AlbumForm(instance=get_album)

  context = {
    'form': form,
  }

  return render(request, 'base/Album/edit_album.html', context)

@login_required
def hapus_album(request, pk):
  get_album = Album.objects.get(pk=pk)
  if request.method == 'POST':
    get_album.delete()
    return redirect('base:daftar_album')

  return render(request, 'base/Album/daftar_album.html')

@login_required
def tambah_album(request):
  if request.method == "POST":
    form = AlbumForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('base:daftar_lagu')
  else:
    form = AlbumForm()

  context = {
    'form': form
  }

  return render(request, 'base/Album/tambah_album.html', context)

@login_required
def daftar_genre(request):
  all_genre = Genre.objects.all()

  search_query = request.GET.get('q')

  if search_query:
    all_genre = all_genre.filter(
      Q(nama__icontains=search_query)
    )
  
  else:
    all_genre = random.sample(list(all_genre), min(len(all_genre), 30))

  context = {
    'genres': all_genre
  }

  return render(request, 'base/Genre/daftar_genre.html', context)

@login_required
def detail_genre(request, pk):
  get_genre = Genre.objects.get(pk=pk)
  all_lagu_with_genre = get_genre.lagu_set.all()

  all_lagu_with_genre = random.sample(list(all_lagu_with_genre), min(len(all_lagu_with_genre), 15))

  search_query = request.GET.get('q')

  if search_query:
    all_lagu_with_genre = all_lagu_with_genre.filter(
      Q(judul__icontains=search_query)
    )

  context = {
    'genre': get_genre,
    'all_lagu_with_genres': all_lagu_with_genre,
  }

  return render(request, 'base/Genre/detail_genre.html', context)

@login_required
def tambah_genre(request):
  if request.method == 'POST':
    form = GenreForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('base:daftar_genre')
  else:
    form = GenreForm()

  context = {
    'form': form
  }

  return render(request, 'base/Genre/tambah_genre.html', context)

@login_required
def edit_genre(request, pk):
  get_genre = Genre.objects.get(pk=pk)

  if request.method == 'POST':
    form = GenreForm(request.POST, instance=get_genre)
    if form.is_valid():
      form.save()
      return redirect('base:daftar_genre')
  else:
    form = GenreForm(instance=get_genre)

  context = {
    'form': form,
  }

  return render(request, 'base/Genre/edit_genre.html', context)

@login_required
def hapus_genre(request, pk):
    try:
        get_genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return redirect('base:daftar_genre')

    if request.method == 'POST':
        get_genre.delete()
        return redirect('base:daftar_genre')

    return render(request, 'base/Genre/daftar_genre.html', {'genre': get_genre})

@login_required
def daftar_playlist(request):
  all_playlist = Playlist.objects.all()

  search_query = request.GET.get('q')

  if search_query:
    all_playlist = all_playlist.filter(
      Q(nama__icontains=search_query)
    )

  context = {
    'playlists': all_playlist
  }

  return render(request, 'base/Playlist/daftar_playlist.html', context)

@login_required
def detail_playlist(request, pk):
    get_playlist = Playlist.objects.get(pk=pk)
    all_lagu = Lagu.objects.all()  # Mengambil semua lagu yang tersedia

    context = {
        'playlist': get_playlist,
        'all_lagu': all_lagu  # Mengirimkan semua lagu ke template
    }

    return render(request, 'base/Playlist/detail_playlist.html', context)

@login_required
def tambah_playlist(request):
  if request.method == 'POST':
    form = PlaylistForm(request.POST, request.FILES)
    if form.is_valid():
      playlist = form.save(commit = False)
      playlist.user = request.user
      playlist.save()
      return redirect('base:daftar_playlist')
  else:
    form = PlaylistForm()

  context = {
    'form': form
  }

  return render(request, 'base/Playlist/tambah_playlist.html', context)

@login_required
def edit_playlist(request, pk):
  get_playlist = Playlist.objects.get(pk=pk)

  if request.method == 'POST':
    form = PlaylistForm(request.POST, request.FILES, instance=get_playlist)
    if form.is_valid():
      form.save()
      return redirect('base:daftar_playlist')
  else:
    form = PlaylistForm(instance=get_playlist)

  context = {
    'form': form
  }

  return render(request, 'base/Playlist/edit_playlist.html', context)

@login_required
def hapus_playlist(request, pk):
  get_playlist = Playlist.objects.get(pk=pk)

  if request.method == 'POST':
    get_playlist.delete()
    return redirect('base:daftar_playlist')

  return render(request, 'base/Playlist/daftar_playlist.html')


@login_required
def tambah_lagu_on_playlist(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)

    if request.method == 'POST':
        lagu_id = request.POST.get('lagu')
        if lagu_id:
            lagu = Lagu.objects.get(id=lagu_id)
            playlist.lagu_set.add(lagu)

    return redirect('base:detail_playlist', pk=playlist.id)

@login_required
def hapus_lagu_on_playlist(request, playlist_id, lagu_id):
    playlist = Playlist.objects.get(id=playlist_id)
    lagu = Lagu.objects.get(id=lagu_id)
    playlist.lagu_set.remove(lagu)

    return redirect('base:detail_playlist', pk=playlist.id)
