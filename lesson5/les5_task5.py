'''
Создать (программно) текстовый файл,
записать в него программно набор чисел,
разделенных пробелами.
Программа должна подсчитывать
сумму чисел в файле и выводить ее на экран.
'''
import random

lst = [random.randint(0, 1000) for r in range(10)]

with open('les5_task5.txt', 'w', encoding='utf-8') as file:
    print(f'записали в файл список чисел: {lst}')
    file.write(" ".join(map(str, lst)))

with open('les5_task5.txt', 'r', encoding='utf-8') as file:
    summ = 0
    line = list(map(int, file.readline().split(' ')))
    print(f'список чисел из файла: {line}')
    for number in line:
        summ += number
    print(f'сумма чисел равна: {summ}')

