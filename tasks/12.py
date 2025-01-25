# Написать программу, которая принимает от пользователя два числа
# и выводит их произведение.

try:
    number_1 = float(input('Enter first number: '))
    number_2 = float(input('Enter second number: '))

    num_product = number_1 * number_2
    print('Product: ', num_product)

except ValueError:
    print('Error: Please, enter a number')