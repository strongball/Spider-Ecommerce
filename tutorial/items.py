# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
#
#
#cat xxx.json | json_pp| less
import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class TorrentItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    size = scrapy.Field()

class BaItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()

class HumItem(scrapy.Item):
    bigCat = scrapy.Field()
    bigCatNO = scrapy.Field()
    cat = scrapy.Field()
    catNO = scrapy.Field()

class JobItem(scrapy.Item):
    bigCat = scrapy.Field()
    cat = scrapy.Field()

    name = scrapy.Field()
    company = scrapy.Field()
    detail = scrapy.Field()
    place = scrapy.Field()
