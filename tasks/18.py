# Создать кортеж, содержащий 3 элемента различных типов данных,
# и распаковать его в отдельные переменные.

some_tuple = ('Hello, Python!', 343, {'city': 'Minsk', 'country': 'Belarus'})

var_1, var_2, var_3 = some_tuple

print('Tuple:', some_tuple)
print(f'var_1: {var_1} {type(var_1)}')
print(f'var_2: {var_2} {type(var_2)}')
print(f'var_3: {var_3} {type(var_3)}')