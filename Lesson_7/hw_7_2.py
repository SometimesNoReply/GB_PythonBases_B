# Homework:  Lesson 7. Task 2

"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — ​одежда​, которая может иметь определенное название. К
типам одежды в этом проекте относятся ​пальто ​и ​костюм​. У этих типов одежды существуют
параметры: ​размер ​(для ​пальто​) ​и ​рост ​(для ​костюма​). Это могут быть обычные числа: ​V и
H​, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5)​, для костюма ​(2*H + 0.3)​. Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:  реализовать  абстрактные  классы  для
основных  классов  проекта,  проверить  на практике работу декоратора ​@property​.
"""

from abc import ABC, abstractmethod



class Clothes(ABC):
    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def calc_material(self):
        pass

    @property
    def name(self):
        return self.__name


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.v = v

    def calc_material(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.h = h

    def calc_material(self):
        return 2 * self.h + 0.3


co = Coat('Пальто для жеребца', 65)
su = Suit('Костюм для карнавала', 10)
print(f"{co.name} требует {co.calc_material()} кг материала")
print(f"{su.name} требует {su.calc_material()} кв.м материала")
