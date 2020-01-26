# ===================================
# Lesson 1
# Homework
# Task 5
# ===================================

print("Параметр a обозначает сколько километров преодолел спортсмен в 1ый день")
print("Параметр b обозначает требуемую для достижения дистанции\n")

i_first_day_distance = float(input("Введите параметр а\n"))
i_target_distance = float(input("Введите параметр b\n"))

current_day = 1
current_day_distance = i_first_day_distance

while current_day_distance < i_target_distance:
    current_day += 1
    current_day_distance *= 1.1

print(f"Дистанцию в {i_target_distance} спортсмен преодолеет на {current_day}-й день")
