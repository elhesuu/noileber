# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 09:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20160819_1144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='body',
            new_name='body_html',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='raw_body',
            new_name='body_raw',
        ),
    ]
