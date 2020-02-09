# Homework:  Lesson 6. Task 1

"""
Создать класс ​TrafficLight ​(светофор) и определить у него один атрибут ​color ​(цвет) и метод
running  ​(запуск).  Атрибут  реализовать  как  приватный.  В  рамках  метода  реализовать
переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
состояния (красный) составляет 7 секунд, второго (желтый) ​— 2 секунды, третьего (зеленый)
—  на  ваше усмотрение.  Переключение между режимами должно осуществляться только в
указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
и вызвав описанный метод.
"""

from itertools import cycle
from time import sleep


class TrafficLight:
    __RED = 0
    __YELLOW = 1
    __GREEN = 2
    __tu = (__RED, __YELLOW, __GREEN)
    __signal = ("красный", "желтый", "зеленый")

    def __init__(self):
        self.__color = None

    def running(self):
        battery_charge = 100
        print('Светофор заработал')
        #
        for i in cycle(TrafficLight.__tu):
            # останов
            battery_charge -= 11
            if battery_charge <= 0:
                print('У сфетофора разрядился аккумулятор')
                break
            # работа - смена
            self.__color = i
            print(f"  Зажегся {TrafficLight.__signal[i]} свет светофора")
            # работа - ожидание
            if i == TrafficLight.__RED:      sleep(7)
            if i == TrafficLight.__YELLOW:   sleep(2)
            if i == TrafficLight.__GREEN:    sleep(1)


tl = TrafficLight()
tl.running()
