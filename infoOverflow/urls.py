from django.contrib import admin
from django.urls import path, include
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog', include('blog.urls')),

    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.sign_up, name='sign_up'),
    path('logout/', views.logout, name='logout'),

    path('change_password/', views.change_password, name='change_password'),

    path('password_reset_done/', views.MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/', views.MyPasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
