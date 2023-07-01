from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TicketSpider():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)
        self.login_url = "https://kyfw.12306.cn/otn/resources/login.html"
        self.init_url = "https://kyfw.12306.cn/otn/view/index.html"
        self.search_url = "https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc"
        self.passenger_url = "https://kyfw.12306.cn/otn/confirmPassenger/initDc"

    def get_input(self):
        # self.from_station = input("From: ")
        # self.to_station = input("To: ")
        # self.depart_time = input("Depart_time: ")
        # self.passengers = input("Name: ").split(",")
        # self.trains = input("Trains: ").split(",")
        self.from_station = "北京"
        self.to_station = "上海"
        self.depart_time = "2023-07-13"
        self.passengers = "曲大典"
        self.trains = "G103"


    def _login(self):
        self.driver.get(self.login_url)
        WebDriverWait(self.driver, 1000).until(
            EC.url_to_be(self.init_url)
        )
        print ("Login Success")

    def _order_ticket(self):
        self.driver.get(self.search_url)
        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, "fromStationText"),self.from_station)
        )

        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, "toStationText"), self.to_station)
        )

        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, "train_date"), self.depart_time)
        )

        WebDriverWait(self.driver, 1000).until(
            EC.element_to_be_clickable((By.ID, "query_ticket"))
        )

        searchBtn = self.driver.find_element(By.ID, "query_ticket")
        searchBtn.click()

        WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, ".//tbody[@id='queryLeftTable']/tr"))
        )

        tr_list = self.driver.find_elements(By.XPATH, "//tbody[@id='queryLeftTable']/tr[not(@datatran)]")

        for tr in tr_list:
            train_number = tr.find_element(By.XPATH, ".//a[@class='number']").text
            if train_number in self.trains:
                print ("Found it !")
                left_ticket = tr.find_element(By.XPATH, ".//td[4]").text
                if left_ticket == "有" or left_ticket.isdigit():

                    orderBtn = tr.find_element(By.CLASS_NAME, "btn72")
                    print ("Button Found!")
                    orderBtn.click()

                    WebDriverWait(self.driver, 1000).until(
                        EC.url_to_be(self.passenger_url)
                    )

                    WebDriverWait(self.driver, 1000).until(
                        EC.presence_of_element_located((By.XPATH, ".//ul[@id='normal_passenger_id']/li/label"))

                    )
                    print ("People Found !")
                    passengers_label = self.driver.find_elements(By.XPATH, ".//ul[@id='normal_passenger_id']/li/label")
                    for i in passengers_label:
                        name = i.text
                        if name in self.passengers:
                            i.click()

                    submitBtn = self.driver.find_element(By.ID, "submitOrder_id")

                    print ("Submit Botton Found !")
                    submitBtn.click()

                    WebDriverWait(self.driver, 1000).until(
                        EC.presence_of_element_located((By.XPATH, ".//a[@id='qr_submit_id']"))

                    )

                    purchase_button = self.driver.find_element(By.XPATH, ".//a[@id='qr_submit_id']")
                    print ("Purchase Button Found !")

                    time.sleep(1)
                    while purchase_button:
                        purchase_button.click()
                        purchase_button = self.driver.find_element(By.XPATH, ".//a[@id='qr_submit_id']")
                    return



    def run(self):
        self.get_input()
        self._login()
        self._order_ticket()




if __name__ == '__main__':
    spdier = TicketSpider()
    spdier.run()