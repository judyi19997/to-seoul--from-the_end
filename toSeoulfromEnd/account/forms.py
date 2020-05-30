from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm #상속받을 기본 유저 Form
from django.contrib.auth import get_user_model
# from . import models

user = get_user_model()

class makeLogin(AuthenticationForm):
    pass

class makeSignup(UserCreationForm):

    class Meta:
        model = user
        fields = ['username','password1', 'password2', 'email','gender','is_staff','date']

