from methods.authorization_methods import TestAuthMethod
from locators.registration_page_locators import TestRegistrationPageLocators
from locators.main_page_locators import TestMainPageLocators


class Page:

    @property
    def main(self):
        return TestMainPageLocators()

    @property
    def registration(self):
        return TestRegistrationPageLocators()

    @property
    def registration_method(self):
        return TestAuthMethod()