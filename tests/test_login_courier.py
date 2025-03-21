import pytest
import allure
from api_methods import ApiMethods
from data import ErrorText

@allure.feature('Логин курьера')
class TestLoginCourier:

    @allure.story('Авторизация курьера')
    @allure.title('Курьер успешно авторизуется')
    def test_login_courier_success(self, courier):
        login, password, _ = courier
        login_data = {
            "login": login,
            "password": password
        }
        response = ApiMethods.login_courier(login_data)
        assert response.status_code == 200
        assert "id" in response.json()

    @allure.story('Авторизация курьера с неверными данными')
    @allure.title('Ошибка авторизации при неверном логине или пароле')
    def test_login_courier_invalid_data(self, courier):
        login, password, _ = courier
        login_data = {
            "login": login,
            "password": "wrong_password"
        }
        response = ApiMethods.login_courier(login_data)
        assert response.status_code == 404
        assert response.json().get('message') == ErrorText.NON_EXISTENT_ACC_DATA_ERROR_TEXT

    @allure.story('Авторизация курьера с отсутствующим логином')
    @allure.title('Ошибка авторизации без логина')
    def test_login_courier_without_login(self):
        login_data = {
            "password": "random_password"
        }
        response = ApiMethods.login_courier(login_data)
        assert response.status_code == 400
        assert response.json().get('message') == ErrorText.EMPTY_LOGIN_PASSWORD_FIELD_ERROR_TEXT

    @allure.story('Авторизация курьера с отсутствующим паролем')
    @allure.title('Ошибка авторизации без пароля')
    def test_login_courier_without_password(self):
        login_data = {
            "login": "random_login"
        }
        response = ApiMethods.login_courier(login_data)
        assert response.status_code == 400
        assert response.json().get('message') == ErrorText.EMPTY_LOGIN_PASSWORD_FIELD_ERROR_TEXT