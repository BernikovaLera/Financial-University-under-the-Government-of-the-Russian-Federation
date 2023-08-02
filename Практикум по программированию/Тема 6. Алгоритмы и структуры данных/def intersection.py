# Задание 12

# Даны два списка чисел, упорядоченных по возрастанию (каждый список состоит из различных элементов). 
# Найдите пересечение данных множеств, т.е. те числа, которые входят в оба массива. Алгоритм должен иметь сложность O(n+m). 
# То есть, количество операций алгоритма должно быть не больше, чем заранее известная константа, умноженная на (n+m) .
# Решение оформите в виде функции intersection(a: list, b: list) -> list, возвращающий пересечение двух данных списков.
# Полученный список должен быть упорядочен по возрастанию.

def intersection(a: list, b: list) -> list:
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            i += 1
        elif b[j] < a[i]:
            j += 1
        else:
            result.append(a[i])
            i += 1
            j += 1
    return result
a = [6, 0, 3, 4]
b = [2, 4, 6, 8]
common_elements = []

for element in a:
    if element in b:
        common_elements.append(element)

print(common_elements)