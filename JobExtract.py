from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from lxml import etree
import re

class LagouSpider():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)
        self.url = "https://www.lagou.com/wn/jobs?labelWords=&fromSearch=true&suginput=&kd=python"

    def run(self):
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source
            self.parse_list_page(source)
            WebDriverWait(self.driver,1000).until(
                EC.presence_of_element_located((By.XPATH, "//ul[@class='lg-pagination']//li[last()]"))
            )
            nextBtn = self.driver.find_element(By.XPATH,"//ul[@class='lg-pagination']//li[last()]")
            if "lg-pagination-next lg-pagination-disabled" in nextBtn.get_attribute("class"):
                break
            else:
                nextBtn.click()
            time.sleep(1)


    def parse_list_page(self, source):
        html = etree.HTML(source)
        infos = html.xpath("//div[@class='item__10RTO']")
        for info in infos:
            import_info = info.xpath(".//a[@id='openWinPostion']/text()")
            title = import_info[0]
            location = import_info[1]
            location = re.sub(r'[\[\]]', '', location)





if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()