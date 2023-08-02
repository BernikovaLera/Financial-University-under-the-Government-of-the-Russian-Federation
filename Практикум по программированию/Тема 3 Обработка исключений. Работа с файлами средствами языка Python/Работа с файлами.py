# Задание 1
# Напишите функцию, которая принимает имя файла в текущей папке. 
# Если файла нет, то возвращает текст: "404. File (filename) not found", иначе возвращает содержимое файла.
# Пример:
# >> test_file.txt
# << Text from file

try:
    filename = input("Введите имя файла: ")
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print("404. File not found")