from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment, Profile, Post

# Users
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email']      # también agregar password

# Profile
# class ProfileUpdateForm(forms.ModelForm):
# 	class Meta:
# 		model = Profile
# 		fields = ['picture', 'description']

# Posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'content', 'picture'] 

# Comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'user', 'post']

class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
