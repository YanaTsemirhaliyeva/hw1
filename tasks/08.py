# Создать словарь с пятью парами «ключ-значение»,
# где ключи - названия фруктов, а значения - их цвета.
# Вывести значения всех ключей.

colors_fruits = {
    'apple': 'green',
    'lemon': 'yellow',
    'orange': 'orange',
    'grape': 'purple',
    'banana': 'yellow'
}

for fruit in colors_fruits.keys():
    print(fruit)