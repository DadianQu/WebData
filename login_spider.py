import scrapy


class LoginSpiderSpider(scrapy.Spider):
    name = "login_spider"
    allowed_domains = ["facebook.com"]
    start_urls = ["https://facebook.com"]

    def start_requests(self):
        url = "https://www.facebook.com/"
        data = {"email":"dadianqu@gmail.com","password":"Qdd19930419!"}
        request = scrapy.FormRequest(url, formdata= data, callback=self.parse_page)
        yield request

    def parse_page(self,response):
        request = scrapy.Request(url = "https://www.facebook.com/marketplace/?ref=bookmark", callback=self.parse_detail)
        yield request

    def parse_detail(self, response):
        with open ("tem.html", "w", encoding='utf-8') as fp:
            fp.write(response.text)

