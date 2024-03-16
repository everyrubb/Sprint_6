from selenium.webdriver.common.by import By

class LocatorsPage():

    @property
    def main_page(self):
        """Кнопка «Личный кабинет» на главной странице"""
        return By.CLASS_NAME, "Home_HomePage__ZXKIX"

    @property
    def order_button(self):
        """Кнопка «Личный кабинет» на главной странице"""
        return By.CLASS_NAME, "Button_Button__ra12g"

    @property
    def dropdown_section(self):
        """Кнопка «Личный кабинет» на главной странице"""
        return By.CLASS_NAME, "accordion"

    @property
    def open_dropdown_section(self):
        """Кнопка «Личный кабинет» на главной странице"""
        return By.XPATH, "//div[not(@hidden)]"

    def dropdown_element_question(self, id):
        """Кнопка «Личный кабинет» на главной странице"""
        return By.ID, f"accordion__heading-{id}"

    def dropdown_element_answer(self, id):
        """Кнопка «Личный кабинет» на главной странице"""
        return By.ID, f"accordion__panel-{id}"