# Homework:  Lesson 5. Task 6

"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный
предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их
количество.  Важно,  чтобы  для  каждого  предмета  не  обязательно  были  все  типы  занятий.
Сформировать  словарь,  содержащий  название  предмета  и  общее  количество  занятий  по
нему. Вывести словарь на экран.
Примеры строк файла:
    Информатика:   100(л)   50(пр)   20(лаб).
    Физика:   30(л)   ​—​   10(лаб)
    Физкультура:   ​—   30(пр)   —
Пример словаря:
    {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

di = dict()

with open('hw_5_6_in.txt', 'r', encoding='UTF-8') as f:
    for i_line in f:
        i_li = i_line.split(" ")
        subj_name = i_li[0][:-1]                # без двоеточия
        subj_lect = i_li[1].split("(")[0]       # левое грязное значащее
        subj_prac = i_li[2].split("(")[0]
        subj_labo = i_li[3].split("(")[0]
        if subj_lect == "-": subj_lect = 0      # только цыфры
        if subj_prac == "-": subj_prac = 0
        if subj_labo == "-": subj_labo = 0
        subj_lect = int(subj_lect)              # без строк
        subj_prac = int(subj_prac)
        subj_labo = int(subj_labo)
        di[subj_name] = sum((subj_lect, subj_prac, subj_labo))



for key, value in di.items():
    print(f"По предмету {key} всего {value} занятий")