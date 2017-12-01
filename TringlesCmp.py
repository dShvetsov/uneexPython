# Написать класс Triangle, моделирующий треугольник
#
#     объект T типа Triangle создаётся из трёх вещественных чисел — сторон треугольника
#
#         T пуст, если не выполняется строгое неравенство треугольника или хотя бы одна из сторон не положительна
#
#             abs(T) — площадь треугольника (0, если T пуст)
#
#         сравнение на неравенство двух объектов типа Triangle есть результат сравнения их площадей
#
#             два объекта S и T типа Triangle равны, если попарно равны их стороны (в некотором порядке)
#
#         строковое представление: a:b:c, где a, b и c — стороны треугольника в порядке их задания
#
#         Input:
#
#         Toggle line numbers
#
#            1 Tri = Triangle(3,4,5), Triangle(5,4,3), Triangle(7,1,1), Triangle(5,5,5), Triangle(7,4,4)
#        2 for a,b in zip(Tri[:-1],Tri[1:]):
#               3     print(a if a else b)
#                  4     print("{}={:.2f} {}={:.2f}".format(a, abs(a), b, abs(b)))
#                  5     print(a == b)
#        6     print(a >= b)
#        7     print(a < b)
#
#     Output:
#
#     3.0:4.0:5.0
#     3.0:4.0:5.0=6.00 5.0:4.0:3.0=6.00
#     True
#     True
#     False
#     5.0:4.0:3.0
#     5.0:4.0:3.0=6.00 7.0:1.0:1.0=0.00
#     False
#     True
#     False
#     5.0:5.0:5.0
#     7.0:1.0:1.0=0.00 5.0:5.0:5.0=10.83
#     False
#     False
#     True
#     5.0:5.0:5.0
#     5.0:5.0:5.0=10.83 7.0:4.0:4.0=6.78
#     False
#     True
#     False


class Triangle:
    def __init__(self, a,b,c):
        self.a, self.b, self.c = a,b,c
        self.all = (self.a, self.b, self.c)

    def __bool__(self):
        m = max(self.all)
        return (sum(self.all) - m) > m

    def __abs__(self):
        if not self:
            return 0
        p = sum(self.all) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

#    def __neq__(self, other):
#        return abs(self) != abs(other)

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __le__(self, other):
        return abs(self) <= abs(other)

    def __eq__(self, other):
        t1 = sorted(self.all)
        t2 = sorted(other.all)
        return t1 == t2

    def __str__(self):
        return "{:.1f}:{:.1f}:{:.1f}".format(*self.all)
