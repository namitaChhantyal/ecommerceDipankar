from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from . import models
from .models import Order


class Signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # fields=['firstname','lastname','phonenumber','email','password','confirm password']


# class Orderform(Order):
#     class Meta:
#         model = Order
#         fields = '_all_'
