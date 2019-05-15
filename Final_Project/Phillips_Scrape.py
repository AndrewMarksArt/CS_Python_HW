from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import urllib

import pandas as pd

phillips_contemporary_evening = "https://www.phillips.com/auctions/auction/NY010319"

# path for to_csv
path = 'C:/Users/andre/PycharmProjects/CS_Python_HW/Final_Project/' + 'phillips_contemporary_evening' + '.csv'

# Use URL from above, open a chrome browser, go to URL, then wait
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(phillips_contemporary_evening)
time.sleep(1)

# Scroll to bottom of page to get all lots loaded then wait
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

# close cookies window
element = driver.find_element_by_xpath('//*[@id="cookie-policy"]/div/div/div/div/div[1]/div[2]/button')
element.click()

# Scroll back to top of the page and wait
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(1)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight/12);")
time.sleep(1)

lots = driver.find_element_by_xpath('//*[@class="standard-grid border-top col-xs-12 row"]')
lot_lists = lots.text.splitlines()


del lot_lists[24:27]

keys = ['Lot Number', 'Artist', 'Title', 'Estimate']


all_lots = [lot_lists[x:x+4] for x in range(0, len(lot_lists), 4)]

for i in range(len(all_lots)):
    print(all_lots[i])

# print out the list of dictionaries element by element for readability
# for i in range(len(auction)):
#     print(auction[i])

# df = pd.DataFrame(auction)
# df = df[keys]

# export_csv = df.to_csv(path, index=None, header=True)
# print(df)


