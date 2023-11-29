from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, CustomUserCreationForm, LoginForm ,ProfileForm
from django.contrib.auth.forms import AuthenticationForm

# cloud_journey/src/pets/views.py
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from books.models import Book,Profile
from .forms import BookForm,ProfileForm

# for deploying atuomate  code-------------------------------------------------
import os
import git
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def update(request):
    if request.method == "POST":
        repo = git.Repo("ashrafabir.pythonanywhere.com/")
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")


@csrf_exempt
def touch_wsgi(request):
    wsgi_file = "/var/www/ashrafabir_pythonanywhere_com_wsgi.py"
    os.utime(wsgi_file, None)
    return HttpResponse("Reload triggered")


# ---------------------------------------------------------------------------


class BooksListView(ListView):
    model = Book
    template_name = "index.html"  # Make sure to specify the template name
    context_object_name = (
        "book_list"  # Specify the context variable name to be used in the template
    )


# Create your views here.
# Home page
def index(request):
    return render(request, "index.html")


# signup page

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')  # Replace 'index' with your desired URL
    else:
        form = CustomUserCreationForm()
        profile_form = ProfileForm()
    return render(request, 'signup.html', {'form': form, 'profile_form': profile_form})

# login page
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(
                    "index"
                )  # Replace 'home' with the URL name of your home page
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


# logout page
def user_logout(request):
    logout(request)
    return redirect("login")


# ----------------for adding books---------------------------
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")  # Redirect to the user profile page
    else:
        form = BookForm()
    return render(request, "add_book.html", {"form": form})


# ------------------------------------------------------------------
# ----------------for updating books---------------------------
def update_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("index")  # Redirect to the user profile page
    else:
        form = BookForm(instance=book)
    return render(request, "update_book.html", {"form": form, "book": book})


# -----------------------------------------------------------------------


# for deleting books from the list Book model----------------------
def delete_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return redirect("index")


# ------------------------------------------------------------
