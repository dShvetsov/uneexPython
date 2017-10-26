#!/usr/bin/env python3

# В первой строке ввести координаты центра круга и его радиус (числа x, y, r через запятую).
# Во второй и последующих строках ввести пары чисел — координаты точек.
# Ввод заканчивается парой 0,0 (она не входит в проверку!).
# Вывести YES, если все точки принадлежат кругу и NO, если не все.
# Input:
#
# 1,1,2
# 1,2
# 1,3
# 2,2
# 0,0
#
# Output:
#
# YES

x_center, y_center, radius = eval(input())
radius_sqr = radius ** 2;

x, y = eval(input())

while( (x, y) != (0, 0) ):
    distance_from_center_sqr = (x - x_center)**2 + (y - y_center)**2
    if distance_from_center_sqr > radius_sqr :
        print ("NO")
        break
    x, y = eval(input())
else:
    print ("YES")
