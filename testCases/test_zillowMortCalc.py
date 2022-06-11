import pytest
from hamcrest import *
from pages.mortcalc import ZillowMortgageCalculatorPage
import logging
import time

LOGGER = logging.getLogger(__name__)



@pytest.mark.L0
def test_Mortgage_Calculator_Fixed(browser):
    '''
    TODO: need a JIRA Story to set up a proxy
          and change from verifying monthly P&I to full monthly value
          monthlypayment_amt
          see also page object for changes
    '''
    homevalue_amt = "539,000"
    homedownpayment_amt = "107,800"
    downpercentage_amt = "25"
    interestrate_amt = "4.375"

    monthlypayment_amt = "$2,018"
    # TODO: "$2,474" Can't  use as there is rotating taxes need constant proxy

    page = ZillowMortgageCalculatorPage(browser)
    page.load()
    LOGGER.info("\n\n")
    LOGGER.info(f"This File's  __name__ is set to: {format(__name__)}")
    LOGGER.info(f"Browser Title : {browser.title}")
    LOGGER.info(f"Browser name  : {browser.name}")
    LOGGER.info(f"Browser URL   : {browser.current_url}")

    # oddly had to do out of order, elseL interest changed on us
    LOGGER.info(f"Home Price   : {homevalue_amt}")
    page.enter_homevalue(homevalue_amt)
    LOGGER.info(f"Home iRate   : {interestrate_amt}")
    page.enter_interestrate(interestrate_amt)
    LOGGER.info(f"Home Down    : {homedownpayment_amt}")
    page.enter_downpayment(homedownpayment_amt)
    LOGGER.info(f"Home Down %  : {downpercentage_amt}")
    page.enter_downpaymentpercent(downpercentage_amt)
    # default 30 year value

    # Verify monthly P&I number til we get a proxy set up or advanced feature
    time.sleep(2) # delay for form to catch up to data entry
    calculated_monthly_payment_amt = page.get_monthlypayment()
    LOGGER.info(f"Verify monthly payment : "
          f"{calculated_monthly_payment_amt} == {monthlypayment_amt}")
    assert_that(calculated_monthly_payment_amt, equal_to(monthlypayment_amt))


@pytest.mark.L1
def test_Interst_Rate_help_tooltip(browser):
    page = ZillowMortgageCalculatorPage(browser)
    page.load()

    irate_title = "Interest rate"

    # Verify Interest Rate Help Icon
    # click help icon
    page.click_test_help_button()
    # Verify the tooltip title
    found_irate_help_tooltip_title = page.get_test_help_button_title()
    LOGGER.info(f"Verify tooltip title : "
          f"{found_irate_help_tooltip_title} == {irate_title}")
    assert_that(found_irate_help_tooltip_title, equal_to(irate_title))
    # close the tooltip
    page.click_test_help_button_tooltip_x()

@pytest.mark.L1
def test_Interst_Rate_link(browser):
    page = ZillowMortgageCalculatorPage(browser)
    page.load()

    expected_page_title = 'Current Mortgage Rates'
    page.click_test_current_rates_link()
    page.get_current_tab()
    time.sleep(2) # give it a moment to produce the title
    LOGGER.info(f"Verify Page title  : {expected_page_title} < IN > {browser.title}")
    assert_that(browser.title,
            contains_string(expected_page_title))
    page.close_current_tab()
