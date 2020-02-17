# Homework:  Lesson 7. Task 1

"""
Реализовать  класс  ​Matrix  ​(матрица).  Обеспечить  перегрузку  конструктора  класса  (метод
__init__()​), который должен принимать данные (список списков) для формирования матрицы.

Следующий  шаг  —  реализовать  перегрузку  метода  ​__str__()  для  вывода  матрицы  в
привычном виде.

Далее  реализовать  перегрузку  метода  ​__add__()  для  реализации  операции сложения двух
объектов класса ​Matrix ​(двух матриц). Результатом сложения должна быть новая матрица.
"""


class Matrix:
    def __init__(self, li_li):
        self.rows_cnt = len(li_li)                          # строк
        self.cols_cnt = len(max(li_li, key=len))            # столбцов
        self.mtx = li_li
        # настройка
        self.recalc_width()                                 # ширина элемента для вывода
        self.fill_zeroes()                                  # отсутствие считаем нулевыми элементами

    def __str__(self):
        s = f"Матрица {self.rows_cnt}x{self.cols_cnt}:\n"
        for r in self.mtx:
            for c in r:
                s = s + f"{c}".rjust(self.width)
            s = s + "\n"
        return s

    def fill_zeroes(self):
        # отсутствие считаем нулевыми элементами
        for r in self.mtx:
            if len(r) < self.cols_cnt:
                for _ in range(self.cols_cnt - len(r)):
                    r.append(0)

    def recalc_width(self):
        # ширина элемента для вывода
        self.width = max(len(str(max(max(self.mtx, key=max)))),
                         len(str(min(min(self.mtx, key=min))))
                         ) + 1 + 3

    def __add__(self, other):
        # требуем
        if type(self) != type(other):
            raise TypeError
        # требуем одинакового размера
        if self.rows_cnt != other.rows_cnt or self.cols_cnt != other.cols_cnt:
            raise IndexError
        # вычисляем
        new_matrix = self.mtx
        for i_r in range(self.rows_cnt):
            for i_c in range(self.cols_cnt):
                new_matrix[i_r][i_c] = new_matrix[i_r][i_c] + other.mtx[i_r][i_c]
        return Matrix(new_matrix)




matrix_a = [[1, 2, 3], [1], [1, 2, 11, 4, 5]]
m_a = Matrix(matrix_a)
m_b = Matrix([[-1, -2, -3], [10, 20, 30, 40], [1, 2, 11, 100, 1000]])
print(m_a)
print(m_b)
m_c = m_a + m_b
print(m_c)
