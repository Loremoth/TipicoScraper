# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EventItem(scrapy.Item):
    name = scrapy.Field()
    selections = scrapy.Field()


class SelectionItem(scrapy.Item):
    name = scrapy.Field()
    values = scrapy.Field()
