from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

pd.set_option("display.max_columns", 30)

# URLs for auctions we want to get data from
christies_imp_mod_evening = "https://www.christies.com/salelanding/index.aspx?lid=1&intsaleid=28066&dt=274201912049&saletitle="
christies_imp_mod_day = "https://www.christies.com/salelanding/index.aspx?lid=1&intsaleid=28068&dt=304201913323&saletitle="
christies_contemporary_evening = "https://www.christies.com/salelanding/index.aspx?lid=1&intsaleid=28020&dt=3042019151828&saletitle="
christies_contemporary_morning = "https://www.christies.com/salelanding/index.aspx?lid=1&intsaleid=28019&dt=3042019153918&saletitle="

# Path for saving to CSV
path = 'C:/Users/andre/PycharmProjects/CS_Python_HW/Final_Project/' + 'christies_contemporary_morning' + '.csv'

# Use URL from above, open a chrome browser, go to URL, then wait
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(christies_contemporary_morning)
driver.implicitly_wait(5)

# click ok to cookies button
time.sleep(1)
element = driver.find_element_by_xpath('//*[@id="index"]/div[1]/div[2]/div[4]/div[2]/div')
element.click()

# Scroll to bottom of page to get all lots loaded then wait
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

# Click load all lots button
element = driver.find_element_by_xpath('//*[@id="loadAllUpcomingPast"]')
element.click()
time.sleep(1)

# Scroll to bottom of page to get all lots loaded then wait
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)

# Scroll back to top of the page and wait
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(1)

# click 1st lot for imp/mod evening
# element = driver.find_element_by_xpath('//*[@id="lot_6202437"]/div/div/a')
# for imp/mod day
# element = driver.find_element_by_xpath('//*[@id="lot_6202501"]/div/div/a')
# Contemporary evening
# element = driver.find_element_by_xpath('//*[@id="lot_6205125"]/div/div/a')
element = driver.find_element_by_xpath('//*[@id="lot_6204698"]/div/div/a')
element.click()

lot_info = []
all_lots = []
# loop through all lots
for i in range(167):
    try:
        element = driver.find_element_by_xpath('//*[@id="close_signup"]')
        element.click()
    except:
        print('pop up not found')

    # get lot number
    lot_number = driver.find_element_by_xpath('//*[@id="main_center_0_lblLotNumber"]')

    # get artist name and remove (birth-death)
    name = driver.find_element_by_xpath('//*[@id="main_center_0_lblLotPrimaryTitle"]').text
    pos = name.find('(')
    artist_name = name[:pos-1]

    # get title of work
    title = driver.find_element_by_xpath('//*[@id="main_center_0_lblLotSecondaryTitle"]')

    # get estimate
    estimate = driver.find_element_by_xpath('//*[@id="main_center_0_lblPriceEstimatedPrimary"]')

    # set currency
    currency = 'USD'

    # get artist age born - died
    start_pos = name.find('(')
    end_pos = name.find(')')
    artist_age = name[start_pos+1:end_pos]

    # get details
    details_raw = driver.find_element_by_xpath('//*[@id="main_center_0_lblLotDescription"]')
    details = details_raw.text.splitlines()
    try:
        signed = details[2]
        medium = details[3]
        size = details[4]
        date = details[5]
    except:
        signed = 'NaN'
        medium = 'NaN'
        size = 'NaN'
        date = 'NaN'

    # get provenance
    try:
        provenance = driver.find_element_by_xpath('//*[@id="main_center_0_lblLotProvenance"]').text
    except:
        provenance = ''

    # get exhibition info
    exhibited = ''

    # put everything into a list
    lot_info = [lot_number.text,
                artist_name,
                title.text,
                estimate.text,
                currency,
                artist_age,
                signed,
                medium,
                size,
                date,
                provenance,
                exhibited]

    # put list of lot info into list of lots
    all_lots.append(lot_info)

    try:
        element = driver.find_element_by_xpath('//*[@id="main_center_0_lnkNextLot"]')
        element.click()
        #time.sleep(1)
    except:
        print('end of lots')

# Elements to grab
keys = ['Lot Number', 'Artist', 'Title', 'Estimate', 'Currency', 'Artist Age', 'Signed', 'Medium', 'Size', 'Date', 'Provenance', 'Exhibited']
auction = [{k:v for k,v in zip(keys, i)} for i in all_lots]

df = pd.DataFrame(auction)
df = df[keys]

export_csv = df.to_csv(path, index=None, header=True)
print(df)
