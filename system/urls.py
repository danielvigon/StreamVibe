from django.urls import path
from system.views import system_view
from system import views

# The list urlpatterns brings the

urlpatterns = [
    path('', views.index),
    path('list-users/', views.list_users),
    path('list-movies/', views.list_movies),
]