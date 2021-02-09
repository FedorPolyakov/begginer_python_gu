'''
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты:

speed,
color,
name,
is_police (булево).

А также методы:

go,
stop,
turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'машина поехала'

    def stop(self):
        return f'машина остановилась'

    def turn(self, direction):
        if direction not in ['налево', 'направо']:
            direction = 'в поле'
        return f'машина повернула {direction}'

    def show_speed(self):
        return f'текущая скорость машины: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Превышение скорости на {self.speed - 60}. Ваша скорость {self.speed}'
        return f'текущая скорость машины: {self.speed}'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Превышение скорости на {self.speed - 40} км/ч. Ваша скорость {self.speed} км/ч'
        return f'текущая скорость машины: {self.speed}'


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


A = TownCar(99, 'black', 'Mazda', False)
print(A.speed)
print(A.color)
print(A.name)
print(A.is_police)
print(A.go())
print(A.stop())
print(A.turn('налево'))
print(A.show_speed())

B = WorkCar(30, 'grey', 'Cat', False)
print(B.speed)
print(B.color)
print(B.name)
print(B.is_police)
print(B.go())
print(B.stop())
print(B.turn('налево направо'))
print(B.show_speed())

C = SportCar(209, 'red', 'Ferrari', False)
print(C.speed)
print(C.color)
print(C.name)
print(C.is_police)
print(C.go())
print(C.stop())
print(C.turn('направо'))
print(C.show_speed())

D = PoliceCar(130, 'white', 'Ford', True)
print(D.speed)
print(D.color)
print(D.name)
print(D.is_police)
print(D.go())
print(D.stop())
print(D.turn('налево'))
print(D.show_speed())
