#!/usr/bin/env python3

# Ввести кортеж целых чисел, затем два натуральных числа M и N, и вывести список из элементов,
# (1) не стоящих на местах, кратных M, и (2) при этом не кратных N
# Input:
#
# 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
# 3,4
#
# Output:
#
# [2, 3, 5, 6, 9, 11, 14, 15]

l = eval(input())
n, m = eval(input())

first_condition = lambda x : x % m != 0
second_condition = lambda x : x % n != 0

# it seems, that task has wrong description
l = [v for i, v in enumerate(l) if first_condition(v) and second_condition(i)]
print (l)
