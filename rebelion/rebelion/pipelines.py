# -*- coding: utf-8 -*-

# Define your item pipelines here

# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time
import datetime

from django.utils.text import slugify
from base.models import Category
from base.utils import truncated_day_timestamp
from noileber.settings import ALLOWED_TAGS

from bs4 import BeautifulSoup
import bleach
import html2text
from stop_words import get_stop_words

class RebelionPipeline(object):
    def get_related_by_name(self, Type, name):
        existing = Type.objects.filter(name__icontains=name).first()
        return existing or Type.objects.create(name=name)

    def parse_date(self, date=''):
        return datetime.datetime.strptime(date.strip(), '%d-%m-%Y').date()

    def is_valid_item(self, item):
        return item['date'] and item['headline'] and item['body']

    def cleanup_html(self, raw):
        return bleach.clean(raw, ALLOWED_TAGS, strip=True)

    def as_markdown(self, raw):
        return html2text.html2text(self.cleanup_html(raw))

    def as_slug(self, str):
        meaningful = [word for word in str.split(' ') if word not in get_stop_words('spanish')]
        return slugify(' '.join(meaningful[:6]))[:120]

    def process_item(self, item, spider):

        if (self.is_valid_item(item)):
            item['category'] = self.get_related_by_name(Category, item['category'])
            item['date'] = self.parse_date(item['date'])
            item['day_timestamp'] = time.mktime(item['date'].timetuple())
            item['body_raw'] = item['body']
            item['slug'] = self.as_slug(item['headline'])
            item['body_md'] = self.as_markdown(item['body'].decode('utf-8'))
            item.save()
            return item
