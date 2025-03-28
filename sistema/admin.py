from django.contrib import admin
from sistema import models

# Register your models here.

# * user register here (optional) *
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'email', 'active',)

@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'release_year', 'studio', 'genre',)

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)