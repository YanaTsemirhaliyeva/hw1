# Написать программу,
# которая принимает строку от пользователя и 
# выводит количество символов в этой строке.

# принимаем строку от пользователя
user_input = input('Enter a string: ')

# вычисляем количество символов в строке
str_length = len(user_input)

print('Number of characters in string: ' + str(str_length))