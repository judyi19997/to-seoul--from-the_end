from django.urls import path,include
from . import views

urlpatterns = [
    path('loginPage', views.loginView, name = "loginPage"),
    path('logoutPage', views.logoutView, name = 'logoutPage'),
    path('signupPage', views.signupView, name = 'signupPage'),
]