# Задание 3
# Напишите функцию, которая по заданному параметру (число) будет находить ближайшее простое число, 
# большее данного. Например, если дано число 11, то функция возвращает 13. 
# Если входной параметр не является простым числом, то функции должна вернуть 0.


def smallestPrimeNumber(a): # функция: +1 пока не простое число
    if (not simpleNum(a)):
        return 0
    a +=1
    while (not simpleNum(a)):
        a +=1
    return a
def simpleNum(a): # функция нахождения простого числа
    for i in range(2, (a // 2) + 1):
        if (a % i == 0):
            return False
    return True
a = int(input("Введите число: "))
print(smallestPrimeNumber(a))


