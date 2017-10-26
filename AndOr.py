#!/usr/bin/env python3

# Ввести два объекта Python и вывести первый непустой из них. Если оба пустые, вывести NO.
# Input:
#
# []
# 123
#
# Output:
#
# 123

first = eval(input())
second = eval(input())

print (first or second or "NO")
