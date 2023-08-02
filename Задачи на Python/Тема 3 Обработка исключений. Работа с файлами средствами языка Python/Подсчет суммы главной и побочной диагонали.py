# Задание 3
# Написать функцию подсчета суммы главной или побочной диагонали. 
# Если матрица не является квадратной, должен вызываться кастомный класс исключения MyError, 
# который принимает строковое сообщение msg в качестве параметра при инициализации. Подсказка: 
# Чтобы определить кастомный класс исключения, нужно создать класс, унаследованный от Exception.
# Пример:
#      1 2 3
# >>   4 5 6
#      7 8 9 1
# << MyError: matrix is ​​not square

class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
def sum_main_diagonal(matrix):
    n = len(matrix)
    if not all(len(row) == n for row in matrix):
        raise MyError("matrix is ​​not square")
    sum_diag = 0
    for i in range(n):
        sum_diag += matrix[i][i]
    return sum_diag
def sum_secondary_diagonal(matrix):
    n = len(matrix)
    if not all(len(row) == n for row in matrix):
        raise MyError("matrix is ​​not square")
    sum_diag = 0
    for i in range(n):
        sum_diag += matrix[i][n-i-1]
    return sum_diag

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 1]]
try:
    print(f'сумма главной диагонали {sum_main_diagonal(matrix)}') 
    print(f'сумма побочной диагонали {sum_secondary_diagonal(matrix)}') 
except MyError as e:
    print(f' MyError: {e.msg}') # Матрица не является квадратной