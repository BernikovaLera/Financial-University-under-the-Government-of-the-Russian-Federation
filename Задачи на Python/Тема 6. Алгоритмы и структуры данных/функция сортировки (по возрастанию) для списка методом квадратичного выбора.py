# Задание 14

# Реализуйте функцию сортировки (по возрастанию) для списка методом квадратичного выбора.
# Предполагается, что количество элементов в списке является квадратом целого числа.
# Алгоритм квадратичного выбора:
# Создаем пустой список для отсортированных элементов.
# Разделяем список на √n групп по √n элементов и находим минимальный элемент в каждой подгруппе. 
# Выбираем минимальный элемент из минимальных элементов подгрупп и помещаем его в конец списка для отсортированных элементов (из подгруппы удаляем).
# Выбираем минимальный элемент из оставшихся элементов подгруппы, из которой удалили минимальный элемент на предыдущем шаге.
# Возвращаемся к пункту 3.
# После того, как все минимальные подгруппы окажутся пустыми, сортировка будет выполнена.
# Если количество элементов в списке, являющемся параметром функции, не равно квадрату целого числа, то функция должна генерировать исключение.

import math

def quadratic_selection_sort(lst):
    n = len(lst)
    if int(math.sqrt(n))**2 != n:
        raise ValueError("The length of the list is not a perfect square.")
    sorted_lst = []
    while len(sorted_lst) < n:
        min_elems = []
        for i in range(0, n, int(math.sqrt(n))):
            if i + int(math.sqrt(n)) <= n:
                min_elems.append(min(lst[i:i+int(math.sqrt(n))]))
        min_elem = min(min_elems)
        sorted_lst.append(min_elem)
        for i in range(0, n, int(math.sqrt(n))):
            if i + int(math.sqrt(n)) <= n:
                if min_elem in lst[i:i+int(math.sqrt(n))]:
                    lst[i:i+int(math.sqrt(n))].remove(min_elem)
    return sorted_lst

# Пример использования
a = [4, 2, 7, 8]
print(quadratic_selection_sort(a)) # ValueError: The length of the list is not a perfect square.

