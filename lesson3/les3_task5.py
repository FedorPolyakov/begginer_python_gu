'''
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''


def summs(lst, s=0):
    while True:
        if '' in lst:
            lst.remove('')
        else:
            break
    for i in lst:
        if '.' in i:
            try:
                i = float(i)
            except ValueError as e:
                print(f'{e}')
        else:
            try:
                i = int(i)
            except ValueError as e:
                print(f'{e}')
        s += i
    return s


summ = 0
while True:
    string = input('Для выхода из ввода наберите отдельно "!". Введите числа через пробел: ').split(' ')
    if '!' in string:
        string.remove('!')
        summ = summs(string, summ)
        print(summ)
        break
    summ = summs(string, summ)
    print(summ)

