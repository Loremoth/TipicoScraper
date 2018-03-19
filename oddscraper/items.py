# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import string

import scrapy


def remove_escapes(value):
    string.replace(value, "\n", " ")
    string.replace(value, "\t", " ")


class Event(scrapy.Item):
    name = scrapy.Field()
    selections = scrapy.Field()


class Selection(scrapy.Item):
    name = scrapy.Field()
    values = scrapy.Field()


class Odd(scrapy.Item):
    name = scrapy.Field()
    value = scrapy.Field()
