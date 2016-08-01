# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
#from web.models import *
import models

# Create your views here.
def login(request):
	return render_to_response('login.html')

def logout(request):
	auth.logout(request)
	return HttpResponse("<h4>You've just logged out! <a href='/login/'>click here</a> to go back to main page</h4>")


def account_login(request):
    username = request.POST['user']
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    print user, '====='
    if user is not None:  # and user.is_active:
        # correct password and user is marked "active"
        auth.login(request, user)
        return HttpResponseRedirect("/")
    else:
        return render_to_response('login.html', {'err': 'Wrong username or password!'})

def index(request):

    hosts = models.Host.objects.all()
	#return render_to_response('index.html',{'login_user': request.user})
    return render_to_response('index.html',{
        'hosts': hosts,'login_user': request.user
    })