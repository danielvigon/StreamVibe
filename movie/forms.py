from django import forms
from system.models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'release_year', 'studio', 'genre', 'synopsis',]