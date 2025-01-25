# Создать кортеж из 6 элементов разных типов данных
# и вывести на экран тип каждого элемента.

dif_tuple = (777, 'ML', 3.14, (0, 1), {'name': 'Tanya', 'role': 'mentor'}, ['a', 'b', 'c'])

for elem in dif_tuple:
    print(f'Element: {elem}, Type: {type(elem)}')