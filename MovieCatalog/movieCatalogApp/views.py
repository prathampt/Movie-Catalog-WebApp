from django.shortcuts import render
from django import forms
from . import utils, models
from django.http import HttpResponse
from django.db.models import Q

class form(forms.Form):
    movie = forms.CharField(max_length=100)

def index(request):
    genres_mixed = models.Movie.objects.values_list('genre', flat=True).distinct()
    genres = []
    for each in genres_mixed:
        for element in each.split(', '):
            genres.append(element)
    genres = set(genres)

    sorting_options = [
        ('-rating', 'Top Rated'),
        ('release_date', 'Release Date'),
    ]

    genre = request.GET.get('genre')
    sort_option = request.GET.get('sort', '-rating')

    filtered_movies = models.Movie.objects.all()
    if genre:
        filtered_movies = filtered_movies.filter(genre__icontains=genre)

    movies = filtered_movies.order_by(sort_option)

    if sort_option=='release_date':
        sorting_options = sorting_options[::-1]

    return render(request, 'movieCatalogApp/index.html', {
        "movies" : movies[:20],
        'genres': genres,
        'genre': genre,
        'sorting_options': sorting_options
    })

def profile(request):
    return render(request, 'movieCatalogApp/profile.html')
    
def search(request, movie_title):
    movie = None
    split = movie_title.strip().split(" ")

    query = Q()
    for name in split:
        query |= Q(title__icontains=name)

    movie = models.Movie.objects.filter(query).first()
        
    if movie == None:
        movie = utils.fetch_movie_from_omdb(movie_title)
        error = movie.get('error_message')
        if error == None:
            utils.store_movie_to_db(movie)
        else:
            return HttpResponse(error)


    return render(request, 'movieCatalogApp/movie.html', {
        "movie" : movie
        })
    
def searchBox(request):
    if request.method == 'POST':
        movie = form(request.POST)
        if movie.is_valid():
            movie_title = request.POST['movie']
    return search(request, movie_title)