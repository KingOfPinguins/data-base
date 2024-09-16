
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

EXEC_PATH = "D:\\WORK\\SCRIPTS\\SELENIUM_ALL\\drivers\\"

LIST_ELEM = '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]'

address =    LIST_ELEM[0:-10] + '[2]/div[7]/div[3]'
web_page =   LIST_ELEM[0:-10] + '[2]/div[7]/div[6]'
phone =      LIST_ELEM[0:-10] + '[2]/div[7]/div[5]'


scroll_number = 20

class data_collector():
    def __init__(self, LOCATION, INTEREST, CITY):
        
        logg = log(INTEREST, CITY)
        logg.add_to_log("Start")
        
        sleep(2)
        logg.add_to_log("PROCESS FOR - " + INTEREST + " STARTED")

        start_timer = datetime.datetime.now() # start timer
        GOOGLE_LINK = "https://www.google.ca/maps/@" + str(LOCATION) + "?entry=ttu"
        logg.add_to_log(GOOGLE_LINK)

        NAME_DB = INTEREST.replace(' ', '_') + '_' + CITY.replace(' ', '_') # name of DB 

        p = parcer_simple(NAME_DB) # variable
        
        #prof = r"C:\Users\pc\AppData\Roaming\Mozilla\Firefox\Profiles\nf7q4so2.working-profile"
        prof = r"C:\Users\pc\AppData\Local\Mozilla\Firefox\Profiles\nf7q4so2.working-profile"
        
        
        options = Options()
        options.profile = prof
        options.set_preference("intl.accept_languages", "en-US")

        driver = webdriver.Firefox(options=options)
        #driver = webdriver.Chrome()
        driver.implicitly_wait(5) # wait 10 sec if needed
        logg.add_to_log("open site - " + GOOGLE_LINK)

        driver.get(GOOGLE_LINK)
        
        logg.add_to_log("DATA for searching:" + "\nLOCATION:" + LOCATION + "\nINTEREST:" + INTEREST + "\nCITY:" + CITY )

        element = driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')
        element.send_keys(INTEREST)
        logg.add_to_log("search  - " + INTEREST)

        logg.add_to_log("Insert key-word:" + INTEREST)
        sleep(2)
        check = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[1]/div[1]/button/span') 

        check.click()
        logg.add_to_log("pressed search button")
        
        sleep(2)
        driver.implicitly_wait(10)
        sleep(2)

        # choose list of elements, in the bottom
        list_frame = driver.find_element(By.XPATH, LIST_ELEM)
                                                   #/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]
        logg.add_to_log("List item found:" + str(list_frame))
        counter = 0
        timer = 2
        logg.add_to_log("SCROLLING STARTED")
        for i in range(scroll_number):
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 1500;", list_frame)

            sleep(timer)
            counter += 1
            if counter == 10:
                logg.add_to_log("timer ++ " + str(timer))
                timer += 1
                counter = 0
        logg.add_to_log("SCROLLING DONE ")


        #################################################################################################################
        #data = driver.find_element(By.XPATH, '/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div')

        #company_data = ""
        total_data_list = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]')
        
        logg.add_to_log("SPENT time for" + INTEREST + " - " + str(datetime.datetime.now() - start_timer))
        logg.close_log()
        
        #print(str(total_data_list.text))
        #print('\n\n')
        
        data_for_parcer = total_data_list.text
        p.parce(data_for_parcer)
        driver.close()

def main():
    # get sity list
    with open('city_locations.yaml', 'r') as file_y:
        LOCATION_ALL = yaml.safe_load(file_y)
    
    
    CITYs_USA = 'Orlando' 
    # LOCATION_LIST = [LOCATION_ALL['USA']['Florida'][CITY_USA],
    #                  LOCATION_ALL['canada']['ontario']['Vaughan'],
    #                  LOCATION_ALL['canada']['ontario']['Toronto'],
    #                  LOCATION_ALL['canada']['ontario']['Richmond Hill'],
    #                  LOCATION_ALL['canada']['ontario']['Markham'],
    #                  ]
    
    # Homestead
    # Miami
    # Hollywwood
    # Fort Lauderdale
    # Pompano Beach
    # Boca Raton
    # Orlando
    
    CITYs = ['Orlando', 'Tampa', 'Sarasota', ]
    STATE = 'Florida'
    COUNTRY = 'USA'
    
    LOCATION_LIST = []
    
    # for country in COUNTRYs:
    #     for state in STATES:
    #         for city in CITYs:
    #             LOCATION_LIST.append(LOCATION_ALL[country][state][city])
            
    
    #LOCATION = LOCATION_ALL['USA']['Florida'][CITY]
    INTERESTS = ["ppf",
                "car tint", 
                "auto tinting", 
                "3m ppf", 
                "car detailing shop", 
                "xpel ppf", 
                "sun tek ppf", 
                "kitchen countertop", 
                "stone and tile",
                "paint protection film",
                "tint",
                "tinting"
                ]
    # manager = multiprocessing.Manager()
    # return_dict = manager.dict()
    jobs = []
    
    jobs_counter = 0
    for CITY in CITYs:
        LOCATION = LOCATION_ALL[COUNTRY][STATE][CITY]
        for INTEREST in INTERESTS:
            try:
                print("<<<<<<<<<>>>>>>>>>" + str(len(jobs)))
                if jobs_counter > 4:
                    print("PAUSE")
                    sleep(60)
                    jobs_counter = 0
                #p = Process(target=data_collector, args=(return_dict, LOCATION, INTEREST, ))
                p = Process(target=data_collector, args=(LOCATION, INTEREST, CITY,))
                jobs.append(p)
                p.start()
                jobs_counter += 1
                
            except:
                print("SOMETHING WENT WRONG:", LOCATION, INTEREST, CITY)

    

if __name__ == "__main__":
    main()

