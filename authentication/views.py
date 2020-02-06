from django.shortcuts import render
from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpResponseRedirect 
from .models import Student , Professor
from django.db import connection
from django.views import generic
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib.auth.models import Permission, User
from django.conf import settings
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password


def index(request):
    return render(request, "authentication/home.html")

def signup(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        gender= request.POST.get('gender')
        acheivement = request.POST.get('acheivement')
        stream = request.POST.get('stream')
        contact_number = request.POST.get('contact_number')
        url = request.POST.get('url')
        sign_up_pswd = make_password(request.POST.get('password'))
        # sign_up = sign_up.save(commit = False)
        # sign_up.status = 1
        user = User(username = name ,password= sign_up_pswd)
        user.save()
        if(request.POST.get("accounttype")=="professor"):
            obj = Professor(name= name , email = email , username= user , acheivements =acheivement, stream=stream , contact_number= contact_number , url=url)
            obj.save()
            return redirect('index')
        else:
            obj = Student(name= name , email = email , username= user , acheivements =acheivement, stream=stream , contact_number= contact_number , url=url)
            obj.save()
            return redirect('index')
    else:
        return render(request,"authentication/register.html")

def signin(request):
    if request.method=="POST":
        un= request.POST.get("username")
        pw = request.POST.get("password")
        user = authenticate(request, username=un, password=pw)
        if  user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request,"authentication/login.html" ,{'msg': "wrong password/username"})
    else:
        return render(request , "authentication/login.html",{'msg': "." })

def dashboard(request):
    try:
        obj = Student.objects.get(name = request.user.username)
        return render(request , "authentication/dashboard.html" , {'accounttype':'student','user':obj} )
    except Student.DoesNotExist:
        obj = Professor.objects.get(name = request.user.username)
        return render(request , "authentication/dashboard.html" , {'accounttype':'professor','user':obj} )
    # else:
    #     return render(request , "dashboard.html" , {'accounttype':'student','user':obj} )

def edit(request):
    try:
        obj = Student.objects.get(name = request.user.username)
    except Student.DoesNotExist:
        obj = Professor.objects.get(name = request.user.username)
    
    if(request.method=="POST"):    
        obj.email=request.POST.get('email')
        obj.acheivement = request.POST.get('acheivement')
        obj.stream = request.POST.get('stream')
        obj.contact_number = request.POST.get('contact_number')
        # obj.url = request.POST.get('url')
        obj.save()
        return redirect('dashboard')
    else:
        return render(request,"authentication/dashboard.html" ,{'user':obj})
    
def status(request):
    return redirect('index') 

def logoutView(request):
    logout(request)
    return redirect('index')

def ratings(request):
    return redirect('index')