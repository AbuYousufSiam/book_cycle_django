# books/models.py
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )  # Connecting with the User model
    # Adding new attributes for user
    address = models.CharField(max_length=200)
    phone = models.PositiveBigIntegerField(null=True)

    def __str__(self):
        return str(self.user)


class Book(models.Model):
    # Adding new attributes for user
    choice_list = [
        ("Wanted", "Wanted"),
        ("Available", "Available"),
    ]
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    details = models.CharField(max_length=500, default="No description")
    genre = models.CharField(max_length=50, default="Not defined")
    language = models.CharField(max_length=20, default="Not defined")
    cover_image = models.ImageField(upload_to="book_covers/", default=0)
    pages = models.PositiveIntegerField(default=0)  # Default value set to 0
    is_available = models.CharField(max_length=20, choices=choice_list)
    user = models.CharField(max_length=50, default="Anonymous")
    upload_date = models.DateField()

    def __str__(self):
        return str(self.user)
