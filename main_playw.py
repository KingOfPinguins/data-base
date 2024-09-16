import playwright
from playwright.sync_api import sync_playwright
from parcer import parcer
import yaml
from time import sleep

class run_collecting():
    def __init__(self, LOCATION, INTEREST, CITY) -> None:
        GOOGLE_LINK = "https://www.google.com/maps/@" + str(LOCATION) + "?entry=ttu"

        NAME_DB = INTEREST.replace(' ', '_') + '_' + CITY.replace(' ', '_') # name of DB 

        p = parcer(NAME_DB) # variable
        
        playwright = sync_playwright().start()

        browser = playwright.chromium.launch(headless=False)
        #browser = playwright.
        context = browser.new_context()
        page = context.new_page()
        
        page.goto(GOOGLE_LINK)
        
        page.get_by_role("textbox", name="Поиск на Google Картах").fill(INTEREST)
        sleep(2)
        page.get_by_label("Поиск", exact=True).click()
        sleep(2)
        page.goto("https://www.google.com/maps/search/car/@43.7173166,-79.7076942,10z/data=!4m2!2m1!6e6?entry=ttu")
        sleep(2)
        
        ### SCROLL
        
        #/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]
        #side_bar = page.locator('/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/div[1]')
        #sleep(5)
        print("try scroll")
        #test = page.locator("text=/html/body/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div") 

        #test.scroll_into_view_if_needed()
        #test.scroll_into_view_if_needed()
        #side_bar.scroll_into_view_if_needed()
        page.mouse.wheel(0, 15000)
        print('scroll')
        sleep(2)
        page.mouse.wheel(0, 15000)
        print('scroll')
        sleep(2)
        page.mouse.wheel(0, 15000)
        print('scroll')
        sleep(2)
        page.mouse.wheel(0, 15000)
        print('scroll')
        sleep(5)
        
        ### END

        # ---------------------
        #context.close()
        #browser.close()
        

with open('city_locations.yaml', 'r') as file_y:
    LOCATION_ALL = yaml.safe_load(file_y)

INTEREST = 'car'   
CITY = 'Toronto'  
LOCATION = LOCATION_ALL['canada']['ontario'][CITY]

aa = run_collecting(LOCATION, INTEREST, CITY)