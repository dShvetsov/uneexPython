# Определить класс Vector, работающий с трёхмерными векторами Вектора должны поддерживать:
#
#     Конструктор вектора из трёх вещественных чисел
#     Сложение и вычитание векторов A+B, A-B
#     Умножение и деление на число A*n, A/n; а также и n*A
#     Скалярное произведение A@B
#     Преобразование в строковый вид "x:y:z, где x, y и z — представление вещественного числа с двумя знаками после запятой (см. пример)
#
# Input:
#
# A = Vector(1,2,3)
# B = Vector(-1,3,-2)
# C = Vector(7,3,5)
# print("A, B, C:", A, B, C)
# print(A, "+", B, "=", A+B)
# print(A, "-", C, "=", A-C)
# print(A, "*", 2, "=", A*2)
# print(2, "*", B, "=", 2*B)
# print(C, "/", 3, "=", C/3)
# print(B, "@", C, "=", "{:.2f}".format(B@C))
#
# Output:
#
# A, B, C: 1.00:2.00:3.00 -1.00:3.00:-2.00 7.00:3.00:5.00
# 1.00:2.00:3.00 + -1.00:3.00:-2.00 = 0.00:5.00:1.00
# 1.00:2.00:3.00 - 7.00:3.00:5.00 = -6.00:-1.00:-2.00
# 1.00:2.00:3.00 * 2 = 2.00:4.00:6.00
# 2 * -1.00:3.00:-2.00 = -2.00:6.00:-4.00
# 7.00:3.00:5.00 / 3 = 2.33:1.00:1.67
# -1.00:3.00:-2.00 @ 7.00:3.00:5.00 = -8.00

from functools import reduce

class Vector:
    def __init__(self, *arg):
        self.v = arg

    def __add__(self, other):
        if (type(other) is not type(self)):
            raise TypeError
        return Vector(*[i + j for i, j  in zip(self.v , other.v)])

    def __sub__(self, other):
        if (type(other) is not type(self)):
            raise TypeError
        return Vector(*[i - j for i, j  in zip(self.v , other.v)])

    def __str__(self):
        return ":".join(["{:.2f}".format(i) for i in self.v])

    def __repr__(self):
        return ":".join(["{:.2f}".format(i) for i in self.v])

    def __rmul__(self, n):
        return Vector(*[i * n for i in self.v])

    def __mul__(self, n):
        return Vector(*[i * n for i in self.v])

    def __truediv__(self, n):
        return Vector(*[i / n for i in self.v])

    # Скалярное произведение
    def __matmul__(self, other):
        if type(other) is not type(self):
            raise TypeError
        mul = [i * j for i, j in zip(self.v, other.v)]
        return sum(mul)
