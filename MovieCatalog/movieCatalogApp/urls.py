from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('movie/<str:movie_title>', views.search, name='search'),
    path('searchBox', views.searchBox, name='searchBox'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='login'),
    path('add_bookmark/<int:movie_id>/', views.add_bookmark_guest, name='add_bookmark'),
    path('mark_as_watched/<int:bookmark_id>/', views.mark_as_watched, name='mark_as_watched'),
    path('remove_bookmark/<int:bookmark_id>/', views.remove_bookmark, name='remove_bookmark')
]