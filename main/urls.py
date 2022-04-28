from turtle import home
from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name="index") , 
    path('signup/', views.signup, name="signup"), 
    path('login/', views.login, name="login" ), 
    path('marketplace/', views.market , name="marketplace" ) , 
    path('pricing/', views.Pricing , name="pricing") ,
    path('graphics/',views.Graphicsanddesign , name="graphicsanddesign"),
    path('business/', views.Business , name="business") ,
    path('data/', views.Data , name="Data"), 
    path('marketing/', views.Marketing, name="marketing" ),
    path('musicandaudio/', views.Musicandaudio , name="musicandaudio") ,
    path('programming/', views.Programming , name="programming") ,
    path('video/', views.video , name="video"),
    path('Writing/', views.Writing , name="writing") , 


]

