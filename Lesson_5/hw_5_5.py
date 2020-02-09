# Homework:  Lesson 5. Task 5

"""
Создать  (программно)  текстовый  файл,  записать  в  него  программно  набор  чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить
ее на экран.
"""

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0]
data = [str(i) for i in data]

with open('hw_5_5_outin.txt', 'w') as f:
    f.write(" ".join(data))

with open('hw_5_5_outin.txt', 'r') as f:
    i_str = f.read()

li = i_str.split(" ")
li = [float(i) for i in li]
print(sum(li))

