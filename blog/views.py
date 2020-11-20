from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Post, Comment
from .forms import PostForm, CommentForm


def post_list(request):
    if request.method == "GET":
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        if request.path == "/popular/":
            posts = Post.objects.annotate(comment_count=Count('comments')).order_by('comment_count')
        elif request.path == "/software/":
            posts = posts.filter(category='Software')
        elif request.path == "/websolution/":
            posts = posts.filter(category='Web Solution')
        elif request.path == "/design/":
            posts = posts.filter(category='Design')
        elif request.path == "/other/":
            posts = posts.filter(category='Other')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_software_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category='Software').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_websolution_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category='Web Solution').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_design_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category='Design').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_other_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), category='Other').order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.publish()
            comment.save()
            return redirect('blog:post_detail', pk=post.pk)

    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.publish()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return  render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog:post_list')

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('blog:post_detail', pk=comment.post.pk)

@login_required
def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.publish()
            comment.save()
            return redirect('blog:post_detail', pk=comment.post.pk)

    return render(request, 'blog/post_detail.html', {'post': comment.post})
