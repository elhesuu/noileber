import scrapy
import re
import bleach

from scrapy.http.request import Request
from rebelion.items import RebelionArticleItem
from base.models import Article
from django.db.models import Max
from rebelion import settings

class RebelionSpider(scrapy.Spider):
    name = 'rebelion'
    allowed_domains = ['rebelion.org']

    def __init__(self):
        self.consecutive_failed_passes = 0
        self.last_crawled_id = self.start_from = Article.objects.aggregate(Max('rebelion_id'))['rebelion_id__max'] or settings.START_FROM

    def start_requests(self):
        while (
            self.last_crawled_id <= self.start_from + settings.MAX_PASSES
            and self.consecutive_failed_passes < settings.MAX_FAILED_PASSES
            ):
            url = 'http://www.rebelion.org/noticia.php?id={}'.format(self.last_crawled_id)
            yield Request(url, meta={ 'dont_redirect': True }, callback=self.parse)
            self.last_crawled_id += 1

    def select(self, selector_list, selector):
        return selector_list.css(selector).extract_first(default='').encode('utf-8')

    def find(self, text_list, pattern):
        for item in text_list:
            match = re.compile(pattern).search(item)
            if match:
                return match.group(0)
        return ''

    # flat text list
    def selector_text_list(self, selector_list):
        flattened = []
        for node in selector_list:
            flattened.append(bleach.clean(node.extract(), [], strip=True).encode('utf-8'))
        return flattened

    def handle(self, response, id):
        main = response.xpath('/html/body/center[1]/div')
        content = response.xpath('//*[@id="CuerpoNoticia"]')

        item = RebelionArticleItem()
        item['date'] = self.select(main, 'td.fecha ::text')
        item['category'] = self.select(main, '.ruta_blanco a:nth-child(2) ::text')
        item['subcategory'] = self.select(main, '.ruta_blanco a:nth-child(3) ::text')
        item['pre'] = self.select(response, '.pretitulo *::text')
        item['headline'] = self.select(content, '.titulo *::text')
        item['author'] = self.select(content, '.autor *::text')

        entradillas = self.selector_text_list(content.css('.entradilla'))
        item['translated_by'] = self.find(entradillas, '.*Traduc.*')
        item['license'] = self.find(entradillas, '.*permiso del autor mediante.*')
        item['lead'] = self.find(entradillas, '^((?!(Traduc|permiso)).)*$')

        item['body'] = self.select(response, '#TextoNoticia')
        item['source'] = self.select(response, 'a.fuente ::attr(href)')
        item['rebelion_id'] = id

        print 'Crawled: ', id
        return item

    def parse_id_from_url(self, url):
        match = re.search(r'(\d+)', url)
        return match.group() if match else False

    def parse(self, response):
        is_valid_url = 'www.rebelion.org/noticia.php?id=' in response.url
        id = self.parse_id_from_url(response.url)

        if (is_valid_url and id and
            response.status == 200 and
            'noticia inexistente' not in (response.text or '').lower()):
            self.consecutive_failed_passes = 0
            return self.handle(response, id)
        else:
            self.consecutive_failed_passes += 1
            if self.consecutive_failed_passes == settings.MAX_FAILED_PASSES:
                print '{} consecutive failed passes. Stopping'.format(settings.MAX_FAILED_PASSES)
