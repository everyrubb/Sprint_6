from selenium.webdriver.common.by import By


class LocatorsPage():
    "Я знаю, что ревьюверы хотят в виде констант, но я сделала так. Для меня это более удобный и читабельный вариант"

    @property
    def main_page(self):
        """Отображается главная страница «Яндекс.Самоката»"""
        return By.CLASS_NAME, "Home_HomePage__ZXKIX"

    @property
    def order_header(self):
        """Заголовок «Для кого замокат» на странице формы оформления заказа «Яндекс.Самоката"""
        return By.XPATH, "//div[@class='Order_Header__BZXOb' and text()='Для кого самокат']"

    @property
    def order_button(self):
        """Кнопка «Заказать» в хедере на главной странице «Яндекс.Самоката"""
        return By.CLASS_NAME, "Button_Button__ra12g"

    @property
    def order_middle_button(self):
        """Кнопка «Заказать» в инструкции «Как это работает»"""
        return By.XPATH, "//div[@class = 'Home_FinishButton__1_cWm']/button[text()='Заказать']"

    @property
    def dropdown_section(self):
        """Выпадающий список «Вопросы о важном»"""
        return By.CLASS_NAME, "accordion"

    @property
    def open_dropdown_section(self):
        """Открытый блок в выпадающем списке «Вопросы о важном»"""
        return By.XPATH, "//div[not(@hidden)]"

    def dropdown_element_question(self, id):
        """Элемент вопроса в выпадающем списке «Вопросы о важном"""
        return By.ID, f"accordion__heading-{id}"

    def dropdown_element_answer(self, id):
        """Элемент ответа в выпадающем списке «Вопросы о важном"""
        return By.ID, f"accordion__panel-{id}"

    @property
    def input_name(self):
        """Инпут Имени в форме оформления заказа"""
        return By.XPATH, "//div[@class='Input_InputContainer__3NykH']//input[contains(@placeholder, 'Имя')]"

    @property
    def input_surname(self):
        """Инпут Фамилия в форме оформления заказа"""
        return By.XPATH, "//div[@class='Input_InputContainer__3NykH']//input[contains(@placeholder, 'Фамилия')]"

    @property
    def input_address(self):
        """Инпут Адрес в форме оформления заказа"""
        return By.XPATH, "//div[@class='Input_InputContainer__3NykH']//input[contains(@placeholder, 'Адрес')]"

    @property
    def select_subway(self):
        """Секция метро в форме оформления заказа"""
        return By.XPATH, "//input[contains(@placeholder, 'Станция метро')]"

    @property
    def select_list_subway(self):
        """Выпадающий список метро в форме оформления заказа"""
        return By.CLASS_NAME, "select-search__options"

    def select_station_subway(self, station):
        """Выбор метро в выпадающем листе на странице оформления заказа"""
        return By.XPATH, f"//li[@class='select-search__row']//button[.//div[contains(@class, 'Order_Text__2broi') and text()='{station}']]"

    def complete_station(self, station):
        """Выбор метро в выпадающем листе на странице оформления заказа"""
        return By.XPATH, f"//input[@value='{station}']"

    @property
    def input_telephone(self):
        """Инпут телефон в форме оформления заказа"""
        return By.XPATH, "//div[@class='Input_InputContainer__3NykH']//input[contains(@placeholder, 'Телефон')]"

    @property
    def order_next_button(self):
        """Кнопка «Далее» на странице заказа"""
        return By.XPATH, "//div[@class = 'Order_NextButton__1_rCA']/button[text()='Далее']"

    @property
    def order_header_about_rent(self):
        """Заголовок «Для кого замокат» на странице формы оформления заказа «Яндекс.Самоката"""
        return By.XPATH, "//div[@class='Order_Header__BZXOb' and text()='Про аренду']"

    @property
    def input_data_piker(self):
        """Календарь выбора даты в форме заказа"""
        return By.CLASS_NAME, "react-datepicker__input-container"

    @property
    def order_data_piker(self):
        """Календарь выбора даты в форме заказа"""
        return By.CLASS_NAME, "react-datepicker"


    def select_data_on_piker(self, date_piker):
        """Календарь выбора даты в форме заказа"""
        return By.XPATH, f"//div[contains(@class, 'react-datepicker')]//div[contains(@class, 'react-datepicker__day') and text()='{date_piker}']"


    def select_data_in_input(self, date_piker):
        """Календарь выбора даты в форме заказа"""
        return By.XPATH, f"//div[@class='react-datepicker__input-container']//input[contains(@value, '{date_piker}')]"

    @property
    def input_dropdown_rental_period(self):
        """Календарь выбора даты в форме заказа"""
        return By.CLASS_NAME, "Dropdown-control"

    @property
    def menu_dropdown_rental_period(self):
        """Календарь выбора даты в форме заказа"""
        return By.CLASS_NAME, "Dropdown-menu"

    def select_dropdown_rental_period(self, rental_period):
        """Выбор варианта срока аренд в меню в форме заказа"""
        return By.XPATH, f"//div[@class='Dropdown-option' and text()='{rental_period}']"

    def input_select_rental_period(self, rental_period):
        """Выбор варианта срока аренд в меню в форме заказа"""
        return By.XPATH, f"//div[contains(@class, 'is-selected') and text()='{rental_period}']"

    def checkbox_color(self, color):
        """Выбор варианта срока аренд в меню в форме заказа"""
        return By.XPATH, f"//label[text()='{color}']"

    @property
    def select_checkbox_color(self):
        """Выбор варианта срока аренд в меню в форме заказа"""
        return By.XPATH, "//div[contains(@class, 'FilledContainer')]"

    @property
    def input_comment(self):
        """Инпут комментарий курьеру в форме оформления заказа"""
        return By.XPATH, "//div[@class='Input_InputContainer__3NykH']//input[contains(@placeholder, 'Комментарий для курьера')]"

    @property
    def order_final_button(self):
        """Кнопка «Далее» на странице заказа"""
        return By.XPATH, "//div[@class = 'Order_Buttons__1xGrp']/button[text()='Заказать']"

    @property
    def order_modal_header(self):
        """Кнопка «Далее» на странице заказа"""
        return By.XPATH, "//div[@class = 'Order_ModalHeader__3FDaJ'and text()='Хотите оформить заказ?']"

    @property
    def order_modal_sure_button(self):
        """Кнопка «Далее» на странице заказа"""
        return By.XPATH, "//div[@class = 'Order_Buttons__1xGrp']/button[text()='Да']"

    @property
    def order_modal_header_successfully_placed(self):
        """Кнопка «Далее» на странице заказа"""
        return By.XPATH, "//div[@class = 'Order_ModalHeader__3FDaJ'and text()='Заказ оформлен']"

    @property
    def logo_scooter(self):
        """Кнопка «Далее» на странице заказа"""
        return By.CLASS_NAME, "Header_LogoScooter__3lsAR"

    @property
    def logo_yandex(self):
        """Кнопка «Далее» на странице заказа"""
        return By.CLASS_NAME, "Header_LogoYandex__3TSOI"

    @property
    def header_yandex_dzen(self):
        """Кнопка «Далее» на странице заказа"""
        return By.XPATH, "//header[@id='dzen-header']"
