# Задание 2
# Написать функцию умножения неограниченного количества чисел. Если аргумент не является числом, то должна возвращаться ошибка ValueError
# Примеры:
# >> 1 2 3 4
# << 24
# >> 1 2 3 t
# << ValueError: invalid char

def multiply(*args):
    result = 1
    for num in args:
        if not isinstance(num, (int, float)):
            raise ValueError("Аргумент должен быть числом")
        result *= num
    return result

print(multiply(1, 2, 3, 4))  # 24
print(multiply(1, 2, 4, "t"))  # ValueError: Аргумент должен быть числом