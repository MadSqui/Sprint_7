import pytest
import allure
from api_methods import ApiMethods
from data import get_order_payload

@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.story('Создание заказа с одним цветом')
    @allure.title('Можно указать один цвет для заказа')
    @pytest.mark.parametrize("color", ["BLACK", "GREY"])
    def test_create_order_with_one_color(self, color):
        order_response = ApiMethods.create_order(color)
        assert order_response.status_code == 201
        assert "track" in order_response.json()

    @allure.story('Создание заказа с двумя цветами')
    @allure.title('Можно указать два цвета для заказа')
    def test_create_order_with_two_colors(self):
        order_response = ApiMethods.create_order("BLACK, GREY")
        assert order_response.status_code == 201
        assert "track" in order_response.json()

    @allure.story('Создание заказа без указания цвета')
    @allure.title('Можно создать заказ без указания цвета')
    def test_create_order_without_color(self):
        order_response = ApiMethods.create_order("")
        assert order_response.status_code == 201
        assert "track" in order_response.json()