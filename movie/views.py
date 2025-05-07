from django.shortcuts import redirect, render
from movie.forms import MovieForm

# Create your views here.

def register_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/list-movies/')
    else:
        form = MovieForm()
    return render(request, 'register.html', {'form': form})
