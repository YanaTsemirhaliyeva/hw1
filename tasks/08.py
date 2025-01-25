# Создать словарь с пятью парами «ключ-значение»,
# где ключи - названия фруктов, а значения - их цвета.
# Вывести значения всех ключей.

colors_fruits = {
    'apple': 'green',
    'lemon': 'yellow',
    'orange': 'orange',
    'grape': 'purple',
}

for color in colors_fruits.values():
    print(color)