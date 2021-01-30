
'''
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон.
 Функция должна принимать параметры как именованные аргументы.
 Реализовать вывод данных о пользователе одной строкой.
'''


def user(first_name, last_name, year, city, email, phone):
    return f'имя фамилия: {first_name} {last_name}, год рождения: {year},' \
           f' город проживания: {city}, email: {email}, телефон: {phone}'

print(user(email='abc@ya.com', phone='89991234567', first_name='Mike', last_name='Ozzborne', year='1962', city='Moscow'))