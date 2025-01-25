# Создать список чисел от 1 до 20,
# а затем создать новый список, содержащий только четные числа из первого списка.

numbers = list(range(1, 21))
even_numbers = [number for number in numbers if number % 2 == 0]

print('List:', numbers)
print('Even numbers in list:', even_numbers)