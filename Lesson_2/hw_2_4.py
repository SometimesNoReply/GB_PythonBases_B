# ===================================
# Lesson 2
# Homework. Task 4
# ===================================

i_str = input("Введите предложение: ")
if len(i_str) == 0:
    i_str = "Многопоточность определяет когнитивный диссонанс на подсознательном уровне"

print(f'Обрабатываемое предложение: "{i_str}"')
print('Результат обработки:')
tmp_li = i_str.split(' ')
for idx, elem in enumerate(tmp_li, 1):
    print(f"{idx} {elem if len(elem) <=10 else elem[:10]}")
