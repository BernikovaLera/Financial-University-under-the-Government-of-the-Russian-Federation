# Задание 5
# Создайте класс Point (точка), у которого имеются 2 атрибута x и y (координаты) и методы __init__() и __str__(), и класс Rect (прямоугольник) у которого есть:
# два атрибута (верхний левый угол и правый нижний угол прямоугольника), значениями которых являются объекты класса Point;
# методы __init__() и __str__();
# метод sides(), возвращающий длины сторон прямоугольника;
# метод perim(), вычисляющий периметр прямоугольника
# Продемонстрируйте работу с классами, создав необходимые объекты и вызвав их методы.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Точки({self.x}, {self.y})"
class Rect:
    def __init__(self, upper_left_corner, lower_right_corner):
        self.upper_left_corner = upper_left_corner
        self.lower_right_corner = lower_right_corner
    def __str__(self):
        return f"Прямоугольник({self.upper_left_corner}, {self.lower_right_corner})"
    def sides(self):
        side_a = abs(self.lower_right_corner.x - self.upper_left_corner.x)
        side_b = abs(self.upper_left_corner.y - self.lower_right_corner.y)
        return side_a, side_b
    def perim(self):
        side_a, side_b = self.sides()
        return 2 * (side_a + side_b)

challengePoint1 = Point(2,4) # объекты класса Point
challengePoint2 = Point(3,5)
challengeRect = Rect(challengePoint1, challengePoint2) # объект класса Rect

print(challengePoint1) # вывод
print(challengePoint2)
print(challengeRect)
print(f"Стороны: {challengeRect.sides()}")
print(f"Периметр: {challengeRect.perim()}")