"""iitthing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from loginpage import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.login , name='login_index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^userhome/$', views.homescreen, name='home_screen'),
    url(r'^catalog/$', views.studypostcatalog, name='catalog_screen'),
    url(r'^newsession/$', views.createnewsession, name='create_session'),
    url(r'^viewsessionpost/$', views.viewsessionpost, name='view_session'),
    url(r'^accounts/profile/$', views.homeredirect, name='home_redirect'),
    url(r'^map/$', views.mapscreen, name='map'),
    url(r'^signup/$', views.signup, name='signup'),
]
