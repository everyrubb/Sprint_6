from selenium.webdriver.common.by import By


class TestMainPageLocators:

    "Я знаю, что ревьюверы хотят в виде констант, но я сделала так. Для меня это более удобный и читабельный вариант"

    @property
    def main_page(self):
        """Отображается главная страница «Яндекс.Самоката»"""
        return By.CLASS_NAME, "Home_HomePage__ZXKIX"

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
    def logo_scooter(self):
        """Логотип «Самокат» В Яндекс Самокате"""
        return By.CLASS_NAME, "Header_LogoScooter__3lsAR"

    @property
    def logo_yandex(self):
        """Логотип Яндекса в Яндекс.Самокате"""
        return By.CLASS_NAME, "Header_LogoYandex__3TSOI"

    @property
    def header_yandex_dzen(self):
        """Хедер Яндекс Дзена"""
        return By.XPATH, "//header[@id='dzen-header']"