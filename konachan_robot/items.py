# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KonachanItem(scrapy.Item):
    # 定于一个item的属性
    host = scrapy.Field()  # 哪个网站的
    name = scrapy.Field()  # 图片名
    url = scrapy.Field()  # 图片URL
