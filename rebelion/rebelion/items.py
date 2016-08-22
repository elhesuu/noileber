# -*- coding: utf-8 -*-
#
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from base.models import Article


class RebelionArticleItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = Article
    date = scrapy.Field()
    category_id = scrapy.Field()
    subcategory = scrapy.Field()
    author = scrapy.Field()
    pre = scrapy.Field()
    headline = scrapy.Field()
    lead = scrapy.Field()
    body = scrapy.Field()
    source = scrapy.Field()
