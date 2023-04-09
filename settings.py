
valid_email = 'mar.nikitos@bk.ru'
valid_password = 'Nikitina123456'
valid_mobile = '89671496581'
name = 'Марина'
surname = 'Ломакина'
region = 'Москва г'
email = 'mar.nikitos91@yandex.ru'
password = 'Nikitina12345'
valid_name = 'ЕА'
valid_name_max = 'РОСТЕЛЕКОМРОСТЕЛЕКОМРОСТЕЛЕКОМ'
thirty_one_letters_name = 'РОСТЕЛЕКОМРОСТЕЛЕКОМРОСТЕЛЕКОМР'

invalid_email = 'mar.nikitos91@bk.ru'
invalid_password = 'Nikitina123456890'
invalid_mobile = '8967149658881'
invalid_name = 'Е'



class BaseUrl:
    base_url = 'https://b2c.passport.rt.ru/'

    CHECK_IN = "Регистрация"
    CONFIRM_EMAIL = 'Подтверждение email'
    EMAIL_INVALID = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    NAME_INVALID = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    FOG_PASSWORD = 'Восстановление пароля'
    ENTRY_VK = 'Войти'
    OK = "Одноклассники"