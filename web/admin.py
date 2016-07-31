# -*- coding: utf-8 -*-
from django.contrib import admin
from web.models import *

# Define Admin panel here.
class Host_User_Admin(admin.ModelAdmin):
    list_display = ('id','name','status','manager','department')

class Host_Admin(admin.ModelAdmin):
    list_display = ('id','ip','location','comment','version','comment','version','supervisor','path','category','visible','update_at')


# Register your models here.
admin.site.register(Host,Host_Admin)
admin.site.register(Category)
admin.site.register(Host_User,Host_User_Admin)