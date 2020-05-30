from django.shortcuts import render,redirect
# from django.contrib.auth.forms
from .forms import makeLogin, makeSignup
from django.contrib.auth import login, authenticate, logout #장고 지원 로그인/로그아웃/회원가입 


# Create your views here.

def loginView(request):
    if request.method == "POST":
        inputForm = customModel(request = request , data = request.POST)
        if inputForm.is_valid():
            user_id = inputForm.cleaned_data['username']
            user_pw = inputForm.cleaned_data['password']
            User = authenticate(request = request, username = user_id, password = user_pw) #? 왜 login이 아니라 authenticate 메소드 사용????
            if User is not None:
                login(request, User)
                return redirect('loginPage')

    else :
        newForm = customModel()
        return render (request, 'account.html', {'newForm' : newForm})

def logoutView(request):
    logout(request)
    return redirect('home') #home html 아직 안만듬.

def signupView(request):
    if request.method == "POST":
        inputForm = makeSignup(request.POST)
        user = inputForm.save()
    else:
        newForm = makeSignup()
        return render(request, 'account.html' , {'newForm':newForm})



