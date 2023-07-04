import scrapy
from Cars.items import CarsItem

class CarspiderSpider(scrapy.Spider):
    name = "carSpider"
    allowed_domains = ["car.autohome.com.cn"]
    start_urls = ["https://car.autohome.com.cn/pic/series-t/19.html"]

    def parse(self, response):
        uiboxes = response.xpath("//div[@class='uibox']")
        for uibox in uiboxes:
            category = uibox.xpath(".//div[@class='uibox-title']/a/text()").get()
            urls = uibox.xpath(".//ul/li/a/img/@src").getall()
            # for url in urls:
            #     url = response.urljoin(url)
            #     print (url)
            urls = list(map(lambda url:response.urljoin(url), urls))
            item = CarsItem(category=category,urls=urls)
            yield item



