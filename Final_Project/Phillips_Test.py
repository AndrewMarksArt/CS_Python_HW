#
# Andrew Marks, web scrapping final assignment for python insights
# Spring semester 2019
#

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

import pandas as pd


def get_auction_lots(site_url):
    """
    takes a string that is the url for the web site we want to scrape, gets the lot information and returns a list
    :param site_url: string, url of website we want to scrape
    :return: list of auction details
    """

    # Use URL from above, open a chrome browser, go to URL, then wait
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(site_url)
    time.sleep(1)

    # close cookies window
    element = driver.find_element_by_xpath('//*[@id="cookie-policy"]/div/div/div/div/div[1]/div[2]/button')
    element.click()

    # create an empty list to hold auction details
    lot_details = []

    # Loop through lots and get the information needed using find by x path
    # Use try / except if certain details are missing
    for i in range(45):

        lot_num = driver.find_element_by_xpath('//div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/h1').text

        # if a lot was pulled before the auction there is a blank page with only a lot number
        # try and find artist name and if not click the next button to move on
        try:
            artist_name = driver.find_element_by_xpath(
                '//div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/a/h2').text
        except:
            # click the next button to move on the the next auction lot
            element = driver.find_element_by_xpath('//*[@class="arrow next"]')
            element.click()
            time.sleep(0.25)
        title = driver.find_element_by_xpath('//*[@class="title"]').text

        # slice estimate string to separate the low and high estimates
        try:
            est_range = driver.find_element_by_xpath('//*[@class="estimates"]').text
            s_pos = est_range.find('$')
            m_pos = est_range.find('-')
            low_est = est_range[s_pos + 1:m_pos - 1]
            high_est = est_range[m_pos + 2:]
        except:
            low_est = 'no est'
            high_est = 'no est'

        currency = 'USD'

        line_1 = driver.find_element_by_xpath(
            '//div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/p[2]/span[1]').text
        line_2 = driver.find_element_by_xpath(
            '//div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/p[2]/span[2]').text
        line_3 = driver.find_element_by_xpath(
            '//div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/p[2]/span[3]').text
        try:
            line_4 = driver.find_element_by_xpath(
                '//div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/p[2]/span[4]').text
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

        # append all lot details in order to the list
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

        # click the next button to move on the the next auction lot
        element = driver.find_element_by_xpath('//*[@class="arrow next"]')
        element.click()
        time.sleep(0.25)

    return lot_details


def auction_to_dict(lot_details, keys):
    """
    takes a list of lot details and maps them to a dictionary
    :param lot_details: list, details of lots scrapped from site
    :param keys: list of keys to use for dictionary
    :return: dictionary of lot detials
    """

    # use the list of keys to create a dictionary with all the lots in the auction
    n = len(keys)
    all_lots = [lot_details[x:x + n] for x in range(0, len(lot_details), n)]
    auction = [{k: v for k, v in zip(keys, i)} for i in all_lots]

    return auction


# url of site to scrape
phillips_contemporary_evening = "https://www.phillips.com/detail/DONALD-JUDD/NY010319/1"

# list of keys for the auction lot details
keys = ['Lot Number', 'Artist', 'Title', 'Low Est', 'High Est', 'Currency', 'Signed', 'Material(s)', 'Size', 'Year',
            'Provenance', 'Exhibited', 'Literature']

# use functions above to get lot details from the site we want to scrape and then put them in a dictionary
lot_details = get_auction_lots(phillips_contemporary_evening)
auction = auction_to_dict(lot_details, keys)

# path that will be used to save details as a csv
path = 'C:/Users/andre/PycharmProjects/CS_Python_HW/Final_Project/' + 'phillips_contemporary_evening' + '.csv'

# print out the results of the scrapped lots so we can make sure there is no missing information
for i in range(len(auction)):
    print(auction[i])

# create a pandas DataFrame using the auction dictionary
df = pd.DataFrame(auction)
df = df[keys]

# save the Dataframe as a csv file, if file already exists print except message
try:
    export_csv = df.to_csv(path, index=None, header=True)
except:
    print('file already exists')


