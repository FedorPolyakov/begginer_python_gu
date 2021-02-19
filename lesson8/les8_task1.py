'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def parse_date(cls, date):
        for _ in ['-', '.', ' ']:
            if _ in date:
                date = date.split(_)
                date = list(map(int, date))
                # print(date)
                return cls(date)
        else:
            return cls(f'Неправильно задан разделитель даты')

    @staticmethod
    def validate_date(date):
        if date[0] > 29 and date[1] == 2:
            return f'В феврале меньше 30 дней!'
        elif 0 < date[0] < 32 and 0 < date[1] < 13 and date[2] > 0:
            d = date[0]
            m = date[1]
            y = date[2]
        else:
            return f'Дата неверно задана'
        return f'день: {d}, месяц: {m}, год: {y}'


a = Date.parse_date('31-12-2021')
print(type(a.date))
print(a.date)
print(a.date[0])
print(type(a.date[0]))
print(Date.validate_date(a.date))
