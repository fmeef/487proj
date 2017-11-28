from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def login(request):
    template = loader.get_template('login.html')
    
    return HttpResponse(template.render( template))

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


