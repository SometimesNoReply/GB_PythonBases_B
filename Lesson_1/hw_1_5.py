# ===================================
# Lesson 1
# Homework
# Task 5
# ===================================

i_revenue = float(input(f"Введите выручку фирмы (рубли)\n"))
i_costs = float(input(f"Введите издержки фирмы (рубли)\n"))

if i_revenue >= i_costs:
    print("Финансовый результата - ПРИБЫЛЬ")

    # предположим, что следующая формула верна
    calc_profit = i_revenue - i_costs
    # предположим, что следующая формула верна
    calc_profitability = calc_profit / i_revenue
    print(f"Рентабельность выручки = {calc_profitability:.2}")

    i_staff_count = int(input("Введите количество сотрудников (человек)\n"))
    calc_profit_per_person = calc_profit / i_staff_count
    print(f"Прибыль в расчете на одного сотрудника = {calc_profit_per_person:.2}")
else:
    print("Финансовый результата - УБЫТОК")