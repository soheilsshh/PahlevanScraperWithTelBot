from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class SportPortalAutomation:
    def __init__(self, username, password):
        self.USER_NAME = username
        self.PASSWORD = password
        self.driver = webdriver.Firefox()

    def open_site(self, url):
        self.driver.get(url)
        print("=========> open site")
        sleep(1)

    def find_elements(self):
        self.username_element = self.driver.find_element(By.ID, "txtusv")
        self.password_element = self.driver.find_element(By.ID, "passv")
        self.check_box_element = self.driver.find_element(By.ID, "txtcode")
        self.submit = self.driver.find_element(By.ID, "btlogin")
        print("=========> find needed elements")
        sleep(1)

    def login(self):
        self.username_element.send_keys(self.USER_NAME)
        self.password_element.send_keys(self.PASSWORD)

        text_textcode = self.driver.find_element(By.ID, "lbcode")
        exe_codetext = eval(text_textcode.text)
        self.check_box_element.send_keys(exe_codetext)
        print("=========> send info into input box and submit")
        self.submit.click()
        sleep(1)

    def navigate_to_courses(self):
        courses = self.driver.find_element(By.XPATH, '//*[@id="nav-accordion"]/li[4]/a')
        courses.click()
        print("=========> click on course link")
        sleep(1)

    def select_course_options(self):
        selecting_list = [
            self.driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_dpfields"]/option[6]'),
            self.driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_dpsalon"]/option[9]')
        ]
        submit_query = self.driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_btreport"]')
        for select in selecting_list:
            print(f"clicking on {select.text}")
            select.click()

        print("click to query")
        sleep(1)
        submit_query.click()
        sleep(3)

    def show_course_details(self):
        try:
            detail_list = [
                self.driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_dlsessions"]/tbody/tr[2]/td/div/div[7]/b[1]'),
                self.driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_dlsessions"]/tbody/tr[2]/td/div/div[7]/b[2]'),
                self.driver.find_element(By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_dlsessions"]/tbody/tr[2]/td/div/div[11]/b')
            ]

            print(f"Total course: {detail_list[0].text}\nNumber of sessions remaining: {detail_list[1].text}\nCapacity per session: {detail_list[2].text}")
        except Exception as e:
            print("There is no session available.")
            print(f"Error: {e}")

    def close_driver(self):
        self.driver.quit()
        print("=========> driver closed")
