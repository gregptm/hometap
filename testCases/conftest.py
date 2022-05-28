from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    #driver = webdriver.Firefox()

    return driver

