from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import UserRegisterForm

# Create your views here.

def home(request):
    context = {}
    return render(request, 'social/index.html', context)

def login(request):
    if request.method == 'POST':
        form = (request.POST)
        if form.is_valid():
            form.auth()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = ()
    context = {'form': form}
    return render(request, 'social/register.html', context)

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