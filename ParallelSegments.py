#!/usr/bin/python3

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

