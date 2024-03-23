from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.order_page import OrderPage


class Page:

    def __init__(self, driver) -> None:
        super().__init__()
        self.driver = driver

    @property
    def main_page(self):
        return MainPage(self.driver)

    @property
    def order_page(self):
        return OrderPage(self.driver)

    @property
    def base_page(self):
        return BasePage(self.driver)
