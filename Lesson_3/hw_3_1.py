# Homework:  Lesson 3. Task 1

"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
ноль.
"""


def my_division(dividend: float, divider: float) -> float:
    """
    Функция принимает 2 числа и возвращает результат деления первого на второе.

    :param dividend: делимое.
    :param divider: делитель. Если делитель равен 0, генерируется исключение ZeroDivisionError.
    :return:
    """
    if divider == 0:
        raise ZeroDivisionError
    # по условиям задачи жестко не требуется функции возвращать значение, но пусть будет
    return dividend / divider


a = float(input("Введите делимое: "))
b = float(input("Введите делитель: "))
try:
    print(f"Частное от деления {a} на {b} будет равно {my_division(a, b)}")
except ZeroDivisionError:
    print(f"На 0 делить нельзя!")
