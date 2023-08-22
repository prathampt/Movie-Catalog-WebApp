from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from . import utils, models
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Movie, UserBookmark
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.urls import reverse


class form(forms.Form):
    movie = forms.CharField(max_length=100)

def signup(request):
    return render(request, 'movieCatalogApp/signUp.html')

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
    
def search(request, movie_title):
    start = False
    movie = None
    split = movie_title.strip().split(" ")

    query = Q()
    for name in split:
        query &= Q(title__icontains=name)

    movie = models.Movie.objects.filter(query).first()
        
    if movie == None:
        movie = utils.fetch_movie_from_omdb(movie_title)
        error = movie.get('error_message')
        if error == None:
            utils.store_movie_to_db(movie)
            start = True
        else:
            return HttpResponse(error)


    return render(request, 'movieCatalogApp/movie.html', {
        "movie" : movie,
        "start" : start
        })
    
def searchBox(request):
    if request.method == 'POST':
        movie = form(request.POST)
        if movie.is_valid():
            movie_title = request.POST['movie']
    return search(request, movie_title)

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('profile')
    else:
        form = RegistrationForm()
    
    return render(request, 'movieCatalogApp/registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'movieCatalogApp/login.html', {'form': form})

@login_required
def add_bookmark(request, movie_id=1):
    movie = get_object_or_404(Movie, pk=movie_id)
    user = request.user

    if UserBookmark.objects.filter(user=user, movie=movie).exists():
        return HttpResponseBadRequest("You have already bookmarked this movie.")

    if request.method == 'POST':
        rating = request.POST.get('rating')
        comments = request.POST.get('comments')

        user_bookmark = UserBookmark.objects.create(
            user=user, movie=movie, rating=rating, comments=comments
        )
        user_bookmark.save()
    
    search_url = reverse("search", kwargs={"movie_title": movie.title})

    return HttpResponseRedirect(search_url)

@login_required
def mark_as_watched(request, bookmark_id):
    bookmark = get_object_or_404(UserBookmark, pk=bookmark_id)

    if bookmark.user == request.user:
        bookmark.watched = True
        bookmark.watched_at = timezone.now()
        bookmark.save()

    return redirect('profile')

@login_required
def profile(request):
    user_bookmarks = UserBookmark.objects.filter(user=request.user)
    return render(request, 'movieCatalogApp/profile.html', {'user_bookmarks': user_bookmarks})

@login_required
def remove_bookmark(request, bookmark_id):
    bookmark = UserBookmark.objects.get(id=bookmark_id)
    if bookmark.user == request.user:
        bookmark.delete()
    return redirect('profile')

def add_bookmark_guest(request, movie_id):
    if not request.user.is_authenticated:
        messages.info(request, "Please register to bookmark movies.")
        return redirect('registration')
    
    return add_bookmark(request, movie_id)

def user_logout(request):
    logout(request)
    return redirect('login')