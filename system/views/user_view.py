from django.shortcuts import render
from system.models import User

def list_users(request):
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render (request, 'user/list-users.html', context)