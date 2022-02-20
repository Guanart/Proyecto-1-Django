from django.contrib import admin
from django.urls import path, include
from social.views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]
