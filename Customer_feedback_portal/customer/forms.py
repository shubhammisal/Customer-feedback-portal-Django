from cProfile import label
from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from customer.models import feedback
from django.db import models

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','password1','password2',)

class FeedBackForm(forms.ModelForm):
    class Meta:
        model=feedback
        fields="__all__"
        labels={
            "Name":"Full Name",
            "Mobile_Number":"Mobile Number",
            "feedback":"Write FeedBack"
        }
