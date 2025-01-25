# Написать функцию, которая принимает строку и выводит ее в обратном порядке.

# def reverse_str(str):
#     return ''.join(reversed(str))

def reverse_str(str):
    return str[::-1]

user_input = input('Enter a string: ')
reversed_output = reverse_str(user_input)
print('Reversed string: ' + reversed_output)