#coding=utf-8

"""mysite URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from web import views

admin.autodiscover()
urlpatterns = [

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^account_login/$', views.account_login),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^pie/$', views.pie),
    #url(r'test_shell$',views.checkurl),
    url(r'^$', views.index),
    #url(r'/?(id3=collect_log)$',views.index),
    #url(r'^data/(?P<id>\d+)/$', views.checkurl),
    url(r'^data/(?P<id>\d+)/$', views.data),
    url(r'^ajax_list/$', views.ajax_list, name='ajax-list'),
    url(r'^ajax_dict/$', views.ajax_dict, name='ajax-dict'),
]
