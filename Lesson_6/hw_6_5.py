# Homework:  Lesson 6. Task 5

"""
 Реализовать класс ​Stationery ​(канцелярская принадлежность). Определить в нем атрибут ​title
(название) и метод ​draw ​(отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
три  дочерних класса ​Pen ​(ручка), ​Pencil ​(карандаш), ​Handle ​(маркер). В каждом из классов
реализовать переопределение метода ​draw​. Для каждого из классов метод должен выводить
уникальное  сообщение.  Создать  экземпляры  классов  и  проверить,  что выведет описанный
метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("запуск отрисовки")


class Pen(Stationery):
    def __init__(self):
        super().__init__("Ручка")

    def draw(self):
        print("запуск отрисовки черной ручкой")


class Pencil(Stationery):
    def __init__(self):
        super().__init__("Карандаш")

    def draw(self):
        print("запуск отрисовки твердым карандашом")


class Handle(Stationery):
    def __init__(self):
        super().__init__("Маркер")

    def draw(self):
        print("запуск отрисовки красным маркером")


s = Stationery('абстрактное средство рисования')
p = Pen()
ps = Pencil()
h = Handle()

s.draw()
p.draw()
ps.draw()
h.draw()
