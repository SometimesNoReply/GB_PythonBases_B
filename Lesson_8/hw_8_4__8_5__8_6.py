# Homework:  Lesson 8. Task 4

"""
Начните  работу  над  проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные  типы  оргтехники  (принтер,  сканер,  ксерокс).  В  базовом  классе  определить
параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""

# Homework:  Lesson 8. Task 5

"""
Продолжить  работу  над  первым  заданием.  Разработать  методы,  отвечающие  за  приём
оргтехники  на  склад  и  передачу  в  определенное  подразделение  компании.  Для  хранения
данных  о  наименовании  и  количестве  единиц  оргтехники,  а  также  других  данных,  можно
использовать любую подходящую структуру, например словарь.
"""

# Homework:  Lesson 8. Task 6

"""
Продолжить  работу  над  вторым  заданием.  Реализуйте  механизм  валидации  вводимых 
пользователем  данных.    
"""


class OfficeEquipment:
    # Базовый класс офисной техники

    def __init__(self, serial_number: str, model: str):
        """
        Конструктор
        :param serial_number:    заводской номер устройства офисной техники
        :param model:            модель (производитель) устройства
        """
        self.serial_number = serial_number
        self.model = model
        self._device_type = None

    def __str__(self):
        return f"Прибор {self.model} с заводским номером {self.serial_number}"

    @property
    def device_type(self):
        return self._device_type


class Printer(OfficeEquipment):
    def __init__(self, serial_number: str, model: str, print_on_CD_DVD: bool):
        """
        Конструктор
        :param serial_number:    заводской номер устройства офисной техники
        :param model:            модель (производитель) устройства
        :param print_on_CD_DVD:  признак, что принтер способен печатать на CD,DVD дисках
        """
        super().__init__(serial_number, model)
        self._device_type = "Принтер"
        self.print_on_CD_DVD = print_on_CD_DVD


class Scanner(OfficeEquipment):
    def __init__(self, serial_number: str, model: str, film_adapter: bool):
        """
        Конструктор
        :param serial_number:    заводской номер устройства офисной техники
        :param model:            модель (производитель) устройства
        :param film_adapter:     признак наличия слайд-сканера в устройстве
        """
        super().__init__(serial_number, model)
        self._device_type = "Сканер"
        self.film_adapter = film_adapter


class Xerox(OfficeEquipment):
    def __init__(self, serial_number: str, model: str, sensor_display: bool):
        """
        Конструктор
        :param serial_number:    заводской номер устройства офисной техники
        :param model:            модель (производитель) устройства
        :param sensor_display:   признак наличия сенсорного дисплея в устройстве
        """
        super().__init__(serial_number, model)
        self._device_type = "Ксерокс"
        self.sensor_display = sensor_display


class Warehouse:
    def __init__(self):
        self.devices = dict()  # словарь устройств. ключ - экземпляр устройства, значение - его месронахождение
        self.have = dict()  # словарь количества устройств на складе по типам

    def info(self):
        # вывод на экран информации
        print("На складе по типам устройств имеется:")
        for key, value in self.have.items():
            print(f' - Приборов типа "{key}" имеется {value} шт')

        print("Склад следит за:")
        for key, value in self.devices.items():
            print(f' - Устройство "{key}" находится {value}')

    def __validate_element(self, el):
        """
        Валидация, что проверяемый тип переменной является потомком класса оргтехники (OfficeEquipment).
        В случае нарушения вызывает исключение TypeError
        :param el:   проверяемый тип переменной
        """
        if not issubclass(el.__class__, OfficeEquipment):
            raise TypeError

    def receipt(self, oe: OfficeEquipment):
        """
        поступление на склад
        :param oe: объект офисной техники
        """
        self.__validate_element(oe)
        self.devices[oe] = 'на складе'
        # количество
        if self.have.get(oe.device_type) is None:
            self.have[oe.device_type] = 1
        else:
            self.have[oe.device_type] += 1

    def give_out(self, oe: OfficeEquipment, dept_to: str):
        """
        выдать со склада
        :param oe: объект офисной техники
        :param dept_to: отдел назначения
        """
        self.__validate_element(oe)
        # нет в списках - не выдаем
        if self.devices.get(oe) is None:
            return
        # есть в списке - выдаем
        if self.devices[oe] == 'на складе':
            self.devices[oe] = f'в отделе {dept_to}'
            self.have[oe.device_type] -= 1

    def take_back(self, oe: OfficeEquipment, dept_from: str):
        """
        вернуть на склад
        :param oe: объект офисной техники
        :param dept_from: отдел изъятия
        """
        self.__validate_element(oe)
        # нет в списках - не изымаем
        if self.devices.get(oe) is None:
            return
        # есть в списке - изымаем
        if self.devices[oe] == f'в отделе {dept_from}':
            self.devices[oe] = 'на складе'
            self.have[oe.device_type] += 1


li = [
    Printer("012459", "HP", True),
    Printer("012460", "HP", True),
    Scanner("77-54234-1", "Canon", False),
    Scanner("555.44QA", "Canon", True),
    Xerox("123-123-0001", "XEROX", True),
    "bug-тест",
]

w = Warehouse()
for elm in li:
    try:
        w.receipt(elm)
    except TypeError:
        print(f"ВНИМАНИЕ {elm} - не разрешенный элемент для склада")

w.give_out(li[1], "#20")
w.give_out(li[2], "Research")
w.take_back(li[2], "Research")
w.give_out(li[3], "HR")
w.give_out(li[4], "Security")
w.info()
