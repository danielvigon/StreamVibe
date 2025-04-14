from django.shortcuts import render
from system.models import Movie

def list_movies(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies,
    }
    return render (request, 'movie/list-movies.html', context)