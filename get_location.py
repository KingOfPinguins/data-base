import datetime
from time import sleep
from parcer import parcer_simple
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#import multiprocessing
from multiprocessing import Process

from logger import log
import yaml



cities_all = []

with open("city-california.txt", "r") as dat:
    cities_pr = dat.readlines()
    for city in cities_pr:
        cities_all.append(city.replace('\n', ''))

lin = "USA CALIFORNIA Adelanto"

COUNTRY = "USA"
STATE = "CALIFORNIA"
#CITY = "Adelanto"

class locations_collector():
    def __init__(self, COUNTRY, STATE, CITY):
        self.data_lat_long = ""
        start_timer = datetime.datetime.now() # start timer
        options = Options()
        options.set_preference("intl.accept_languages", "en-US")
        driver = webdriver.Firefox(options=options)
        driver.implicitly_wait(5)
        GOOGLE_LINK = "https://www.google.ca/maps/@"
        driver.get(GOOGLE_LINK)
        element = driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')
        element.send_keys(COUNTRY + ' ' + STATE + ' ' + CITY)
        check = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[1]/div[1]/button/span') 

        check.click()
        sleep(3)
        url_ss = driver.current_url.split('/')
        
        lat_long = url_ss[6]
        print(str(CITY) + ': ' + str(lat_long))
        self.data_lat_long = str(CITY) + ': ' + str(lat_long.replace('@', ''))
        sleep(1)
        driver.close()
        
        




if __name__ == "__main__":
    counter = 0
    data = []
    for city in cities_all:
        # try:
        #     if counter >= 6:
        #         sleep(5)
        #         counter = 0
        #     p = Process(target=locations_collector, args=(COUNTRY, STATE, CITY,))
        #     p.start()
        #     counter += 1

                
        # except:
        #     print("SOMETHING WENT WRONG:", COUNTRY, STATE, CITY)
        collector = locations_collector(COUNTRY, STATE, city)
        data.append(collector.data_lat_long)
    print(data)