from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Profile

# New form that inherits from the user creation form. Allows us to add another field to the form


class UserRegisterForm(UserCreationForm):
    # Inherites from UserCreationForm, add additional fields
    email = forms.EmailField()

    # Keeps configs in one space, model affected will be User model.
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    # Inherites from UserCreationForm, add additional fields
    email = forms.EmailField()

    # Keeps configs in one space, model affected will be User model.
    class Meta:
        model = User
        fields = ['username', 'email']

# create profilr form


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
