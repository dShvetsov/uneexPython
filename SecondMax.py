#!/usr/bin/env python3

# Ввести последовательность S и вывести второй максимум этой последовательности,
# т. е. элемент a∈S : ∃ b∈S : b>a и a⩾c ∀c∈S, c≠b.
# Если второго максимума нет, вывести NO.
# Пользоваться функциями наподобие max() или sorted() нельзя.
# Input:
#
# 3,4,5,6,7
#
# Output:
#
# 6

def find_max(s):
    cur_max = None
    for i in s:
        if cur_max is None or cur_max < i:
            cur_max = i
    return cur_max

def delete_number(s, num):
    while s.count(num) > 0:
        index = s.index(num)
        s = s[:index] + s[index+1:]
    return s

s = eval(input())
first_max = find_max(s)
s = delete_number(s, first_max)
second_max = find_max(s)

print( second_max or "NO" )
