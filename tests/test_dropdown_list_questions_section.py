import allure
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from const import Const


class TestDropDownSection:

    @allure.title('Проверка работы выпадающего списка «Вопросы о важном»')
    @allure.description('При тапе на вопрос должен открываться соответствующий ответ')
    @pytest.mark.parametrize(
        'question, answer, id',
        [
            ['Сколько это стоит? И как оплатить?', 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.', 0],
            ['Хочу сразу несколько самокатов! Так можно?', 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.', 1],
            ['Как рассчитывается время аренды?', 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.', 2],
            ['Можно ли заказать самокат прямо на сегодня?', 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.', 3],
            ['Можно ли продлить заказ или вернуть самокат раньше?', 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.', 4],
            ['Вы привозите зарядку вместе с самокатом?', 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.', 5],
            ['Можно ли отменить заказ?', 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.', 6],
            ['Я жизу за МКАДом, привезёте?', 'Да, обязательно. Всем самокатов! И Москве, и Московской области.', 7]
        ]
    )

    def test_check_question_in_dropdown_list(self, driver, page, question, answer, id):
        with allure.step("Step 1. Открываем сайт (https://qa-scooter.praktikum-services.ru/) «Яндекс.Самокат»"):
            with allure.step("Пользователь находится на главной странице «Яндекс.Самоката»"):
                driver.get(Const.MAIN_PAGE)
                WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(page.main.main_page))
        with allure.step("Step 2. Скролим до выпадающего списка «Вопросы о важном»"):
            with allure.step("На экране отображается список вопросов в виде аккордеон»"):
                element = driver.find_element(*page.main.dropdown_section)
                driver.execute_script("arguments[0].scrollIntoView();", element)
                WebDriverWait(driver, 3).until(EC.element_to_be_clickable(page.main.dropdown_section))
                current_question = driver.find_element(*page.main.dropdown_element_question(id))
                WebDriverWait(driver, 10).until(expected_conditions.visibility_of(current_question))
        with allure.step(f"Step 3. Тапнуть на вопрос {question}"):
            with allure.step(f"Открылся ответ {answer}"):
                driver.find_element(*page.main.dropdown_element_question(id)).click()
                WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((page.main.open_dropdown_section)))
                current_answer = driver.find_element(*page.main.dropdown_element_answer(id))
                WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((page.main.dropdown_element_answer(id))))
        with allure.step("Step 4. Содержание вопроса и ответа соответствует требованиям заказчика"):
            with allure.step(f"Вопрос {question}"):
                assert question == current_question.text
            with allure.step(f"Ответ {answer}"):
                assert answer == current_answer.text
