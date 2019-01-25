# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.conf import settings


class KonachanRobotPipeline(object):
    def __init__(self):
        # 创建实例的时候打开文件句柄
        self.file_yande = open(settings.get("YANDE_FILE_NAME"), 'w')
        self.file_konachan = open(settings.get("KONACHAN_FILE_NAME"), 'w')

    def open_spider(self, spider):
        print("爬虫开始")

    def process_item(self, item, spider):
        # 将item中的信息 使用初始化时保存的句柄保存到文件中
        if item['host'] == "konachan":
            self.file_konachan.write("{0},{1}\n".format(item["name"], item["url"]))
        else:
            self.file_yande.write("{0},{1}\n".format(item["name"], item["url"]))
        return item

    def close_spider(self, spider):
        print("爬虫结束")
        # 最后不要忘了关闭文件句柄
        self.file_konachan.close()
        self.file_yande.close()
