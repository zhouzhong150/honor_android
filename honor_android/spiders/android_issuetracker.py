import os
import uuid
import scrapy
from honor_android.items import AndroidIssueTrackerHTMLItem
from honor_android.util.file_util import FileUtil
from definitions import OUTPUT_DIR

class AndroidIssuetrackerSpider(scrapy.Spider):
    name = 'android_issuetracker_1'
    allowed_domains = ['issuetracker.google.com']
    component_list = []
    count = 0
    repeat_count = 0
    page_url_list = []

    def get_data(self):
        file = os.path.join(OUTPUT_DIR, 'android_issuetracker_component.jl')
        return FileUtil.load_data_list(file)

    def start_requests(self):
        data_list = self.get_data()
        start = 0
        end = 1
        for index, data in enumerate(data_list):
            if  index>=start and index <end:
                question_url = 'https://issuetracker.google.com/issues?q=comment:' + str(data.get('id'))
                yield scrapy.Request(url=question_url, callback=self.parse_question, meta={'id': data.get('id'), 'page_num': 1})

    def parse_question(self, response):
        continue_flag = 1
        page_list = response.xpath('/html/body/div[1]/app-root/div/div/b-router-outlet/b-ng2-router-outlet/list-issues-page/div[2]/div/b-issues-grid/div/pop-grid/table/tbody/*')

        for page in page_list:
            page_url = page.xpath('td[6]/div/div/a/@href').extract()[0]
            if page_url in self.page_url_list:
                continue_flag = 0
                break
            else:
                self.page_url_list.append(page_url)
                title = page.xpath('td[6]/div/div/a/text()').extract()[0]
                page_url = 'https://issuetracker.google.com/' + page_url
                yield scrapy.Request(url=page_url, callback=self.parse_page, meta={"id": response.meta.get('id'), "url": page_url, 'title': title})

        question_url = 'https://issuetracker.google.com/issues?q=comment:' + str(response.meta.get('id')) + '&p=' + str(response.meta.get('page_num') + 1)
        if continue_flag == 1:
            yield scrapy.Request(url=question_url, callback=self.parse_question,
                                 meta={'id': response.meta.get('id'),
                                       'page_num': response.meta.get('page_num') + 1})

    def parse_page(self, response):
        if response.status != 200:
            print(response.status, response.request)
        else:
            if response.meta.get('url') in self.page_url_list:
                self.repeat_count = self.repeat_count + 1
                print("repeat url", response.meta.get('url'), self.count)
            else:
                self.count = self.count + 1
                print("process url", response.meta.get('url'), self.count)
                response.meta.get('url')
                html_item = AndroidIssueTrackerHTMLItem()
                html_item['id'] = str(uuid.uuid1())
                html_item['url'] = response.meta.get('url')
                html_item['component_id'] = response.meta.get('id')
                html_item['title'] = response.meta.get('title')
                html_item['html'] = response.text
                yield html_item