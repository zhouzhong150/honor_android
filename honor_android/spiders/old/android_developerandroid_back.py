import uuid
import scrapy
from honor_android.items import AndroidDeveloperAndroidHTMLItem


class AndroidDeveloperSpider(scrapy.Spider):
    name = 'android_developerandroidxxxxx'
    allowed_domains = ['developer.android.com']
    count = 0

    url_data = {
        "guide": [],
        "design_qaulity": []
    }

    title_data = {
        "guide": [],
        "design_qaulity": []
    }

    language_list = ['en', 'zh_cn']

    def start_requests(self):
        guide_start_url = 'https://developer.android.com/guide?hl=en'
        design_qaulity_start_url = 'https://developer.android.com/design?hl=en'
        yield scrapy.Request(url=guide_start_url, callback=self.parse_list, meta={"type": 'guide'})
        yield scrapy.Request(url=design_qaulity_start_url, callback=self.parse_list, meta={"type": 'design_qaulity'})



    def parse_list(self, response):
        type = response.meta.get('type')
        li_list = response.xpath('/html/body/section/devsite-book-nav/nav/div[2]/div[2]/ul/*')
        for li in li_list:
            self.parse_digui(li, 1, '', type)

        print(len(self.url_data.get(type)))

        url_list = self.url_data.get(type)
        url_list[0] = 'https://developer.android.com/gdsdsd'
        for index, url in enumerate(url_list):
            for language in self.language_list:
                yield scrapy.Request(url=url + '?hl=' + language, callback=self.parse_page, meta={"url": url + '?hl=' + language, "index": index})

    def parse_digui(self, response, depth, title, type):
        try:
            ul = response.xpath('div/ul').extract()
            if len(ul) == 0:

                tem_title = response.xpath('a/span/text()').extract()[0]
                if title != '':
                    title = title + '/'

                title = title + tem_title
                url = response.xpath('a/@href').extract()[0]
                if 'http' not in url:
                    url = 'https://developer.android.com' + url

                self.url_data.get(type).append(url)
                self.title_data.get(type).append(title)

            else:
                li_list = response.xpath('div/ul/*')
                tem_title = response.xpath('div/div/span/text()').extract()[0]
                if title != '':
                    title = title + '/'

                title = title + tem_title

                for li in li_list:
                    self.parse_digui(li, depth + 1, title, type)

        except BaseException as e:
            print(e)


    def parse_page(self, response):

        if response.status != 200:
            print(response.status, response.request)
        else:
            print("process url", response.meta.get('url'), self.count)
            self.count = self.count + 1
            response.meta.get('url')
            html_item = AndroidDeveloperAndroidHTMLItem()
            html_item['id'] = str(uuid.uuid1())
            html_item['url'] = response.meta.get('url')
            html_item['html'] = response.text
            yield html_item






