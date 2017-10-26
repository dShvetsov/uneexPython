#!/usr/bin/env python3

# Ввести небольшое натуральное число 2⩽N⩽1000000 и проверить, является ли оно степенью натурального числа (>1).
# Вывести YES или NO соответственно.
# Input:
#
# 1024
#
# Output:
#
# YES

from math import sqrt

def isAnyPower(n):
    sqrt_n = int(sqrt(n))
    for base in range(2, n):
        for exponent in range(2, sqrt_n):
            compared_value = base ** exponent
            if compared_value == n:
                return True
            elif compared_value > n:
                break
    return False

n = eval(input())

print ("YES" if isAnyPower(n) else "NO")
