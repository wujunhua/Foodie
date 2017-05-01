# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-01 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('rating', models.FloatField()),
                ('num_ratings', models.IntegerField(default=0)),
            ],
        ),
    ]
