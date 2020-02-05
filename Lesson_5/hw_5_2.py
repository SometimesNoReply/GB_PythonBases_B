# Homework:  Lesson 5. Task 2

"""
Создать  текстовый  файл  (не  программно),  сохранить  в  нем  несколько  строк,  выполнить
подсчет количества строк, количества слов в каждой строке.
"""

content = []
with open('hw_5_2_in.txt', 'r') as f:
    content = f.readlines()
    print(f"В файле {len(content)} строк.")

for i, s in enumerate(content, 1):
    n = 0
    if len(s) > 0:
        n = 1 + s.count(' ')  # Будем считать, что нет пробелов повторяющихся и на концах
    print(f"В {i} строке {n} слов")
