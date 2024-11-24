# Создайте класс User с полями username и password.
# Реализуйте собственные исключения:

# UsernameTooShortException — выбрасывается,
# если длина username меньше 5 символов.

# PasswordTooWeakException — выбрасывается,
# если пароль не соответствует заданным требованиям (например,
# меньше 8 символов или не содержит цифр).

# Создайте метод validate_user(), который проверяет
# корректность username и password и выбрасывает исключения
# при необходимости.

class UsernameTooShortException(Exception):
    pass


class PasswordTooWeakException(Exception):
    pass


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.validate_user()

    def validate_user(self):
        if len(self.username) < 5:
            raise UsernameTooShortException("username < 5")

        if len(self.password) < 8:
            raise PasswordTooWeakException('password < 8')
        elif not any(char.isdigit() for char in self.password):
            raise PasswordTooWeakException('no digit')
        return 'Принято'


user = User("Maximus", "qwerty123456")
print(user.validate_user())
