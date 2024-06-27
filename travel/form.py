from django.forms import ModelForm
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django import forms


class Signupform(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'username', 'email', 'password1', 'password2')

class EditUser(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'username', 'email', 'profile')