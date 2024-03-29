# задание 21
#? Дана дробь n / m , n и m - натуральные числа.
#? Напишите 2 функции, которые сокращают эту дробь, то есть находят числа p и q такие, что n / m = p / q , и дробь p / q — несократимая
#? Случай 1 аргументами функции являются числа n, m, функция возвращает кортеж (p, q);
#? Случай 2 аргументом функции является список [n, m], функция не возвращает значения, а изменяет этот список на [p, q].

# код Случай 1

def ReduceFraction(n, m):
    if n > m:
        k = n
    else:
        k = m
    while k != 1:
        if n % k == 0 and m % k == 0:
            return n // k, m // k
        else:
            k -= 1
    return n, m
n, m = int(input("Числитель: ")), int(input("Знаменатель: "))
print("Ответ: ")
print(*ReduceFraction(n, m)) # функция возвращает кортеж

# код Случай 2
def met(n, m):
    if n > m:
        k = n
    else:
        k = m
    while k != 1:
        if n % k == 0 and m % k == 0:
            return n // k, m // k
        else:
            k -= 1
    return n, m
n, m = [int(s) for s in input("Введите числитель и знаменатель через пробел: ").split()]
print("Ответ: ")
print(met(n, m))