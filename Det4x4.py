#!/usr/bin/env python3

# Матрица 4×4 задаётся кортежем из 4 кортежей по 4 целых числа в каждом.
# Посчитать определитель этой матрицы.
# Допустимо заранее составить (а не вычислять на ходу) последовательность из всех
# перестановок индексов и знаков этих перестановок.
# Input:
#
# (5, -4, 4, -7), (1, -2, 6, 0), (3, -8, -6, -4), (-1, 2, -9, 3)
#
# Output:
#
# 702

from itertools import permutations, combinations
from functools import reduce

def number_of_inversion(a):
    return sum(1 for x,y in combinations(range(len(a)), 2) if a[x] > a[y])

def determinant(A):
    """ A is list of lists """
    n = len(A)
    perm = permutations(range(n))
    det = 0
    for p in perm:
        det_elem = (x[y] for x, y in zip(A, p))
        value = reduce(lambda m, x: m * x, det_elem, 1)
        sign = +1 if number_of_inversion(p) % 2 == 0 else -1
        det += sign * value
    return det


A = eval(input())

print(determinant(A))
