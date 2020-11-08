from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView
from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse_lazy

from .forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

# SIGN UP
def sign_up(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.save()

            return render(request, 'account/login.html', {'print': user.id})
        else:
            return render(request, 'account/sign_up.html', {'form': user_form})
    else:
        form = UserCreationForm()
        return render(request, 'account/sign_up.html', {'form': form})

def login(request):
    if request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']

        user = auth.authenticate(request, id=id, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            return render(request, 'account/login.html', {'error': 'id or password is incorrect.'})
    else:
        return render(request, 'account/login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'account/login.html')

def home(request):
    return render(request, 'account/index.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.info(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.info(request, 'Please correct the error below')
            return redirect('/change_password')

    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'account/change_password.html', {'form': form})


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'

class MyPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('password_reset_done')
    template_name = 'account/password_reset_form.html'
    mail_title = "비밀번호 재설정"

    def form_valid(self, form):
        return super().form_valid(form)

class MyPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('login')
    template_name = 'account/password_reset_confirm.html'

    def form_valid(self, form):
        return super().form_valid(form)

