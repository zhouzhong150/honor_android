# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
import json
import os
from definitions import OUTPUT_DIR


class HonorAndroidPipeline:

    def open_spider(self, spider):
        if spider.name == 'android_jianshu':
            self.android_jianshu_html = open(os.path.join(OUTPUT_DIR,'android_jianshu_html.jl'), 'w')
        if spider.name == 'android_developerandroid':
            self.android_developerandroid_html = open(os.path.join(OUTPUT_DIR,'android_developerandroid_html.jl'), 'w')
        if spider.name == 'android_sourceandroid_crawl':
            self.android_sourceandroid_crawl_html = open(os.path.join(OUTPUT_DIR,'android_sourceandroid_crawl_html.jl'), 'w')
        if spider.name == 'android_developerandroid_crawl':
            self.android_developerandroid_crawl_html = open(os.path.join(OUTPUT_DIR,'android_developerandroid_crawl_html.jl'), 'w')
        if spider.name == 'android_issuetracker_component':
            self.android_issuetracker_component = open(os.path.join(OUTPUT_DIR,'android_issuetracker_component.jl'), 'w')
        if spider.name == 'android_issuetracker':
            self.android_issuetracker_html = open(os.path.join(OUTPUT_DIR,'android_issuetracker_16_html.jl'), 'w')
        if spider.name == 'android_issuetracker_a':
            self.android_issuetracker_a_html = open(os.path.join(OUTPUT_DIR,'android_issuetracker_17_html.jl'), 'w')
        if spider.name == 'android_issuetracker_b':
            self.android_issuetracker_b_html = open(os.path.join(OUTPUT_DIR,'android_issuetracker_1_html.jl'), 'w')



    def process_item(self, item, spider):
        line = json.dumps((dict(item))) + "\n"
        if spider.name == 'android_jianshu':
            self.android_jianshu_html.write(line)
        if spider.name == 'android_developerandroid':
            self.android_developerandroid_html.write(line)
        if spider.name == 'android_sourceandroid_crawl':
            self.android_sourceandroid_crawl_html.write(line)
        if spider.name == 'android_developerandroid_crawl':
            self.android_developerandroid_crawl_html.write(line)
        if spider.name == 'android_issuetracker_component':
            self.android_issuetracker_component.write(line)
        if spider.name == 'android_issuetracker':
            self.android_issuetracker_html.write(line)
        if spider.name == 'android_issuetracker_a':
            self.android_issuetracker_a_html.write(line)
        if spider.name == 'android_issuetracker_b':
            self.android_issuetracker_b_html.write(line)

        return item


    def close_spider(self, spider):
        if spider.name == 'android_jianshu':
            self.android_jianshu_html.close()
        if spider.name == 'android_developerandroid':
            self.android_developerandroid_html.close()
        if spider.name == 'android_sourceandroid_crawl':
            self.android_sourceandroid_crawl_html.close()
        if spider.name == 'android_developerandroid_crawl':
            self.android_developerandroid_crawl_html.close()
        if spider.name == 'android_issuetracker_component':
            self.android_issuetracker_component.close()
        if spider.name == 'android_issuetracker':
            self.android_issuetracker_html.close()
        if spider.name == 'android_issuetracker_a':
            self.android_issuetracker_a_html.close()
        if spider.name == 'android_issuetracker_b':
            self.android_issuetracker_b_html.close()
