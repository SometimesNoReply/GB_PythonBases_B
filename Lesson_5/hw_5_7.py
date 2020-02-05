# Homework:  Lesson 5. Task 7

"""
Создать  вручную  и  заполнить  несколькими  строками  текстовый  файл,  в  котором  каждая
строка  должна  содержать  данные  о  фирме:  название,  форма  собственности,  выручка,
издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо  построчно  прочитать  файл,  вычислить  прибыль  каждой  компании,  а  также
среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее ​не включать​.

Далее  реализовать  список.  Он  должен  содержать  словарь  с  фирмами  и  их  прибылями,  а
также  словарь  со  средней  прибылью.  Если  фирма  получила  убытки,  также  добавить  ее  в
словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{​"firm_1"​: ​5000​, ​"firm_2"​: ​3000​, ​"firm_3"​: ​1000​}, {​"average_profit"​: ​2000​}]
Подсказка: использовать менеджер контекста.
"""

import json

# готовим словари
di_profit = dict()
di_avr_profit = {'average_profit': None}

# переменные
calc_sum = 0
calc_cnt = 0

# читаем
with open('hw_5_7_in.txt', 'r', encoding='UTF-8') as f:
    for i_line in f:
        i_li = i_line.split(" ")
        firm_name = i_li[0]
        firm_revenue = float(i_li[2])
        firm_expenses = float(i_li[3])
        firm_profit = firm_revenue - firm_expenses
        di_profit[firm_name] = firm_profit
        if firm_profit >= 0:
            calc_sum += firm_profit
            calc_cnt += 1

# считаем
if calc_cnt > 0:
    di_avr_profit['average_profit'] = calc_sum / calc_cnt

# укладываем
data = [di_profit, di_avr_profit]

# записываем
with open('hw_5_7_out.json', 'w') as f:
    json.dump(data, f)
