#!/usr/bin/env python3

# Ввести текст, состоящий из нескольких строк (заканчивается пустой строкой).
# Каждая строка состоит из «слов» (последовательностей непробельных символов), разделённых пробелами или табуляциями.
# Некоторые слова — целые числа (возможно, отрицательные), другие числами не являются (хотя могут содержать цифры).
# Найти и вывести наибольшее из этих чисел.
# Input:
#
# enemies -565 glanduliform h252Tbeaic -tv5naa2re4 55 silicamortar eared
# ra50ertc-8 -4 94 ohgutyd38 163 -562 u8e8qisn handout crossword 22s4cico
# -v80s6eessl beaning en1A1i-2l 545 december flo ch00a0-h1t vignettist
# ­­
#
# Output:
#
# 545

import sys

def isnumber(n_str):
    if len(n_str) < 1:
        return False
    n_str = n_str[1::] if n_str[0] == "-" else n_str
    return n_str.isdigit()


if __name__ == "__main__":
    int_g = (int(i) for line in sys.stdin for i in line.split() if isnumber(i))
    try:
        m = max(int_g)
    except ValueError:
        m = None
    print(m)
