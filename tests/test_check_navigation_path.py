import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from const import Const

class TestNavigationPath:

    def test_check_open_main_page_tap_logo_scooter(self, page, driver):
        with allure.step("Step 1. Открываем сайт (https://qa-scooter.praktikum-services.ru/) «Яндекс.Самокат»"):
            with allure.step("Пользователь находится на главной странице «Яндекс.Самоката»"):
                driver.get(Const.MAIN_PAGE)
                WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.main_page))
        with allure.step("Step 1. Тапаем на логотип «Самокат»"):
            with allure.step("Пользователь находится на главной странице «Самоката»"):
                driver.find_element(*page.logo_scooter).click()
                assert Const.MAIN_PAGE == driver.current_url

    def test_check_open_dzen_page_tap_logo_yandex(self, page, driver):
        with allure.step("Step 1. Открываем сайт (https://qa-scooter.praktikum-services.ru/) «Яндекс.Самокат»"):
            with allure.step("Пользователь находится на главной странице «Яндекс.Самоката»"):
                driver.get(Const.MAIN_PAGE)
                WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.main_page))
        with allure.step("Step 1. Тапаем на логотип «Самокат»"):
            with allure.step("Пользователь находится на главной странице «Яндекс.Дзена»"):
                driver.find_element(*page.logo_yandex).click()
                driver.switch_to.window(driver.window_handles[1])
                WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.header_yandex_dzen))
                assert 'dzen.ru' in driver.current_url
