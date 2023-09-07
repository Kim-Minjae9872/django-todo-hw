from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from user.models import User

# Create your views here.


def index(request):
    if request.method == "GET":
        return render(request, 'index.html')
    else:
        return HttpResponse('Invalid request method', status=405)


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        User.objects.create_user(
            username=username, password=password, email=email)
        return redirect('/user/login/')
    else:
        return HttpResponse('Invalid request method', status=405)


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/todo/')
        else:
            return HttpResponse('Invalid auth', status=401)

    elif request.method == "GET":
        return render(request, 'login.html')
