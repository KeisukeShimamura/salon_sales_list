import scrapy


class HotPapperBeautySpider(scrapy.Spider):
    name = 'hot_papper_beauty'
    allowed_domains = ['beauty.hotpepper.jp']
    start_urls = ['http://beauty.hotpepper.jp/']

    def parse(self, response):
        pass
