import pytest
from pageObjects.mortcalc import ZillowMortgageCalculator


def test_test(browser):
    page = ZillowMortgageCalculator(browser)
    page.load()
    print("\n\n")
    print(f"This File's  __name__ is set to: {format(__name__)}")
    print(f"driver Title : {browser.title}")
    print(f"Driver name  : {browser.name}")
    print(f"Driver URL   : {browser.current_url}")
    pass


if __name__ == "__main__":
    test_test()
