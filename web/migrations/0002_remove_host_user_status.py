# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-31 13:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host_user',
            name='status',
        ),
    ]
