from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from hamcrest import *
import time


class ZillowMortgageCalculator:
    URL = "https://www.zillow.com/mortgage-calculator/"

    l_title_interestratehelptooltip_xpath = (By.XPATH,
                                                                      "(//h4[normalize-space()='Interest rate'])[1]")
    l_tooltip_x_interestratehelp_xpath = (By.XPATH,
                                                                   "(//*[name()='svg'][@role='img'])[32]")

    l_label_interestrate_id = (By.ID, 'label_4')
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

    l_link_currentrates_xpath = (
    By.XPATH, "(// a[normalize-space() = 'See current rates'])[1]")

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

        monthlypayment_pi = self.browser.find_element(*self.l_text_monthlypayment_id)
        # Verify Monthly Payment
        print(f"Verify monthly payment : "
              f"{monthlypayment_pi.text} == {expected_value} "
              f"{type(monthlypayment_pi.text)} == {type(expected_value)}")
        assert_that(monthlypayment_pi.text, equal_to(expected_value))
        print(f"Verify monthly payment : "
              f"{monthlypayment_pi.text} == {expected_value}")

    def click_full_report(self):
        print("click link full report")
        self.l_link_fullreport_xpath = (By.XPATH, "//a[normalize-space()='Full report']")
        fullreport_link = self.browser.find_element(*self.l_link_fullreport_xpath)
        fullreport_link.click()


    def test_help_button(self):
        # Click the Help button
        irate_label = self.browser.find_element(*self.l_label_interestrate_id)
        irate_help_button = self.browser.find_element(*self.l_button_interestratehelp_xpath)
        irate_help_button.click()
        time.sleep(2)
        # Verify the tooltip title
        irate_help_tooltip = self.browser.find_element(*self.l_title_interestratehelptooltip_xpath)

        assert_that(irate_help_tooltip.text, equal_to(irate_label.text))
        print(f"Verify tooltip title : {irate_help_tooltip.text} == {irate_label.text}")

        # close tooltip
        irate_help_tooltip = self.browser.find_element(*self.l_tooltip_x_interestratehelp_xpath)
        irate_help_tooltip.click()

    def test_current_rates_link(self):
        # Click the Current Rate Link
        currentrates_link = self.browser.find_element(*self.l_link_currentrates_xpath)
        currentrates_link.click()
        time.sleep(2)

        # Verify Page Title
        window_name = self.browser.window_handles[1]
        print(f"window name : {window_name}")
        self.browser.switch_to.window(window_name=window_name)

        print(f"Verify Page title  : {self.browser.title}")
        assert_that(self.browser.title, contains_string('Current Mortgage Rates'))
        time.sleep(2)

        # Close the tab opened
        self.browser.close()
        time.sleep(4)
