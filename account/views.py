import math

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView
from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse_lazy

from blog.models import Post, Comment
from .forms import UserCreationForm, UserChangeForm
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


@login_required
def my_page(request):
    if request.method == 'POST':
        form = UserChangeForm(data=request.POST, instance=request.user)

        if form.is_valid():
            user = form.save()
            user.save()
            messages.info(request, 'Your profile was successfully updated!')
            return redirect('/my_page')
        else:
            messages.info(request, 'Please correct the error below')
            return redirect('/my_page')

    filter_posts = Post.objects.filter(user=request.user)
    posts = {}
    for post in list(filter_posts):
        date = str(post.published_date)[:7]
        if date in posts:
            posts[date].append(post)
        else:
            posts[date] = [post]

    return render(request, 'account/my_page.html', {'posts': posts, 'count': filter_posts.count(), 'grade': request.user.get_user_grade()})

@login_required
def delete_user(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('/')
    return render(request, 'account/delete_user.html')
