from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class ZillowMortgageCalculator:
    URL = "https://www.zillow.com/mortgage-calculator/"

    l_button_interestratehelp_class = (
        By.CLASS_NAME, "TriggerButton-c11n-8-64-1__sc-19o64qd-0 drLVVu")
    l_button_interestratehelp_xpath = (
        By.XPATH, "(//button[@type='button'])[8]")
    l_dropdown_loanprogram_id = (By.ID, "form-1_term")
    # note id's are aurogenerated each time so unreliable
    l_errormsg_interestrate_classname = (
        By.CLASS_NAME, "StyledFormHelp-c11n-8-64-1__sc-h3s6hy-0 lfSzwh")
    l_link_currentrates_xpath = (
        By.XPATH, "(// a[normalize-space() = 'See current rates'])[1]")
    l_textbox_downpayment_id = (By.ID, "form-1_downPayment")
    l_textbox_downpaymentpercent_id = (
        By.ID, "form-1_downPaymentPercent")
    l_textbox_homeprice_id = (By.ID, "homePrice")
    l_textbox_interestrate_id = (By.ID, "rate")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def type_entry(self, value, element):
        print(f"value        : {value}")
        print(f"element      : {element}")
        # why why why
        element.clear()
        element.clear()
        element.send_keys(value + Keys.TAB)

    def enter_homevalue(self, value):
        theElement = self.browser.find_element(*self.l_textbox_homeprice_id)
        print(f"value        : {value}")
        print(f"theElement   : {theElement}")
        self.type_entry(value, theElement)

    def enter_downpayment(self, value):
        theElement = self.browser.find_element(*self.l_textbox_downpayment_id)
        print(f"value        : {value}")
        print(f"theElement   : {theElement}")
        self.type_entry(value, theElement)

    def enter_downpaymentpercent(self, value):
        theElement = self.browser.find_element(
            *self.l_textbox_downpaymentpercent_id)
        print(f"value        : {value}")
        print(f"theElement   : {theElement}")
        self.type_entry(value, theElement)

    def enter_interestrate(self, value):
        theElement = self.browser.find_element(*self.l_textbox_interestrate_id)
        print(f"value        : {value}")
        print(f"theElement   : {theElement}")
        self.type_entry(value, theElement)
