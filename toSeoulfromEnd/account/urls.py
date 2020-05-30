from django.urls import path,include
from . import veiws

urlpatterns = [
    path('loginPage', veiws.loginView, name = "loginPage"),
    path('logoutPage', veiws.logoutView, name = 'logoutPage'),
    path('signupPage', veiws.signupView, name = 'signupPage'),
]