#!/usr/bin/env python3

# Ввести построчно четвёрки вида «число число число слово»,
# где первые три числа — это координаты галактики по имени «слово»
# (некоторые галактики могут называться одинаково, но координаты у всех разные).
# Последняя строка ввода не содержит пробелов и не учитывается.
# Вывести в алфавитном порядке имена любых двух наиболее удалённых друг от друга галактик.
# Input:
#
# 35.764 -797.636 -770.320 almost
# 88.213 -61.688 778.457 gene
# -322.270 -248.555 -812.730 trend
# 721.262 630.355 968.287 dow
# -895.519 -970.173 97.282 non
# -561.036 -350.840 -723.149 disco
# -151.546 -900.962 -658.862 bidder
# -716.197 478.576 -695.843 hawaii
# -744.664 -173.034 -11.211 sad
# -999.968 990.467 650.551 erik
# .
#
# Output:
#
# almost erik

def dist(pair):
    q, w = pair
    return (q[0]-w[0])**2 + (q[1]-w[1])**2 + (q[2]-w[2])**2

if __name__ == "__main__":
    galaxies = dict()
    while True:
        inp = input()
        if not ' ' in inp:
            break
        *coords, name = inp.split()
        coords = tuple(float(i) for i in coords)
        galaxies[coords] = name

    x, y = max( ((i, j) for i in galaxies for j in galaxies if i > j), key=dist)

    print(*sorted((galaxies[x], galaxies[y])))
