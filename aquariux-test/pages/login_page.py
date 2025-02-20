from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginPage:
    DemoAccount_Tab = "//div[@data-testid='tab-login-account-type-demo']"
    User_Field=  "//input[@data-testid='login-user-id']"
    Password_Field= "//input[@data-testid='login-password']"
    SignIn_button=  "//button[@data-testid='login-submit']"

    def __init__(self, driver):
       self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def clickOn_Demo_Account_Tab(self):
      demoAccountTab = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH,self.DemoAccount_Tab)))
      demoAccountTab.click()

    def input_username(self,username):
        self.driver.find_element(By.XPATH, self.User_Field).clear()
        self.driver.find_element(By.XPATH, self.User_Field).send_keys(username)
    def input_password(self,password):
        self.driver.find_element(By.XPATH, self.Password_Field).clear()
        self.driver.find_element(By.XPATH, self.Password_Field).send_keys(password)

    def clickOn_signInBtn(self):
       self.driver.find_element(By.XPATH,self.SignIn_button).click()
    
    def login(self,url,username,password):
       self.open_page(url)
       self.clickOn_Demo_Account_Tab()
       self.input_username(username)
       self.input_password(password)
       self.clickOn_signInBtn()
