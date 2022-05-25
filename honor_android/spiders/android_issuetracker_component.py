import uuid

import scrapy

from honor_android.items import AndroidIssueTrackerHTMLItem, AndroidIssueTrackerComponentItem


class AndroidIssuetrackerSpider(scrapy.Spider):
    name = 'android_issuetracker_component'
    allowed_domains = ['issuetracker.google.com']

    count = 0
    repeat_count = 0
    page_url_list = []

    def start_requests(self):
        start_url = 'https://issuetracker.google.com/components/190923/manage'
        yield scrapy.Request(url=start_url, callback=self.parse_digui, meta={"name": 'Android Public Tracker', 'id': 190923})


    def parse_digui(self, response):
        component = {
            "name": response.meta.get('name'),
            "id": response.meta.get('id')
        }
        print(component)
        item = AndroidIssueTrackerComponentItem()
        item['id'] = component.get('id')
        item['name'] = component.get('name')
        yield item

        li_list = response.xpath('/html/body/div[1]/app-root/div/div/b-router-outlet/b-ng2-router-outlet/manage-component-page/div[2]/div/mat-tab-group/div/mat-tab-body[1]/div/div/form/div[6]/b-component-children-list/ul/*')

        for li in li_list:
            tem_name = li.xpath('a/text()').extract()[0]
            component_name = response.meta.get('name') + '.' + tem_name
            component_url = li.xpath('a/@href').extract()[0]

            index = component_url.find('/')
            component_url = component_url[index + 1:]
            index = component_url.find('/')
            component_id = component_url[:index]
            new_url = 'https://issuetracker.google.com/components/' + str(component_id) + '/manage'
            yield scrapy.Request(url=new_url, callback=self.parse_digui, meta={"name": component_name, 'id': component_id})

