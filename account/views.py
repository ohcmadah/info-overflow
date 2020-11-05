from django.shortcuts import render
from .forms import UserCreationForm
from .models import UserManager

# SIGN UP
def signup(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            UserManager.create_user(user)
