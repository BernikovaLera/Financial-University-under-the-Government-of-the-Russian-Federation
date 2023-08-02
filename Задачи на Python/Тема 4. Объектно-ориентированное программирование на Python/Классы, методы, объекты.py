# Задание 7
# Создайте класс Order (заказ) со следующими аттрибутами:
# product_code – код_товара;
# price (цена);
# count (количество)
# Методы класса:
# __init__;
# __str__.
# Создайте 2 класса-потомка: Opt (опт) и Retail (розница) с методами __init__, __str__ и summary, позволяющим узнать стоимость заказа. 
# Для опта стоимость единицы товара составляет 95% от цены, а при покупке более 500 штук – 90% цены. 
# В розницу стоимость единицы товара составляет 100% цены. Стоимость заказа равна произведению цены на количество.
# Продемонстрируйте работу с классами, создав необходимые объекты и методы.

class Order:
    def __init__(self, product_code, price, count):
        self.product_code = product_code
        self.price = price
        self.count = count
    def __str__(self):
        return f"Заказ(Код продукта: {self.product_code}, Количество: {self.count}, Цена: {self.price})"
class Opt(Order):
    def __init__(self, product_code, price, count):
        super().__init__(product_code, price, count)
    def __str__(self):
        return f"ОПТ({super().__str__()})"
    def summary(self):
        discount = 0.95 if self.count <= 500 else 0.90
        return self.price * self.count * discount
class Retail(Order):
    def __init__(self, product_code, price, count):
        super().__init__(product_code, price, count)
    def __str__(self):
        return f"Розница({super().__str__()})"
    def summary(self):
        return self.price * self.count

opt_order = Opt("TY1010", 100, 200) # объекты классов Opt и Retail
retail_order = Retail("LM3958", 100, 30)
print(opt_order) 
print(f"Оптовая стоимость заказа: {opt_order.summary()}")
print(retail_order)
print(f"Розничная стоимость заказа: {retail_order.summary()}")