from django.urls import path
from movie import views

urlpatterns = [
    path('register/', views.register_movie, name='register_movie'),
    path('list/', views.list_movies, name='list_movies'),
]