'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл
на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл
'''
# Вообще не правильно применять библиотеку googletrans,
# т.к. она работает только с интернетом, поэтому, по хорошему,
# можно создать алгоритм по переводу слов с русского на английский,
# но для выполнения данного задания это излишне.
from googletrans import Translator
translator = Translator()
with open('text_4.txt') as file:
    lines = [line.split('\n')[0] for line in file]
print(lines)
print(translator.translate('one', dest='ru'))

trans = [translator.translate(line, dest='ru').text for line in lines]
print(trans)

with open('text_4_trans.txt', 'w', encoding='utf-8') as file:
    file.writelines(trans)
