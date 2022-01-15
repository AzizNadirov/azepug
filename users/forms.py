from django import forms
from django.conf import settings
from users.models import Profile

from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = Profile
        fields = ['user_name', 'email','password1','password2']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_name', 'email', 'image', 'about']

