from system.models import User
from django.shortcuts import render

def list_users(request):
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request, 'users/users-list.html', context)