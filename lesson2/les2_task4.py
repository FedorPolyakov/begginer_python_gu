'''
Пользователь вводит строку из нескольких слов, разделённых пробелами.
 Вывести каждое слово с новой строки.
 Строки необходимо пронумеровать.
 Если в слово длинное, выводить только первые 10 букв в слове.
'''
str = input(f'Введите слова через пробелы: ').split(' ')
# удалим лишние пробелы
while True:
    if '' in str:
        str.remove('')
    else:
        break

for i in range(len(str)):
    if len(str[i]) > 10:
        str[i] = str[i][:10]
    print(f'{i+1} - {str[i]}')
