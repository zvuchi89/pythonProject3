# 4. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
#
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
#
# Далее необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
#
# Пример:
#
# {
# “названия”: [“компьютер”, “принтер”, “сканер”],
# “цены”: [20000, 6000, 2000],
# “количества”: [5, 2, 7],
# “ед”: [“шт.”]
# }
#

print('Заполните ниже необходимые данные\n')

list_product = []

for i in range(1, 4):
    product_name = input(f'Введите название {i} продукта: \n')
    price_product = int(input(f'Укажите {i} цену продукта: \n'))
    quantity_product = int(input(f'Укажите количество {i}: \n'))
    unit_measure = input(f'Укажите единицу измерения {i} продукта: \n')

    list_product.append((i, {'название': product_name, 'цена': price_product,
                             'количество': quantity_product,
                             'eд': unit_measure}))

product_name = []
price_product = []
quantity_product = []
unit_measure = []

for i in list_product:
    product_name.append(i[1].get('название'))
    price_product.append(i[1].get('цена'))
    quantity_product.append(i[1].get('количество'))
    unit_measure.append(i[1].get('eд'))

product_dict = {'название продукта:': product_name,
                'цена продукта:': price_product,
                'количество:': quantity_product,
                'единица измерения:': unit_measure}

print('\n Аналитика товаров:\n')

for key, value in product_dict.items():
    print(key, value)

print('\n Структура данных о товарах готова!\n')

for ind, el in enumerate(list_product, 1):
    print(ind, el)
