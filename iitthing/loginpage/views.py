from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth import models as auth_models 
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response

# Create your views here.

def login(request):
    return redirect('/login')

def homescreen(request):
    return HttpResponse("Home screen")

def studypostcatalog(request):
    return HttpResponse("Study post catalog")

def createnewsession(request):
    return HttpResponse("Create new session screen")

def homeredirect(request):
    if request.user.is_authenticated():
        return redirect('/viewsessionpost')
    else:
        return HttpResponse("UNAUTHORIZED ACCESS, DISPATCHING GOONS")

@csrf_protect
def viewsessionpost(request, query):
    if request.user.is_authenticated():
        sessionsview = loader.get_template('sessions.html')
        print query
        if(query != None):
            return redirect("/viewsessionpost")
        return render_to_response('sessions.html', RequestContext(request))
    else:
        return HttpResponse("UNAUTHORIZED ACCESS. DISPATCHING GOONS.")

def mapscreen(request):
    return HttpResponse("View session post screen")


