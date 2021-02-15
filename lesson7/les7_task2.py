"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
from abc import ABC


class Clothes(ABC):
    def __init__(self):
        pass

    @property
    @classmethod
    def calculate(self):
        pass

    def __add__(self, other):
        return self.calculate + other.calculate


class Coat(Clothes):
    def __init__(self, value):
        super().__init__()
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value < 10:
            print('Размер меньше 10 -> установим 10й')
            self.__value = 10
        elif value > 70:
            print('Размер больше 70 -> установим 70й')
            self.__value = 70
        else:
            self.__value = value

    @property
    def calculate(self):
        return self.__value / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, value):
        super().__init__()
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if value < 100:
            print('Размер меньше 100 cm-> установим 100 cm')
            self.__value = 100
        elif value > 250:
            print('Размер больше 250 cm -> установим 250й')
            self.__value = 250
        else:
            self.__value = value

    @property
    def calculate(self):
        return (2 * self.__value)/100 + 0.3


A = Coat(5)
print(f'{A.calculate}')
B = Costume(190)
print(f'{B.calculate}')
