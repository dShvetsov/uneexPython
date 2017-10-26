#!/usr/bin/env python3

# Ввести кортеж целых чисел V, затем число N.
# Написать генератор, возвращающий сначала все числа из кортежа (в порядке следования),
# не превосходящие его нулевой элемент, затем все числа, не превосходящие первый, и т. д. вплоть до последнего элемента.
# Вывести N-й элемент этой последовательности, или "NO", если таковой не существует.
# Input:
#
# 10, 10, 1, 7, 8, 0, 5
# 10
#
# Output:
#
# 7

def GenTriseq(v):
    for i in v:
        less_than_i = filter(lambda x : i >= x, v)
        for j in less_than_i:
            yield j

v = eval(input())
n = eval(input())

for i,elem in enumerate(GenTriseq(v)):
    if i == n:
        print (elem)
        break
else:
    print("NO")
