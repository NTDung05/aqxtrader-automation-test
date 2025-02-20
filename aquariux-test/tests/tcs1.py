from selenium import webdriver
from pages.login_page  import LoginPage
from pages.trade_page import TradePage
from pages.common_page import CommonPage
from GLOBAL_VARIABLES import GLOBAL_VARIABLES


marketName = "DASHUSD.std"

def test_user_able_Market_with_Stop_Loss_and_Take_Profit():
         driver = webdriver.Chrome()
         common_page = CommonPage(driver)
        #step1: login webpage
         login_page = LoginPage(driver)
         login_page.login(GLOBAL_VARIABLES.page_url,GLOBAL_VARIABLES.userName,GLOBAL_VARIABLES.passWord)
        #step 2: edit size, stop loss, profit
         trade_page = TradePage(driver)
         trade_page.clickOn_market(marketName)
         trade_page.verify_order_type_is_displayed()
         trade_page.clickOn_increase_size()
         trade_page.clickOn_increase_stoploss()
         trade_page.clickOn_increase_take_profit()
        #step 3: click on "Place Buy Order" button
         trade_page.clickOn_order_button()
         trade_page.verify_trade_confirmation_popup_is_displayed()
         trade_page.clickOn_confirmation_button()
        #step 4: verify successful alert
         common_page.verify_successful_notification_alert_is_displayed("Market Order Submitted")
