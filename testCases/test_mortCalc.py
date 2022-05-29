import pytest
from pageObjects.page_mortCalc import *
import logging

log = logging.getLogger(__name__)

# class TestMortgageCalculator(ZillowMortgageCalculatorPage):

baseURL = "https://www.zillow.com/mortgage-calculator/"
downpayment = '539000'

@pytest.mark.wip
def test_home_page_title(self, driver):
    self.driver = driver
    self.driver.get(self.baseURL)
    actual_title=self.driver.title
    self.driver.close()
    if actual_title=="Mortgage Calculator - Free House Payment Estimate | Zillow":
        assert True
    else:
        assert False

@pytest.mark.greg
def test_set_down_payment(setup):
    driver = setup
    driver.get(baseURL)
    log.info("downpayment amount:{}".format(downpayment))
    calculatorPage = ZillowMortgageCalculatorPage(driver)
    calculatorPage.set_down_payment(downpayment)

if __name__ == "__main__":
    test_set_down_payment()