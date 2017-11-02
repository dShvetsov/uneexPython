#!/usr/bin/env python3

# Ввести квадратную целочисленную матрицу построчно и посчитать её определитель
# (например, методом конденсации Доджсона).
# Размер матрицы (1≤N≤12) определяется длиной её нулевой строки.
# Input:
#
# 8, 8, 5, 6, 3
# 1, 4, 4, 9, 0
# 9, 6, 7, 7, 3
# 4, 1, 0, 1, 4
# 6, 7, 9, 7, 3
#
# Output:
#
# 2784

def det2x2(mat):
    return mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]

def minor(mat, i, j):
    mini_mat = [ [mat[0][0], mat[i][0]],
                 [mat[0][j], mat[i][j]] ]
    return det2x2(mini_mat)

def Dodgson_step(mat):
    result_mat = []
    for i in range(len(mat) - 1):
        result_line = []
        for j in range(len(mat) - 1):
            result_line.append( minor(mat, i + 1, j + 1) )
        result_mat.append(result_line)
    return result_mat


class ZeroLine(Exception) :
    pass

def non_zero00(mat):
    if mat[0][0] != 0:
        return mat, False
    for i, v in enumerate(mat[1::]):
        if v[0] != 0:
            mat[0], mat[i + 1] = mat[i + 1], mat[0]
            return mat, True
    raise ZeroLine()

def Dodgson_algo(mat):
    d = []
    first_elems = []
    sign = 1
    while len(mat) != 2:
        mat, was_swap = non_zero00(mat)
        if was_swap :
           sign *= -1
        first_elems.append(mat[0][0])
        d += first_elems
        mat = Dodgson_step(mat)
    result_d = 1
    for i in d:
        result_d *= i
    return sign * det2x2(mat) // result_d

def print_matrix(mat):
    for line in mat:
        for v in line:
            print(v, end=', ')
        print('')
    print('')

def read_matrix():
    first_line = eval(input())
    matrix = [first_line]
    for l in range(len(first_line) - 1):
        matrix.append(eval(input()))
    return matrix

matrix = read_matrix()
try :
    det = Dodgson_algo(matrix)
except ZeroLine:
    # det of matrix is zero
    det = 0
print( det )

