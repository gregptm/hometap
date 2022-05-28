import pytest
from pageObjects.page_mortCalc import ZillowMortgageCalculatorPage
import logging

log = logging.getLogger(__name__)

class TestMortgageCalculator(ZillowMortgageCalculatorPage):

    baseURL = "https://www.zillow.com/mortgage-calculator/"
    downpayment = '539000'

    @pytest.mark.greg
    def test_home_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title=self.driver.title
        self.driver.close()
        if actual_title=="Mortgage Calculator - Free House Payment Estimate | Zillow":
            assert True
        else:
            assert False

    @pytest.mark.greg
    def test_set_down_payment(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        log.info("downpayment amount:{}".format(self.downpayment))
        page = ZillowMortgageCalculatorPage()
        page.set_down_payment(self.downpayment)
