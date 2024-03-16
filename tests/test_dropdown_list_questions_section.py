import allure
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from const import Const


class TestDropDownSection:

    @allure.title('Наполнение вопросов')
    @pytest.mark.parametrize(
        'question, answer, id',  # Параметры передали в декоратор в виде единой строки
        [
            ['Сколько это стоит? И как оплатить?', 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.', 0],  # Тестовые данные передали вторым аргументом,
            ['Хочу сразу несколько самокатов! Так можно?', 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.', 1],
            ['Как рассчитывается время аренды?', 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.', 2],
            ['Можно ли заказать самокат прямо на сегодня?', 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.', 3],
            ['Можно ли продлить заказ или вернуть самокат раньше?', 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.', 4],  # Тестовые данные передали вторым аргументом,
            ['Вы привозите зарядку вместе с самокатом?', 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.', 5],
            ['Можно ли отменить заказ?', 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.', 6],  # Тестовые данные передали вторым аргументом,
            ['Я жизу за МКАДом, привезёте?', 'Да, обязательно. Всем самокатов! И Москве, и Московской области.', 7]
        ]
    )
    @allure.title('Проверка работы выпадающего списка «Вопросы о важном»')
    @allure.description('При тапе на вопрос должен открываться соответствующий ответ')
    def test_check_question_in_dropdown_list(self, driver, page, question, answer, id):
        with allure.step("step 1. Запрос отправлен, посмотрим код ответа"):
            driver.get(Const.MAIN_PAGE)
            WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.main_page))
        with allure.step("step 2. Запрос отправлен, посмотрим код ответа"):
            element = driver.find_element(*page.dropdown_section)
            driver.execute_script("arguments[0].scrollIntoView();", element)
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable(page.dropdown_section))
            current_question = driver.find_element(*page.dropdown_element_question(id))
            WebDriverWait(driver, 10).until(expected_conditions.visibility_of(current_question))
        with allure.step("step 3. Запрос отправлен, посмотрим код ответа"):
            driver.find_element(*page.dropdown_element_question(id)).click()
            WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((page.open_dropdown_section)))
            current_answer = driver.find_element(*page.dropdown_element_answer(id))
            WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((page.dropdown_element_answer(id))))
        with allure.step("step 4. Запрос отправлен, посмотрим код ответа"):
            assert question == current_question.text
            assert answer == current_answer.text
