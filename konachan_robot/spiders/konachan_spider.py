# -*- coding: utf-8 -*-
import scrapy
from ..items import KonachanItem

HOST_NAME = "https://www.konachan.com"


class KonachanSpiderSpider(scrapy.Spider):
    name = 'konachan_spider'
    allowed_domains = ['konachan.com']
    start_urls = ['https://www.konachan.com/post', 'https://yande.re/post']  # 此处为入口，

    def parse(self, response):
        # 获取当前页所有的项目url
        urls = [HOST_NAME + i for i in response.xpath("//ul[@id='post-list-posts']//li/div[1]/a[1]/@href").extract()]
        for url in urls:
            if response.url.find("konachan") > -1:
                yield scrapy.Request(url, callback=self.parse_image)
            else:
                pass
        # 自动翻页
        next_url = response.xpath("//a[@class='next_page']/@href").extract()
        if next_url:
            yield scrapy.Request(HOST_NAME + next_url[0], callback=self.parse)

    def parse_image(self, response):
        # 直接获取信息
        item = KonachanItem()
        if response.url.find("konachan") > -1:
            item['host'] = "konachan"
        else:
            item['host'] = "yande"
        item['url'] = response.xpath('//div[@class="content"]/div[1]/img[1]/@src').extract()[0]
        item['name'] = response.url.split("/")[-1]
        yield item
