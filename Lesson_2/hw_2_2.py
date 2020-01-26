# ===================================
# Lesson 2
# Homework. Task 2
# ===================================
i_str = input(f'Напишите предложение:')
if not len(i_str):
    i_str = 'Ехал Грека через реку, видит Грека в реке рак'

print(f'Исходное предложение: {i_str}')
foo_li = i_str.split(' ')
li_len = len(foo_li)
if li_len > 1:
    li_len -= li_len & 1
    li_len -= 2
    while li_len >= 0:
        foo_li[li_len], foo_li[li_len+1] = foo_li[li_len+1], foo_li[li_len]
        li_len -= 2
calc_str = ' '.join(foo_li)
print(f'Измененное предложение: {calc_str}')