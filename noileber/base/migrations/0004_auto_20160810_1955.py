# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-10 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_article_rebelion_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='headline',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='article',
            name='pre',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='article',
            name='source',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='article',
            name='subcategory',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=400),
        ),
    ]
