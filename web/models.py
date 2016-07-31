# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Host(models.Model):
    ip = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    location = models.CharField(max_length=15,blank=True,null=True)
    version = models.CharField(max_length=10,blank=True,null=True)
    comment = models.CharField(max_length=50,blank=True,null=True)
    path = models.CharField(max_length=100)
    supervisor = models.ForeignKey('Host_User')
    category = models.ForeignKey('Category')
    visible = models.BooleanField()
    create_at = models.DateTimeField()
    update_at = models.DateTimeField()

    def __unicode__(self):
        return self.ip

class Category(models.Model):
    choice = (('admin', 'Admin'), ('superuser', 'Superuser'), ('user', 'User'))
    name = models.CharField(max_length=100, choices=choice)

    def __unicode__(self):
        return self.name

class Host_User(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=10,blank=True,null=True)
    status = models.BooleanField()
    manager = models.CharField(max_length=10,blank=True,null=True)
    department = models.CharField(max_length=10,blank=True,null=True)
    comment = models.CharField(max_length=50,blank=True,null=True)

    def __unicode__(self):
        return self.user.username