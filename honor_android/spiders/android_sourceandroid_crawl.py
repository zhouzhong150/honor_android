import uuid
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from honor_android.items import AndroidSourceAndroidHTMLItem

class AndroidSourceandroidCrawlSpider(CrawlSpider):
    name = 'android_sourceandroid_crawl'
    allowed_domains = ['source.android.com']
    start_urls = ['http://source.android.com/']
    drop_count = 0
    process_count = 0


    rules = (
        Rule(LinkExtractor(allow=r'https://source.android.com/devices'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'https://source.android.com/setup'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'https://source.android.com/security'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'https://source.android.com/reference'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'https://source.android.com/compatibility'), callback='parse_item', follow=True),

    )

    def parse_item(self, response):
        url = str(response.request.url)
        process_flag = 0
        if '?hl=' in url:
            if '?hl=en' in url or '?hl=zh_cn' in url:
                process_flag = 1
        else:
            process_flag = 1

        if process_flag:
            self.process_count = self.process_count + 1
            print("process url", response.request, self.process_count)
            item = AndroidSourceAndroidHTMLItem()
            item['id'] = str(uuid.uuid1())
            item['url'] = str(response.request.url)
            item['html'] = response.text
            yield item

        else:
            self.drop_count = self.drop_count + 1
            print("drop url", response.request, self.drop_count)

