# Написать функцию, которая принимает список чисел и возвращает их сумму.

def get_sum(numbers):
    return sum(numbers)

numbers_list = [1, 11, 22, 33, 44]
numbers_sum = get_sum(numbers_list)
print('Sum of numbers in list:', numbers_sum)