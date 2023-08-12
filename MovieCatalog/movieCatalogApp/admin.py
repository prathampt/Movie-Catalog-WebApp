from django.contrib import admin

from .models import Movie, UserBookmark

admin.site.register(Movie)
admin.site.register(UserBookmark)
