# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-18 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesite', '0021_auto_20170218_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='employees',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='product',
            name='sustainability',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
