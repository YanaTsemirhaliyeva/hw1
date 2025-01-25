# Написать функцию, которая принимает словарь с информацией о студенте (имя, возраст, курс)
# и выводит эту информацию в форматированном виде.

def format_data(data):
    print(f'Information about student {data.get('name')}')
    print(f'Age: {data.get('age')}')
    print(f'Course: {data.get('course')}')


student_info = {
    'name': 'Yana',
    'age': 35,
    'course': 'Data Science'
}

format_data(student_info)
