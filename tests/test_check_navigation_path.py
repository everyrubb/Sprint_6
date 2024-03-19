import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from const import Const

class TestNavigationPath:

    @allure.title('Проверка перехода при тапе на логотип «Самокат» на лендинг Яндекс.Самокат ')
    @allure.description('Проверяем, что при нажатии на логотип «Самокат» пользователь переходит на лендинг «Самокат»')
    def test_check_open_main_page_tap_logo_scooter(self, page, driver):
        with allure.step("Step 1. Открываем страницу регистрации (https://qa-scooter.praktikum-services.ru/order') «Яндекс.Самокат»"):
            with allure.step("Пользователь находится на странице регистрации«Яндекс.Самоката»"):
                driver.get(Const.REGISTRATION_PAGE)
                WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.registration.input_name))
        with allure.step("Step 2. Тапаем на логотип «Самокат»"):
            with allure.step("Пользователь находится на главной странице «Самоката»"):
                driver.find_element(*page.main.logo_scooter).click()
                assert Const.MAIN_PAGE == driver.current_url

    @allure.title('Проверка перехода при тапе на логотип «Яндекс» на «Яндекс.Дзен» ')
    @allure.description('Проверяем, что при нажатии на логотип «Яндекс» пользователь переходит на Яндекс.Дзен')
    def test_check_open_dzen_page_tap_logo_yandex(self, page, driver):
        with allure.step("Step 1. Открываем сайт (https://qa-scooter.praktikum-services.ru/) «Яндекс.Самокат»"):
            with allure.step("Пользователь находится на главной странице «Яндекс.Самоката»"):
                driver.get(Const.MAIN_PAGE)
                WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.main.main_page))
        with allure.step("Step 2. Тапаем на логотип «Самокат»"):
            with allure.step("Пользователь находится на главной странице «Яндекс.Дзена»"):
                driver.find_element(*page.main.logo_yandex).click()
                driver.switch_to.window(driver.window_handles[1])
                WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.main.header_yandex_dzen))
                assert 'dzen.ru' in driver.current_url
