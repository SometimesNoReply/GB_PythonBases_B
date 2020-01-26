# ===================================
# Lesson 2
# Homework. Task 6
# ===================================

DI_CHAR_TITLE = "название"
DI_CHAR_PRICE = "цена"
DI_CHAR_COUNT = "количество"
DI_CHAR_MEASURE = "ед. изм."

goods = [
    (1, {DI_CHAR_TITLE: "компьютер", DI_CHAR_PRICE: 20000, DI_CHAR_COUNT: 5, DI_CHAR_MEASURE: "шт."}),
    (2, {DI_CHAR_TITLE: "принтер", DI_CHAR_PRICE: 6000, DI_CHAR_COUNT: 2, DI_CHAR_MEASURE: "шт."}),
    (3, {DI_CHAR_TITLE: "сканер", DI_CHAR_PRICE: 2000, DI_CHAR_COUNT: 7, DI_CHAR_MEASURE: "шт."})
]
counter = 4

while True:
    # решаем: добавить ли?
    do_input = "?"
    while not do_input in {'Y', 'N'}:
        do_input = input(f"Вы надумали добавить новые данные о товаре? [y/n]\n")
        do_input = do_input.upper()

    if do_input == 'N':
        # хватит вводить, пошли обрабатывать статистику
        break

    # вводим
    print(f'Вводится товар №{counter}. Укажите данные:')
    tmp_di = dict()
    tmp_di.setdefault(DI_CHAR_TITLE, input(f"    Введите {DI_CHAR_TITLE}: "))
    tmp_di.setdefault(DI_CHAR_PRICE, input(f"    Введите {DI_CHAR_PRICE}: "))  # пусть строка. ведь нет обработки
    tmp_di.setdefault(DI_CHAR_COUNT, input(f"    Введите {DI_CHAR_COUNT}: "))  # пусть строка. ведь нет обработки
    tmp_di.setdefault(DI_CHAR_MEASURE, input(f"    Введите {DI_CHAR_MEASURE}: "))
    goods.append((counter, tmp_di))
    print(f'Товар №{counter} введен.')
    counter += 1

# сбор аналитики
di_analytics = dict()

# собираем характеристики
se = set()
for elm_tu in goods:
    se = se.union(set(elm_tu[1].keys()))

# мудруем каркас словаря
for elm in se:
    di_analytics.setdefault(elm, [])

# наполняем
for tu_elm in goods:
    for di_key, di_value in tu_elm[1].items():
        calc_li = di_analytics[di_key]
        calc_li.append(di_value)
        di_analytics.setdefault(di_key, calc_li)

# убираем дубликаты
for di_key, di_value in di_analytics.items():
    di_analytics[di_key] = list(set(di_value))

print('========= результат ========')
print("ВХОДНЫЕ ДАННЫЕ: ", goods)
print("ИТОГ АНАЛИТИКИ: ", di_analytics)
