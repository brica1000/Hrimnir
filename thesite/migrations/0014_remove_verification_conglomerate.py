# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-11 18:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thesite', '0013_auto_20170211_1856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verification',
            name='conglomerate',
        ),
    ]
