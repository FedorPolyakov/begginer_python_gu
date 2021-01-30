'''
 Реализовать функцию my_func(),
 которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов
'''


def my_func(a, b, c):
    st = {a, b, c}
    s = 0
    if len(st) > 2:
        st.discard(min(st))
        for i in st:
            s += i
    elif len(st) == 2:
        for i in st:
            s += i
    else:
        s = 2 * st.pop()
    return s


print(my_func(6, 5, 4))
