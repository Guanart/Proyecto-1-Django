from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.contrib.auth.models import User
from .models import Profile, Post, Comment
from .forms import UserRegisterForm, CommentForm, CommentUpdateForm, PostForm

# Home

def search(query):
    posts = Post.objects.filter(Q(name__icontains=query) | Q(content__icontains=query)).order_by('-created')
    return posts

def paginator(request, posts):
    page = request.GET.get('page')
    try:
        paginator = Paginator(posts, 4)
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return posts, paginator

def home(request):
    context = {}
    try:
        query = request.GET.get('search')
        if query:
            posts = search(query)
        else:
            posts = Post.objects.all().order_by('-created')
    except Post.DoesNotExist:
        raise Http404('No posts')

    posts, paginador = paginator(request, posts)
    context['posts'] = posts
    context['paginator'] = paginador
    return render(request, 'social/home.html', context)

# Users and Profile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'social/register.html', context)


def profile(request, username):
    context = {}
    try:
        user_profile = Profile.objects.get(user__username=username) # Retorna una instancia
        user = User.objects.get(username=username)
        context['username'] = username
        context['profile'] = user_profile
        context['posts'] = user.posts.all()                         # Retorna un QuerySet
    except Profile.DoesNotExist:
        raise Http404(f'User "{username}" doesn\'t exists')
    
    return render(request, 'social/profile.html', context)


@login_required
def editProfile(request):
    pass


# Posts

def post_view(request, pk):
    if request.method == 'POST':    # new comment
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('post', args=(pk,)))
    else:
        context = {}
        try:
            post = Post.objects.get(pk=pk)
            context['post'] = post
            context['comments'] = post.comments.all()           # Retorna un QuerySet
            context['form'] = CommentForm()
        except Post.DoesNotExist:
            raise Http404(f'Post unavailable')

        return render(request, 'social/post.html', context)

from django.utils import timezone

@login_required
def new_post(request):
    context = {}
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)    # recibe la imagen
        if form.is_valid():                             # valida los 3 campos del formulario
            form = form.save(commit=False)              # guarda el formulario sin commit
            form.user = request.user                    # agrega el campo usuario al formulario
            form.save()                                 # commit del formulario
            return HttpResponseRedirect(reverse('home'))
    else:
        context['form'] = PostForm()
    return render(request, 'social/new_post.html', context)


@login_required
def delete_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('profile', username=request.user.username)
    except Post.DoesNotExist:
        raise Http404('Post not found')  


@login_required
def edit_post(request, pk):
    context = {}
    try:
        post = Post.objects.get(pk=pk)
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('post', args=(pk,)))
        else:
            context['form'] = PostForm(instance=post)
        return render(request, 'social/edit_post.html', context)

    except Post.DoesNotExist:
        raise Http404('Post not found')  


# Comments

@login_required
def edit_comment(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
        user = comment.user.username
        post = comment.post.id
        if request.user.username == user and request.method == 'POST':
            form = CommentUpdateForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('post', args=(post,)))
        else:
            return HttpResponse('User not valid')     
    except Comment.DoesNotExist:
        raise Http404('Comment not found')


@login_required
def delete_comment(request, pk):
    try:
        comment = Comment.objects.get(pk=pk)
        user = comment.user.username
        post = comment.post.id
        if request.user.username == user:
            comment.delete()
            return HttpResponseRedirect(reverse('post', args=(post,)))
        else:
            return HttpResponse('User not valid')     
    except Comment.DoesNotExist:
        raise Http404('Comment not found')
