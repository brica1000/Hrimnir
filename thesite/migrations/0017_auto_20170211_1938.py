# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-11 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesite', '0016_auto_20170211_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='employees',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sustainability',
        ),
        migrations.AddField(
            model_name='conglomerate',
            name='employees',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='conglomerate',
            name='sustainability',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
