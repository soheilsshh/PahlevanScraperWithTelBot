import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time

#set the global pass and username
USER_NAME = 40123313
PASSWORD = 6440160877

#create driver 
driver = webdriver.Firefox()

driver.get("https://sport.shahroodut.ac.ir/SportLogin")
#driver.maximize_window()

#define elemnt 
username_elemnt = driver.find_element(By.ID , "txtusv")
pasword_elemnt = driver.find_element(By.ID , "passv")
check_box_element = driver.find_element(By.ID , "txtcode")
submit = driver.find_element(By.ID , "btlogin")

#send key for username
username_elemnt.send_keys(USER_NAME)

#send key for password
pasword_elemnt.send_keys(PASSWORD)

#send key for text code
text_textcode = driver.find_element(By.ID , "lbcode")
exe_codetext = eval(text_textcode.text)
check_box_element.send_keys(exe_codetext)


#create action
action = ActionChains(driver)
action.click(on_element = submit)
action.perform()
WebDriverWait(driver , 600)


#get all of cors
cours = driver.find_element(By.LINK_TEXT , "دوره ها و کلاس ها")
cours.click()


# # Set up the Chrome WebDriver
# driver = webdriver.Chrome()


#     # Open Google
# driver.get("https://sport.shahroodut.ac.ir/SportLogin")
    
#     # Find the search bar and enter a query
# search_box = driver.find_element(By.NAME, "txtusv")
# print(search_box)
# # search_box.send_keys("Selenium with Python")
# # search_box.send_keys(Keys.RETURN)
    
#     # Wait for results to load
# # time.sleep(2)
    
# #     # Get search result titles
# # results = driver.find_elements(By.CSS_SELECTOR, "h3")
# # for index, result in enumerate(results[:5]):  # Print top 5 results
# #     print(f"{index+1}. {result.text}")
    

# # driver.quit()



# #url for scraping : https://sport.shahroodut.ac.ir/SportLogin

# URL = 'https://sport.shahroodut.ac.ir/SportLogin'
# page = requests.get(URL)

# soup = BeautifulSoup(page.content , 'html.parser')

# result = soup.find_all("div" , class_="text-right")
# print(result)