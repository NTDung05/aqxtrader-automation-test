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
    #step 3: Go to Order History tab
    assets_page.clickOn_order_history_tab()
    assets_page.verify_order_history_is_displayed()
    #step 4: verify all columns in order history are displayed
    assets_page.verify_all_columns_in_history_are_displayed()
    #step 5: verify symbol, status, type are correct
    assets_page.verify_symbol_of_order_history_is_correct("DASHUSD.std")
    assets_page.verify_status_of_order_history_is_correct("EXPIRED")
    assets_page.verify_type_of_order_history_is_correct("BUY LIMIT")