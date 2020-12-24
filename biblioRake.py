from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.select import Select
from time import sleep
from requests import get
from selenium.common.exceptions import NoSuchElementException
from os import system

from tests import test
from userDetails import email, passwd


url = "https://biblioteka.netlify.app/"
unitCodes = ['SPH309', 'SPH329', 'SPH306', 'SPH337', 'SPH317', 'SPH324', 'SPH336', 'SPH337', 'SPH317',]
# unitCodes = [ 'SPH324']


#initiated driver
driver = webdriver.Chrome(executable_path="/home/gamin3/Desktop/schoolWork/bibRake/webdrivers/chromedriver")
#============================================ [X-PATHS] ===============
#page1

inputXpath = '//*[@id="root"]/div/div[3]/div[2]/div/input'
# resultsXpath = '//*[@id="root"]/div/div[3]/div[2]/div[2]/ul/button[1]'
resultsXpath = '//*[@id="root"]/div/div[3]/div[2]/div[2]/ul/button/span[1]/li'
ulXpath = '//*[@id="root"]/div/div[3]/div[2]/ul'

# gDriveLnk = '//*[@id="root"]/div/div[3]/div[3]/ul/div[1]/li/a'
# //*[@id="root"]/div/div[3]/div[3]/ul/div[1]/li/a/span[1]

downloadFrom = '/html/body/div[3]/div[3]/div/div[3]/div[2]/div[2]/div[3]'

# ingineBreak = '"/html/body/div[3]/div[3]/div/div[3]/div[2]/div[2]/div[3]'
userNameXpath = '//*[@id="identifierId"]'
nextXpath = '//*[@id="identifierNext"]/div/button/div[2]'


for unit in unitCodes:

    #start session
    driver.get(url)

    #search unit content
    driver.find_element_by_xpath(inputXpath).send_keys(unit + u'\ue007')
    sleep(4)
    #go to unit
    driver.find_element_by_xpath(resultsXpath).click()
    sleep(4)

    links = []

    #getting google drive links from the website
    for i in range(1,19):
        try:
            gDriveLnk = f'//*[@id="root"]/div/div[3]/div[3]/ul/div[{i}]/li/a'
            link = driver.find_element_by_xpath(gDriveLnk).get_attribute('href')
            # print("Here")
            links.append(link)
        except NoSuchElementException:
            pass

    print("\n\n\tlinks Successfully scrapped \n\n ")
    # driver.close()

    for l in links:
        try:
            driver.get(url = l)
            driver.find_element_by_xpath(downloadFrom).click()
        except NoSuchElementException:
            driver.find_element_by_xpath(userNameXpath).send_keys(email)
            driver.find_element_by_xpath(nextXpath).click()

        sleep(4)
        # driver.close()

        print("Document downloaded successfully")

    test(unit)
    print("\tSuccess")
