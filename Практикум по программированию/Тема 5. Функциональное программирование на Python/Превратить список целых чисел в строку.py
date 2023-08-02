# Задание 8
# При помощи функций map(), filter(), reduce() превратить список целых чисел в строку, 
# содержащую строковое представление этих чисел, разделенных пробелами.
# Пример:
# ввод 1 15 246 156930
# вывод один, пятнадцать, двести сорок шесть, сто пятьдесят шесть тысяч девятьсот тридцать

numbers = [1, 15, 246, 156930]

# функция для преобразования цифры в слово
def digit_to_word(digit):
    if digit == 0:
        return ""
    elif digit == 1:
        return "один"
    elif digit == 2:
        return "два"
    elif digit == 3:
        return "три"
    elif digit == 4:
        return "четыре"
    elif digit == 5:
        return "пять"
    elif digit == 6:
        return "шесть"
    elif digit == 7:
        return "семь"
    elif digit == 8:
        return "восемь"
    elif digit == 9:
        return "девять"

# функция для преобразования двухзначного числа в слово
def two_digits_to_word(number):
    if number < 10:
        return digit_to_word(number)
    elif number < 20:
        if number == 10:
            return "десять"
        elif number == 11:
            return "одиннадцать"
        elif number == 12:
            return "двенадцать"
        elif number == 13:
            return "тринадцать"
        elif number == 14:
            return "четырнадцать"
        elif number == 15:
            return "пятнадцать"
        elif number == 16:
            return "шестнадцать"
        elif number == 17:
            return "семнадцать"
        elif number == 18:
            return "восемнадцать"
        elif number == 19:
            return "девятнадцать"
    else:
        first_digit = number // 10
        second_digit = number % 10
        if second_digit == 0:
            return digit_to_word(first_digit) + "десять"
        else:
            return digit_to_word(first_digit) + "десят " + digit_to_word(second_digit)

# функция для преобразования трехзначного числа в слово
def three_digits_to_word(number):
    first_digit = number // 100
    second_and_third_digits = number % 100
    if second_and_third_digits == 0:
        return digit_to_word(first_digit) + "сот"
    else:
        return digit_to_word(first_digit) + "сот " + two_digits_to_word(second_and_third_digits)

# функция для преобразования четырехзначного числа в слово
def four_digits_to_word(number):
    first_digit = number // 1000
    second_third_and_fourth_digits = number % 1000
    if second_third_and_fourth_digits == 0:
        return digit_to_word(first_digit) + "тысяч"
    else:
        return digit_to_word(first_digit) + "тысяч " + three_digits_to_word(second_third_and_fourth_digits)

# функция для преобразования пятизначного числа в слово
def five_digits_to_word(number):
    first_two_digits = number // 1000
    last_three_digits = number % 1000
    if last_three_digits == 0:
        return two_digits_to_word(first_two_digits) + "тысяч"
    else:
        return two_digits_to_word(first_two_digits) + "тысяч " + three_digits_to_word(last_three_digits)

# функция для преобразования шестизначного числа в слово
def six_digits_to_word(number):
    first_three_digits = number // 1000
    last_three_digits = number % 1000
    if last_three_digits == 0:
        return three_digits_to_word(first_three_digits) + "тысяч"
    else:
        return three_digits_to_word(first_three_digits) + "тысяч " + three_digits_to_word(last_three_digits)

# функция для преобразования числа в слово
def number_to_word(number):
    if number < 0 or number > 999999:
        return ""
    elif number == 0:
        return "ноль"
    elif number < 10:
        return digit_to_word(number)
    elif number < 100:
        return two_digits_to_word(number)
    elif number < 1000:
        return three_digits_to_word(number)
    elif number < 10000:
        return four_digits_to_word(number)
    elif number < 100000:
        return five_digits_to_word(number)
    else:
        return six_digits_to_word(number)

# преобразование списка чисел в список слов
words = [number_to_word(number) for number in numbers]

# объединение списка слов в одну строку через запятую
result = ", ".join(words)

print(result) # вывод результата