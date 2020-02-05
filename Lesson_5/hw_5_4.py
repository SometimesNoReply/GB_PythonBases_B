# Homework:  Lesson 5. Task 4

"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно
данные. При этом английские числительные должны заменяться на русские. Новый блок строк
должен записываться в новый текстовый файл.
"""

di = {
    'One':'1',
    'Two':'2',
    'Three':'3',
    'Four':'4',
}

with open('hw_5_4_in.txt', 'r', encoding='UTF-8') as f_in:
    with open('hw_5_4_out.txt', 'w', encoding='UTF-8') as f_out:
        for i_line in f_in:
            for key, value in di.items():
                i_line = i_line.replace(key,value)
            f_out.write(i_line)
