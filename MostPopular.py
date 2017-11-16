#!/usr/bin/env python3

# Ввести строку, состоящую из разделённых пробелами последовательностей маленьких и больших латинских букв.
# Вывести, сколько различных слов (без учёта регистра) встречается в этой строке чаще всего.
# Input:
#
# dAh Dit dah dIT dAH Dit GIgly diGLy biglY GiGly bOOm quack OH quack
#
# Output:
#
# 2

if __name__ == "__main__":
    strings = dict()
    for s in input().split():
        s = s.casefold()
        word_count = strings.setdefault(s, 0)
        strings[s] = word_count + 1

    reverse_index = dict()
    for key, value in strings.items():
        reverse_index.setdefault(value, [])
        reverse_index.get(value).append(key)

    pairs = [(key, value) for key, value in reverse_index.items()]
    most_popular = max(pairs, key=lambda x:x[0])[1]
    print (len(most_popular))
