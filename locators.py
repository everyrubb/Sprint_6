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

    @property
    def select_station_subway(self):
        """Выбор метро в выпадающем листе на странице оформления заказа"""
        return By.XPATH, "//li[@class='select-search__row']//button[.//div[contains(@class, 'Order_Text__2broi') and text()='Бульвар Рокоссовского']]"

    @property
    def complete_station(self):
        """Выбор метро в выпадающем листе на странице оформления заказа"""
        return By.XPATH, "//input[@value='Бульвар Рокоссовского']"

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

    @property
    def select_data_on_piker(self):
        """Календарь выбора даты в форме заказа"""
        return By.XPATH, "//div[contains(@class, 'react-datepicker')]//div[contains(@class, 'react-datepicker__day') and text()='15']"

    @property
    def select_data_in_input(self):
        """Календарь выбора даты в форме заказа"""
        return By.XPATH, "//div[@class='react-datepicker__input-container']//input[@value='15.03.2024']"

    @property
    def input_dropdown_rental_period(self):
        """Календарь выбора даты в форме заказа"""
        return By.CLASS_NAME, "Dropdown-control"
