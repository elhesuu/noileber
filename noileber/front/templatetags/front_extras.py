from django import template
register = template.Library()

import markdown
import html2text
import bleach

from bs4 import BeautifulSoup
from noileber.settings import ALLOWED_TAGS

def html_from_markdown(value):
    return markdown.markdown(value)

def non_empty_tags(value):
  soup = BeautifulSoup(value)
  for node in soup.find_all():
    if len(node.text) == 0:
        node.extract()
    if node.string:
      node.string.replace_with(node.string.strip())

  return value #soup.prettify()

def cleanup_html(value):
  cleaner = bleach.clean(non_empty_tags(value), ALLOWED_TAGS, strip=True)
  as_markdown = html2text.html2text(cleaner)
  return html_from_markdown(as_markdown)

register.filter('markdown', html_from_markdown)
register.filter('cleanup', cleanup_html)