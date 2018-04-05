# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


def array_to_value(element):
    return element[0]


def take_second(array):
    return array[1]


def remove_escapes(value):
    value = [item.replace("\n", "") for item in value]
    value = [item.replace("\t", "") for item in value]
    return value


class Odd(scrapy.Item):
    label = scrapy.Field()
    value = scrapy.Field()


class Selection(scrapy.Item):
    selection = scrapy.Field(output_processor=take_second)
    odds = scrapy.Field()

class Event(scrapy.Item):
    name = scrapy.Field(input_processor=remove_escapes)
    selections = scrapy.Field()

