# Задание 11

# Даны два списка a и b упорядоченных по неубыванию. Объедините их в один упорядоченный по неубыванию список. 
# Сложность алгоритма при этом должна обязательно быть меньше квадратичной.
# Решение оформите в виде функции, возвращающей новый список без модификации исходных списков merge(a: list, b: list) -> list.

def merge(a, b):
    result = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result += a[i:]
    result += b[j:]
    return result

a = [1, 3, 5]
b = [2, 4, 6]
merged = merge(a, b)
print(merged)  # [1, 2, 3, 4, 5, 6]