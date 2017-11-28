from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth import models as auth_models 

# Create your views here.

def login(request):
    return redirect('/login')

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


