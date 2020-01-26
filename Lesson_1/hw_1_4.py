# ===================================
# Lesson 1
# Homework
# Task 4
# ===================================

i_number = int(input("Введите число (целое без знака)\n"))

max_char = 0

while i_number > 0:
    last_char = i_number % 10
    if last_char > max_char:
        max_char = last_char
    i_number = i_number // 10

print(f"Самая большая цифра в числе - это {max_char}")