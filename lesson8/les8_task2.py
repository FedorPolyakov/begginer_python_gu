'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''


class DivideByZero(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return f'Ошибка: {self.txt}'


number_1, number_2 = map(int, input('Введите делимое и делитель: ').split(' '))
try:
    if number_2 == 0:
        raise DivideByZero(f'Делитель не может быть равен 0!')
except ValueError:
    print("Вы ввели не число")
except DivideByZero as err:
    print(err)
else:
    print(number_1/number_2)
