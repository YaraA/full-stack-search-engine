# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NytItem(scrapy.Item):
    # the fields for the nyt item:
    authors = scrapy.Field()
    title = scrapy.Field()
    body = scrapy.Field()
    url = scrapy.Field()
    summary = scrapy.Field()
    pass
