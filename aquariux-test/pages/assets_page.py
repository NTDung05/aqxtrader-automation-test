from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class AssetsPage:
    assetsOption = "//div[@data-testid='side-bar-option-assets']"
    assetsOpenList = "//tr[@data-testid='asset-open-list-item']"
    editButton = "//div[@data-testid='asset-open-button-edit']"
    editConfirmButton = "//div[@data-testid='edit-confirmation-modal']"
    increaseTakeProfitButton = "//div[@data-testid='edit-input-takeprofit-price-increase']"
    updateBuyOrderButton = "//button[@data-testid='edit-button-order']"

    EditConfirmationPopup =  "//div[@data-testid='edit-confirmation-modal']"
    confirmButton = "//button[@data-testid='edit-confirmation-button-confirm']"
    closeButton = "//div[@data-testid='asset-open-button-close']"
    closeConfirmPopup = "//div[@data-testid='confirmation-modal']"
    decreaseSizeIcon ="//div[@data-testid='close-order-input-volume-decrease']"
    closeOrderButton = "//div[@data-testid='close-order-button-submit']"
    pendingOrderTab = "//div[@data-testid='tab-asset-order-type-pending-orders']"

    editPendingAsset = "//div[@data-testid='asset-pending-button-edit']"
    assetsPendingList = "//tr[@data-testid='asset-pending-list-item']"
    increasePriceButton = "//div[@data-testid='edit-input-price-increase']"
    increaseStopLostButton = "//div[@data-testid='edit-input-stoploss-price-increase']"
    editExpiryDropdown = "//div[@data-testid='edit-dropdown-expiry']"
    goodTillCancelledType = "//div[@data-testid='edit-dropdown-expiry-good-till-cancelled']"
    goodTillDayType = "//div[@data-testid='edit-dropdown-expiry-good-till-day']"

    orderHistoryTab = "//div[@data-testid='tab-asset-order-type-history']"
    orderHistoryList = "//tr[@data-testid='asset-history-position-list-item']"
    openDate = "//th[@data-testid='asset-history-column-open-date']"
    closeDate = "//td[@data-testid='asset-history-column-close-date']"
    orderNo = "//td[@data-testid='asset-history-column-order-id']"
    symbol = "//td[@data-testid='asset-history-column-symbol']/span"
    status = "//td[@data-testid='asset-history-column-status']/div"
    type = "//td[@data-testid='asset-history-column-order-type']/span"
    profit_loss ="//td[@data-testid='asset-history-column-profit']"
    size = "//td[@data-testid='asset-history-column-size']"
    units = "//td[@data-testid='asset-history-column-units']"
    entryPrice = "//td[@data-testid='asset-history-column-entry-price']"
    closePrice = "//td[@data-testid='asset-history-column-close-price']"
    takeProfit =   "//td[@data-testid='asset-history-column-take-profit']"
    stopLoss = "//td[@data-testid='asset-history-column-stop-loss']"
    swap = "//td[@data-testid='asset-history-column-swap']"
    commission= "//td[@data-testid='asset-history-column-commission']"
    remarks = "//td[@data-testid='asset-history-column-remarks']"

    def __init__(self, driver):
        self.driver = driver

    def clickOn_assets_option(self):
       assetsOption = WebDriverWait(self.driver, 10).until(
           EC.presence_of_element_located((By.XPATH,self.assetsOption)))
       assetsOption.click()
    def verify_open_position_is_displayed(self):
        assetsOpenList = WebDriverWait(self.driver, 10).until(
           EC.visibility_of_element_located((By.XPATH, self.assetsOpenList)))
        assert assetsOpenList.is_displayed()

    def clickOn_edit_button(self):
        self.driver.find_element(By.XPATH, self.editButton).click()

    def verify_edit_form_is_displayed(self):
        editConfirmPopup = WebDriverWait(self.driver, 10).until(
         EC.visibility_of_element_located((By.XPATH, self.editConfirmButton)))
        assert editConfirmPopup.is_displayed() == True

    def clickOn_increase_take_profit_button(self):
        self.driver.find_element(By.XPATH, self.increaseTakeProfitButton).click()

    def clickOn_update_button(self):
        self.driver.find_element(By.XPATH, self.updateBuyOrderButton).click()

    def verify_edit_confirm_popup_is_displayed(self):
        assert self.driver.find_element(By.XPATH, self.EditConfirmationPopup).is_displayed()

    def clickOn_confirm_button(self):
        self.driver.find_element(By.XPATH, self.confirmButton).click()

    def clickOn_close_button(self):
        self.driver.find_element(By.XPATH, self.closeButton).click()

    def verify_confirm_close_popup_is_displayed(self):
        closeConfirmPopup = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.closeConfirmPopup)))
        assert closeConfirmPopup.is_displayed()

    def clickOn_decrease_size(self):
        self.driver.find_element(By.XPATH, self.decreaseSizeIcon).click()

    def clickOn_close_order_button(self):
        self.driver.find_element(By.XPATH, self.closeOrderButton).click()

    def clickOn_pending_order_tab(self):
        pendingOrderTab = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.pendingOrderTab)))
        pendingOrderTab.click()

    def verify_asset_pending_list_is_displayed(self):
        assetPendingList = WebDriverWait(self.driver, 10).until(
          EC.visibility_of_element_located((By.XPATH, self.assetsPendingList)))
        assert assetPendingList.is_displayed()

    def clickOn_edit_pending_order_button(self, type, expiry):
        self.driver.find_element(By.XPATH, "//span[text()='"+type+"']/../../td[text()='"+expiry+"']/.."+self.editPendingAsset ).click()

    def clickOn_increase_price_button(self):
        self.driver.find_element(By.XPATH, self.increasePriceButton).click()

    def clickOn_increase_stoploss_button(self):
        self.driver.find_element(By.XPATH, self.increaseStopLostButton).click()

    def updateExpiryDropdown(self, oldExpiryDropdown, ):
        self.driver.find_element(By.XPATH, self.editExpiryDropdown).click()
        if oldExpiryDropdown == "Good Till Day":
            self.driver.find_element(By.XPATH, self.goodTillCancelledType).click()
        else:
            self.driver.find_element(By.XPATH, self.goodTillDayType).click()

    def clickOn_order_history_tab(self):
        orderHistoryTab = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.orderHistoryTab)))
        orderHistoryTab.click()

    def verify_order_history_is_displayed(self):
        orderHistoryList = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.orderHistoryList)))
        assert orderHistoryList.is_displayed()

    def verify_all_columns_in_history_are_displayed(self):
        assert self.driver.find_element(By.XPATH, self.openDate).is_displayed()
        assert self.driver.find_element(By.XPATH, self.closeDate).is_displayed()
        assert self.driver.find_element(By.XPATH, self.symbol).is_displayed()
        assert self.driver.find_element(By.XPATH, self.orderNo).is_displayed()
        assert self.driver.find_element(By.XPATH, self.status).is_displayed()
        assert self.driver.find_element(By.XPATH, self.type).is_displayed()
        assert self.driver.find_element(By.XPATH, self.profit_loss).is_displayed()
        assert self.driver.find_element(By.XPATH, self.size).is_displayed()
        assert self.driver.find_element(By.XPATH,self.units).is_displayed()
        assert self.driver.find_element(By.XPATH,self.entryPrice).is_displayed()
        assert self.driver.find_element(By.XPATH,self.closePrice).is_displayed()
        assert self.driver.find_element(By.XPATH,self.takeProfit).is_displayed()
        assert self.driver.find_element(By.XPATH, self.stopLoss).is_displayed()
        assert self.driver.find_element(By.XPATH, self.swap).is_displayed()
        assert self.driver.find_element(By.XPATH, self.remarks).is_displayed()

    def verify_symbol_of_order_history_is_correct(self, symbol):
       assert self.driver.find_element(By.XPATH, self.symbol).text == symbol

    def verify_type_of_order_history_is_correct(self, type):
        assert self.driver.find_element(By.XPATH, self.type).text == type

    def verify_status_of_order_history_is_correct(self, status):
        print(self.driver.find_element(By.XPATH, self.status).text)
        assert self.driver.find_element(By.XPATH, self.status).text == status

