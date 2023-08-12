from django.shortcuts import render
from . import utils, models

def index(request):
    return render(request, 'movieCatalogApp/index.html', {
        "movies" : models.Movie.objects.all()
    })

def profile(request):
    return render(request, 'movieCatalogApp/profile.html')
    
def search(request, movie_title):
    if request.method == 'POST':
        pass

    movie = models.Movie.objects.filter(title=movie_title).first()
    if movie == None:
        movie = utils.fetch_movie_from_omdb(movie_title)
        utils.store_movie_to_db(movie)
    return render(request, 'movieCatalogApp/movie.html', {
        "movie" : movie
        })
    
    