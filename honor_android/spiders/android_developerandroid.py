import os
import uuid
import scrapy

from definitions import OUTPUT_DIR
from honor_android.items import AndroidDeveloperAndroidHTMLItem
from honor_android.util.file_util import FileUtil


class AndroidDeveloperSpider(scrapy.Spider):
    name = 'android_developerandroid'
    allowed_domains = ['developer.android.com']
    count = 0


    def start_requests(self):
        print("start")
        url_list = self.get_url_list()
        for url in url_list:
            yield scrapy.Request(url=url, callback=self.parse_page, meta={"url": url})
        print("complete")

    def get_url_list(self):
        file = os.path.join(OUTPUT_DIR, 'android_developerandroid_crawl_html.jl')
        data = FileUtil.load_data_list(file)
        url_list = []
        for data_ in data:
            url = data_.get('url') + '?hl=zh_cn'
            url_list.append(url)
        return url_list




    def parse_page(self, response):
        if response.status != 200:
            print(response.status, response.request)
        else:
            print("process url", response.meta.get('url'), self.count)
            self.count = self.count + 1
            html_item = AndroidDeveloperAndroidHTMLItem()
            html_item['id'] = str(uuid.uuid1())
            html_item['url'] = response.meta.get('url')
            html_item['html'] = response.text
            yield html_item






