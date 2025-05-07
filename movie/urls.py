from django.urls import path
from movie import views

urlpatterns = [
    path('register/', views.register_movie, name='register_movie'),
]
