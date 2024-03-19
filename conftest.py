import pytest
from selenium import webdriver
from locators import LocatorsPage


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()

    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def page():
    page = LocatorsPage()
    return page