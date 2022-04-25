from turtle import home
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name="index") , 
    path('signup/', views.signup, name="signup"), 
    path('login/', views.login, name="login" ), 
    path('marketplace/', views.market , name="marketplace" ) , 

    
]

