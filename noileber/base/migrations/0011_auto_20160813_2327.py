# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 21:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_article_date_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='date_timestamp',
            new_name='day_timestamp',
        ),
    ]
