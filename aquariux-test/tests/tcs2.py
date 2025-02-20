from selenium import webdriver

from GLOBAL_VARIABLES import GLOBAL_VARIABLES
from pages.login_page  import LoginPage
from pages.assets_page import AssetsPage

from pages.common_page import CommonPage

driver = webdriver.Chrome()
common_page = CommonPage(driver)
login_page = LoginPage(driver)

def test_user_able_edit_open_position():
    #step 1: log in webpage
    login_page.login(GLOBAL_VARIABLES.page_url, GLOBAL_VARIABLES.userName, GLOBAL_VARIABLES.passWord)

    #step 2: Go to Assets Page
    assets_page = AssetsPage(driver)
    assets_page.clickOn_assets_option()
    assets_page.verify_open_position_is_displayed()

    #step 3: Click on Edit button in Open Position list
    assets_page.clickOn_edit_button()
    #step 4: Verify edit form is displayed
    assets_page.verify_edit_form_is_displayed()
    #step 5: Edit profit
    assets_page.clickOn_increase_take_profit_button()
    #step 6: Click on Update button
    assets_page.clickOn_update_button()
    #step 7: Verify edit confirm popup is displayed
    assets_page.verify_edit_confirm_popup_is_displayed()
    #step 8: Click on Confirm
    assets_page.clickOn_confirm_button()
    #step 9: Verify alert
    common_page.verify_successful_notification_alert_is_displayed("Market Order Updated")

def test_user_able_partial_close_open_position():

    #step 1: log in webpage
    login_page.login(GLOBAL_VARIABLES.page_url, GLOBAL_VARIABLES.userName, GLOBAL_VARIABLES.passWord)
    #step 2: Go to Assets page
    assets_page = AssetsPage(driver)
    assets_page.clickOn_assets_option()
    assets_page.verify_open_position_is_displayed()
    #step 3: Click on Close button in Open Position list
    assets_page.clickOn_close_button()
    #step 4: Verify close form is displayed
    assets_page.verify_confirm_close_popup_is_displayed()
    #step 5: Click on decrease size
    assets_page.clickOn_decrease_size()
    #step 6: Click on Close Button
    assets_page.clickOn_close_order_button()
    #Step 7: Verify alert
    common_page.verify_successful_notification_alert_is_displayed("Close Order")

def test_user_able_close_open_position():
    # step 1: log in webpage
    login_page.login(GLOBAL_VARIABLES.page_url, GLOBAL_VARIABLES.userName, GLOBAL_VARIABLES.passWord)
    # step 2: Go to Assets page
    assets_page = AssetsPage(driver)
    assets_page.clickOn_assets_option()
    assets_page.verify_open_position_is_displayed()
    # step 3: Click on Close button in Open Position list
    assets_page.clickOn_close_button()
    #step 4: Verify close form is displayed
    assets_page.verify_confirm_close_popup_is_displayed()
    # step 5: Click on Close Button
    assets_page.clickOn_close_order_button()
    # Step 6: Verify alert
    common_page.verify_successful_notification_alert_is_displayed("Close Order")
