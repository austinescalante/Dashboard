from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# New form that inherits from the user creation form. Allows us to add another field to the form


class UserRegisterForm(UserCreationForm):
    # Inheritas from UserCreationForm, add additional fields
    email = forms.EmailField()

    # Keeps configs in one space, model affected will be User model.
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
