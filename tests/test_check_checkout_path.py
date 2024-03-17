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
        #Здесь проверяем весь флоу заполнения заказа без методов
        with allure.step("Предусловие. Открываем страницу регистрации (https://qa-scooter.praktikum-services.ru/order) «Яндекс.Самокат»"):
            with allure.step("Пользователь находится на странице регистрации «Яндекс.Самоката»"):
                driver.get(Const.REGISTRATION_PAGE)
                WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.input_name))
        with allure.step("Step 1. Вводим имя в форму заказа»"):
            with allure.step("Пользователь ввел имя в форму заказа. Оно отобразилось в поле ввода"):
                driver.find_element(*page.input_name).send_keys(Const.NAME)
        with allure.step("Step 2. Вводим фамилию в форму заказа»"):
            with allure.step("Пользователь ввел фамилию в форму заказа. Оно отобразилось в поле ввода"):
                driver.find_element(*page.input_surname).send_keys(Const.SURNAME)
        with allure.step("Step 3. Вводим адрес в форму заказа»"):
            with allure.step("Пользователь ввел адрес в форму заказа. Оно отобразилось в поле ввода"):
                driver.find_element(*page.input_address).send_keys(Const.ADDRESS)
        with allure.step("Step 4. Выбираем станцию метро из выпадающего списка"):
            with allure.step("Пользователь выбрал станцию. Оно отобразилось в поле ввода"):
                driver.find_element(*page.select_subway).click()
                WebDriverWait(driver, 3).until(EC.presence_of_element_located(page.select_station_subway))
                driver.find_element(*page.select_station_subway).click()
                WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.complete_station))
        with allure.step("Step 5. Вводим номер телефона"):
            with allure.step("Пользователь выбрал станцию. Оно отобразилось в поле ввода"):
                driver.find_element(*page.input_telephone).send_keys(Const.PHONE)
        with allure.step("Step 6. Нажимаем кнопку «Далее»"):
            with allure.step("Пользователь перешел на следующую страницу оформления заказа"):
                driver.find_element(*page.order_next_button).click()
                WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.order_header_about_rent))
        with allure.step("Step 7. Выбираем дату в календаре «Когда привезти самокат»"):
            with allure.step("Пользователь выбрал дату. Дата отобразилась в инпуте"):
                driver.find_element(*page.input_data_piker).click()
                WebDriverWait(driver, 3).until(EC.presence_of_element_located(page.order_data_piker))
                driver.find_element(*page.select_data_on_piker).click()
                WebDriverWait(driver, 3).until(EC.presence_of_element_located(page.select_data_in_input))
        with allure.step("Step 8. Выбираем срок аренды из выпадающего списка"):
            with allure.step("Пользователь выбрал срок аренды. Срок отобразился в инпуте"):
                driver.find_element(*page.input_dropdown_rental_period).click()
                WebDriverWait(driver, 3).until(EC.presence_of_element_located(page.menu_dropdown_rental_period))
        with allure.step("Step 9. Выбираем цвет самоката "):
            with allure.step("Пользователь выбрал цвет самоката. Чекбокс отметился выбранным"):
                driver.find_element(*page.select_dropdown_rental_period).click()
                WebDriverWait(driver, 3).until(EC.presence_of_element_located(page.input_select_rental_period))
                driver.find_element(*page.checkbox_color).click()
                WebDriverWait(driver, 3).until(EC.visibility_of_element_located(page.select_checkbox_color))
        with allure.step("Step 10. Добавляем комментарий курьеру "):
            with allure.step("Пользователь ввел данные для курьера"):
                driver.find_element(*page.input_comment).send_keys(Const.COMMENT)
        with allure.step("Step 11. Нажать кнопку «Заказать»"):
            with allure.step("Отобразилось модальное окно «Хотите оформить заказ?»"):
                driver.find_element(*page.order_final_button).click()
                WebDriverWait(driver, 3).until(EC.visibility_of_element_located(page.order_modal_header))
                assert driver.find_element(*page.order_modal_header)

    def test_check_pop_up_window_successful_order(self, page, driver, methods):
        methods.order_about_person_page(driver, page)
        driver.find_element(*page.order_next_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.order_header_about_rent))
        methods.order_about_rental_page(driver, page)
        driver.find_element(*page.order_final_button).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(page.order_modal_header))
        driver.find_element(*page.order_modal_sure_button).click()
        assert driver.find_element(*page.order_modal_header_successfully_placed)


    # Проверка, что после оформления заказа появилось всплывающее окно с сообщением об успешном создании заказа.