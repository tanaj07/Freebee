from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, '/Users/tanajkhanuja/Desktop/bee/main/templates/main/index.html')
    
def signup(request):
    context = {}
    return render(request, '/Users/tanajkhanuja/Desktop/bee/main/templates/main/Signup.html', context)

def login(request):
    context = {}
    return render(request, '/Users/tanajkhanuja/Desktop/bee/main/templates/main/login.html' , context)

def market(request):
    context = {}
    return render(request,'/Users/tanajkhanuja/Desktop/bee/main/templates/main/marketplace.html', context)