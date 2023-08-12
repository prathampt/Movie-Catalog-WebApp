from django.shortcuts import render
from . import utils

def index(request):
    return render(request, 'movieCatalogApp/index.html', {
        "movie" : utils.fetch_movie_from_omdb() # take movies from db
    })

def profile(request):
    return render(request, 'movieCatalogApp/profile.html')
