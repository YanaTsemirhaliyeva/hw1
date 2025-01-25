# Создать словарь, содержащий информацию о студенте: имя, возраст, курс.
# Вывести всю информацию о студенте на экран.

student_info = {
    'name': 'Yana',
    'age': 35,
    'course': 'Data Science'
}

for key, value in student_info.items():
    print(f'{key}: {value}')