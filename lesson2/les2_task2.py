'''
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''

lst = input(f'Введите элементы списка через запятую: ').split(',')
lst = list(lst)
print(lst)
last = 1
if len(lst) % 2 != 0:
    last = 2
for i in range(0, len(lst)-last, 2):
    lst[i], lst[i+1] = lst[i+1], lst[i]

print(lst)
