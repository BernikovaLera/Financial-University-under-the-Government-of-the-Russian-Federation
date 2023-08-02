# Задача 7
#? Имеются 2 списка целых чисел, упорядоченные по возрастанию. 
#? Получите новый список, содержащий все элементы исходных списков, 
#? в котором элементы также упорядочены в порядке возрастания, не используя сортировку.

#Код:
mas_1 = map(int, input("Первый список чисел: ").split())
mas_2 = map(int, input("второй список чисел: ").split())
sortMas_1 = sorted(mas_1)
print("Отсортированный первый список: ", sortMas_1)
sortMas_2 = sorted(mas_2)
print("Отсортированный первый список: ", sortMas_2)
list = sortMas_1 + sortMas_2
n = 1 
while n < len(list):
    for i in range(len(list)-n):
        if list[i] > list[i+1]:
            list[i],list[i+1] = list[i+1],list[i]
    n += 1
print(list)