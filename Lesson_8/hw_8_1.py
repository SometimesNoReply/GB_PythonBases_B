# Homework:  Lesson 8. Task 1

"""
Реализовать  класс  «Дата»,  функция-конструктор  которого  должна  принимать  дату  в  виде
строки  формата  «день-месяц-год».  В  рамках  класса  реализовать  два  метода.  Первый,  с
декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к
типу  «Число».  Второй,  с  декоратором  @staticmethod,  должен  проводить  валидацию  числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
"""

import time


class Date:
    li_date = []

    def __init__(self, string_date: str):
        # функция-конструктор  которого  должна  принимать  дату  в  виде строки  формата  «день-месяц-год».
        Date.li_date = string_date.split('-')

    @classmethod
    def convert(cls):
        # метод с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число»
        for i, el in enumerate(cls.li_date):
            cls.li_date[i] = int(el)

    @staticmethod
    def validate(string_date: str):
        # метод с декоратором  @staticmethod,  должен  проводить  валидацию  числа, месяца и года
        try:
            _ = time.strptime(string_date, '%d-%m-%Y')
        except ValueError:
            return "Error date"
        return "OK"


# Проверить работу полученной структуры на реальных данных.
d = Date('29-02-2020')
print(d.li_date)
d.convert()
print(d.li_date)
print(Date.validate('29-02-2020'))
print(Date.validate('29-02-2021'))
