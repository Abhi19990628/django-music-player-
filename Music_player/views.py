from django.shortcuts import render

from .models import Album,Songs

from django.core.paginator import Paginator

# Create your views here.
def home(request):
    album=Album.objects.all()
    return render(request,'home.html',{"albums":album})

def songs(request):
    album_name = request.GET.get("album")
    song_list = Songs.objects.filter(album_name_id=album_name)  # Error occurs here
    paginator = Paginator(song_list, 1)
    page_number = request.GET.get('page')
    song_page = paginator.get_page(page_number)
    
    return render(request, 'songs.html', {"song_page": song_page, "album_name": album_name})
