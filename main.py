import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://undermine.exchange/#eu-tarren-mill/191462"

driver.get(url)

time.sleep(7)

elements_with_numbers = driver.find_elements(By.CSS_SELECTOR,
                                             "body > div.main > div.main-result > div.item > div.panels > div.details > div > div.base-stats.framed > table > tr:nth-child(3) > td:nth-child(2) > span")

if elements_with_numbers:

    for element in elements_with_numbers:
        text = element.text.strip()
        print("Hochenblume koster nå:", text)
else:
    print("Elements with numbers not found.")

driver.quit()