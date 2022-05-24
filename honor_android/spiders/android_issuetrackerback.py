import uuid

import scrapy

from honor_android.items import AndroidIssueTrackerHTMLItem


class AndroidIssuetrackerSpider(scrapy.Spider):
    name = 'android_issuedsdstracker'
    allowed_domains = ['issuetracker.google.com']
    component_list = []
    count = 0
    repeat_count = 0
    page_url_list = []


    def start_requests(self):
        start_url = 'https://issuetracker.google.com/components/190923/manage'
        yield scrapy.Request(url=start_url, callback=self.parse_digui, meta={"component_name": 'Android Public Tracker', 'component_id': 190923})


    def parse_digui(self, response):
        component = {
            "component_name": response.meta.get('component_name'),
            "component_id": response.meta.get('component_id')
        }
        print(component)
        self.component_list.append(component)

        li_list = response.xpath('/html/body/div[1]/app-root/div/div/b-router-outlet/b-ng2-router-outlet/manage-component-page/div[2]/div/mat-tab-group/div/mat-tab-body[1]/div/div/form/div[6]/b-component-children-list/ul/*')

        for li in li_list:
            tem_name = li.xpath('a/text()').extract()[0]
            component_name = response.meta.get('component_name') + '.' + tem_name
            component_url = li.xpath('a/@href').extract()[0]

            index = component_url.find('/')
            component_url = component_url[index + 1:]
            index = component_url.find('/')
            component_id = component_url[:index]
            new_url = 'https://issuetracker.google.com/components/' + str(component_id) + '/manage'
            yield scrapy.Request(url=new_url, callback=self.parse_digui, meta={"component_name": component_name, 'component_id': component_id})

        question_url = 'https://issuetracker.google.com/issues?q=comment:' + str(component.get('component_id'))

        yield scrapy.Request(url=question_url, callback=self.parse_question, meta= {'last_url': 'first', 'component_id': component.get('component_id'), 'page_num': 1})


    def parse_question(self, response):
        continue_flag = 1
        page_list = response.xpath(
            '/html/body/div[1]/app-root/div/div/b-router-outlet/b-ng2-router-outlet/list-issues-page/div[2]/div/b-issues-grid/div/pop-grid/table/tbody/*')

        for page in page_list:
            page_url = page.xpath('td[6]/div/div/a/@href').extract()[0]
            if page_url in self.page_url_list:
                continue_flag = 0
                break
            else:
                self.page_url_list.append(page_url)
                title = page.xpath('td[6]/div/div/a/text()').extract()[0]
                page_url = 'https://issuetracker.google.com/' + page_url
                yield scrapy.Request(url=page_url, callback=self.parse_page, meta={"url": page_url, 'title': title})

        question_url = 'https://issuetracker.google.com/issues?q=comment:' + str(response.meta.get('component_id')) + '&p=' + str(response.meta.get('page_num') + 1)
        if continue_flag == 1:
            yield scrapy.Request(url=question_url, callback=self.parse_question,
                                 meta={"last_url": response.request.url, 'component_id': response.meta.get('component_id'),
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
                    html_item['html'] = response.text
                    yield html_item