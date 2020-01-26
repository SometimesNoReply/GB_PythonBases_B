# ===================================
# Lesson 2
# Homework. Task 5
# ===================================

rating = [7, 5, 3, 3, 2]

while True:
    print()
    x = input(f'Текущий рейтинг: {rating}. Введите еще одну оценку для рейтинга: ')
    if x.isdecimal():
        # цифра - работаем
        x = int(x)
        cnt = rating.count(x)
        if cnt > 0:
            # есть в списке
            rating.insert(rating.index(x)+cnt, x)
        else:
            # нет в списке
            rating.append(x)
            rating.sort(reverse=True)
    else:
        # нечисло - выходим
        print('Пока. Запускайте ещё')
        break
