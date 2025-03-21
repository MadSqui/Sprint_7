import pytest
import allure
from api_methods import ApiMethods

@allure.feature('Получение списка заказов')
class TestGetOrders:

    @allure.story('Получение списка заказов')
    @allure.title('Система возвращает список заказов')
    def test_get_orders(self):
        response = ApiMethods.get_order_list()
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        assert len(response.json()) >= 0