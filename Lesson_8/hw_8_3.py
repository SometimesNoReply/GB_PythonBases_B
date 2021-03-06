# Homework:  Lesson 8. Task 3

"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на
наличие  только  чисел.  Проверить  работу  исключения  на  реальном  примере.  Необходимо
запрашивать у пользователя данные и заполнять список только числами. Класс-исключение
должен контролировать типы данных элементов списка.

Примечание:  длина  списка  не  фиксирована.  Элементы  запрашиваются  бесконечно,  пока
пользователь  сам  не остановит работу скрипта, введя, например, команду “stop”. При этом
скрипт завершается, сформированный список с числами выводится на экран.

Подсказка:  для  данного  задания  примем,  что  пользователь  может  вводить  только числа и
строки.  При  вводе  пользователем  очередного  элемента  необходимо реализовать проверку
типа элемента и вносить его в список, только если введено число. Класс-исключение должен
не  позволить  пользователю  ввести  текст  (не  число)  и  отобразить  соответствующее
сообщение. При этом работа скрипта не должна завершаться.
"""




class FilterError(Exception):
    def __init__(self, msg):
        self.msg = msg

li = []

while True:
    i_something = input("Какие числа вы знаете? Введите одно:   ")
    if i_something == 'stop':
        print("Вот список с числами, которые вы знаете: ", li)
        break
    try:
        try:
            foo = int(i_something)
        except ValueError:
            raise FilterError('это не число')
        li.append(foo)
    except FilterError as err:
        print(err)


