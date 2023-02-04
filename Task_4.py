print('Заполните ниже необходимые данные\n')
list_product = []
for i in range(1, 4):
    product_name = input(f'Введите название {i} продукта: \n')
    price_product = int(input(f'Укажите {i} цену продукта: \n'))
    quantity_product = int(input(f'Укажите количество {i}: \n'))
    unit_measure = input(f'Укажите единицу измерения {i} продукта: \n')


    list_product.append((i, {'название': product_name, 'цена': price_product,
                         'количество': quantity_product, 'eд': unit_measure}))


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
