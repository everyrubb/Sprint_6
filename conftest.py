import pytest
from selenium import webdriver

from authorization_methods import TestAuthMethod
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

@pytest.fixture(scope='function')
def methods():
    methods = TestAuthMethod()
    return methods