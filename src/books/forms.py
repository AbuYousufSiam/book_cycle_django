from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Book ,Profile


# --this part is for the creation of model fields for book
# information upload in Book model.....----------------------
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


# --------------------------------------------------
class CustomUserCreationForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your first name.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your last name.')
    # address = forms.CharField(max_length=255, required=False, help_text='Required. Your address.')
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address']
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
