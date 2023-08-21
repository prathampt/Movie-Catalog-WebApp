from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('movie/<str:movie_title>', views.search, name='search'),
    path('searchBox', views.searchBox, name='searchBox'),
    path('registration/', views.registration, name='registration'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]