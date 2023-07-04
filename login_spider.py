import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pickle

class LoginSpiderSpider(scrapy.Spider):
    name = "login_spider"
    allowed_domains = ["zhihu.com"]
    start_urls = ["https://www.zhihu.com/"]

    def start_requests(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        driver = webdriver.Chrome(options=options)
        driver.get('https://www.zhihu.com/signin')
        time.sleep(5)
        driver.find_element(By.XPATH, "//div[@class='SignFlow-tab']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//label[@class='SignFlow-accountInput Input-wrapper QZcfWkCJoarhIYxlM_sG']//input[@class='Input i7cW1UcwT6ThdhTakqFm username-input']").send_keys("dadianqu@gmail.com")
        time.sleep(5)
        driver.find_element(By.XPATH, "//label[@class='Input-wrapper QZcfWkCJoarhIYxlM_sG']//input[@class='Input i7cW1UcwT6ThdhTakqFm username-input']").send_keys("Qdd19930715!")
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@class='Button SignFlow-submitButton FEfUrdfMIKpQDJDqkjte Button--primary Button--blue epMJl0lFQuYbC7jrwr_o JmYzaky7MEPMFcJDLNMG']").click()
        time.sleep(5)
        Cookies = driver.get_cookies()
        cookie_dict = {}
        for cookie in Cookies:
            f = open(r"C:\Users\dadia\PycharmProjects\Login" + cookie["name"] + '.facebook', 'wb')
            pickle.dump(cookie, f)
            f.close()
            cookie_dict[cookie["name"]] = cookie["value"]
        driver.close()
        yield scrapy.Request(url=self.start_urls[0], dont_filter=True, cookies = cookie_dict)


