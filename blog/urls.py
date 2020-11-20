from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('software/', views.post_list, name='software'),
    path('websolution/', views.post_list, name='websolution'),
    path('design/', views.post_list, name='design'),
    path('other/', views.post_list, name='other'),
    path('popular/', views.post_list, name='popular'),

    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),

    path('comment/<pk>/remove/', views.comment_remove, name='comment_remove'),
    path('comment/<pk>/edit/', views.comment_edit, name='comment_edit'),
]