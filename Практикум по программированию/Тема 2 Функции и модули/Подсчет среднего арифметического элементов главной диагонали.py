# Задание 23
#? Элементами матрицы являются случайные положительные целые числа из заданного диапазона. 
#? Число строк и столбцов матрицы задается с клавиатуры. 
#? Написать функцию подсчета среднего арифметического элементов над главной диагональю и количество четных элементов под ней. 
#? Если матрица не является квадратной, должно генерироваться исключение.


import random  
def creatArray():
    print('Введите количество столбцов: ')
    x = int(input())
    print('Введите количество строк: ')
    y = int(input())
    return [[random.randint(0,100) for i in range(x)] for j in range(y)]
print(creatArray())

def foo(arr):
    s=0
    n=len(arr)
    for i in range(n):
        s+=arr[i][i]
    return s/n