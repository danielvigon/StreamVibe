from django.shortcuts import redirect, render
from user.forms import UserForm

# Create your views here.

def login(request):
    return render(request, 'login.html')

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/user/login/')
    else:
        form = UserForm()
        return render(request, 'register.html', {'form': form})