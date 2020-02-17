# Homework:  Lesson 8. Task 7

"""
Реализовать  проект  «Операции  с  комплексными  числами».  Создайте  класс  «Комплексное
число»,  реализуйте  перегрузку  методов  сложения  и  умножения  комплексных  чисел.
Проверьте  работу  проекта,  создав  экземпляры  класса  (комплексные  числа)  и  выполнив
сложение  и  умножение  созданных  экземпляров.  Проверьте  корректность  полученного
результата.
"""


class MyComplex:
    def __init__(self, r: float, i: float):
        """
        Конструктор
        :param r: действительная часть комплексного числа
        :param i: мнимая часть комплексного числа
        """
        self.r = r
        self.i = i

    def __str__(self):
        return f"(_ {self.r} {'+' if self.i > 0 else '-'} {abs(self.i)}j _)"

    def __add__(self, other):
        if other.__class__ == MyComplex:
            return MyComplex(self.r + other.r, self.i + other.i)
        elif other.__class__ in {int, float}:
            return MyComplex(self.r + other, self.i)
        else:
            raise TypeError

    def __mul__(self, other):
        if other.__class__ == MyComplex:
            return MyComplex(self.r * other.r - self.i * other.i,
                             self.r * other.i + other.r * self.i)
        elif other.__class__ in {int, float}:
            return MyComplex(self.r * other, self.i * other)
        else:
            raise TypeError


mc_x = MyComplex(2, 3)
mc_y = MyComplex(5, 7)
print(mc_x)
print(mc_y)
print(mc_x + mc_y)
print(mc_x + 0.1)
print(mc_x + 10)
print(mc_x * mc_y)
print(mc_y * mc_x)
print(mc_x * -100)
