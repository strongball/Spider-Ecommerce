import scrapy

from scrapy.http import Request
from tutorial.items import JobItem

class EofSpider(scrapy.Spider):
    name = "104"
    start_urls = ['http://www.104.com.tw/jb/category/?cat=3&jobsource=104_bank1']
    base = "http://www.104.com.tw"
    searchUrl = "http://www.104.com.tw/jobbank/joblist/joblist.cfm?indcat="

    def parse(self, response):
        for sel in response.xpath("//ul[@class='cate-list ind-item']/li"):
            item = JobItem()
            item['bigCat'] = sel.xpath("a/text()").extract()
            node = self.base + sel.xpath("a/@href").extract()[0]

            yield Request(url=node, meta={'bigCat': item, 'dont_redirect': True,"handle_httpstatus_list": [302]}, callback=self.getCatNO, headers ={'XRequested-With':'XMLHttpRequest'})

    def getCatNO(self, response):
        tmp = response.meta['bigCat']
        item = JobItem()
        item['bigCat'] = tmp['bigCat']
        for sel in response.xpath("//ul[@class='cate-list ind-item']/li"):
            item['cat'] = sel.xpath("a/text()").extract()
            node = self.searchUrl + sel.xpath("a/@no").extract()[0]
            yield Request(url=node, meta={'cat': item, 'dont_redirect': True,"handle_httpstatus_list": [302]}, callback=self.parseCtrl, headers ={'XRequested-With':'XMLHttpRequest'})

    def parseCtrl(self, response):
        tmp = response.meta['cat']
        item = JobItem()
        item['bigCat'] = tmp['bigCat']
        item['cat'] = tmp['cat']

        baseUrl = response.url
        # for i in range(1, int(pageNum) + 1):
        for i in response.xpath("//div[@id='box_page_top']/ul/li/a/text()").extract():
            node = baseUrl + "&page=" + str(i)
            yield Request(url=node, meta={'toPage': item, 'dont_redirect': True,"handle_httpstatus_list": [302]},callback=self.parsePage, headers ={'XRequested-With':'XMLHttpRequest'})

    def parsePage(self, response):
        tmp = response.meta['toPage']
        item = JobItem()
        item['bigCat'] = tmp['bigCat']
        item['cat'] = tmp['cat']
        # on focus
        for sel in response.xpath("//div[@class='j_cont line_bottom focus']"):
            item['name'] = sel.xpath("ul[1]/li[3]/div/a/span/text()").extract()
            item['place'] = sel.xpath("ul[1]/li[4]/div/span/text()").extract()
            item['company'] = sel.xpath("ul[2]/li[2]/div/a/span/text()").extract()
            item['detail'] = sel.xpath("div/text()").extract()
            yield item
        # else
        for sel in response.xpath("//div[@class='j_cont line_bottom']"):
            item['name'] = sel.xpath("ul[1]/li[3]/div/a/span/text()").extract()
            item['place'] = sel.xpath("ul[1]/li[4]/div/span/span/text()").extract()
            item['company'] = sel.xpath("ul[2]/li[2]/div/a/span/text()").extract()
            item['detail'] = sel.xpath("div/text()").extract()
            yield item
