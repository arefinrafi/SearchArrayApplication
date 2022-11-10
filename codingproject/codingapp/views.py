from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Khojsearch
from django.contrib.auth.models import User
from .serializers import UserSerializer, KhojsearchSerializer
from rest_framework import viewsets

# Create your views here.

# home section
def MY_ACCOUNNT_LOGIN(request):
    return render(request, 'registration/login.html')

# register section
def REGISTER(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        # print(username,email,password, password2)

        if User.objects.filter(username = username).exists():
            messages.error(request, "username already exists!!!")
            return redirect('handleregister')

        if User.objects.filter(email = email).exists():
            messages.error(request, "email already exists!!!")
            return redirect('handleregister')

        if len(password) < 8 :
            messages.error(request, "Password must be at least 8 character.")
            return redirect('handleregister')

        if password != password2:
            messages.error(request, 'Password Not Matching!!!')
            return redirect('handleregister')


        user = User(
            username = username,
            email = email,
            
        )
        user.set_password(password)
        user.save()
        return redirect('my_account_login')

    else:
        return render(request, 'registration/register.html')


# login section
def LOGIN(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
            
        else:
            messages.error(request, "username or password are invalid!!!")
            return redirect('login')

    return render(request, 'registration/login.html')


# logout section
def LOGOUT(request):
    logout(request)
    return redirect('/')


# Khoj the search serction
@login_required(login_url='login')
def HOME(request):
    if request.method == 'POST':
        user_id = User.objects.get(id=request.user.id)
        inputlist = request.POST.getlist('inputlist')
        inputitem = request.POST.get('inputitem')
        
        inputlistgetitem = inputlist[0].split(',')
        inputlistarray = sorted([int(s) for s in inputlistgetitem], reverse=True)
        print(inputlistarray)

        khoj = Khojsearch(
            user_id = user_id,
            inputlist = inputlistarray,
            
        )
        khoj.save()

        print(inputitem)

        if inputitem in inputlistgetitem:
            print("True")
            messages.success(request, "True")
        else:
            print("False")
            messages.success(request, "False")
    return render(request, 'dashboard.html')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class KhojSearchViewSet(viewsets.ModelViewSet):
    queryset = Khojsearch.objects.all()
    serializer_class = KhojsearchSerializer