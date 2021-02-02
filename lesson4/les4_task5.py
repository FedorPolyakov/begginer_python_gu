'''
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''
from functools import reduce


def multiply(x, next_x):
    return x * next_x


lst = [x for x in range(100,1001,2)]
lst_= [x for x in range(2,11,2)]
# проверим на списке чесел от 2 до 10, т.е. 2*4*6*8*10 = 3840
print(lst_)
print(reduce(multiply, lst_))

print(lst)
print(reduce(multiply, lst))
