# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-31 13:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_remove_host_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host_user',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
