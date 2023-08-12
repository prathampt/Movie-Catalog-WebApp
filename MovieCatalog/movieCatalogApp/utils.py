import requests

def fetch_movie_from_omdb(movie_title=None):
    if movie_title==None:
        endpoint = "http://www.omdbapi.com/?i=tt3896198&apikey=d2837683"
    else:
        endpoint = f"http://www.omdbapi.com/?i=tt3896198&apikey=d2837683&t={movie_title}"

    response = requests.get(endpoint)
    
    if response.status_code == 200:
        movie_data = response.json()

        title = movie_data['Title']
        genre = movie_data['Genre']
        rating = float(movie_data['imdbRating'])
        release_date = movie_data['Released']
        description = movie_data['Plot']
        director = movie_data['Director']
        duration_minutes = int(movie_data['Runtime'].split()[0])
        
        if response.status_code == 200:
            movie_data = response.json()
            context = {
                'title': movie_data['Title'],
                'genre': movie_data['Genre'],
                'rating': float(movie_data['imdbRating']),
                'release_date': movie_data['Released'],
                'description': movie_data['Plot'],
                'director': movie_data['Director'],
                'duration_minutes': int(movie_data['Runtime'].split()[0]),
            }
        else:
            context = None
            context = {
                'error_message': 'Error fetching movie data from OMDb.',
            }
    else:
        context = None
        print("Error fetching movie data from OMDb.")

    return context
