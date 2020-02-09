# Homework:  Lesson 6. Task 4

"""
Реализуйте базовый класс ​Car​. У данного класса должны быть следующие атрибуты: ​speed​,
color​,  ​name​,  ​is_police  ​(булево).  А  также  методы: ​go​, ​stop​, ​turn(direction)​, которые должны
сообщать,  что  машина  поехала,  остановилась,  повернула  (куда).  Опишите  несколько
дочерних классов: ​TownCar​, ​SportCar​, ​WorkCar​, ​PoliceCar​. Добавьте в базовый класс метод
show_speed​,  который  должен  показывать  текущую  скорость  автомобиля.  Для  классов
TownCar ​и ​WorkCar ​переопределите метод ​show_speed​. При значении скорости свыше 60
(​TownCar​) и 40 (​WorkCar​) должно выводиться сообщение о превышении скорости.
Создайте  экземпляры  классов,  передайте  значения  атрибутов.  Выполните  доступ  к
атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return self.name + " is driving"

    def stop(self):
        return self.name + " is stopped"

    def turn(self, direction: str):
        print(self.name + " направляется на " + direction)

    def show_speed(self):
        print('скорость у', self.name, self.speed, "км/ч")


class TownCar(Car):
    def __init__(self):
        super().__init__(35, 'black', 'бумер', False)

    def show_speed(self):
        print('скорость', self.name, self.speed, "км/ч")
        if self.speed > 40:
            print("    ахтунг! Превышена скорость!")


class SportCar(Car):
    def __init__(self):
        super().__init__(300, 'red', 'спорткар', False)


class WorkCar(Car):
    def __init__(self):
        super().__init__(90, 'orange', 'КаМаЗ', False)

    def show_speed(self):
        print('скорость', self.name, self.speed, "км/ч")
        if self.speed > 60:
            print("    ахтунг! Превышена скорость!")


class PoliceCar(Car):
    def __init__(self):
        super().__init__(65, 'khaki', 'БМП', True)


tc, sc, wc, pc = TownCar(), SportCar(), WorkCar(), PoliceCar()

tc.speed = 45
sc.color = 'white'
wc.name = 'белаз'
pc.is_police = False

print(tc.speed)
print(sc.color)
print(wc.name)
print(pc.is_police)

tc.go()
tc.stop()
sc.show_speed()
wc.show_speed()
pc.turn("Берлин")
