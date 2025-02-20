import time

from selenium import webdriver

from pages import trade_page
from pages.login_page  import LoginPage
from pages.trade_page import TradePage
from pages.common_page import CommonPage
from GLOBAL_VARIABLES import GLOBAL_VARIABLES
import time

driver = webdriver.Chrome()
common_page = CommonPage(driver)
login_page = LoginPage(driver)
def test_user_able_place_Limit_order_with_goods_till_day_expiry():
        # step 1: log in webpage
         login_page.login(GLOBAL_VARIABLES.page_url,GLOBAL_VARIABLES.userName,GLOBAL_VARIABLES.passWord)
        #step 2: Select limit order type
         trade_page = TradePage(driver)
         trade_page.verify_order_type_is_displayed()
         trade_page.select_order_type_dropdown("Limit")
        #step 3: Edit size, price
         trade_page.clickOn_increase_size()
         trade_page.clickOn_increase_price()
        #step 4: Select expiry
         trade_page.select_expiry_dropdown("Goods Till Day")
        #step 5: Click on Place Order button
         trade_page.clickOn_order_button()
        #step 6: Verify trade confirmation popup
         trade_page.verify_trade_confirmation_popup_is_displayed()
        #step 7: Click on confirm button
         trade_page.clickOn_confirmation_button()
        #step 8: Verify Alert
         common_page.verify_successful_notification_alert_is_displayed("Limit Order Submitted")


def test_user_able_place_Limit_order_with_goods_till_cancelled_expiry():
    # step 1: log in webpage
    login_page.login(GLOBAL_VARIABLES.page_url, GLOBAL_VARIABLES.userName, GLOBAL_VARIABLES.passWord)
    # step 2: Select limit order type
    trade_page = TradePage(driver)
    trade_page.verify_order_type_is_displayed()
    trade_page.select_order_type_dropdown("Limit")
    # step 3: Edit size, price
    trade_page.clickOn_increase_size()
    trade_page.clickOn_increase_price()
    # step 4: Select expiry
    trade_page.select_expiry_dropdown("Goods Till Cancelled")
    # step 5: Click on Place Order button
    trade_page.clickOn_order_button()
    # step 6: Verify trade confirmation popup
    trade_page.verify_trade_confirmation_popup_is_displayed()
    # step 7: Click on confirm button
    trade_page.clickOn_confirmation_button()
    # step 8: Verify Alert
    common_page.verify_successful_notification_alert_is_displayed("Limit Order Submitted")

def test_user_able_place_Stop_order_with_goods_till_day_expiry():
    # step 1: log in webpage
    login_page.login(GLOBAL_VARIABLES.page_url, GLOBAL_VARIABLES.userName, GLOBAL_VARIABLES.passWord)
    # step 2: Select stop order type
    trade_page = TradePage(driver)
    trade_page.verify_order_type_is_displayed()
    trade_page.select_order_type_dropdown("Stop")
    # step 3: Edit size, price
    trade_page.clickOn_increase_size()
    trade_page.clickOn_increase_price()
    # step 4: Select expiry
    trade_page.select_expiry_dropdown("Goods Till Day")
    # step 5: Click on Place Order button
    trade_page.clickOn_order_button()
    # step 6: Verify trade confirmation popup
    trade_page.verify_trade_confirmation_popup_is_displayed()
    # step 7: Click on confirm button
    trade_page.clickOn_confirmation_button()
    # step 8: Verify Alert
    common_page.verify_successful_notification_alert_is_displayed("Stop Order Submitted")


def test_user_able_place_Stop_order_with_goods_till_cancelled_expiry():
    # step 1: log in webpage
    login_page.login(GLOBAL_VARIABLES.page_url, GLOBAL_VARIABLES.userName, GLOBAL_VARIABLES.passWord)
    # step 2: Select stop order type
    trade_page = TradePage(driver)
    trade_page.verify_order_type_is_displayed()
    trade_page.select_order_type_dropdown("Stop")
    # step 3: Edit size, price
    trade_page.clickOn_increase_size()
    trade_page.clickOn_increase_price()
    # step 4: Select expiry
    trade_page.select_expiry_dropdown("Goods Till Cancelled")
    # step 5: Click on Place Order button
    trade_page.clickOn_order_button()
    # step 6: Verify trade confirmation popup
    trade_page.verify_trade_confirmation_popup_is_displayed()
    # step 7: Click on confirm button
    trade_page.clickOn_confirmation_button()
    # step 8: Verify Alert
    common_page.verify_successful_notification_alert_is_displayed("Stop Order Submitted")