from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

import pandas as pd

phillips_contemporary_evening = "https://www.phillips.com/detail/DONALD-JUDD/NY010319/1"

# path for to_csv
path = 'C:/Users/andre/PycharmProjects/CS_Python_HW/Final_Project/' + 'phillips_contemporary_evening' + '.csv'

# Use URL from above, open a chrome browser, go to URL, then wait
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(phillips_contemporary_evening)
time.sleep(1)

# close cookies window
element = driver.find_element_by_xpath('//*[@id="cookie-policy"]/div/div/div/div/div[1]/div[2]/button')
element.click()


lot_details = []
# Loop through lots
for _ in range(45):
    lot_num = driver.find_element_by_xpath('//div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/h1').text
    artist_name = driver.find_element_by_xpath('//div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/a/h2').text
    title = driver.find_element_by_xpath('//*[@class="title"]').text
    try:
        est_range = driver.find_element_by_xpath('//*[@class="estimates"]').text
        s_pos = est_range.find('$')
        m_pos = est_range.find('-')
        low_est = est_range[s_pos+1:m_pos-1]
        high_est = est_range[m_pos+2:]
    except:
        low_est = 'no est'
        high_est = 'no est'

    currency = 'USD'

    line_1 = driver.find_element_by_xpath('//div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/p[2]/span[1]').text
    line_2 = driver.find_element_by_xpath('//div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/p[2]/span[2]').text
    line_3 = driver.find_element_by_xpath('//div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/p[2]/span[3]').text
    try:
        line_4 = driver.find_element_by_xpath('//div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/p[2]/span[4]').text
    except:
        line_4 = ''

    if line_4 == '':
        signed = ''
        material = line_1
        size = line_2
        year = line_3
    else:
        signed = line_1
        material = line_2
        size = line_3
        year = line_4

    try:
        provenance = driver.find_element_by_xpath('//div/div[2]/div[1]/div/div[1]/div[3]/ul/li[2]/p[2]').text
    except:
        provenance = ''

    try:
        exhibited = driver.find_element_by_xpath('//div/div[2]/div[1]/div/div[1]/div[3]/ul/li[3]/p[2]').text
    except:
        exhibited = ''

    try:
        literature = driver.find_element_by_xpath('//div/div[2]/div[1]/div/div[1]/div[3]/ul/li[4]/p[2]').text
    except:
        literature = ''


    lot_details.append(lot_num)
    lot_details.append(artist_name)
    lot_details.append(title)
    lot_details.append(low_est)
    lot_details.append(high_est)
    lot_details.append(currency)
    lot_details.append(signed)
    lot_details.append(material)
    lot_details.append(size)
    lot_details.append(year)
    lot_details.append(provenance)
    lot_details.append(exhibited)
    lot_details.append(literature)

    element = driver.find_element_by_xpath('//*[@class="arrow next"]')
    element.click()
    time.sleep(0.25)

keys = ['Lot Number', 'Artist', 'Title', 'Low Est', 'High Est', 'Currency', 'Signed', 'Material(s)', 'Size', 'Year', 'Provenance', 'Exhibited', 'Literature']
n = len(keys)
all_lots = [lot_details[x:x+n] for x in range(0, len(lot_details), n)]
auction = [{k:v for k,v in zip(keys, i)} for i in all_lots]

for i in range(len(auction)):
    print(auction[i])


df = pd.DataFrame(auction)
df = df[keys]

try:
    export_csv = df.to_csv(path, index=None, header=True)
except:
    print('file already exists')


# print(df)
