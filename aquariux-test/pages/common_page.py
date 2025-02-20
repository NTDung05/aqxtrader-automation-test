from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CommonPage:
    notiAlert = "//div[@data-testid = 'notification-description']"
    notiTitle = "//div[@data-testid = 'notification-title']"

    def __init__(self, driver):
        self.driver = driver

    def verify_successful_notification_alert_is_displayed(self, message):
       notiAlert = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,self.notiAlert )))
       assert notiAlert.is_displayed()
       if self.driver.find_element(By.XPATH,self.notiTitle).text == message:
           print("successful")

       else:
           print("failed")
