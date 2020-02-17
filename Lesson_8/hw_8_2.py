# Homework:  Lesson 8. Task 2

"""
 Создайте  собственный  класс-исключение,  обрабатывающий  ситуацию  деления  на  нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
ошибкой.
"""


class MyZeroDivisionError(Exception):
    def __init__(self, msg):
        self.msg = msg


i_num = int(input("На какое число вы хотите разделить 100? Введите:   "))
try:
    if i_num == 0:
        raise MyZeroDivisionError('Уважаемый, на ноль делить нельзя!')
    else:
        print(f"100 / {i_num} = {100 / i_num}")
except MyZeroDivisionError as err:
    print(err)
