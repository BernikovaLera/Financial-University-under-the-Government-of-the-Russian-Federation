# Задание 4
# Напишите функцию, которая по строке, являющейся параметром функции, составляет словарь, 
# ключами которого являются все встречающиеся в строке пары стоящих рядом друг с другом символов, 
# а значениями - количество этих пар в строке.


def numberOfRepetitionsOfCharacterPairs(text):
    # цикл от 0 до длины входной строки
    # проверим условие что i+1 меньше длины строки иначе, если символ і последний, то когда буду пытаться получить text[i+1] будет ошибка
    # и проверяю потом что text[i] == text[i+1], если текущий символ равен следующему
    # получается что в listOfDoubleCharacters элемент запишется только если выполнится условие справа
    # т.е. в цикле перебираем всю строку
    # если текущий и след символы равны, то в список добавляем кусочек строки text[i:i+2]
    listOfDoubleCharacters = [text[i:i+2] for i in range(0, len(text)) if (i+1 < len(text) and text[i] == text[i+1])]
    result = {}
    for pair in listOfDoubleCharacters:
        if (pair in result):
            result[pair] += 1
        else:
            result[pair] = 1
    return result
print(numberOfRepetitionsOfCharacterPairs(input("Введите строку: ")))

