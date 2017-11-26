from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    online = models.BooleanField()
    sessionid = models.IntegerField(unique=True)
    usertype = models.CharField(max_length=255)


class Session(models.Model):
    sessionid = models.IntegerField(unique=True)
    topic = models.CharField(max_length=255)
    roomid = models.IntegerField(unique=True)
    courseid = models.IntegerField(unique=True)
    

class Room(models.Model):
    roomid = models.IntegerField(unique=True)
    roomnumber = models.IntegerField()
    building = models.CharField(max_length=255)


class Course(models.Model):
    courseid = models.IntegerField(unique=True)
    coursename = models.CharField(max_length=255)
    coursesubject = models.CharField(max_length=255)
    coursenum = models.IntegerField()
    sectionnum = models.IntegerField()
    
