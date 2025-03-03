import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

#set the global pass and username
USER_NAME = 40123313
PASSWORD = 6440160877

#create driver 
driver = webdriver.Firefox()

driver.get("https://sport.shahroodut.ac.ir/SportLogin")
print("=========> open site")
sleep(1)
#driver.maximize_window()

#define elemnt 
username_elemnt = driver.find_element(By.ID , "txtusv")
pasword_elemnt = driver.find_element(By.ID , "passv")
check_box_element = driver.find_element(By.ID , "txtcode")
submit = driver.find_element(By.ID , "btlogin")
print("=========> finde needed elements")
sleep(1)

#send key for username
username_elemnt.send_keys(USER_NAME)

#send key for password
pasword_elemnt.send_keys(PASSWORD)

#send key for text code
text_textcode = driver.find_element(By.ID , "lbcode")
exe_codetext = eval(text_textcode.text)
check_box_element.send_keys(exe_codetext)
print("=========> send info into input box and submit")
submit.click()
sleep(1)

#get all of cors
cours = driver.find_element(By.XPATH , '//*[@id="nav-accordion"]/li[4]/a')
cours.click()
print("=========>  click on course linke")
sleep(1)

#selecting course
selecting_list = [driver.find_element(By.XPATH , '//*[@id="ctl00_ContentPlaceHolder1_dpfields"]/option[6]'),
                  driver.find_element(By.XPATH , '//*[@id="ctl00_ContentPlaceHolder1_dpsalon"]/option[9]')]
for select in selecting_list:
    print(f"clicking on {select.text}")
    select.click()
 




#finish
# print ("Done")
# driver.quit()
# print("Finished")    


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