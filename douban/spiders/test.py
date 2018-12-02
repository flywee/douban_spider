# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['http://gs.ccnu.edu.cn']
    start_urls = ['http://gs.ccnu.edu.cn//']
    rules = (Rule(LinkExtractor(allow='http://gs.ccnu.edu.cn/info/', deny='http://gs.ccnu.edu.cn/info/\d+\.html'),
                  follow=True),
             Rule(LinkExtractor(allow='http://gs.ccnu.edu.cn/info/\d+\.html'), callback='parse_item', follow=True),)

    def parse(self, response):
        i = {}
        i['url'] = response.url
        return i