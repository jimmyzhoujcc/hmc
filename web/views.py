# -*- coding: utf-8 -*-
from django.shortcuts import render,render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
#from web.models import *
import models
import subprocess,os
import json

# Create your views here.
def pie(request):
	return render_to_response('pie.html')

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
    users = models.Host_User.objects.all()
    auth_users = models.User.objects.all()

    hid = ''
    a_value = ''
    # return render_to_response('index.html',{'login_user': request.user})
    for h in hosts:
        host_id = str(h.id)
        if 'id' + host_id in request.GET:
        #if 'id' in request.GET:
            child = subprocess.Popen(['/bin/bash', '-c', '/Users/jcc/PycharmProjects/test_shell/web/hostname.sh'],
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out = child.stdout.readlines()
            hid = h.id
            for line in out:
                print line.strip()
                a = line.strip()
                a_value = locals()

    return render_to_response('index.html', {
        'hosts': hosts, 'login_user': request.user, 'users': users, 'auth_users': auth_users, 'a': a_value, 'hid': hid
    #return render_to_response('index.html', {
    #    'hosts': hosts, 'login_user': request.user, 'users': users, 'auth_users': auth_users, 'a': a_value, 'hid': hid
    #return render_to_response('index.html',{
    #    'hosts': hosts,'login_user': request.user,'users':users,'auth_users':auth_users,
    })



def checkurl(request,id):
    hosts = models.Host.objects.all()
    a = ''
    users = models.Host_User.objects.all()
    auth_users = models.User.objects.all()
    hid = ''
    a_value = ''
    # return render_to_response('index.html',{'login_user': request.user})
    for h in hosts:
        host_id = str(h.id)
        if 'id' in request.GET:
            child = subprocess.Popen(['/bin/bash', '-c', '/Users/jcc/PycharmProjects/test_shell/web/hostname.sh'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out = child.stdout.readlines()
            hid = h.id
            for line in out:
                print line.strip()
                a = line.strip()
                a_value = locals()
    rlist = [['Jack', 'Chinese', a_value], ['Mike', 'English', '35'], ['Bob', 'Math', '50'], ['Frank', 'Art', '27'],
             ['Lucy', 'Music', '26']]
    rlist2 = []
    rlist2.append({"name": rlist[int(id)][0], "subject": rlist[int(id)][1], "age": rlist[int(id)][2]})
    rjson = json.dumps(rlist2)
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(rjson)
    return response
    #return render_to_response(request,'index.html',locals())


def data(request, id):
    hosts = models.Host.objects.all()
    a=''
    #if "id" in request.GET:
    child = subprocess.Popen(['/bin/bash', '-c', '/Users/jcc/PycharmProjects/test_shell/web/hostname.sh'],
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = child.stdout.readlines()
    for line in out:
        print line.strip()
        a1 = line.strip()
        a = a1
    rlist = [['Jack', id, a], ['Mike', 'English','35'], ['Bob', 'Math','50'], ['Frank', 'Art','27'], ['Lucy', 'Music','26']]
    rlist2 = []
    rlist2.append({"name" : rlist[int(id)][0], "subject" : rlist[int(id)][1], "age" : rlist[int(id)][2]})
    rjson = json.dumps(rlist2)
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(rjson)
    return response

'''
def index(request):

    hosts = models.Host.objects.all()
    users = models.Host_User.objects.all()
    auth_users = models.User.objects.all()
    hid=''
    a_value=''
	#return render_to_response('index.html',{'login_user': request.user})
    for h in hosts:
        host_id=str(h.id)
        if 'id'+host_id in request.GET:
            child = subprocess.Popen(['/bin/bash', '-c', '/Users/jcc/PycharmProjects/test_shell/web/hostname.sh'],
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out = child.stdout.readlines()
            hid=h.id
            for line in out:
                print line.strip()
                a = line.strip()
                a_value = locals()
    return render_to_response('index.html', {
        'hosts': hosts, 'login_user': request.user, 'users': users, 'auth_users': auth_users, 'a': a_value, 'hid': hid
    #return render_to_response('index.html',{
    #    'hosts': hosts,'login_user': request.user,'users':users,'auth_users':auth_users,
    })

def data(request, id):
    hosts = models.Host.objects.all()
    a=''
    #if "id" in request.GET:
    child = subprocess.Popen(['/bin/bash', '-c', '/Users/jcc/PycharmProjects/test_shell/web/hostname.sh'],
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = child.stdout.readlines()
    for line in out:
        print line.strip()
        a1 = line.strip()
        a = a1
    rlist = [['Jack', 'Chinese',a], ['Mike', 'English','35'], ['Bob', 'Math','50'], ['Frank', 'Art','27'], ['Lucy', 'Music','26']]
    rlist2 = []
    rlist2.append({"name" : rlist[int(id)][0], "subject" : rlist[int(id)][1], "age" : rlist[int(id)][2]})
    rjson = json.dumps(rlist2)
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(rjson)
    return response

def data(request, id):
    #rlist = [['Jack', 'Chinese'], ['Mike', 'English'], ['Bob', 'Math'], ['Frank', 'Art'], ['Lucy', 'Music']]
    rlist = [['Jack', 'Chinese','30'], ['Mike', 'English','35'], ['Bob', 'Math','50'], ['Frank', 'Art','27'], ['Lucy', 'Music','26']]
    rlist2 = []
    rlist2.append({"name" : rlist[int(id)][0], "subject" : rlist[int(id)][1], "age" : rlist[int(id)][2]})
    rjson = json.dumps(rlist2)
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(rjson)
    return response
'''

def ajax_list(request):
    a = range(100)
    return HttpResponse(json.dumps(a), content_type='application/json')

def ajax_dict(request):
    hosts = models.Host.objects.all()
    a = ''
    child = subprocess.Popen(['/bin/bash', '-c', '/Users/jcc/PycharmProjects/test_shell/web/hostname.sh'],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = child.stdout.readlines()
    for line in out:
        print line.strip()
        a1 = line.strip()
        a = a1
    name_dict = {'twz': a, 'zqxt': 'I am teaching Django'}
    return HttpResponse(json.dumps(name_dict), content_type='application/json')

'''
def ajax_list(request):
    a = range(100)
    return HttpResponse(json.dumps(a), content_type='application/json')

def ajax_dict(request):
    name_dict = {'twz': 'Love Python And Django', 'zqxt': 'I am teaching Django'}
    return HttpResponse(json.dumps(name_dict), content_type='application/json')
'''