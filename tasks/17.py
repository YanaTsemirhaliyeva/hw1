# Написать программу, которая принимает от пользователя строку
# и выводит True, если строка является палиндромом, и False в противном случае.

def is_palindrom(str):
    s = str.lower().replace(' ', '')
    return s == s[::-1]

user_input = input('Enter a string: ')

if is_palindrom(user_input):
    print(True)
else:
    print(False)