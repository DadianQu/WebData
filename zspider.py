import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ZspiderSpider(CrawlSpider):
    name = "zspider"
    allowed_domains = ["ssr1.scrape.center"]
    start_urls = ["https://ssr1.scrape.center/page/1"]

    rules = (
        Rule(LinkExtractor(allow=r'/page/\d+'), follow=True),
        Rule(LinkExtractor(allow=r'/detail/\d+'), callback='parse_detail'),
    )
    def parse_pageI(self,response):
        pass

    def parse_detail(self, response):
        title = response.xpath("//h2[@class='m-b-sm']/text()").get()



