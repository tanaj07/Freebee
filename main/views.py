from multiprocessing import context
from re import M
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, '/Users/tanajkhanuja/Desktop/bee/main/templates/main/index.html')
    
def signup(request):
    if request.method == "POST":
        
    

     fname = request.POST['fname']
     lname = request.POST['lname']
     email = request.POST['email']
     pass1 = request.POST['pass1']
     pass2 = request.POST['pass2']



    context = {}
    return render(request, '/Users/tanajkhanuja/Desktop/bee/main/templates/main/Signup.html', context)

def login(request):
    context = {}
    return render(request, '/Users/tanajkhanuja/Desktop/bee/main/templates/main/login.html' , context)

def logout(request):
    pass

def market(request):
    context = {}
    return render(request,'/Users/tanajkhanuja/Desktop/bee/main/templates/main/marketplace.html', context)