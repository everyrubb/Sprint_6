import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from const import Const
import pytest


class TestChekoutPath:

    @allure.title('Проверка кнопку «Заказать»  в хедере на лендинге Яндекс Самоката')
    @allure.description('Проверяем, что при нажатии на кнопку «Заказать» в хедере сайта, открывается форма заказа')
    def test_check_open_order_page_tap_button_in_header(self, page, driver):
        with allure.step("Предусловие. Открываем сайт (https://qa-scooter.praktikum-services.ru/) «Яндекс.Самокат»"):
            with allure.step("Пользователь находится на главной странице «Яндекс.Самоката»"):
                driver.get(Const.MAIN_PAGE)
                WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.main.main_page))
        with allure.step("Step 1. Кликаем на кнопку «Заказать в хедере сайта"):
            with allure.step("Открылась форма оформления заказа «Для кого самокат»"):
                driver.find_element(*page.main.order_button).click()
                WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.registration.order_header))
                assert Const.REGISTRATION_PAGE == driver.current_url

    @allure.title('Проверка midle-кнопки «Заказать» на лендинге Яндекс Самоката')
    @allure.description('Проверяем, что при нажатии на кнопку «Заказать» на странице сайта, открывается форма заказа')
    def test_check_open_order_page_tap_midlle_button(self, page, driver):
        with allure.step("Предусловие. Открываем сайт (https://qa-scooter.praktikum-services.ru/) «Яндекс.Самокат»"):
            with allure.step("Пользователь находится на главной странице «Яндекс.Самоката»"):
                driver.get(Const.MAIN_PAGE)
                WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.main.main_page))
        with allure.step("Step 1.Скролим до инструкции «Как это работает» "):
            with allure.step("Отображается инструкция и кнопка «Заказать»"):
                element = driver.find_element(*page.main.order_middle_button)
                driver.execute_script("arguments[0].scrollIntoView();", element)
                WebDriverWait(driver, 3).until(EC.element_to_be_clickable(element))
        with allure.step("Step 2.Тапнуть на кнопку «Заказать»"):
            with allure.step("Открылась форма оформления заказа «Для кого самокат»"):
                driver.find_element(*page.main.order_middle_button).click()
                WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.registration.order_header))
                assert Const.REGISTRATION_PAGE == driver.current_url

    person_data = [
            ['Антонина', 'Иванова', 'Москва', 'Бульвар Рокоссовского', '79997220202', '15', 'двое суток', 'чёрный жемчуг', 'Оставьте у двери'],
            ['Василий', 'Смирнова', 'Саратов', 'Черкизовская', '79957220202', '19', 'четверо суток', 'серая безысходность', 'Оставьте у охраны'],
        ]

    @allure.title('Проверка флоу заказа самоката на сайте «Яндекс.Самоката»')
    @allure.description('Проверяем, форму заполнения при заказе самоката')
    @pytest.mark.parametrize("name, surname, address, station, phone, date_piker, rental_period, color, comment", person_data)
    def test_check_fill_out_order_form(self, page, driver, name, surname, address, station, phone, date_piker, rental_period, color, comment):
        #Здесь проверяем весь флоу заполнения заказа без методов
        with allure.step("Предусловие. Открываем страницу регистрации (https://qa-scooter.praktikum-services.ru/order) «Яндекс.Самокат»"):
            with allure.step("Пользователь находится на странице регистрации «Яндекс.Самоката»"):
                driver.get(Const.REGISTRATION_PAGE)
                WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.registration.input_name))
        with allure.step("Step 1. Вводим имя в форму заказа»"):
            with allure.step("Пользователь ввел имя в форму заказа. Оно отобразилось в поле ввода"):
                driver.find_element(*page.registration.input_name).send_keys(name)
        with allure.step("Step 2. Вводим фамилию в форму заказа»"):
            with allure.step("Пользователь ввел фамилию в форму заказа. Оно отобразилось в поле ввода"):
                driver.find_element(*page.registration.input_surname).send_keys(surname)
        with allure.step("Step 3. Вводим адрес в форму заказа»"):
            with allure.step("Пользователь ввел адрес в форму заказа. Оно отобразилось в поле ввода"):
                driver.find_element(*page.registration.input_address).send_keys(address)
        with allure.step("Step 4. Выбираем станцию метро из выпадающего списка"):
            with allure.step("Пользователь выбрал станцию. Оно отобразилось в поле ввода"):
                driver.find_element(*page.registration.select_subway).click()
                WebDriverWait(driver, 3).until(EC.presence_of_element_located(page.registration.select_station_subway(station)))
                driver.find_element(*page.registration.select_station_subway(station)).click()
                WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.registration.complete_station(station)))
        with allure.step("Step 5. Вводим номер телефона"):
            with allure.step("Пользователь выбрал станцию. Оно отобразилось в поле ввода"):
                driver.find_element(*page.registration.input_telephone).send_keys(phone)
        with allure.step("Step 6. Нажимаем кнопку «Далее»"):
            with allure.step("Пользователь перешел на следующую страницу оформления заказа"):
                driver.find_element(*page.registration.order_next_button).click()
                WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.registration.order_header_about_rent))
        with allure.step("Step 7. Выбираем дату в календаре «Когда привезти самокат»"):
            with allure.step("Пользователь выбрал дату. Дата отобразилась в инпуте"):
                driver.find_element(*page.registration.input_data_piker).click()
                WebDriverWait(driver, 3).until(EC.presence_of_element_located(page.registration.order_data_piker))
                driver.find_element(*page.registration.select_data_on_piker(date_piker)).click()
                print(page.registration.select_data_in_input(date_piker))
                WebDriverWait(driver, 3).until(EC.presence_of_element_located(page.registration.select_data_in_input(date_piker)))
        with allure.step("Step 8. Выбираем срок аренды из выпадающего списка"):
            with allure.step("Пользователь выбрал срок аренды. Срок отобразился в инпуте"):
                driver.find_element(*page.registration.input_dropdown_rental_period).click()
                WebDriverWait(driver, 3).until(EC.presence_of_element_located(page.registration.menu_dropdown_rental_period))
                driver.find_element(*page.registration.select_dropdown_rental_period(rental_period)).click()
                WebDriverWait(driver, 3).until(EC.presence_of_element_located(page.registration.input_select_rental_period(rental_period)))
        with allure.step("Step 9. Выбираем цвет самоката "):
            with allure.step("Пользователь выбрал цвет самоката. Чекбокс отметился выбранным"):
                driver.find_element(*page.registration.checkbox_color(color)).click()
                WebDriverWait(driver, 3).until(EC.visibility_of_element_located(page.registration.select_checkbox_color))
        with allure.step("Step 10. Добавляем комментарий курьеру "):
            with allure.step("Пользователь ввел данные для курьера"):
                driver.find_element(*page.registration.input_comment).send_keys(comment)
        with allure.step("Step 11. Нажать кнопку «Заказать»"):
            with allure.step("Отобразилось модальное окно «Хотите оформить заказ?»"):
                driver.find_element(*page.registration.order_final_button).click()
                WebDriverWait(driver, 3).until(EC.visibility_of_element_located(page.registration.order_modal_header))
                assert driver.find_element(*page.registration.order_modal_header)

    @allure.title('Проверка модального окна с сообщением об успешном создании заказа после оформления заказа')
    @allure.description('Проверяем, что после оформления заказа появляется модальное окно')
    @pytest.mark.parametrize("name, surname, address, station, phone, date_piker, rental_period, color, comment", person_data)
    def test_check_pop_up_window_successful_order(self, page, driver, name, surname, address, station, phone, date_piker, rental_period, color, comment):
        page.registration_method.order_about_person_page(driver, page, name, surname, address, station, phone)
        with allure.step("Тапаем на кнопку «Далее» на первой странице"):
            with allure.step("Пользователь перешел на вторую страницу формы заполнения заказа"):
                driver.find_element(*page.registration.order_next_button).click()
                WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.registration.order_header_about_rent))
        page.registration_method.order_about_rental_page(driver, page, date_piker, rental_period, color, comment)
        with allure.step("Нажимаем кнопку «Заказать»"):
            with allure.step("Отображается модальное окно с номерм заказа"):
                driver.find_element(*page.registration.order_final_button).click()
                WebDriverWait(driver, 3).until(EC.visibility_of_element_located(page.registration.order_modal_header))
                driver.find_element(*page.registration.order_modal_sure_button).click()
                assert driver.find_element(*page.registration.order_modal_header_successfully_placed)
