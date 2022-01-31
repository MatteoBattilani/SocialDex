from django import forms
from django.contrib.auth.models import User
from .models import Profile

from django.contrib.auth.forms import UserCreationForm


"""
    New account's registration form. This is a subclass of UserCreationForm.
"""


class UserRegisterForm(UserCreationForm):
    # added the email field 'cause User in django doesn't have it for default
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# account's update registration form
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# Profile's update registration form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
