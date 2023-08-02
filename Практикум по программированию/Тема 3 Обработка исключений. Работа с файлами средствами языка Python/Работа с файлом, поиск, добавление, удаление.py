# Задание 4
# Создайте текстовый файл, содержащий информацию о товарах и ценах на них. Каждая строка файла имеет вид: НАЗВАНИЕ ТОВАРА: ЦЕНА. Используя данный файл создайте функции:
# поиск цены указанного товара или сообщение о том, что цена не известна; 
# добавление в файл информации о новых товарах
# удаление информации о товаре
product_name = input("Введите название товара: ") 
price = input("Введите цену товара: ")

# добавление в файл информации о товарах
my_file = open("spicok.txt", "a")
my_file.write("PRODUCT NAME: PRICE\n")
my_file.write(product_name + ": ")
my_file.write(price + "\n")
my_file.close()

# добавление в файл информации о НОВЫХ товарах
def add_product(product_name, price): 
    with open("spicok.txt", "a") as file:
        file.write(f"{product_name}: {price}")
add_product("potato", 90)
add_product("\n"+"carrot", 80)
add_product("\n"+"apples", 70)

# поиск цены указанного товара или сообщение о том, что цена не известна
def find_price(product_name):
    with open("spicok.txt", "r") as file:
        for line in file:
            name, price = line.strip().split(": ")
            if name == product_name:
                return int(price)
        return "Цена не известна"
print(find_price("potato")) # Output: 90
print(find_price("oranges")) # Output: Цена не известна

# удаление информации о товаре
def remove_product(product_name):
    with open("spicok.txt", "r") as file:
        lines = file.readlines()
    with open("spicok.txt", "w") as file:
        for line in lines:
            name, price = line.strip().split(": ")
            if name != product_name:
                file.write(line)
remove_product("apples")