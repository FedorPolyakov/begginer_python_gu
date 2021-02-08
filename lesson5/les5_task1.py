'''
1. Создать программно файл в текстовом формате,
 записать в него построчно данные,
  вводимые пользователем.
  Об окончании ввода данных свидетельствует пустая строка.
'''

str_lst = []
while True:
    string = input("Введите данные: ")
    if string == "":
        print('Ввод данных окончен')
        break
    string += '\n'
    str_lst.append(string)
    with open('les5_task1.txt', 'w', encoding='utf-8') as file:
        file.writelines(str_lst)


