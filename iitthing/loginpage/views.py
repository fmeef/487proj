from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth import models as auth_models 
from django.contrib.auth.decorators import login_required

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
    if request.user.is_authenticated():
        return HttpResponse("Authorized")
    else:
        return HttpResponse("UNAUTHORIZED ACCESS. DISPATCHING GOONS.")

def mapscreen(request):
    return HttpResponse("View session post screen")


