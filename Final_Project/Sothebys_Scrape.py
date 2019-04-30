from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# pd.set_option('display.max_columns', 10)

# URLs for auctions we want to get data from
contemporary_art_evening_auction = "http://www.sothebys.com/en/auctions/2019/contemporary-art-evening-auction-n10069.html?locale=en"
contemporary_art_day = 'http://www.sothebys.com/en/auctions/2019/contemporary-art-day-n10070.html?locale=en'
impressionist_modern_art_day = 'http://www.sothebys.com/en/auctions/2019/impressionist-modern-art-day-n10068.html?locale=en'
impressionist_modern_art_evening = 'http://www.sothebys.com/en/auctions/2019/impressionist-modern-art-evening-n10067.html?locale=en'
american_art = 'http://www.sothebys.com/en/auctions/2019/american-art-n10074.html?locale=en'

# path for to_csv
path = 'C:/Users/andre/PycharmProjects/CS_Python_HW/Final_Project/' + 'contemporary_art_evening_auction' + '.csv'

# Use URL from above, open a chrome browser, go to URL, then wait
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(contemporary_art_evening_auction)
time.sleep(1)

# Scroll to bottom of page to get all lots loaded then wait
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

# Grab basic lot info
# Lot Number: , Artist Name: , Title: , Estimate: , USD:
numb_lots_text = driver.find_element_by_xpath('//*[@id="bodyWrap"]/div[3]/div[1]/div[3]/div[1]/div[1]/span[2]')
numb_lots = numb_lots_text.text.split()

N = int(numb_lots[-1])
all_lots = []

for i in range(1, N+1):
    lot_info = driver.find_element_by_xpath('//*[@id="lot-list"]/article[' + str(i) + ']/div[2]')
    lot_list = lot_info.text.splitlines()
    all_lots.append(lot_list)
    time.sleep(0.05)

# Scroll back to top of the page and wait
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(1)

# Click first lot to get details
element = driver.find_element_by_link_text(all_lots[0][1])
element.click()
time.sleep(1)

# grab lot details, append new details, click next to loop through all lots
for i in range(len(all_lots)):
    # get details
    try:
        artist_life = driver.find_element_by_xpath('//*[@id="bodyWrap"]/div[7]/div[5]/div[2]/div[2]')
    except:
        artist_life = ''
    try:
        lot_details = driver.find_element_by_xpath('//*[@id="bodyWrap"]/div[7]/div[5]/div[2]/div[4]/div')
    except:
        lot_details = ''
    try:
        provenance = driver.find_element_by_xpath('//*[@id="bodyWrap"]/div[7]/div[5]/div[2]/div[5]')
    except:
        provenance = ''
    try:
        exhibited = driver.find_element_by_xpath('//*[@id="bodyWrap"]/div[7]/div[5]/div[2]/div[6]')
    except:
        exhibited = ''

    # append the new lot details
    if artist_life == '':
        all_lots[i].append(artist_life)
    else:
        all_lots[i].append(artist_life.text)
    if lot_details == '':
        all_lots[i].append(lot_details)
    else:
        all_lots[i].append(lot_details.text)
    if provenance == '':
        all_lots[i].append(provenance)
    else:
        all_lots[i].append(provenance.text)
    if exhibited == '':
        all_lots[i].append(exhibited)
    else:
        all_lots[i].append(exhibited.text)
    print(all_lots[i])

    # click next button
    element = driver.find_element_by_xpath('//*[@id="bodyWrap"]/div[4]/a[2]')
    element.click()
    time.sleep(1)

print('\n' + '----------------------------' + '\n')

# take list of list (all_lots) and turn it into a list of dictionaries (auction) using the keys below
keys = ['Lot Number', 'Artist', 'Title', 'Estimate', 'Currency', 'Artist Age', 'Details', 'Provenance', 'Exhibited']
auction = [{k:v for k,v in zip(keys, i)} for i in all_lots]

# print out the list of dictionaries element by element for readability
# for i in range(len(auction)):
#     print(auction[i])

df = pd.DataFrame(auction)
df = df[keys]

export_csv = df.to_csv(path, index=None, header=True)
print(df)
