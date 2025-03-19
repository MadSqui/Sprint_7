import allure
from helpers import generate_courier_data


@allure.step('Получаем тело запроса для регистрации курьера')
def courier_data():
    login, password, first_name = generate_courier_data()
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload

@allure.step('Генерируем данные без логина')
def registration_data_without_login():
    data = courier_data()
    data.pop("login")
    return data

@allure.step('Генерируем данные без пароля')
def registration_data_without_password():
    data = courier_data()
    data.pop("password")
    return data

@allure.step('Вносим данные для создания заказа')
def get_order_payload(color):
    return {
    "firstName": "Lupa",
    "lastName": "Pupov",
    "address": "Pererva, 53",
    "metroStation": 5,
    "phone": "+7 000 666 66 66",
    "rentTime": 2,
    "deliveryDate": "2025-03-25",
    "comment": "Можно побыстрее???",
    "color": [color]
}

class ErrorText:
    class LoginErrorText:
        NON_EXISTENT_ACC_DATA_ERROR_TEXT = 'Учетная запись не найдена'
        EMPTY_LOGIN_PASSWORD_FIELD_ERROR_TEXT = 'Недостаточно данных для входа'

    class RegistrationErrorText:
        NOT_ENOUGH_DATA_TO_REG_ERROR_TEXT = 'Недостаточно данных для создания учетной записи'
        LOGIN_USED_ERROR_TEXT = 'Этот логин уже используется. Попробуйте другой.'