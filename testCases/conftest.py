from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest
import json
from datetime import datetime
import os

CONFIG_PATH = 'Configurations/config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']
DRIVE_LOCATION = 0

@pytest.fixture(scope='session')
def config():
    '''
        Get basic config settings from a non code config file
    :return:
    '''
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


def pytest_configure(config):
    """ Create a log file if log_file is not mentioned in pytest.ini file
        override wth
        pytest tests --log-file logs/pytest_$(date '+%F_%H-%M-%S').log
    """
    if not config.option.log_file:
        timestamp = datetime.strftime(datetime.now(), '%F_%H-%M-%S')
        config.option.log_file = f"logs/{__name__}_{timestamp}.log"


@pytest.fixture(scope='session')
def config_browser(config):
    '''
    detects if the browser set in config.json is one we support
    :param config:
    :return:
    '''
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a currently supported '
                        f'browser by the code')
    return config['browser']


@pytest.fixture(scope='session')
def config_wait_time(config):
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


@pytest.fixture(scope='session')
def browser(config_browser, config_wait_time):
    '''
    set up the browser to use, or report it is not supported
    :param config_browser: from config.json
    :param config_wait_time : from config.json
    :return:
    '''
    if config_browser == 'chrome':
        # these still work for chrome
        # driver = Chrome()
        # driver = Chrome("/usr/local/bin/chromedriver")
        driver = Chrome(service=Service(ChromeDriverManager().install()))
    elif config_browser == 'firefox':
        # still works if driver is in path locally
        # does not seem to need GH_TOKEN
        driver = Firefox()
        # TODO: GH_TOKEN SEEMS TO NOW BE FAILING - investigate
        # driver = Firefox(service=Service(GeckoDriverManager().install()))
    else:
        raise Exception(
            f'"{config_browser}" is not a supported browser in our list')

    driver.implicitly_wait(config_wait_time)
    driver.maximize_window()

    #drive the browser to a certain location for consistent tax calculations
    latitude = 42.1058163
    longitude = -71.5448773
    accuracy = 100
    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
        "latitude": latitude,
        "longitude": longitude,
        "accuracy": accuracy
    })

    yield driver

    driver.quit()
