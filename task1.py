# Создайте функцию для чтения файла.
# Прочитать информацию из файла, если его нет
# - обработать ошибку и вернуть пустую строку.

def reading(file_name):
    try:
        with open(file_name, "r", encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return 'Not Found'


result = reading("test.txt")
print(result)
