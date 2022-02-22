from django.contrib import admin
from django.urls import path, include, reverse
from social.views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home, name='home'),
    # Users
    path('login/', LoginView.as_view(template_name='social/Login.html'), name='login'), # el template por defecto es registration/login.html
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/<str:username>/', profile, name='profile'),
    # Posts
    path('post/<int:pk>/', post_view, name='post'),
    path('new-post/', new_post, name='new_post'),
    path('delete-post/<int:pk>/', delete_post, name='delete_post'),
    path('edit-post/<int:pk>/', edit_post, name='edit_post'),
    # Comments
    path('comments/edit/<int:pk>', edit_comment, name='edit_comment'),
    path('comments/delete/<int:pk>', delete_comment, name='delete_comment'),
]