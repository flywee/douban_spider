# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem



class DbspiderSpider(scrapy.Spider):
    name = 'dbspider'
    allowed_domains = ['http://physics.ccnu.edu.cn/']
    offset = 0
    url = "https://movie.douban.com/top250?start="
    start_urls = ((url+str(offset)),)

    def parse(self, response):
        item = DoubanItem()
        movies = response.xpath('//ol[@class="grid_view"]')
        for each in movies:
            item['name'] = each.xpath('.//span[@class="title"][1]/text()').extract()[0]
            item['bd'] = each.xpath('.//p/text()').extract()[0]
            item['star'] = each.xpath('.//span[@class="rating_num"]/text()').extract()[0]
            quote = each.xpath('.//span[@class="inq"]/text()').extract()
            if len(quote) != 0:
                item['quote'] = quote[0]
            yield item

        if self.offset < 225:
            self.offset += 25
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
