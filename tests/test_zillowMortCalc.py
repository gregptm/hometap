import pytest
from hamcrest import *
from pages.mortcalc import ZillowMortgageCalculatorPage
import logging
import time
import warnings
from datetime import datetime

mort_calc_test_logger = logging.getLogger(__name__)


@pytest.mark.L0
@pytest.mark.parametrize(
    'homevalue_amt, '
    'homedownpayment_amt, '
    'downpercentage_amt, '
    'interestrate_amt, '
    'monthlypayment_amt',
    [("539,000", "107,800", "25", "4.375", "$2,018"), ("300,000", "30,000", "10", "2.5", "$1,067")])
def test_Mortgage_Calculator(
        browser,
        homevalue_amt,
        homedownpayment_amt,
        downpercentage_amt,
        interestrate_amt,
        monthlypayment_amt):
    '''
    Test parameterized for a 30 year Fixed and a 5 year Arm
    TODO: need a JIRA Story to set up a proxy
          and change from verifying monthly P&I to full monthly value
          monthlypayment_amt
          see also page object for changes
    '''
    # TODO: "$2,474" Can't  use as there is rotating taxes need constant proxy

    page = ZillowMortgageCalculatorPage(browser)
    page.load()
    mort_calc_test_logger.info("\n\n")
    mort_calc_test_logger.info(f"This File's  __name__ is set to: {format(__name__):>15}")
    mort_calc_test_logger.info(f"Browser Title : {browser.title:>15}")
    mort_calc_test_logger.info(f"Browser name  : {browser.name:>15}")
    mort_calc_test_logger.info(f"Browser URL   : {browser.current_url:>15}")

    # oddly had to do out of order, elseL interest changed on us
    mort_calc_test_logger.info(f"Home Price    : {homevalue_amt:>15}")
    page.enter_homevalue(homevalue_amt)
    mort_calc_test_logger.info(f"Home iRate    : {interestrate_amt:>15}")
    page.enter_interestrate(interestrate_amt)
    mort_calc_test_logger.info(f"Home Down     : {homedownpayment_amt:>15}")
    page.enter_downpayment(homedownpayment_amt)
    mort_calc_test_logger.info(f"Home Down %   : {downpercentage_amt:>15}")
    page.enter_downpaymentpercent(downpercentage_amt)
    # default 30 year value

    # Verify monthly P&I number til we get a proxy set up or advanced feature
    time.sleep(2)  # delay for form to catch up to data entry
    calculated_monthly_payment_amt = page.get_monthlypayment()
    mort_calc_test_logger.info(f"Verify monthly payment"
                f"{calculated_monthly_payment_amt} == {monthlypayment_amt:>15}")
    assert_that(calculated_monthly_payment_amt, equal_to(monthlypayment_amt))


@pytest.mark.L1
def test_Interst_Rate_help_tooltip(browser):
    mort_calc_test_logger.info(f"TEST : Interest Rate Help Tooltip")
    page = ZillowMortgageCalculatorPage(browser)
    page.load()

    irate_title = "Interest rate"

    # Verify Interest Rate Help Icon
    # click help icon
    page.click_test_help_button()
    # Verify the tooltip title
    found_irate_help_tooltip_title = page.get_test_help_button_title()
    mort_calc_test_logger.info(f"Verify tooltip title"
                f"{found_irate_help_tooltip_title} == {irate_title:>15}")
    assert_that(found_irate_help_tooltip_title, equal_to(irate_title))
    # close the tooltip
    page.click_test_help_button_tooltip_x()


@pytest.mark.L1
def test_Interst_Rate_link(browser):

    mort_calc_test_logger.info(f"TEST : Current Interest Rate Link")
    page = ZillowMortgageCalculatorPage(browser)
    page.load()

    expected_page_title = 'Current Mortgage Rates'

    page.click_test_current_rates_link()
    page.switch_to_current_tab()
    time.sleep(2)  # give it a moment to produce the titlE
    mort_calc_test_logger.info(f"Verify page title"
                f"{expected_page_title} < IN > {browser.title:>15}")
    assert_that(browser.title, contains_string(expected_page_title))
    page.close_current_tab()

