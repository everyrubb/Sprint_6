import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from const import Const

class TestAuthMethod():

    def open_order_form(self, driver, page):
        with allure.step("Открываем сайт (https://qa-scooter.praktikum-services.ru/) «Яндекс.Самокат»"):
            driver.get(Const.REGISTRATION_PAGE)
            WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.input_name))

    def set_name(self, driver, page):
        with allure.step("Заполняем поле «Имя»"):
            driver.find_element(*page.input_name).send_keys(Const.NAME)

    def set_surname(self, driver, page):
        with allure.step("Заполняем поле «Фамилия»"):
            driver.find_element(*page.input_surname).send_keys(Const.SURNAME)

    def set_address(self, driver, page):
        with allure.step("Заполняем поле «Адрес»"):
            driver.find_element(*page.input_address).send_keys(Const.ADDRESS)

    def set_station(self, driver, page):
        with allure.step("Выбираем станцию метро"):
            driver.find_element(*page.select_subway).click()
            WebDriverWait(driver, 3).until(EC.presence_of_element_located(page.select_station_subway))
            driver.find_element(*page.select_station_subway).click()
            WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.complete_station))

    def set_phone(self, driver, page):
        with allure.step("Заполняем поле «Телефон»"):
            driver.find_element(*page.input_telephone).send_keys(Const.PHONE)

    def order_about_person_page(self, driver, page):
        self.open_order_form(driver, page)
        self.set_name(driver, page)
        self.set_surname(driver, page)
        self.set_address(driver, page)
        self.set_station(driver,page)
        self.set_phone(driver, page)

    def set_data_piker(self, driver, page):
        with allure.step("Заполняем поле «Когда привезти самокат»"):
            driver.find_element(*page.input_data_piker).click()
            WebDriverWait(driver, 3).until(EC.presence_of_element_located(page.order_data_piker))
            driver.find_element(*page.select_data_on_piker).click()
            WebDriverWait(driver, 3).until(EC.presence_of_element_located(page.select_data_in_input))

    def set_rental_period(self, driver, page):
        with allure.step("Заполняем поле «Срок аренды»"):
            driver.find_element(*page.input_dropdown_rental_period).click()
            WebDriverWait(driver, 3).until(EC.presence_of_element_located(page.menu_dropdown_rental_period))

    def set_color(self, driver, page):
        with allure.step("Заполняем поле «Цвет самоката»"):
            driver.find_element(*page.select_dropdown_rental_period).click()
            WebDriverWait(driver, 3).until(EC.presence_of_element_located(page.input_select_rental_period))
            driver.find_element(*page.checkbox_color).click()
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located(page.select_checkbox_color))

    def set_comment_delivery(self, driver, page):
        with allure.step("Заполняем поле «Комментарии для курьера»"):
            driver.find_element(*page.input_comment).send_keys(Const.COMMENT)

    def order_about_rental_page(self, driver, page):
        self.set_data_piker(driver, page)
        self.set_rental_period(driver, page)
        self.set_color(driver, page)
        self.set_comment_delivery(driver,page)
