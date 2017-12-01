# Написать класс Dots, генерирующий заданное количество точек на заданом отрезке
#
#     При создании объекта типа Dots задаются вещественные границы отрезка
#
# Объект d типа Dots должен поддерживать индексирование по там и правилам:
#
#     d[n] — последовательность из n равноудалённых точек от начала до конца отрезка (включая конец)
#
#     d[i:n] — i-я точка такой последовательности
#
#     d[i:j:n] — последовательность начиная с i-той и заканчивая j-1-й точкой такой последовательности
#     Выход за границы отрезка означает экстраполяцию (см. пример)
#
# Input:
#
# a = Dots(0,40)
# print(*a[5])
# print(a[0:5])
# print(a[2:5])
# print(a[4:5])
# print(a[7:5])
# print(a[-7:5])
# print(*a[1:3:5])
# print(*a[:3:5])
# print(*a[2::5])
# print(*a[::5])
# print(*a[-2:6:5])
#
# Output:
#
# 0.0 10.0 20.0 30.0 40.0
# 0.0
# 20.0
# 40.0
# 70.0
# -70.0
# 10.0 20.0
# 0.0 10.0 20.0
# 20.0 30.0 40.0
# 0.0 10.0 20.0 30.0 40.0
# -20.0 -10.0 0.0 10.0 20.0 30.0 40.0 50.0

class Dots:

    def _gen_seq(self, start, n, step):
        for i in range(n):
            yield start + step * i

    def __init__(self, left, right):
        if left > right:
            left, right = right, left
        self.left = left
        self.right = right
        self.size = right - left

    def _get_sequance(self, n, start= None, end=None):
        if end is None:
            end = n
        if start is None:
            start = 0
        step = self.size / (n - 1) # n - 1 because, left and right is included
        return [step * i + self.left for i in range(start, end) ]

    def __getitem__(self, idx):
        if type(idx) is int:
            return self._get_sequance(idx)
        elif type(idx) is slice:
            if idx.step is None:
                i = idx.start
                n = idx.stop
                if n is None : raise ValueError
                if i is None : raise ValueError
                step = self.size / (n - 1)
                pos = self.left + i * step
                return pos
            else:
                n = idx.step
                i = slice(idx.start or 0, idx.stop or n)
                step = self.size / (n - 1)
                start = self.left + i.start * step
                count_n = i.stop - i.start
                return [k for k in self._gen_seq(start, count_n, step)]
        else:
            raise TypeError
