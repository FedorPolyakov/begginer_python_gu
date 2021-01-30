'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''
def two_numbers(var1, var2):
    try:
        return var1/var2
    except ZeroDivisionError:
        return f'Деление на ноль!'


while True:
    a = input(f'Введите первое число: ')
    b = input(f'Введите второе число: ')
    try:
        a = float(a)
        b = float(b)
        print(two_numbers(a, b))
        break
    except ValueError as e:
        print('Что-то не то вы ввели!')

