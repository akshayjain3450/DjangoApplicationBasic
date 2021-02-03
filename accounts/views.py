from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import extendeduser
from django.contrib.auth.decorators import login_required
import sqlite3

def home(request):
    return render(request, 'home.html')

def successful(request):
    return render(request, 'successful.html')

def login(request):
    if request.method == 'POST':
        # check if the user exists with username and password
        uname = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(username = uname, password = pwd)
        if user is not None:
            auth.login(request, user)
            return render(request, 'successful.html')
        else:
            return render(request, 'home.html', {"error": "Invalid Login Credentials"})
    else:
        return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        # to create a user
        # check if user exists
        try:
            user = User.objects.get(username = request.POST['username'])
            return render(request, 'register.html', {'error': "Username already exists"})
        except User.DoesNotExist:
            user = User.objects.create_user(username = request.POST['username'], password = request.POST['password'])
            fullname = request.POST['fullname']
            email = request.POST['email']
            role = request.POST['role']
            newextendeduser = extendeduser(fullname = fullname, email = email, role = role, user = user)
            newextendeduser.save()
            # directly loggin in user
            auth.login(request, user)
            return redirect(home)
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect(home)

@login_required(login_url = '/login/')
def showuserdata(request):
    datas = extendeduser.objects.all()
    return render(request, "showdata.html", {'data': datas})