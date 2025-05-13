from django.shortcuts import redirect, render
from system.models import Movie
from movie.forms import MovieForm

# Create your views here.

def register_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/list')
    else:
        form = MovieForm()
    return render(request, 'movie-register.html', {'form': form})

def list_movies(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies,
    }
    return render(request, 'movies-list.html', context)
