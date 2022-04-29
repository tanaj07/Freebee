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

def Graphicsanddesign(request):
    context = {}
    return render(request,'/Users/tanajkhanuja/Desktop/bee/main/templates/main/Graphicsanddesign.html' , context)

def Business(request):
    context = {}
    return render(request, '/Users/tanajkhanuja/Desktop/bee/main/templates/main/business.html', context)

def Data(request):
    context = {}
    return render(request, '/Users/tanajkhanuja/Desktop/bee/main/templates/main/data.html', context)

def Marketing(request):
    context = {}
    return render(request , '/Users/tanajkhanuja/Desktop/bee/main/templates/main/marketing.html', context)

def Musicandaudio(request):
    context = {}
    return render(request, '/Users/tanajkhanuja/Desktop/bee/main/templates/main/Musicandaudio.html', context)

def Programming(request):
    context = {}
    return render(request , '/Users/tanajkhanuja/Desktop/bee/main/templates/main/Programming.html', context)

def video(request):
    context = {}
    return render(request , '/Users/tanajkhanuja/Desktop/bee/main/templates/main/video.html' , context)

def Writing(request):
    context = {}
    return render(request, '/Users/tanajkhanuja/Desktop/bee/main/templates/main/writing.html', context)

def Pricing(request):
    return render(request, '/Users/tanajkhanuja/Desktop/bee/main/templates/main/pricing.html' )