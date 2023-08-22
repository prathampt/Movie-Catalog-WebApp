from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    release_date = models.CharField(max_length=50)
    description = models.TextField()
    director = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    trailer_url = models.URLField(default=None)
    cover_image = models.URLField(default=None)

    def __str__(self):
        return f"{self.title} {self.rating}/10"

class UserBookmark(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')])
    comments = models.TextField(blank=True)
    bookmarked_at = models.DateTimeField(auto_now_add=True)
    watched = models.BooleanField(default=False)
    watched_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.movie} is bookmarked by {self.user}"
