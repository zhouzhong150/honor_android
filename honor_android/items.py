# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AndroidJianshuHTMLItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    html = scrapy.Field()



class AndroidSourceAndroidHTMLItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    html = scrapy.Field()

class AndroidDeveloperAndroidHTMLItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    html = scrapy.Field()


class AndroidIssueTrackerHTMLItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    html = scrapy.Field()
    title = scrapy.Field()

class AndroidIssueTrackerComponentItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()