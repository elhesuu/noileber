# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_article_raw'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='headline',
            field=models.CharField(db_index=True, max_length=400),
        ),
    ]
