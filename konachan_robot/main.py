# _*_ coding:utf-8 _*_
# 在IDE中直接执行此文件就能运行爬虫
__author__ = "JemmyH"
from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "konachan_spider"])