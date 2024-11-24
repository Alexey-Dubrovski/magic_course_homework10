# Создайте класс ContactBook с методом add_contact().
# Реализуйте пользовательские исключения:

# DuplicateContactException — выбрасывается, если контакт
# с таким именем уже существует.

# InvalidPhoneNumberException — выбрасывается, если номер
# телефона не соответствует заданному формату
# (например, не содержит 10 цифр).

# P.s. подумайте как хранить контакт. Я предлагаю вариант - в виде
# класса Contact

class DuplicateContactException(Exception):
    pass


class InvalidPhoneNumberException(Exception):
    pass


class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number


class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        if name in self.contacts:
            raise DuplicateContactException('уже есть')

        if len(phone_number) != 11:
            raise InvalidPhoneNumberException('Должно быть 11 цифр')

        self.contacts[name] = Contact(name, phone_number)

    def show_book(self):
        return {
            name: contact.phone_number
            for name, contact in self.contacts.items()
            }


contacts_book = ContactBook()
contacts_book.add_contact("Alex", "89998887766")
contacts_book.add_contact("Alexey", "89998887765")
contacts_book.add_contact("Alexandr", "89998887764")
# contacts_book.add_contact("Alex", "89998887763")
# contacts_book.add_contact("Andrey", "8999888776")
contacts_book.add_contact("Anton", "89998887763")

print(contacts_book.show_book())