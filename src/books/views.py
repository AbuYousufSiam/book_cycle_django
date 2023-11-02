from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, CustomUserCreationForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm

#cloud_journey/src/pets/views.py
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from books.models import Book


class BooksListView(ListView):
    model = Book
    template_name = 'index.html'  # Make sure to specify the template name
    context_object_name = 'book_list'  # Specify the context variable name to be used in the template


# Create your views here.
# Home page
def index(request):
    return render(request, 'index.html')

# signup page
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')  # Replace 'home' with the URL name of your home page
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Replace 'home' with the URL name of your home page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')