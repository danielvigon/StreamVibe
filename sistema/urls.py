from django.urls import path
from sistema import views

# The list urlpatterns brings the

urlpatterns = [
    path('sistema/', views.index),
]