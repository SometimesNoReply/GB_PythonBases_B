# Homework:  Lesson 4. Task 1

"""
Реализовать  скрипт,  в  котором  должна  быть  предусмотрена  функция  расчета  заработной
платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах*ставка в
час)  +  премия.  Для  выполнения  расчета  для  конкретных  значений  необходимо  запускать
скрипт с параметрами
"""

from sys import argv


def calc_salary(hours: float, hour_rate: int, award: int = 0) -> int:
    """
    функция рассчитывает заработную плату сотрудника.

    :param hours: количество отработанных часов (в копейках, int)
    :param hour_rate: часовая ставка (в часах, float)
    :param award: премия (в копейках, int)
    :return: рассчитанная зарплата (в копейках, int)
    """
    return round(hours * hour_rate) + award

# проверка числа параметров
if len(argv) not in (3, 4):
    print("Формат запуска:")
    print("    python hw_4_1.py hours hour_rate award")
    print("Параметры:")
    print("    hw_4_1.py - модуль расчета зарплаты")
    print("    hours - количество отработанных часов (float)")
    print("    hour_rate - часовая ставка работника в копейках (int))")
    print("    award - размер премии в копейках (int). Необязательный параметр")
    exit(1)

# вычисления
try:
    if len(argv) == 3:
        print(f"Зарплата составляет: {calc_salary(float(argv[1]), int(argv[2]))}")
    if len(argv) == 4:
        print(f"Зарплата составляет: {calc_salary(float(argv[1]), int(argv[2]), int(argv[3]))}")
except ValueError:
    print("Неверно задан один из числовых параметров")
