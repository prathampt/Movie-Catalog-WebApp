import requests
from . import models

def fetch_movie_from_omdb(movie_title):
    endpoint = f"http://www.omdbapi.com/?apikey=d2837683&t={movie_title}"

    response = requests.get(endpoint)
        
    if response.status_code == 200:
        movie_data = response.json()
        if movie_data['Response'] == "True":
            try:
                context = {
                    'title': movie_data['Title'],
                    'genre': movie_data['Genre'],
                    'rating': float(movie_data['imdbRating']),
                    'release_date': movie_data['Released'],
                    'description': movie_data['Plot'],
                    'director': movie_data['Director'],
                    'duration_minutes': int(movie_data['Runtime'].split()[0]),
                    'cover_image': movie_data['Poster'],
                    'trailer_url': movie_data['Website']
                }
            except Exception as e:
                context = {
            'error_message': 'Movie is not availabe on server right now.'
        }
        else:
            context = {
            'error_message': 'Movie is not availabe on server right now.'
        }
    else:
        context = {
            'error_message': 'Error fetching movie data from OMDb.'
        }

    return context

def store_movie_to_db(context):
    movie = models.Movie.objects.create(
            title=context["title"],
            genre=context["genre"],
            rating=context["rating"],
            release_date=context["release_date"],
            description=context["description"],
            director=context["director"],
            duration_minutes=context["duration_minutes"],
            cover_image=context["cover_image"],
            trailer_url=context["trailer_url"]
        )
    return True
