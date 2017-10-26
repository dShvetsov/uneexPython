#!/usr/bin/python3

# Ввести восемь чисел через запятую — целочисленные координаты 4-х несовпадающих точек
# A1, A2, A3 и A4: X1, Y1, X2, Y2, X3, Y3, X4, Y4.
# Вывести YES, если прямая A1A2 параллельна прямой A3A4 (или совпадает с ней), и NO — если не параллельна.
# Input:
#
# 1,2,7,14,8,8,18,28
#
# Output:
#
# YES

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __init__(self, t):
        self.x = t[0]
        self.y = t[1]

class Vector:
    def __init__(self, p1, p2):
        self.x = p1.x - p2.x
        self.y = p1.y - p2.y

def determinate(v1, v2):
    return (v1.x * v2.y) - (v2.x * v1.y)

points = eval(input())

p1 = Point(points[0:2])
p2 = Point(points[2:4])
p3 = Point(points[4:6])
p4 = Point(points[6:8])

v1 = Vector(p1, p2)
v2 = Vector(p3, p4)

print("YES" if determinate(v1, v2) == 0 else "NO")

