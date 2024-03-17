import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from const import Const


class TestChekoutPath:

    def test_check_open_order_page_tap_button_in_header(self, page, driver):
        # Проверка, что при нажатии на кнопку «Заказать» в хедере сайта, открывается форма заказа
        with allure.step("Предусловие. Открываем сайт (https://qa-scooter.praktikum-services.ru/) «Яндекс.Самокат»"):
            with allure.step("Пользователь находится на главной странице «Яндекс.Самоката»"):
                driver.get(Const.MAIN_PAGE)
                WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.main_page))
        with allure.step("Step 1. Кликаем на кнопку «Заказать в хедере сайта"):
            with allure.step("Step 1. Открылась форма оформления заказа «Для кого самокат»"):
                driver.find_element(*page.order_button).click()
                WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.order_header))
                assert Const.REGISTRATION_PAGE == driver.current_url

    def test_check_open_order_page_tap_midlle_button(self, page, driver):
    # Проверка, что при нажатии на кнопку «Заказать» в на странице сайта, открывается форма заказа
        with allure.step("Предусловие. Открываем сайт (https://qa-scooter.praktikum-services.ru/) «Яндекс.Самокат»"):
            with allure.step("Пользователь находится на главной странице «Яндекс.Самоката»"):
                driver.get(Const.MAIN_PAGE)
                WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.main_page))
        with allure.step("Step 1.Скролим до инструкции «Как это работает» "):
            with allure.step("Отображается инструкция и кнопка «Заказать»"):
                element = driver.find_element(*page.order_middle_button)
                driver.execute_script("arguments[0].scrollIntoView();", element)
                WebDriverWait(driver, 3).until(EC.element_to_be_clickable(element))
        with allure.step("Step 2.Тапнуть на кнопку «Заказать»"):
            with allure.step("Открылась форма оформления заказа «Для кого самокат»"):
                driver.find_element(*page.order_middle_button).click()
                WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.order_header))
                assert Const.REGISTRATION_PAGE == driver.current_url

    def test_check_fill_out_order_form(self, page, driver):
        driver.get(Const.REGISTRATION_PAGE)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.input_name))
        driver.find_element(*page.input_name).send_keys(Const.NAME)
        driver.find_element(*page.input_surname).send_keys(Const.SURNAME)
        driver.find_element(*page.input_address).send_keys(Const.ADDRESS)
        driver.find_element(*page.select_subway).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(page.select_station_subway))
        driver.find_element(*page.select_station_subway).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.complete_station))
        driver.find_element(*page.input_telephone).send_keys(Const.PHONE)
        driver.find_element(*page.order_next_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.order_header_about_rent))
        driver.find_element(*page.input_data_piker).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(page.order_data_piker))
        driver.find_element(*page.select_data_on_piker).click()
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(page.select_data_in_input))






    # def test_check_pop_up_window_successful_order(self, page, driver):
    # Проверка, что после оформления заказа появилось всплывающее окно с сообщением об успешном создании заказа.