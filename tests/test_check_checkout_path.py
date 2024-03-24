import allure
from const import Const
import pytest

from locators.order_page_locators import OrderPageLocators


class TestChekoutPath:

    @allure.title('Проверка кнопку «Заказать»  в хедере на лендинге Яндекс Самоката')
    @allure.description('Проверяем, что при нажатии на кнопку «Заказать» в хедере сайта, открывается форма заказа')
    def test_check_open_order_page_tap_button_in_header(self, main_page):
        main_page.open_main_page()
        main_page.tap_order_header_button()
        assert Const.ORDER_PAGE == main_page.get_current_url()

    @allure.title('Проверка midle-кнопки «Заказать» на лендинге Яндекс Самоката')
    @allure.description('Проверяем, что при нажатии на кнопку «Заказать» на странице сайта, открывается форма заказа')
    def test_check_open_order_page_tap_midlle_button(self, main_page):
        main_page.open_main_page()
        main_page.scroll_to_middle_button()
        main_page.tap_order_middle_button()
        assert Const.ORDER_PAGE == main_page.get_current_url()

    person_data = [
            ['Антонина', 'Иванова', 'Москва', 'Бульвар Рокоссовского', '79997220202', '15', 'двое суток', 'чёрный жемчуг', 'Оставьте у двери'],
            ['Василий', 'Смирнова', 'Саратов', 'Черкизовская', '79957220202', '19', 'четверо суток', 'серая безысходность', 'Оставьте у охраны'],
        ]
    @allure.title('Проверка флоу заказа самоката на сайте «Яндекс.Самоката»')
    @allure.description('Проверяем, форму заполнения при заказе самоката')
    @pytest.mark.parametrize("name, surname, address, station, phone, date_piker, rental_period, color, comment", person_data)
    def test_check_pop_up_window_successful_order(self, order_page, name, surname, address, station, phone, date_piker, rental_period, color, comment):
        order_page.order_about_person_page(name, surname, address, station, phone)
        order_page.tap_next_page_button()
        order_page.order_about_rental_page(date_piker, rental_period, color, comment)
        order_page.tap_order_final_button()
        assert order_page.find_element(OrderPageLocators.ORDER_MODAL_HEADER_SUCCESSFULLY_PLACED)