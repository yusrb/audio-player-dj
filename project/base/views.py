import os
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import (
  Lagu,
  Genre,
  Album,
  Playlist,
)
from .forms import (
  LaguForm,
  GenreForm,
  AlbumForm,
  PlaylistForm,

  AlbumForm,

  GenreForm,

)

def daftar_lagu(request):
    get_lagu = Lagu.objects.all()
    search_query = request.GET.get('q', '')
    if search_query:
        get_lagu = get_lagu.filter(
            Q(judul__icontains=search_query) |
            Q(artis__icontains=search_query)
        )
    context = {
        'lagus': get_lagu,
        'search_query': search_query
    }
    return render(request, 'base/Lagu/daftar_lagu.html', context)

def detail_lagu(request,pk):
  get_lagu = Lagu.objects.get(pk=pk)
  another_lagu = Lagu.objects.exclude(pk=get_lagu.pk).filter(genre=get_lagu.genre)

  context = {
    'lagu': get_lagu,
    'another_lagus': another_lagu
  }
  return render(request, 'base/Lagu/detail_lagu.html', context)

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

def hapus_lagu(request,pk):
  get_lagu = Lagu.objects.get(pk=pk)
  if request.method == 'POST':
    get_lagu.delete()
    return redirect('base:daftar_konten')

  return render(request, 'base/Lagu/daftar_lagu.html')

def daftar_album(request):
  get_album = Album.objects.all()
  search_query = request.GET.get('q')

  if search_query:
      get_album = get_album.filter(
          Q(nama__icontains=search_query) |
          Q(artis__icontains=search_query)
      )

  context = {
    'albums': get_album,
  }

  return render(request, 'base/Album/daftar_album.html', context)

def detail_album(request, pk):
  get_album = Album.objects.get(pk=pk)
  all_lagu_in_album = get_album.lagu_set.all()

  context = {
    'album': get_album,
    'all_lagu': all_lagu_in_album,
  }

  return render(request, 'base/Album/detail_album.html', context)

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

def hapus_album(request, pk):
  get_album = Album.objects.get(pk=pk)
  if request.method == 'POST':
    get_album.delete()
    return redirect('base:daftar_album')

  return render(request, 'base/Album/daftar_album.html')


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



def tambah_genre(request):
  if request.method == 'POST':
    form = GenreForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('base:daftar_lagu')
  else:
    form = GenreForm()

  context = {
    'form': form
  }

  return render(request, 'base/Genre/tambah_genre.html', context)