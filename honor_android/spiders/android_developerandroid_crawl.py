import uuid
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from honor_android.items import AndroidDeveloperAndroidHTMLItem


class AndroidDeveloperCrawlSpider(CrawlSpider):
    name = 'android_developerandroid_crawl'
    allowed_domains = ['developer.android.com']
    start_urls = ['http://developer.android.com/']
    drop_count = 0
    process_count = 0
    '''
    
    '''
    rules = (
        Rule(LinkExtractor(allow=r'https://developer.android.com/',
                           deny=r'https://developer.android.com/reference|\?|https://developer.android.com/sdk'),
             callback='parse_item',
             follow=True
             ),
    )

    def parse_item(self, response):
        url = str(response.request.url)
        process_flag = 0
        if 'hl=' in url:
            if 'hl=en' in url or 'hl=zh_cn' in url:
                process_flag = 1
        else:
            process_flag = 1

        if process_flag:
            self.process_count = self.process_count + 1
            print("process url", response.request, self.process_count)
            item = AndroidDeveloperAndroidHTMLItem()
            item['id'] = str(uuid.uuid1())
            item['url'] = str(response.request.url)
            item['html'] = response.text
            yield item

        else:
            self.drop_count = self.drop_count + 1
            print("drop url", response.request, self.drop_count)






