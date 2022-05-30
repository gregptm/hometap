import pytest
from pageObjects.mortcalc import ZillowMortgageCalculatorPage


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
    print("\n\n")
    print(f"This File's  __name__ is set to: {format(__name__)}")
    print(f"Browser Title : {browser.title}")
    print(f"Browser name  : {browser.name}")
    print(f"Browser URL   : {browser.current_url}")

    # oddly had to do out of order, elseL interest changed on us
    print(f"Home Price   : {homevalue_amt}")
    page.enter_homevalue(homevalue_amt)
    print(f"Home iRate   : {interestrate_amt}")
    page.enter_interestrate(interestrate_amt)
    print(f"Home Down    : {homedownpayment_amt}")
    page.enter_downpayment(homedownpayment_amt)
    print(f"Home Down %  : {downpercentage_amt}")
    page.enter_downpaymentpercent(downpercentage_amt)
    # default 30 year value

    # Verify monthly P&I number til we get a proxy set up
    page.verify_monthlypayment(monthlypayment_amt)


@pytest.mark.L1
def test_Interst_Rate_Extras(browser):
    page = ZillowMortgageCalculatorPage(browser)
    page.load()

    # Verify Interst Rate Help Icon
    page.test_help_button()
    # Verify Current Interest Rates Link
    page.test_current_rates_link()
