import pytest
from selenium import webdriver

from page import Page


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()

    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def page(driver):
    return Page(driver)