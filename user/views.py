from django.shortcuts import redirect, render
from user.forms import UserForm

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = UserForm()
    return render(request, 'user-register.html', {'form': form})

def login_user(request):
    return render(request, 'user-login.html')