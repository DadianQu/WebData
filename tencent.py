from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from lxml import etree
import re

class tencent_spider():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)
        self.url = "https://careers.tencent.com/en-us/search.html?keyword=python"



    def run(self):
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source
            self.parse_url_list(self.url)

            WebDriverWait(self.driver, 1000).until(
                EC.element_to_be_clickable((By.XPATH, "//ul[@class='page-list']//li[last()]"))
            )
            nextBtn = self.driver.find_element(By.XPATH, "//ul[@class='page-list']//li[last()]")
            if "next disabled" in nextBtn.get_attribute("class"):
                break
            else:
                nextBtn.click()
            time.sleep(1)




    def parse_url_list(self,url):
        # html = etree.HTML(source)
        # self.driver.get(self.url)
        detailBtns = self.driver.find_elements(By.XPATH, "//div[@class='recruit-list']/a[@class='recruit-list-link']")
        for detailBtn in detailBtns:
            time.sleep(1)
            detailBtn.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(1)
            detail_url = self.driver.current_url
            print (detail_url)
            time.sleep(1)
            self.parse_detail(detail_url)
            time.sleep(1)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        # self.driver.close()
        # self.driver.switch_to.window(self.driver.window_handles[0])
        # titles = html.xpath("//div[@class = 'recruit-list']//span[@class='job-recruit-title']/text()")
        # locations = html.xpath("//div[@class = 'recruit-list']//span[@class='job-recruit-location']/text()")

    def parse_detail(self,detail_url):
        self.driver.get(detail_url)
        time.sleep(3)
        source = self.driver.page_source
        html = etree.HTML(source)
        try:
            title = html.xpath("//div[@class='css-cabox8']//h2[@class='css-7papts']/text()")
            location = html.xpath("//dd[@class='css-129m7dg']/text()")
            print (title)
            print (location)
        except:
            pass

if __name__ == '__main__':
    spider= tencent_spider()
    spider.run()

## recruit-list-link

"""
 WebDriverWait(self.driver, 1000).until(
                EC.presence_of_element_located(By.XPATH, "//div[@class='recruit-list']/a[@class='recruit-list-link']")
            )
            nextBtn = self.driver.find_element(By.XPATH, "//div[@class='recruit-list']/a[@class='recruit-list-link']")
"""