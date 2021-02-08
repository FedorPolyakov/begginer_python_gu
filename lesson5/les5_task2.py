"""
Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
"""

lines = 0
words = {}
try:
    with open('les5_task2_tst.txt') as file:
        for line in file:
            lines += 1
            words[lines] = len(line.split(' '))
except IOError:
    print(f'Произлошла ошибка ввода/вывода')

print(f'количество строк в файле: {lines}')
for key in words:
    print(f'количество слов в строке {key}: {words[key]}')
