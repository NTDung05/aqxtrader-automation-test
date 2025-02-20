from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TradePage:
    marketList = "//div[@data-testid='watchlist-list-item']"
    market = "//div[@data-testid='watchlist-symbol' and text() ='JNJ.std']"
    orderTypeDropdown = "//div[@data-testid='trade-dropdown-order-type']"
    increaseSizebutton = "//div[@data-testid='trade-input-volume-increase']"

    incresetStopLossButton = "//div[@data-testid='trade-input-stoploss-price-increase']"
    decreaseStopLossbutton = "//div[@data-testid='trade-input-stoploss-price-decrease']"

    increaseTakeProfitbutton = "//div[@data-testid='trade-input-takeprofit-price-increase']"
    decresetTakeProfitbutton = "//div[@data-testid='trade-input-takeprofit-price-decrease']"

    orderButton = "//button[@data-testid='trade-button-order']"
    tradeConfirmationPopup = "//div[@data-testid='trade-confirmation-modal']"
    confirmButton = "//button[@data-testid='trade-confirmation-button-confirm']"

    limitOrderType = "//div[@data-testid='trade-dropdown-order-type-limit']"
    stopOrderType = "//div[@data-testid='trade-dropdown-order-type-stop']"

    increasePriceButton = "//div[@data-testid='trade-input-price-increase']"

    expiryDropdown = "//div[@data-testid='trade-dropdown-expiry']"
    goodTillCancelledType = "//div[@data-testid='trade-dropdown-expiry-good-till-cancelled']"
    goodTillDayType =  "//div[@data-testid='trade-dropdown-expiry-good-till-day']"

    def __init__(self,driver):
       self.driver = driver

    def clickOn_market(self,marketName):
        marketList = WebDriverWait(self.driver, 10).until(
                  EC.presence_of_element_located((By.XPATH,self.marketList)))
        self.driver.find_element(By.XPATH,"//div[@data-testid='watchlist-symbol' and text() ='"+marketName+"']").click()

    def clickOn_increase_size(self):
        self.driver.find_element(By.XPATH,self.increaseSizebutton).click()

    def clickOn_increase_stoploss(self):
        self.driver.find_element(By.XPATH,self.incresetStopLossButton).click()

    def clickOn_decrease_stoploss(self):
        self.driver.find_element(By.XPATH,self.decreaseStopLossbutton).click()

    def clickOn_increase_take_profit(self):
        self.driver.find_element(By.XPATH,self.increaseTakeProfitbutton).click()

    def clickOn_decrease_take_profit(self):
        self.driver.find_element(By.XPATH,self.decresetTakeProfitbutton).click()

    def clickOn_order_button(self):
        assert self.driver.find_element(By.XPATH, self.orderButton).is_enabled()
        self.driver.find_element(By.XPATH,self.orderButton).click()

    def verify_order_type_is_displayed(self):
        orderTypeDropdown = WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located((By.XPATH,self.orderTypeDropdown)))

    def verify_trade_confirmation_popup_is_displayed(self):
     assert  self.driver.find_element(
         By.XPATH,self.tradeConfirmationPopup).is_displayed()

    def clickOn_confirmation_button(self):
        self.driver.find_element(By.XPATH,self.confirmButton).click()


    def select_order_type_dropdown(self,type):
        self.driver.find_element(By.XPATH,self.orderTypeDropdown).click()
        if type == "Limit":
            self.driver.find_element(By.XPATH, self.limitOrderType).click()
        else:
            self.driver.find_element(By.XPATH, self.stopOrderType).click()

    def clickOn_increase_price(self):
        self.driver.find_element(By.XPATH,self.increasePriceButton).click()

    def select_expiry_dropdown(self, type):
        self.driver.find_element(By.XPATH,self.expiryDropdown).click()
        if type=="Goods Till Cancelled":
            self.driver.find_element(By.XPATH,self.goodTillCancelledType).click()
        else:
            self.driver.find_element(By.XPATH,self.goodTillDayType).click()



