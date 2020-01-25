# ===================================
# Lesson 1
# Homework
# Task 3
# ===================================

i_str = input("Введите число\n")

if len(i_str) > 1:
    # введено число
    # полагаем, что формула означает многочлен
    i_str = float(i_str)
    i_result = i_str + i_str * i_str + i_str ** 3
else:
    # введена цифра
    # полагаем, что формула означает конкатенацию цифр
    i_result = int(i_str) + int(i_str * 2) + int(i_str * 3)

print(f"F(x) = x + xx + xxx")
print(f"F({i_str}) = {i_result}")