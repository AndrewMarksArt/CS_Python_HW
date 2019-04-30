from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from collections import Counter



url = "http://www.sothebys.com/en/auctions/2019/contemporary-art-evening-auction-n10069.html?locale=en"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(3)
driver.get(url)

# scroll to bottom of page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.implicitly_wait(3)

# lot_detail_link = driver.find_element_by_xpath('//*[@id="lot-list"]/article[1]/div[2]/h4[1]')
# element = driver.find_element_by_link_text(lot_detail_link.text)
# element.click()

all_lots = []

for i in range(1, 64):
    lot_info = driver.find_element_by_xpath('//*[@id="lot-list"]/article[' + str(i) + ']/div[2]')
    lot = lot_info.text
    lot_list = lot.splitlines()
    all_lots.append(lot_list)

# scroll back to top
for i in range(2):
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 0);")
    driver.implicitly_wait(3)


artist_names = []
for i in range(len(all_lots)):
    artist_names.append(all_lots[i][1])

print(artist_names)
"""
count_artists = Counter(artist_names)
print(count_artists.items())


for i in artist_names:
    element = driver.find_element_by_link_text(i)
    element.click()
    driver.implicitly_wait(2)
    time.sleep(1)
    driver.execute_script("window.history.go(-1)")
"""


