from django.shortcuts import render,HttpResponse 

def home (request):
    
    return HttpResponse("this is my first page")


