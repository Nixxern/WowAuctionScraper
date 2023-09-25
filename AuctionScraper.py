from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as chromeOptions
import selenium


class Price:
    def __init__(self, g: int, s: int, c: int):
        self.gold = g
        self.silver = s
        self.copper = c

    def getString(self):
        return f"{self.gold} g {self.silver} s {self.copper} c"

    def getcsv(self):
        return f"{self.gold},{self.silver},{self.copper}"


class Scraper:
    # server in format example #eu-tarren-mill
    def __init__(self, server: str):
        options = chromeOptions()
        options.add_argument("headless")
        self.driver = webdriver.Chrome(options)
        self.url = "https://undermine.exchange/" + server + "/"

    def finditem(self, itemid: str):
        foundprice = Price(0, 0, 0)
        url = self.url + itemid

        print("Scraping : " + url)

        self.driver.get(url)

        timeout = 30  # Max wait time before timeout
        try:
            element_present = EC.presence_of_element_located((By.XPATH,
                                                              "/html/body[@class='webp']/div[@class='main']/div[@class='main-result']/div[@class='item']/div[@class='panels']/div[@class='details']/div[@class='scroller']/div[@class='base-stats framed']/table[@class='hidden-region-details']/tr[3]/td[2]/span"))
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutException:
            print("Timed out waiting for page to load")

        goldPrice = self.driver.find_elements(By.XPATH,
                                              "/html/body[@class='webp']/div[@class='main']/div[@class='main-result']/div[@class='item']/div[@class='panels']/div[@class='details']/div[@class='scroller']/div[@class='base-stats framed']/table[@class='hidden-region-details']/tr[3]/td[2]/span/span[@class='gold']")
        silverPrice = self.driver.find_elements(By.XPATH,
                                                "/html/body[@class='webp']/div[@class='main']/div[@class='main-result']/div[@class='item']/div[@class='panels']/div[@class='details']/div[@class='scroller']/div[@class='base-stats framed']/table[@class='hidden-region-details']/tr[3]/td[2]/span/span[@class='silver']")
        copperPrice = self.driver.find_elements(By.XPATH,
                                                "/html/body[@class='webp']/div[@class='main']/div[@class='main-result']/div[@class='item']/div[@class='panels']/div[@class='details']/div[@class='scroller']/div[@class='base-stats framed']/table[@class='hidden-region-details']/tr[3]/td[2]/span/span[@class='copper']")

        if goldPrice:
            for p in goldPrice:
                foundprice.gold = int(p.text.strip())
        if silverPrice:
            for p in silverPrice:
                foundprice.silver = int(p.text.strip())
        if copperPrice:
            for p in copperPrice:
                foundprice.copper = int(p.text.strip())

        return foundprice
