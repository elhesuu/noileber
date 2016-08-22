from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=400)
    is_region = models.BooleanField(default=0)
    is_latin_america = models.BooleanField(default=0)
    slug = models.SlugField(default='', max_length=120)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name.encode('utf-8', 'ignore')

class Article(models.Model):
    date = models.DateField('date published')
    slug = models.SlugField(default='', max_length=120)
    day_timestamp = models.IntegerField('day', db_index=True, default=0)
    rebelion_id = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=400, default='')
    pre = models.CharField(max_length=400) # pretitulo
    headline = models.CharField(max_length=400, db_index=True) # titulo
    lead = models.TextField() # endradilla
    translated_by = models.CharField(max_length=400, default='') # endradilla
    license = models.CharField(max_length=400, default='') # endradilla
    body_md = models.TextField() # textonoticia
    body_raw = models.TextField(default='')
    author = models.CharField(max_length=400, default='')
    source = models.CharField(max_length=400) # fuente

    def __str__(self):
        return self.headline.encode('utf-8', 'ignore')
