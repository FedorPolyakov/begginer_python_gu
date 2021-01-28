'''
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''
number = int(input('Введите целое положительное число: '))

while True:
    if number < 0 or number == 0:
        print(f'Вы ввели 0 или отрицательное число!')
        number = int(input('Введите целое положительное число: '))
    else:
        break

max_number = 0
print(f'Вариант 1')
while True:
    if number == 0:
        break
    if max_number < number % 10:
        max_number = number % 10
    number = number // 10
print(f'Самая большая цифра в числе: {max_number}')

print(f'Вариант 2')
number = str(number)
length = len(number)
while length > 0:
    if max_number < int(number[length-1]):
        max_number = int(number[length-1])
    length -= 1
print(f'Самая большая цифра в числе: {max_number}')




