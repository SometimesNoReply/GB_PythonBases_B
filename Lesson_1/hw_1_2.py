# ===================================
# Lesson 1
# Homework
# Task 2
# ===================================

i_time = int(input("Введите количество секунд (целое число) "))
print("Вы ввели", i_time)

calc_s = i_time % 60
i_time = i_time // 60       # now it is minutes

calc_m = i_time % 60
calc_h = i_time // 60

print(f"Знайте, что в формате hh:mm:ss это выглядит как {calc_h:0>2d}:{calc_m:0>2d}:{calc_s:0>2d}")
