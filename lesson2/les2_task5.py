'''
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
'''
# in_lst = input(f'Введите элементы начального рейтинга через запятую по убыванию: ').split(',')
# in_lst = ['1','2','3','4','5']
in_lst = [7, 5, 3, 3, 2]
for i in range(len(in_lst)):
    in_lst[i] = int(in_lst[i])

while True:
    new_elem = input(f'Введите новый элемент, для завершения ввода элементов наберите "exit": ')
    if new_elem == 'exit':
        break
    new_elem = int(new_elem)
    if new_elem in in_lst:
        in_lst.insert(in_lst.index(new_elem), new_elem)
    elif new_elem <= min(in_lst):
        in_lst.append(new_elem)
    elif new_elem >= max(in_lst):
        in_lst.insert(0, new_elem)
    else:
        for i in range(len(in_lst)-1):
            if in_lst[i] > new_elem and new_elem > in_lst[i+1]:
                index = i+1
        in_lst.insert(index, new_elem)
    print(f'Пользователь ввел {new_elem}. Результат: {in_lst}')

print(f'Конечный результат: {in_lst}')