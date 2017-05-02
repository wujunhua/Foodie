# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-02 23:14
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.models import Group

def add_group():
    group, created = Group.objects.get_or_create(name='customer')
    if created:
        logger.info('customer Group created')

class Migration(migrations.Migration):

    dependencies = [
        ('foodie', '0003_auto_20170502_2308'),
    ]

    operations = [
        migrations.RunPython(add_group),
    ]
