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

    def set_name(self, driver, page, name):
        with allure.step("Заполняем поле «Имя»"):
            driver.find_element(*page.input_name).send_keys(name)

    def set_surname(self, driver, page, surname):
        with allure.step("Заполняем поле «Фамилия»"):
            driver.find_element(*page.input_surname).send_keys(surname)

    def set_address(self, driver, page, address):
        with allure.step("Заполняем поле «Адрес»"):
            driver.find_element(*page.input_address).send_keys(address)

    def set_station(self, driver, page, station):
        with allure.step("Выбираем станцию метро"):
            driver.find_element(*page.select_subway).click()
            WebDriverWait(driver, 3).until(EC.presence_of_element_located(page.select_station_subway(station)))
            driver.find_element(*page.select_station_subway(station)).click()
            WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.complete_station(station)))

    def set_phone(self, driver, page, phone):
        with allure.step("Заполняем поле «Телефон»"):
            driver.find_element(*page.input_telephone).send_keys(phone)

    def order_about_person_page(self, driver, page, name, surname, address, station, phone):
        self.open_order_form(driver, page)
        self.set_name(driver, page, name)
        self.set_surname(driver, page, surname)
        self.set_address(driver, page, address)
        self.set_station(driver,page, station)
        self.set_phone(driver, page, phone)

    def set_data_piker(self, driver, page, date_piker):
        with allure.step("Заполняем поле «Когда привезти самокат»"):
            driver.find_element(*page.input_data_piker).click()
            WebDriverWait(driver, 3).until(EC.presence_of_element_located(page.order_data_piker))
            driver.find_element(*page.select_data_on_piker(date_piker)).click()
            print(page.select_data_in_input(date_piker))
            WebDriverWait(driver, 3).until(EC.presence_of_element_located(page.select_data_in_input(date_piker)))

    def set_rental_period(self, driver, page, rental_period):
        with allure.step("Заполняем поле «Срок аренды»"):
            driver.find_element(*page.input_dropdown_rental_period).click()
            WebDriverWait(driver, 3).until(EC.presence_of_element_located(page.menu_dropdown_rental_period))
            driver.find_element(*page.select_dropdown_rental_period(rental_period)).click()
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located(page.input_select_rental_period(rental_period)))

    def set_color(self, driver, page, color):
        with allure.step("Заполняем поле «Цвет самоката»"):
            driver.find_element(*page.checkbox_color(color)).click()
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located(page.select_checkbox_color))

    def set_comment_delivery(self, driver, page, comment):
        with allure.step("Заполняем поле «Комментарии для курьера»"):
            driver.find_element(*page.input_comment).send_keys(comment)

    def order_about_rental_page(self, driver, page, date_piker, rental_period, color, comment):
        self.set_data_piker(driver, page, date_piker)
        self.set_rental_period(driver, page, rental_period)
        self.set_color(driver, page, color)
        self.set_comment_delivery(driver,page, comment)
