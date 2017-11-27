from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return HttpResponse("Login screen")

def homescreen(request):
    return HttpResponse("Home screen")

def studypostcatalog(request):
    return HttpResponse("Study post catalog")

def createnewsession(request):
    return HttpResponse("Create new session screen")

def viewsessionpost(request):
    return HttpResponse("View session post screen")

def mapscreen(request):
    return HttpResponse("View session post screen")


