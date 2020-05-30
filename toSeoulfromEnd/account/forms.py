from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsercreationForm #상속받을 기본 유저 Form
from django.contrib.auth import get_user_model
# from . import models

User = get_user_model

class makeLogin(AuthenticationForm):
    pass

class makeSignup(UsercreationForm):

    class Meta:
        model = User
        fields = ['username','password1', 'password2', 'email','gender','is_staff']

