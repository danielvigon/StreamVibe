from django.db import models
from django.utils import timezone

# Create your models here.

class User (models.Model):
    name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    cpf = models.CharField(max_length = 11)
    phone_number = models.CharField(max_length = 12)
    email = models.EmailField()
    address = models.CharField(max_length = 100)
    register_date = models.DateField(default = timezone.now)
    active = models.BooleanField(default = True)
    image = models.ImageField(blank = True, upload_to = 'image/Y%/%m')

    def __str__(self):
        return f"{self.name} {self.last_name}"

class Genre(models.Model):
    name = models.CharField(max_length=50)
    register_date = models.DateField(default = timezone.now)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=50)
    release_year = models.IntegerField()
    studio = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre, on_delete = models.SET_NULL, null = True, blank = True)
    synopsis = models.TextField(max_length=500)
    register_date = models.DateField(default = timezone.now)

    def __str__(self):
        return self.name