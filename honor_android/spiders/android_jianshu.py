import json
import os
import requests
import scrapy
from honor_android.items import AndroidJianshuHTMLItem
from honor_android.util.file_util import FileUtil
from definitions import ROOT_DIR, DATA_DIR, OUTPUT_DIR


class AndroidJianshuSpider(scrapy.Spider):
    name = 'android_jianshu'
    allowed_domains = ['www.jianshu.com']


    def start_requests(self):
        doc_list = self.get_doc_list()
        print(doc_list)
        print("doc num: ", len(doc_list))
        print("start write url")
        FileUtil.write2jl(doc_list, os.path.join(OUTPUT_DIR, 'android_jianshu_url.jl'))
        print("end write url")

        print("start write html")
        for index, doc in enumerate(doc_list):
            slug = doc.get('slug')
            url = 'https://www.jianshu.com/p/{}'.format(slug)
            id = doc.get('id')
            yield scrapy.Request(url=url, callback=self.parse_page, meta={"url": url, "id": id, "index": index})

        print("end write html")


    def get_doc_list(self):
        print("ss")
        type_id = 28
        count = 1000
        page = 1
        url = 'https://www.jianshu.com/programmers'
        params = {
            "page": page,
            "count": count,
            "type_id": type_id
        }
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
        }
        try:
            response = requests.get(url, params=params, headers=headers, timeout=200000)
            return json.loads(response.text)
        except BaseException as e:
            print("connect errrrrrr")
            print(e)
            print("haha")
            return None




    def parse_page(self, response):
        html_item = AndroidJianshuHTMLItem()
        print("process url: ", response.meta.get('url'), " index: ", response.meta.get('index'))

        html_item['id'] = response.meta.get('id')
        html_item['url'] = response.meta.get('url')
        html_item['html'] = response.text
        yield html_item

        pass

