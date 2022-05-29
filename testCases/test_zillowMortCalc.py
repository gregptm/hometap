import pytest
from pageObjects.mortcalc import ZillowMortgageCalculator
import time

def test_test(browser):
    homevalue_amt = "539,000"
    homedownpayment_amt = "107,800"
    downpercentage_amt = "25"
    interstrate_amt = "4.375"

    page = ZillowMortgageCalculator(browser)
    page.load()
    print("\n\n")
    print(f"This File's  __name__ is set to: {format(__name__)}")
    print(f"driver Title : {browser.title}")
    print(f"Driver name  : {browser.name}")
    print(f"Driver URL   : {browser.current_url}")

    print(f"Home Price   : {homevalue_amt}")
    #page.enter_homevalue(homevalue_amt)
    #page.enter_value(homedownpayment_amt)
    #page.enter_value(downpercentage_amt)
    # default 30 year value
    page.enter_interestreate(interstrate_amt)
    time.sleep(5)
    pass


if __name__ == "__main__":
    test_test()
