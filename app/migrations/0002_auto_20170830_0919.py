# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 09:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
