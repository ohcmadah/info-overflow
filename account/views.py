from django.shortcuts import render
from django.contrib.auth.models import User

# SIGN UP
def signup(request):
    if request.method == 'POST':
        for p in request.POST:
            if p != "":
                if p['password'] == p['password-check']:
                    user = User.objects.create_user(
                        username=p['name'],
                        password=p['password']

                    )
