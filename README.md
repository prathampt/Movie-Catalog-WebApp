# Movie-Catalog-WebApp

Welcome to the Movie Catalog Web App! This web application allows users to search and bookmark their favorite movies. Users can register, log in, search for movies, add bookmarks, and manage their profile.
This web app is made using Django.
## Features

- User registration and authentication.
- Search for movies by title.
- View detailed information about a movie.
- Add movies to bookmarks with ratings and comments.
- Mark movies as watched in the bookmarks.
- Remove movies from bookmarks.
- Sort movies by rating and release date.

## Setup

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/movie-catalog-app.git
```

2. Navigate to the project directory:

```bash
cd movie-catalog-app
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Create a new database and run migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Open a web browser and visit `http://127.0.0.1:8000/` to access the web app.

## Technologies Used

- Django: A powerful Python web framework.
- Bootstrap: A popular front-end framework for responsive design.
- OMDB API: Used for fetching movie data.
- PostgreSQL: The database used to store movie and user information.

## How to Use

1. Register an account or log in if you already have one.
2. Search for movies using the search bar on the home page.
3. Click on a movie's title to view detailed information.
4. Use the "Bookmark" button to add the movie to your bookmarks.
5. In the profile section, you can manage your bookmarks, mark movies as watched, and remove bookmarks.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to create a pull request or open an issue in the repository.
