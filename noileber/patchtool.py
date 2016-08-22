#!/usr/bin/env python
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'noileber.settings'

import django
django.setup()

import html2text

from base.models import Article

#137738
#184725
#185814
#190084

def patch_empty_md_bodies():
  empty = Article.objects.all()[185814:200000]

  for record in empty:
    record.body_md = html2text.html2text(record.body_raw or record.body_html)
    record.save()
    print record.id, record.headline

patch_empty_md_bodies()