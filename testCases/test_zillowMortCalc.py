import pytest
from pageObjects.mortcalc import ZillowMortgageCalculator, \
    ZillowMortgageCalculatorFullReport
import time


def test_test(browser):
    homevalue_amt = "539,000"
    homedownpayment_amt = "107,800"
    downpercentage_amt = "25"
    interestrate_amt = "4.375"
    monthlypayment_amt = "$2,018"  #"$2,474"

    page = ZillowMortgageCalculator(browser)
    page.load()
    print("\n\n")
    print(f"This File's  __name__ is set to: {format(__name__)}")
    print(f"driver Title : {browser.title}")
    print(f"Driver name  : {browser.name}")
    print(f"Driver URL   : {browser.current_url}")

    print(f"Home Price   : {homevalue_amt}")
    page.enter_homevalue(homevalue_amt)
    print(f"Home iRate   : {interestrate_amt}")
    page.enter_interestrate(interestrate_amt)
    print(f"Home Down    : {homedownpayment_amt}")
    page.enter_downpayment(homedownpayment_amt)
    print(f"Home Down %  : {downpercentage_amt}")
    page.enter_downpaymentpercent(downpercentage_amt)
    # default 30 year value

    time.sleep(15)
    page.verify_monthlypayment(monthlypayment_amt)

    #page.click_full_report()
    #page2 = ZillowMortgageCalculatorFullReport(browser)
    #page2.verify_monthlypayment(monthlypayment_amt)


if __name__ == "__main__":
    test_test()
