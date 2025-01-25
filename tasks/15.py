# Написать функцию, которая принимает список чисел
# и возвращает максимальное из них.

def get_max_num_1(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num
        
def get_max_num_2(numbers):
    return max(numbers)

def get_max_num_3(numbers):
    return sorted(numbers)[-1]
        
nums = [-1, 54, 4, -19, 365]

print('Func_1:', get_max_num_1(nums))
print('Func_2:', get_max_num_2(nums))
print('Func_3:', get_max_num_3(nums))