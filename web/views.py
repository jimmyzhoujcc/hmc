# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from web.models import *

# Create your views here.
def index(request):

	#return render_to_response('index.html',{'login_user': request.user})
    return render_to_response('index.html')