import pytest
import allure
from api_methods import ApiMethods
from data import *

@allure.feature('Создание курьера')
class TestCreateCourier:

    @allure.story('Регистрация нового курьера')
    @allure.title('Курьер успешно создается')
    def test_create_courier(self):
        data = courier_data()
        login_pass, response = ApiMethods.register_new_courier_and_return_login_password(data)
        assert response.status_code == 201
        assert len(login_pass) == 3

    @allure.story('Регистрация нового курьера с существующим логином')
    @allure.title('Невозможно создать курьера с уже существующим логином')
    def test_create_courier_with_existing_login(self, courier):
        login, password, first_name = courier
        duplicate_data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        login_pass, response = ApiMethods.register_new_courier_and_return_login_password(duplicate_data)
        assert response.status_code == 409
        assert response.json().get('message') == ErrorText.LOGIN_USED_ERROR_TEXT

    @allure.story('Регистрация курьера с отсутствующим логином')
    @allure.title('Невозможно создать курьера без логина')
    def test_create_courier_without_login(self):
        data = registration_data_without_login()
        login_pass, response = ApiMethods.register_new_courier_and_return_login_password(data)
        assert response.status_code == 400
        assert response.json().get('message') == ErrorText.NOT_ENOUGH_DATA_TO_REG_ERROR_TEXT

    @allure.story('Регистрация курьера с отсутствующим паролем')
    @allure.title('Невозможно создать курьера без пароля')
    def test_create_courier_without_password(self):
        data = registration_data_without_password()
        login_pass, response = ApiMethods.register_new_courier_and_return_login_password(data)
        assert response.status_code == 400
        assert response.json().get('message') == ErrorText.NOT_ENOUGH_DATA_TO_REG_ERROR_TEXT