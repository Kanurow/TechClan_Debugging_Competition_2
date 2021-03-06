from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class CreateUserForm():
    class Meta:
        model = Users
        fields = ['username', 'email', 'password1', 'password2']

class SpecializationForm():
    class Meta:
        model = Specialization
        fields = '__all__'