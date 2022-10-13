from django.contrib import admin
from django.urls import path
from example import views

 
urlpatterns = [
    
    #path("", views.register, name ='example')
    #path("", views.home, name ='example')
    #path("", views.setcookie, name ='example')
    #path("", views.getcookie, name ='example')
    path("", views.setsession, name ='example')
]