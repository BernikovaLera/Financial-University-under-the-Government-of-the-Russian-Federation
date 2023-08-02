# Задание 6
# Создайте класс Sheet (ведомость) со следующими атрибутами:
# discipline_list – список дисциплин, значением является список с названиями дисциплин;
# discipline – дисциплина группы, при задании значения проверять наличие дисциплины в атрибуте discipline_list;
# group – группа.
# Методы класса:
# put – добавляет в ведомость информацию об оценке студента (фамилия, оценка – параметры метода). Для хранения данных внутри класса используйте словарь, в котором ключом является фамилия студента. Возможные оценки – «отлично», «хорошо», «удов», «неуд»;
# get – возвращает оценку, полученную студентом (фамилия студента – параметр метода);
# change – изменяет оценку, полученную студентом (фамилия студента и новая оценка – параметры метода);
# del – удаляет информацию о студенте из ведомости (фамилия студента – параметр метода);
# result – возвращает кортеж из 5 чисел (количество каждого вида оценок в ведомости);
# __init__ – конструктор;
# __str__ – возвращает строку, содержащую заголовки (название экзамена, группа) и результаты экзамена в виде таблицы;
# count – возвращает количество студентов в ведомости;
# names – возвращает список фамилий, имеющихся в ведомости.
# Продемонстрируйте работу с классами, создав необходимые объекты и вызвав их методы.

class Sheet:
    discipline_list = ['Математика', 'Химия', 'География', 'Программирование', 'Машинное обучение']
    def __init__(self, discipline, group):
        if discipline not in self.discipline_list:
            raise ValueError(f"Дисциплины '{discipline}' нет в списке дисциплин")
        self.discipline = discipline
        self.group = group
        self.students = {}
    def put(self, name, grade):
        if grade not in ['отлично', 'хорошо', 'удов', 'неуд']:
            raise ValueError("Неверная оценка")
        self.students[name] = grade
    def get(self, name):
        return self.students.get(name, "Студент не найден")
    def change(self, name, new_grade):
        if new_grade not in ['отлично', 'хорошо', 'удов', 'неуд']:
            raise ValueError("Неверная оценка")
        if name not in self.students:
            raise KeyError("Студент не найден")
        self.students[name] = new_grade
    def delete(self, name):
        if name in self.students:
            del self.students[name]
    def result(self):
        grades = {'отлично': 0, 'хорошо': 0, 'удов': 0, 'неуд': 0}
        for grade in self.students.values():
            grades[grade] += 1
        return tuple(grades.values())
    def __str__(self):
        output = f"Экзамен: {self.discipline}\nГруппа: {self.group}\nПолученные результаты:\n"
        for name, grade in self.students.items():
            output += f"{name}: {grade}\n"
        return output
    def count(self):
        return len(self.students)
    def names(self):
        return list(self.students.keys())

sheet = Sheet("Программирование", "ДПИ22-1с") # объект класса Sheet

sheet.put("Иванов", "отлично") # студенты
sheet.put("Смирнов", "хорошо")
sheet.put("Витальев", "хорошо")
sheet.put("Кузнецов", "удов")
sheet.put("Попов", "неуд")

print(sheet.get("Ivanov")) # получаем оценку студента
sheet.change("Смирнов", "отлично") # изменяем оценку студента
sheet.delete("Кузнецов") # удаляем студента из ведомости
print(sheet.result()) # выводим результаты
print(sheet) # выводим объект класса Sheet
print(sheet.count()) # выводим количество студентов
print(sheet.names()) # иыводим список фамилий
