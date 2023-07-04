import scrapy


class LoginSpiderSpider(scrapy.Spider):
    name = "login_spider"
    allowed_domains = ["douban.com"]
    start_urls = ["https://douban.com"]

    def start_requests(self):
        url = "https://www.douban.com/"
        data = {"name":"16637792035","password":"Qdd19930715!"}
        request = scrapy.FormRequest(url, formdata= data, callback=self.parse_page)
        yield request

    def parse_page(self,response):
        with open("login.html", "w", encoding='utf-8') as fp:
            fp.write(response.text)
