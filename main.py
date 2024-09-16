
import datetime
from time import sleep
from parcer import parcer
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import multiprocessing
from multiprocessing import Process

from logger import log
import yaml

EXEC_PATH = "D:\\WORK\\SCRIPTS\\SELENIUM_ALL\\drivers\\"
#GOOGLE_LINK = "https://www.google.com/maps/@44.2608014,-81.281664,7z?entry=ttu"

#LIST_ELEM = '/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]'
#LIST_ELEM = '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div'
LIST_ELEM = '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]'
#            /html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[3]/div/a                
#            /html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[3]/div/a  
#            /html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[23]/div/a     
#            /html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[29]/div/a

address =    LIST_ELEM[0:-10] + '[2]/div[7]/div[3]'
web_page =   LIST_ELEM[0:-10] + '[2]/div[7]/div[6]'
phone =      LIST_ELEM[0:-10] + '[2]/div[7]/div[5]'


scroll_number = 15

class data_collector():
    def __init__(self, return_dict, LOCATION, INTEREST, CITY):
        
        logg = log(INTEREST, CITY)
        logg.add_to_log("Start")
        
        sleep(2)
        logg.add_to_log("PROCESS FOR -" + INTEREST + "STARTED")

        start_timer = datetime.datetime.now() # start timer
        GOOGLE_LINK = "https://www.google.com/maps/@" + str(LOCATION) + "?entry=ttu"
        logg.add_to_log(GOOGLE_LINK)

        NAME_DB = INTEREST.replace(' ', '_') + '_' + CITY.replace(' ', '_') # name of DB 

        p = parcer(NAME_DB) # variable

        driver = webdriver.Firefox()
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
        for i in range(scroll_number):
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + 1500;", list_frame)
            logg.add_to_log("One scroll - 1500")
            try:
                    check_end = driver.find_element(By.XPATH, LIST_ELEM + '/div[' + str(i) + ']/div/p/span/span')
                    logg.add_to_log("counter: " + str(i))
                    #check_end = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[91]/div/p/span/span')
                    
                    if "Больше результатов нет" in check_end.text:
                        logg.add_to_log("--- NO MORE RESULTS ---")
                        break
            except:
                logg.add_to_log("--- CONTINUE ---")
                sleep(2)

            sleep(timer)
            counter += 1
            if counter == 10:
                logg.add_to_log("timer ++ " + str(timer))
                timer += 1
                counter = 0


        #################################################################################################################
        #data = driver.find_element(By.XPATH, '/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div')

        #company_data = ""
        total_data_list = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]')
        done = 0
        counter = 1
        item_counter = 1
        for item in range(1000):
            logg.add_to_log("GETTING DATA counter: " + str(item))
            try:
                item_data = driver.find_element(By.XPATH, LIST_ELEM + '/div[' + str(item_counter) + ']/div/a')
                logg.add_to_log("element found from list of elements " + str(LIST_ELEM + '/div[' + str(item_counter) + ']/div/a'))
                item_data.click()
                logg.add_to_log("element clicked")
                try:
                    check_end = driver.find_element(By.XPATH, LIST_ELEM + '/div[' + str(item_counter) + ']/div/p/span/span')
                    logg.add_to_log("counter: " + str(item))
                    #check_end = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[91]/div/p/span/span')
                    
                    if "Больше результатов нет" in check_end.text:
                        logg.add_to_log("--- NO MORE RESULTS ---")
                        #break
                except:
                    logg.add_to_log("--- CONTINUE ---")
                #item_data.click()
                #logg.add_to_log("element clicked")
                sleep(2)
                
                #/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]
                #   To Do: delete this part - start
                data_from_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]')
                                                                  #'/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]'
                logg.add_to_log("get data from element " + str(data_from_element.text))
                #if "Предложить правку" in data_from_element.text or len(data_from_element.text) <= 1 : # adopt this line
                #    data_from_element = driver.find_element(By.XPATH, '/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[7]')

                #name = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[8]/div[9]/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/h1')
                #logg.add_to_log("get name from element " + str(name.text))
                #   To Do: delete this part - end
                
                # def_addr = "NO Address"
                # try:
                #     address_web = driver.find_element(By.XPATH, address)
                #     def_addr = address_web.text
                #     logg.add_to_log("def_addr " + str(def_addr))
                # except:
                #     logg.add_to_log("address not found")

                # def_web_page = "NO Web Page"
                # try:
                #     webpage = driver.find_element(By.XPATH, web_page)
                #     def_web_page = webpage.text
                #     logg.add_to_log("def_web_page " + str(def_web_page))
                # except:
                #     logg.add_to_log("web_page not found")

                # def_phone = "NO Phone"
                # try:
                #     phone_web = driver.find_element(By.XPATH, phone)
                #     def_phone = phone_web.text
                #     logg.add_to_log("def_phone " + str(def_phone))
                # except:
                #     logg.add_to_log("def_phone not found")
                
                logg.add_to_log("<<<< " + '-' + str(LOCATION) + '-' + INTEREST + '-' + CITY + '-' + str(counter) + '-' + " >>>>")

                item_counter = item_counter + 2
                counter = counter + 1

                data_for_parsing = str(data_from_element.text)
                p.parce(data_for_parsing, item + 1)
                logg.add_to_log("data in the parcer")

                done = 0

                return_dict['INTEREST'] = INTEREST
                return_dict['LOCATION'] = LOCATION
                return_dict['CITY'] = CITY
                return_dict['COUNTER'] = str(counter)

            except:
                logg.add_to_log("Done except? - done: " + str(done))
                done = done + 1
                item_counter = item_counter + 2
                if done >= 10:
                    logg.add_to_log("break")
                    
                    break
        logg.add_to_log("SPENT time for" + INTEREST + " - " + str(datetime.datetime.now() - start_timer))
        logg.close_log()
        
        print(str(total_data_list.text))
        print('\n\n')

def main():
    # get sity list
    with open('city_locations.yaml', 'r') as file_y:
        LOCATION_ALL = yaml.safe_load(file_y)
    
    CITY = 'Homestead'  
    LOCATION = LOCATION_ALL['USA']['Florida'][CITY]
    INTERESTS = [#"ppf",
                "car tint", 
                #"auto tinting", 
                #"3m ppf", 
                #"car detailing shop", 
                #"xpel ppf", 
                #"sun tek ppf", 
                #"kitchen countertop", 
                #"stone and tile",
                #"paint protection film",
                #"tint",
                #"tinting"
                ]
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []
    
    for INTEREST in INTERESTS:
        #start_timer = datetime.datetime.now()
        #return_dict = {}
        
        try:
            p = Process(target=data_collector, args=(return_dict, LOCATION, INTEREST, CITY,))
            jobs.append(p)
            p.start()
            
        except:
            print("SOMETHING WENT WRONG:", LOCATION, INTEREST, CITY)

    

    

if __name__ == "__main__":
    main()

