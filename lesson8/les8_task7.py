'''
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''

class ComplexNumber:
    def __init__(self, num, num_i):
        self.num = num
        self.num_i = num_i

    def __str__(self):
        return f'{self.num if self.num != 0 else ""}' \
               f'{"+" if self.num_i >= 0 and self.num != 0 else ""}' \
               f'{self.num_i}j'

    def __add__(self, other):
        return ComplexNumber(self.num+other.num, self.num_i + other.num_i)

    def __mul__(self, other):
        return ComplexNumber(self.num*other.num - self.num_i*other.num_i, self.num*other.num_i+other.num*self.num_i)


a = ComplexNumber(1, 1)
b = ComplexNumber(1, -3)
print(a+b)
print(a*b)
