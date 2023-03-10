# 3. Реализовать структуру «Рейтинг», представляющую собой не
# возрастающий набор натуральных чисел
# (каждый элемент ряда меньше или равен предыдущему).
#
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#
# Набор натуральных чисел можно задать непосредственно в коде,
# например, my_list = [7, 5, 3, 3, 2].
# """

top_list = [7, 5, 3, 3, 2]
print("Текущий рейтинг:", top_list)
top_number = int(input('Введите новый элемент рейтинга: '))
count = 1
for i in range(1, count + 1):
    if top_number > 0:
        top_list.append(top_number)
        top_list.sort(reverse=True)
        print('Новый результат рейтинга:', top_list)
    else:
        print('Вы ввели недопустимый элемент!')


