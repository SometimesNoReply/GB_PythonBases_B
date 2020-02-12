# Homework:  Lesson 6. Task 3

"""
 Реализовать  базовый  класс  ​Worker  ​(работник),  в  котором  определить  атрибуты:  ​name​,
surname​,  ​position  ​(должность),  ​income  ​(доход).  Последний  атрибут  должен  быть
защищенным  и  ссылаться  на  словарь,  содержащий  элементы:  оклад  и  премия,  например,
{"wage": wage, "bonus": bonus}. ​Создать класс ​Position ​(должность) на базе класса ​Worker​.
В классе Position реализовать методы получения полного имени сотрудника (​get_full_name​) и
дохода с учетом премии (​get_total_income​). Проверить работу примера на реальных данных
(создать  экземпляры  класса  ​Position​,  передать  данные,  проверить  значения  атрибутов,
вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name: str, surname: str, position: str, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, worker: Worker):
        super().__init__(worker.name, worker.surname, worker.position, worker._income["wage"], worker._income["bonus"])

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return int(self._income["wage"]) + int(self._income["bonus"])


# создать
w = Worker("Bill", "Gates", "philanthropist", 0, 100500)
# передать
p = Position(w)
# проверить
print(f"p.name = {p.name}")
print(f"p.surname = {p.surname}")
print(f"p.position = {p.position}")
print(f"p._income = {p._income}")
# вызвать
print(f"{p.get_full_name()} зарабатывает {p.get_total_income()}")
