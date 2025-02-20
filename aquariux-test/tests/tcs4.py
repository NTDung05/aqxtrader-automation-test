from selenium import webdriver

from GLOBAL_VARIABLES import GLOBAL_VARIABLES
from pages.login_page  import LoginPage
from pages.assets_page import AssetsPage

from pages.common_page import CommonPage

driver = webdriver.Chrome()
common_page = CommonPage(driver)
login_page = LoginPage(driver)

def test_user_able_edit_pending_limit_order():
    #step 1: log in webpage
    login_page.login(GLOBAL_VARIABLES.page_url, GLOBAL_VARIABLES.userName, GLOBAL_VARIABLES.passWord)
    #step 2: Go to Assets Page
    assets_page = AssetsPage(driver)
    assets_page.clickOn_assets_option()
    #step 3: Go to Pending Order tab
    assets_page.clickOn_pending_order_tab()
    assets_page.verify_asset_pending_list_is_displayed()
    #step 4: click on Edit button with limit type and good till day expiry
    assets_page.clickOn_edit_pending_order_button("BUY LIMIT","Good Till Day")
    #step 5: verify edit form
    assets_page.verify_edit_confirm_popup_is_displayed()
    #step 6: edit price, stop loss, profit, expiry
    assets_page.clickOn_increase_price_button()
    assets_page.clickOn_increase_stoploss_button()
    assets_page.clickOn_increase_take_profit_button()
    assets_page.updateExpiryDropdown("Good Till Day")
    #step 7: click on update
    assets_page.clickOn_update_button()
    #step 8: verify edit confirm popup is displayed
    assets_page.verify_edit_confirm_popup_is_displayed()
    #step 9: click on confirm
    assets_page.clickOn_confirm_button()
    #step 10: verify alert
    common_page.verify_successful_notification_alert_is_displayed("Limit Order Updated")

def test_user_able_edit_pending_stop_order():
    # step 1: log in webpage
    login_page.login(GLOBAL_VARIABLES.page_url, GLOBAL_VARIABLES.userName, GLOBAL_VARIABLES.passWord)
    # step 2: Go to Assets Page
    assets_page = AssetsPage(driver)
    assets_page.clickOn_assets_option()
    # step 3: Go to Pending Order tab
    assets_page.clickOn_pending_order_tab()
    assets_page.verify_asset_pending_list_is_displayed()
    # step 4: click on Edit button with stop type and good till cancelled expiry
    assets_page.clickOn_edit_pending_order_button("BUY STOP","Good Till Cancelled")
    # step 5: verify edit form
    assets_page.verify_edit_confirm_popup_is_displayed()
    # step 6: edit price, stop loss, profit, expiry
    assets_page.clickOn_increase_price_button()
    assets_page.clickOn_increase_stoploss_button()
    assets_page.clickOn_increase_take_profit_button()
    assets_page.updateExpiryDropdown("Good Till Cancelled")
    # step 7: click on update
    assets_page.clickOn_update_button()
    # step 8: verify edit confirm popup is displayed
    assets_page.verify_edit_confirm_popup_is_displayed()
    # step 9: click on confirm
    assets_page.clickOn_confirm_button()
    # step 10: verify alert
    common_page.verify_successful_notification_alert_is_displayed("Stop Order Updated")