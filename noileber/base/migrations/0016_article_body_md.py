# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_auto_20160819_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='body_md',
            field=models.TextField(default=''),
        ),
    ]
