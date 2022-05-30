from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from hamcrest import *
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

    # StyledButton-c11n-8-64-1__sc-wpcbcc-0iGaQCCzgmi__i17mpm-2 jfcxZT
    # // a[normalize - space() = 'Full report']

    #l_text_monthlypayment_id = (
    #    By.XPATH, "//*[name()='text' and contains(@y,'20')]")
    #l_text_monthlypayment_id = (
    #    By.XPATH, "//*[ @ "
    #              'id = "breakdown-panel"]/div/div/div[1]/svg/g/g[4]/text[2]')
    l_text_monthlypayment_id = (By.CLASS_NAME, "arc-label-value")

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
        element.click()
        element.send_keys(value + Keys.TAB )
        #element.send_keys(Keys.ENTER + Keys.TAB)
        #element.send_keys(Keys.SHIFT, Keys.TAB)
        #element.send_keys(Keys.ENTER)
        theElement = self.browser.find_element(*self.l_text_monthlypayment_id)
        print(f"the value: {value} the result:  {theElement.text}")

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


    def verify_monthlypayment(self, expected_value):
        theElement = self.browser.find_element(*self.l_text_monthlypayment_id)
        # Verify Monthly Payment
        print(f"Verify monthly payment : "
              f"{theElement.text} == {expected_value} "
              f"{type(theElement.text)} == {type(expected_value)}")
        assert_that(theElement.text, equal_to(expected_value))
        print(f"Verify monthly payment : "
              f"{theElement.text} == {expected_value}")

    def click_full_report(self):
        print("click link full report")
        self.l_link_fullreport_xpath = (By.XPATH, "//a[normalize-space()='Full report']")
        theElement = self.browser.find_element(*self.l_link_fullreport_xpath)
        theElement.click()


    def verify_monthlypayment(self, expected_value):

        theElement = self.browser.find_element(*self.l_text_monthlypayment_id)
        # Verify Monthly Payment
        print(f"Verify monthly payment : "
              f"{theElement.text} == {expected_value} "
              f"{type(theElement.text)} == {type(expected_value)}")
        assert_that(theElement.text, equal_to(expected_value))
        print(f"Verify monthly payment : "
              f"{theElement.text} == {expected_value}")


class ZillowMortgageCalculatorFullReport:
#    l_text_monthlypayment_id = (
#        By.CSS_SELECTOR, ".Text-c11n-8-64-1__sc-aiai24-0.cWTZVT")
    l_text_monthlypayment_id = (By.XPATH, "//*[name()='text' and contains(@y,'20')]")

    def __init__(self, browser):
        self.browser = browser

    def verify_monthlypayment(self, expected_value):

        theElement = self.browser.find_element(*self.l_text_monthlypayment_id)
        # Verify Monthly Payment
        print(f"Verify monthly payment : "
              f"{theElement.text} == {expected_value} "
              f"{type(theElement.text)} == {type(expected_value)}")
        assert_that(theElement.text, equal_to(expected_value))
        print(f"Verify monthly payment : "
              f"{theElement.text} == {expected_value}")

