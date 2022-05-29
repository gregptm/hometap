from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ZillowMortgageCalculator:
    URL = "https://www.zillow.com/mortgage-calculator/"
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)
