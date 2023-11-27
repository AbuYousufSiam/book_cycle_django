# books/models.py
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    address = models.CharField(max_length=200)

    def __str__(self):
        return str(self.user)
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)
    genre = models.CharField(max_length=50, default="n")
    language = models.CharField(max_length=20, default="en")
    cover_image = models.ImageField(upload_to="book_covers/", default=0)
    pages = models.PositiveIntegerField(default=0)  # Default value set to 0
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
