# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_auto_20160820_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='', max_length=120),
        ),
    ]
