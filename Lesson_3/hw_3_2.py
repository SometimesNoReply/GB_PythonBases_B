# Homework:  Lesson 3. Task 2

"""
Реализовать  функцию,  принимающую  несколько  параметров,  описывающих  данные
пользователя:  имя,  фамилия,  год  рождения,  город  проживания,  email,  телефон.  Функция
должна  принимать  параметры  как  именованные  аргументы.  Реализовать  вывод  данных  о
пользователе одной строкой.
"""


def print_user_info(name: str, surname: str, birthyear: int, city: str, email: str, phone: str):
    """
    Функция принимает параметры и выводит их на печать в одну строку.

    :param name: имя.
    :param surname: фамилия.
    :param birthyear: год рождения
    :param city: город проживания
    :param email: e-mail
    :param phone: телефон
    :return: Ничего не возвращает
    """
    print(f"Данные пользователя: {list([name, surname, birthyear, city, email, phone])}")


print_user_info(name="Всеволод", surname="Иванов", email="vse_iva@mail.ru",
                phone="(123) 456-78-90", birthyear=1999, city="New York")


di = {
    'name':"Всеволод",
    'surname':"Иванов",
    'email':"vse_iva@mail.ru",
    'phone':"(123) 456-78-90",
    'birthyear':1999,
    'city':"New York"
}
print_user_info(**di)