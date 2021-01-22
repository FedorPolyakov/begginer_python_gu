'''
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
'''
SEC_IN_MIN = 60
SEC_IN_HOUR = 3600
user_seconds = int(input(f'Введите время в секундах: '))
hours = user_seconds // SEC_IN_HOUR
minutes = (user_seconds - hours * SEC_IN_HOUR) // SEC_IN_MIN
print(f'{hours}:{minutes}:{user_seconds - (hours * SEC_IN_HOUR + minutes * SEC_IN_MIN)}')
