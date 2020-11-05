from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import UserCreationForm
from .models import User

# SIGN UP
def sign_up(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.save()

            return redirect('/')
    else:
        form = UserCreationForm()
        return render(request, 'sign_up.html', {'form': form})

def login(request):
    if request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']

        user = auth.authenticate(request, id=id, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            return render(request, 'login.html', {'error': 'id or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')
    else:
        return render(request, 'login.html')

def home(request):
    return render(request, 'index.html')
