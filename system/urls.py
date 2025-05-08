from django.urls import path
from system import views

# The list urlpatterns brings the

urlpatterns = [
    path('', views.index),
    path('users-list/', views.list_users, name='list_users'),
]