import scrapy

from tutorial.items import BaItem

class DmozSpider(scrapy.Spider):
    name = "bath"
    allowed_domains = ["forum.gamer.com.tw"]
    start_urls = [
        "http://forum.gamer.com.tw/"
    ]

    def parse(self, response):
        for sel in response.xpath("//td[@class='FM-blist3']/a/text()"):
            item = BaItem()
            item['name'] = sel.extract()
            yield item
